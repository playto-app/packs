# Contributing a game pack

Thanks for considering sharing a pack. Packs are the clearest way to help other Playto users get good translations fast for games you already know well.

## Before you start

- Run Playto with the game for a few sessions so your glossary has real content (not just empty stubs).
- Check the [`packs/`](packs/) directory — if a pack for your game + language pair already exists, open an issue or PR against that folder instead of starting a new one.

## Directory layout

Packs are organized by **game, then by source-target language pair**. A pack is specific to one localization of the game (the language the game is displayed in) + one target language (the one you want translations in).

```
packs/
└── slay-the-spire/
    ├── README.md              # auto-generated game-level overview
    ├── en-ja/                 # EN game build → Japanese translations
    │   ├── README.md          # auto-generated pair summary
    │   └── slay-the-spire.playto-pack
    └── ja-en/                 # JP game build → English translations
        ├── README.md
        └── slay-the-spire.playto-pack
```

**READMEs are auto-generated.** You don't write or edit them. CI regenerates both the game-level and pair-level READMEs from the pack's metadata on every push to main. If you want to add subjective notes (known gaps, special capture tips), put them in the pack's `profile.context.prompt_hint` field before exporting — they'll be rendered into the README.

### Folder / slug rules

- **Game slug** — lowercase, hyphens for spaces, no special characters. Match the game's widely-known title (avoid internal code names).
- **Pair folder** — `<source>-<target>` using ISO 639-1 codes. Examples: `ja-en` (JP source → EN target), `en-ja`, `zh-en`, `ko-en`.
- **Pack filename** — whatever the Playto export produces (usually the game slug, e.g. `slay-the-spire.playto-pack`). Exactly one `.playto-pack` file per pair folder.

### Why pair folders?

Game packs aren't interchangeable between language pairs. Two things differ between, for example, `ja-en` and `en-ja`:

- **Game build** — `ja-en` contributors are playing the Japanese-localized version; `en-ja` contributors are playing the English-localized one. Capture region, text-box positions, and font metrics often differ between localizations.
- **Contributor** — usually a different person for each pair.

The **glossary term pairs themselves are symmetric**, so if a `ja-en` pack already exists, you can bootstrap an `en-ja` pack quickly (see below).

## Reusing an existing pack's glossary

If a pack already exists for your game in one direction (say `ja-en`) and you want to contribute the reverse (`en-ja`):

1. Open the existing pack's JSON, copy each entry in `profile.context.glossary` with `source` and `target` swapped (glossary pairs are symmetric).
2. Re-capture your own capture settings for the game build you're running (JP capture region ≠ EN capture region usually).
3. Export a fresh pack from Playto on your machine, paste the swapped glossary entries into the new pack's `profile.context.glossary`.
4. Credit the original glossary contributor in your pack's `profile.context.prompt_hint` field.
5. Open a PR for the new `<source>-<target>/` folder.

Simpler alternative: just import the existing pack into your Playto, play the game in the reverse direction, re-export — Playto will have carried the glossary across.

## PR checklist

- [ ] Exported pack file opens cleanly when re-imported into a fresh Playto install (test round-trip on your own machine before submitting).
- [ ] Pair folder matches the pack's actual `fromLang` / `toLang` in `game.languages`.
- [ ] Glossary entries match in-game canon — not personal preferences. Use the localization the game itself ships in your target language if one exists.
- [ ] No copyrighted source content bundled (screenshots of cutscenes, full script dumps, etc.). Glossary mappings are OK; entire translated scripts are not.
- [ ] No personal info (Steam username, save-slot names, friends visible in UI) — scan the `.playto-pack` JSON for any leaked user-visible text.

You do **not** need to add or update READMEs — CI does that.

## Export: pack, not glossary

In Playto, the Profile tab has two export buttons. Contributions here use the **pack** export:

- **Export pack** → produces `<game-slug>.playto-pack`. Contains metadata + language pair + glossary + capture settings. **Use this.**
- **Export glossary** → produces `glossary.json` with only the term pairs. Useful for personal backup, but it doesn't carry the capture settings that make a pack immediately usable on import. Don't submit this format for community packs.

At import time the Playto app shows a preview dialog that lets users choose "Import All" (apply capture settings + glossary) or "Glossary only" — the pack format is strictly a superset.

## What gets reviewed

A Playto maintainer will check:

1. **CI passes** — the validator confirms directory layout, JSON shape, and glossary consistency.
2. **Pack file loads** — quick round-trip import.
3. **Glossary quality** — spot-check 5-10 entries for accuracy. Obvious errors block the merge; stylistic choices usually don't.
4. **Scope** — single game + single pair per PR. Don't bundle multiple pairs in one PR unless you're the sole contributor and the glossaries are trivially derived (see above).
5. **Copyright safety** — see the license note in [README.md](README.md#license).

Reviews happen weekly. Please don't ping for expedite unless a pack is time-sensitive (e.g. matching a game's actual release day).

## Updates

To update an existing pack (add new glossary terms, fix an error):

- Open a PR replacing the `.playto-pack` file in the same `packs/<game>/<pair>/` folder.
- The auto-generated README will refresh on merge.

## Disputed or low-quality packs

If a merged pack has factual errors, open an issue in [`playto-app/feedback`](https://github.com/playto-app/feedback) with the `game-support` template. The original contributor will be pinged first; unresolved issues can lead to a correction PR.

## License reminder

By submitting a pack, you agree the translation mappings (glossary entries, capture settings, contributor name) are shared under **CC-BY-4.0**. Any trademarked game content you reference remains the property of its original rights holder — your pack is a translation guide, not a republication.
