#!/usr/bin/env python3
"""Validate Playto game packs under packs/.

Checks (hard errors fail the PR):
  1. Directory layout: packs/<game-slug>/<src-tgt>/game-pack.playto-pack
  2. game-slug is lowercase + hyphens + alphanumeric only (no spaces, no special chars)
  3. Pair folder name is <src>-<tgt> with 2-letter ISO codes
  4. game-pack.playto-pack is valid JSON
  5. Required top-level fields present (format_version, game, profile)
  6. profile.context.glossary exists and is non-empty
  7. Pair folder name matches pack metadata (from/to lang)
  8. Glossary consistency: if top-level 'glossary' array exists (v1 format),
     it must match profile.context.glossary keys (no silent drift — the
     motivating bug that prompted #588)

Soft warnings (logged but don't fail):
  - Missing game-level README.md at packs/<game-slug>/README.md
  - Missing pair-level README.md at packs/<game-slug>/<pair>/README.md
  - Pack format_version older than the current standard
"""

import json
import re
import sys
from pathlib import Path

CURRENT_FORMAT_VERSION = 2
SUPPORTED_FORMAT_VERSIONS = (1, 2)

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PAIR_RE = re.compile(r"^([a-z]{2})-([a-z]{2})$")

ROOT = Path(__file__).resolve().parent.parent
PACKS_DIR = ROOT / "packs"

errors: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def validate_pack_file(pack_path: Path, expected_from: str, expected_to: str) -> None:
    rel = pack_path.relative_to(ROOT)
    try:
        data = json.loads(pack_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"{rel}: invalid JSON — {e}")
        return

    # Required top-level fields
    for field in ("format_version", "game", "profile"):
        if field not in data:
            fail(f"{rel}: missing top-level field '{field}'")
            return

    fv = data.get("format_version")
    if fv not in SUPPORTED_FORMAT_VERSIONS:
        fail(f"{rel}: unsupported format_version={fv} (allowed: {SUPPORTED_FORMAT_VERSIONS})")
        return
    if fv < CURRENT_FORMAT_VERSION:
        warn(f"{rel}: format_version={fv} is older than current v{CURRENT_FORMAT_VERSION}; consider re-exporting")

    # game.languages matches pair folder
    game = data.get("game", {})
    langs = game.get("languages", {}) if isinstance(game, dict) else {}
    pack_from = (langs.get("from") or "").lower()
    pack_to = (langs.get("to") or "").lower()
    if pack_from != expected_from or pack_to != expected_to:
        fail(
            f"{rel}: pair folder is '{expected_from}-{expected_to}' but pack metadata says "
            f"'{pack_from}-{pack_to}' (game.languages.from / .to)"
        )

    # profile.context.glossary required and non-empty
    profile = data.get("profile", {})
    ctx = profile.get("context", {}) if isinstance(profile, dict) else {}
    glossary = ctx.get("glossary", {}) if isinstance(ctx, dict) else {}
    if not isinstance(glossary, dict) or not glossary:
        fail(f"{rel}: profile.context.glossary is empty or missing (packs must carry at least one term)")
        return

    # Glossary consistency check (v1 format — top-level array must match dict keys)
    top_level = data.get("glossary")
    if top_level is not None:
        if not isinstance(top_level, list):
            fail(f"{rel}: top-level 'glossary' present but not an array")
        else:
            top_sources = {e.get("source") for e in top_level if isinstance(e, dict)}
            ctx_sources = set(glossary.keys())
            only_top = top_sources - ctx_sources
            only_ctx = ctx_sources - top_sources
            if only_top or only_ctx:
                fail(
                    f"{rel}: top-level 'glossary' array and profile.context.glossary disagree "
                    f"(only in top-level: {sorted(only_top)[:5]}, only in context: {sorted(only_ctx)[:5]}). "
                    "Re-export from the app or use format_version 2 to avoid this drift."
                )


def main() -> int:
    if not PACKS_DIR.is_dir():
        print(f"No packs/ directory at {PACKS_DIR} — nothing to validate.")
        return 0

    game_dirs = [d for d in PACKS_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")]
    if not game_dirs:
        print("No game folders under packs/ yet — nothing to validate.")
        return 0

    for game_dir in sorted(game_dirs):
        if not SLUG_RE.match(game_dir.name):
            fail(
                f"packs/{game_dir.name}: game folder name is not a valid slug "
                f"(lowercase letters/digits with single hyphens, e.g. 'slay-the-spire-2')"
            )
            continue

        if not (game_dir / "README.md").is_file():
            warn(f"packs/{game_dir.name}: missing game-level README.md")

        pair_dirs = [d for d in game_dir.iterdir() if d.is_dir()]
        if not pair_dirs:
            fail(f"packs/{game_dir.name}: no language-pair folders (expected at least one like 'en-ja/')")
            continue

        for pair_dir in sorted(pair_dirs):
            m = PAIR_RE.match(pair_dir.name)
            if not m:
                fail(
                    f"packs/{game_dir.name}/{pair_dir.name}: pair folder must be '<src>-<tgt>' with "
                    "2-letter lowercase ISO codes (e.g. 'en-ja', 'zh-en')"
                )
                continue
            src_lang, tgt_lang = m.group(1), m.group(2)

            pack_file = pair_dir / "game-pack.playto-pack"
            if not pack_file.is_file():
                fail(
                    f"packs/{game_dir.name}/{pair_dir.name}: missing 'game-pack.playto-pack' "
                    "(filename is fixed so CI and the in-app browser can find it)"
                )
                continue

            if not (pair_dir / "README.md").is_file():
                warn(f"packs/{game_dir.name}/{pair_dir.name}: missing pair-level README.md")

            validate_pack_file(pack_file, src_lang, tgt_lang)

    # Report
    for w in warnings:
        print(f"::warning::{w}")
    for e in errors:
        print(f"::error::{e}")

    if errors:
        print(f"\nFailed with {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1

    total_packs = sum(1 for _ in PACKS_DIR.rglob("game-pack.playto-pack"))
    print(f"\nOK — {total_packs} pack(s) validated, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
