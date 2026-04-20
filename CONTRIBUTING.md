# Contributing a game pack

Thanks for considering sharing a pack. Packs are the clearest way to help other Playto users get good translations fast for games you already know well.

## Before you start

- Run Playto with the game for a few sessions so your glossary has real content (not just empty stubs).
- Check the [`packs/`](packs/) directory — if a pack for your game + language pair already exists, open an issue or PR against that folder instead of starting a new one.

## Directory layout

Packs are organized by **game, then by source-target language pair**. A pack is specific to one localization of the game (the language the game is displayed in) + one target language (the one you want translations in).

```
packs/
└── slay-the-spire-2/
    ├── README.md              # game overview shared across all language pairs
    ├── preview.png            # optional, game-level screenshot
    ├── ja-en/                 # JP game build → English translations
    │   ├── README.md              # pair-specific notes, contributor, screenshot
    │   └── game-pack.playto-pack
    └── en-ja/                 # EN game build → Japanese translations
        ├── README.md
        └── game-pack.playto-pack
```

### Folder / slug rules

- **Game slug** — lowercase, hyphens for spaces, no special characters. Match the game's widely-known title (avoid internal code names).
- **Pair folder** — `<source>-<target>` using ISO 639-1 codes. Examples: `ja-en` (JP source → EN target), `en-ja`, `zh-en`, `ko-en`.
- **Pack filename** — `game-pack.playto-pack` (fixed) so CI / in-app browser can find it.

### Why pair folders?

Game packs aren't interchangeable between language pairs. Two things differ between, for example, `ja-en` and `en-ja`:

- **Game build** — `ja-en` contributors are playing the Japanese-localized version; `en-ja` contributors are playing the English-localized one. Capture region, text-box positions, and font metrics often differ between localizations.
- **Contributor** — usually a different person for each pair.

The **glossary term pairs themselves are symmetric**, so if a `ja-en` pack already exists, you can bootstrap an `en-ja` pack quickly (see below).

## Reusing an existing pack's glossary

If a pack already exists for your game in one direction (say `ja-en`) and you want to contribute the reverse (`en-ja`):

1. Copy the glossary entries from the existing pack, swapping `source` and `target` fields on each entry.
2. Re-capture your own capture settings for the game build you're running (JP capture region ≠ EN capture region usually).
3. Credit the original glossary contributor in your new pack's `README.md`.
4. Open a PR for the new `<source>-<target>/` folder.

This lowers the barrier for the second pair — you're not starting from scratch.

## PR checklist

- [ ] Exported pack file opens cleanly when re-imported into a fresh Playto install (test round-trip on your own machine before submitting).
- [ ] Pair folder matches the pack's actual `fromLang` / `toLang` (no mismatched metadata).
- [ ] `README.md` inside the pair folder fills in: game name + store + pair + capture mode used + recommended AI engine + contributor handle + pack version.
- [ ] Game-level `README.md` at `packs/<game>/README.md` exists (create it if you're the first contributor for that game, listing all available pairs as they're added).
- [ ] Glossary entries match in-game canon — not personal preferences. Use the localization the game itself ships in your target language if one exists.
- [ ] No copyrighted source content bundled (screenshots of cutscenes, full script dumps, etc.). Glossary mappings are OK; entire translated scripts are not.
- [ ] No personal info (Steam username, save-slot names, friends visible in UI) in any screenshot.

## What gets reviewed

A Playto maintainer will check:

1. **Pack file loads** — quick round-trip import to confirm format validity.
2. **Glossary quality** — spot-check 5-10 entries for accuracy. Obvious errors block the merge; stylistic choices usually don't.
3. **Scope** — single game + single pair per PR. Don't bundle multiple pairs in one PR unless you're the sole contributor and the glossaries are trivially derived (see above).
4. **Copyright safety** — see the license note in [README.md](README.md#license).

Reviews happen weekly. Please don't ping for expedite unless a pack is time-sensitive (e.g. matching a game's actual release day).

## Updates

To update an existing pack (add new glossary terms, fix an error):

- Open a PR against the same `packs/<game>/<pair>/` folder.
- Bump a version line in the pack's README if you want (e.g. `v1`, `v1.1`) — Playto doesn't enforce versioning yet, but it helps reviewers diff.

## Disputed or low-quality packs

If a merged pack has factual errors, open an issue in [`playto-app/feedback`](https://github.com/playto-app/feedback) with the `game-support` template. The original contributor will be pinged first; unresolved issues can lead to a correction PR.

## License reminder

By submitting a pack, you agree the translation mappings (glossary entries, capture settings, contributor name) are shared under **CC-BY-4.0**. Any trademarked game content you reference remains the property of its original rights holder — your pack is a translation guide, not a republication.
