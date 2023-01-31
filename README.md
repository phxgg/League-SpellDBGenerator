# League-SpellDBGenerator

This is a tool to generate a spell database for the League of Legends API.

> **Warning**:
> This is a work in progress.

## Future plans

- [ ] Add support to generate classes for multiple languages
- [ ] The current endpoint `http://ddragon.leagueoflegends.com/cdn/{ddragon_version}/data/en_US/champion.json` gives us very detailed data about champions but some of this data might be useless for us. Maybe switch to a different endpoint that gives us less data but is more relevant to us. (e.g. `https://ddragon.leagueoflegends.com/cdn/{DDragon_Version}/data/en_US/championFull.json`)
