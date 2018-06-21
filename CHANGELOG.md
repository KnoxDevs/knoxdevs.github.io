# Change Log

## [0.4.0] (2018-06-20)

** Implement enchancements: **
- Split `_data` and `assets\cluster_images` to separate repositories to cut down the amount of effort contributors need to place, and make it more clear for the planned KnoxDevs Directory API in the future.

- Add Code of Conduct to how to contribute to the repo.

- Separate content in `about.md` to `code_of_conduct.md` and `organizers.md` to make more clear on changes to each of those sections.

** Addressed issues: **

- Fixed spelling format errors that resulted in bad links.

- Enforced style of `_` to donate spaces between words, not only in file naming, but also in anchor naming

- Also enforced style of all lowercase for anchors to ensure later on correct copying is made.

## [0.3.3] (2018-06-06)

** Implemented enhancements:**
- More concise language on the READMEs in the individual data subfolders to guide website visitors who link to the repo on trying to submit a PR before submitting an issue or messaging on slack only.

** Addressed issues: **
- Reformated data entries (like groups) to address non-clear language.  [\#2](https://github.com/KnoxDevs/knoxdevs.github.io/issues/1)

## [0.3.2] (2018-06-01)

** Implemented enhancements:**

- Added a Changelog
- Built tempaltes for issues and PRs.
- Made sure all previously externally linked images were added to and then served from the `assets` folder.

** Addressed issues: **
- Added language guiding a user to install jekyll and build locally before sending a PR. [\#1](https://github.com/KnoxDevs/knoxdevs.github.io/issues/1)

## [0.3.0]

** Implemented enhancements:**

- Removed Companies from the `_data` folder, something that could be revisited later. Hard part is deciding \*who\* should be listed, fairness between companies large and small. Who decides how much of a _developer_ company a particular company is?
- Merged Organizations, Conferences Coworking Spaces, (newly added) Event Spaces, under `Resources` tab to also remove clutter in top level navigation.
