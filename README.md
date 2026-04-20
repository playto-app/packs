# Playto community game packs

Shared game-specific glossaries, capture settings, and per-game tuning for [Playto](https://playto.dev).

A **game pack** is a small file (`.playto-pack`) that bundles:
- Game metadata (title, display name, process name)
- Default source / target language
- Capture settings (region / cursor config, preset sizes)
- Glossary (character names, skill names, item names, lore terms)
- Word frequency data (if the contributor has played a while)

Importing a pack means you start with the settings and vocabulary knowledge of someone who already spent hours on that game. The glossary entries are injected into translation prompts so proper nouns and skill names render correctly.

## Install a pack

1. Browse the [`packs/`](packs/) directory below and pick a game.
2. Download the `.playto-pack` file from that game's folder.
3. In Playto, open the **Profile** tab → **Import pack** → select the file.
4. Optionally review imported glossary entries in **Profile → Glossary**.

## Contribute a pack

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full PR flow. Short version:

1. Play the game with Playto. Build up a glossary. Tune capture settings.
2. Export: **Profile → Export pack** → save `<game>.playto-pack`.
3. Fork this repo, create `packs/<game-slug>/`, drop in your `.playto-pack` + a README describing the game + capture settings used.
4. Open a PR. Reviews are weekly-async.

## Current packs

| Game | Source lang | Contributor | Notes |
|------|------------|-------------|-------|
| _(seed packs will appear here once the first wave is merged)_ |

## License

Pack files submitted here are licensed **CC-BY-4.0** (Creative Commons Attribution). Contributors retain authorship credit; Playto users can import and use them freely.

**Game titles, character names, skill names, and other terms that are trademarks of the game's publisher remain the property of their respective rights holders.** This repo only contains user-generated translation mappings, not copyrighted source content. See [CONTRIBUTING.md](CONTRIBUTING.md) for what's OK to include and what's not.
