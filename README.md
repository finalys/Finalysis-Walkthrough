# Finalysis Walkthrough

## Introduction & History
Hi, I'm Finalys. You may know me as the author of Finalysis which started in 2020 as a personal project to learn about python. 

[Check out the very first Finalysis I tweeted.](https://twitter.com/_finalys_/status/1241254832989593606?s=20&t=voDlHTU61L76QXQsW92XNQ)

Finalysis started off as a project to summarize and derive insights from Shadowverse tournaments, mainly SVO and JCG. Now that I've sort of achieved what I wanted to learn, it is time to share my knowledge as I try to understand how GitHub works (previously I've been doing everything on Jupyter). I hope to work with others in the future on GitHub :)

The purpose is to share my process of how I process data from Shadowverse Tournaments, which should be suitable for beginners like me. I am pretty sure there are better/efficient ways to perform such tasks. I'm not from a STEM background so results is what matters to me more. I'm not too concerned with the most time-optimal method since the data that we're working with isn't too large (pretty sure I gave the wrong justification but oh wells).

As this is my very first public repo, I will try my best to pick up good habits and make it very digestable for fellow beginners. I hope to inspire more people to take the very first step, ideally in something that interest you like how Shadowverse did to me. 

Again, I reiterate that I still consider myself a beginner so if there are any improvements/suggestions please feel free to let me know! 

Contact me via Discord: **Finalys#7064**

## Coverage

**Calling the API, creating hashes**
- *File:* `ShadowverseAPI.ipynb`
- Retrieving useful information for shadowverse-portal
- Cleaning the information
- Other utilities: Scraping image assets
    
**JCG Analysis**
- *Files:* `JCGAnalysis.ipynb`, `DeckClassify.py`
- Scraping from the JCG website
- Cleaning and getting player information & decks
- Identify the deck archetypes brought by players & descriptive statistics
- Breakdown of each deck brought by players
- Matchup analysis **(Work-in-progress)**
- Export file to Excel

## Changelog

>V1.3:
>- Added image utitlies in `ShadowverseAPI.ipynb`
>- Added 2 new sections to `JCGAnalysis.ipynb`: *Brackets Page, Matchup Analysis (WIP)*
>- Updated `SVCardInfo.xlsx` for **Celestial Dragonblade** emergency patch


>V1.2:
>- Added 3 new sections to `JCGAnalysis.ipynb`: *Deck Classification & Summarization, Deck Breakdown, Exporting the results*
>- Added `DeckClassify.py` as part of *Deck Classification & Summarization*
>- Added more visuals to `JCGAnalysis.ipynb`, more gifs!
>- Updated `SVCardInfo.xlsx` for **Celestial Dragonblade** expansion


>V1.1:
>- Added `JCGAnalysis.ipynb`

>V1.0:
>- My first GitHub commit!