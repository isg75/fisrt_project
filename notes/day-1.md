# Day 1 - Notes

**R&D** = Research and Development

Original dataset:  `./data/raw/SYB66.xlsx`

### Reading the dataset

- Country codes don’t seem to fit a pattern → we might need to clean this
- Series column → Shorten values (GDP, RD, Gross, which words do we need to keep, what can be turned into an acronym, etc., right now they’re rather long sentences and readability is a bit tricky)

### Five questions to answer for the project:

- Which region invests more in RD
- Which region has more researchers?
- Which outry in Europe invests the most in RD?
- Which region invests less?
- Which region is the one with less researchers?

### Thoughts:

- Probably good to first go on a larger scope (world, continents, countries) and then if we have time we can go deeper on regions and states
- Do we need more data?

### Next steps:

- Standardize column names
- Cleaning ‘series’ column → split between RD and investors
- region and country columns → check what’s going on / split countries and regions, see the codes, do they follow any standard?
- drop the source column
- do we need footnotes?

### Task breakdown:

- Camil & Camil → works on ‘series’ colum, drop footnotes and source columns
- Clara & Bru → work on regions, country codes, areas, etc. → figure the geographic mess and how to sort it, split it, arrange it
- Lorena → will find a project name, has done enough work over the weekend to take a breather now