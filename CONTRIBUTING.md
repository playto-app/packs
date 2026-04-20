# Contributing a game pack

Thanks for considering sharing a pack. Packs are the clearest way to help other Playto users get good translations fast for games you already know well.

## Before you start

- Run Playto with the game for a few sessions so your glossary has real content (not just empty stubs).
- Check the [`packs/`](packs/) directory — if a pack for your game already exists, open an issue or PR against that folder instead of starting a new one.

## Directory layout

Each pack lives under `packs/<game-slug>/`:

```
packs/
└── slay-the-spire-2/
    ├── README.md              # game info, contributor note, screenshot
    ├── game-pack.playto-pack  # exported from Profile → Export pack
    └── preview.png            # optional: in-game screenshot showing capture region
```

Slug rules:
- Lowercase, hyphens for spaces, no special characters
- Match the game's widely-known title (avoid internal code names)

## PR checklist

- [ ] Exported pack file opens cleanly when re-imported into a fresh Playto install (test round-trip on your own machine before submitting).
- [ ] `README.md` inside the pack folder fills in: game name + store + source/target lang + capture mode used + recommended AI engine + contributor handle.
- [ ] Glossary entries match in-game canon — not personal preferences. E.g. use the localization the game itself ships in your target language if one exists.
- [ ] No copyrighted source content bundled (screenshots of cutscenes, full script dumps, etc.). Glossary mappings are OK (they're user-generated metadata); entire translated scripts are not.
- [ ] No personal info (Steam username, save-slot names, friends visible in UI) in the screenshot.

## What gets reviewed

A Playto maintainer will check:

1. **Pack file loads** — we may do a quick round-trip import to confirm format validity.
2. **Glossary quality** — spot-check 5-10 entries for accuracy. Obvious errors block the merge; stylistic choices usually don't.
3. **Scope** — single game, not bundles of games. Bundles add review friction.
4. **Copyright safety** — see the license note in [README.md](README.md#license).

Reviews happen weekly. Please don't ping for expedite unless a pack is time-sensitive (e.g. matching a game's actual release day).

## Updates

To update an existing pack (add new glossary terms, fix an error):
- Open a PR against the same `packs/<game-slug>/` folder.
- Bump a version line in the pack's README if you want (e.g. `v1`, `v1.1`) — Playto doesn't enforce versioning yet, but it helps reviewers diff.

## Disputed or low-quality packs

If a merged pack has factual errors, open an issue in [`playto-app/feedback`](https://github.com/playto-app/feedback) with the `game-support` template. The original contributor will be pinged first; unresolved issues can lead to a correction PR.

## License reminder

By submitting a pack, you agree the translation mappings (glossary entries, capture settings, contributor name) are shared under **CC-BY-4.0**. Any trademarked game content you reference remains the property of its original rights holder — your pack is a translation guide, not a republication.
