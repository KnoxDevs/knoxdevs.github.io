# KnoxDevs Website

This repository is a collection of pages and data files that are used by Github Pages to build a `jekyll` site for KnoxDevs based on a template developed by [mmistakes](https://github.com/mmistakes/minimal-mistakes). 

## Want to contribute to this project?

Check out the [Contributing Guide](https://github.com/KnoxDevs/knoxdevs.github.io/blob/master/Contributing.md)

**TL;DR**
1. [fork and clone the github repo](https://guides.github.com/activities/forking/)
2. add your contribution to a new branch named `<username>/<feature-name>`
3. [install jekyll](https://jekyllrb.com/docs/installation/)
4. install jekyll project ruby dependencies `bundle install`
5. serve locally `bundle exec jekyll serve` and check that your
   addition is served properly
6. submit a PR where the two or so files you are changing can easily
   be seen. Some tips for good PRs are in that
   [guide](https://github.com/KnoxDevs/knoxdevs.github.io/blob/master/Contributing.md)
7. profit. 

## Have an Issue or Request?

Submit an Issue above. As we get better at managing this repo, that's where feature requests can be handled.

## Structure
Here's the general structure:

```
.
├── _config.yml
├── _data
├── _layouts
├── _pages
├── .forestry
├── .migrations
├── assets
└── index.md
```

By using `remote_theme` in `_config.yml`, we avoid cluttering this repository with an `_includes`, `_sass`, and javascript and css files. The objective was to keep the repository as simple as possible and use the chosen theme directly. If more customization is needed, all of theme elements from [mmistakes](https://github.com/mmistakes/minimal-mistakes) can be incorporated if desired.

### _data folder

This folder contains all of the data (stored in `.yml` files) associated with bloggers, groups, organizers, and much more. There is a README file there to explain more.

### _layouts folder

This folder only contains the default.html template where some customizations were made for the cards used predominately throughout the website. The minimal-mistakes theme uses much more layouts than that, but again, the remote theme is referenced every time Github rebuilds the website on a new push.

### _pages folder

This folder contains the markdown files used for each page. These markdown files also contain a mix of `html` and `liquid` tags to acheive the customization desired (mainly for the cards). This website has four (plus the home page which is at the top-level `index.md`). This may change as new features / or new decisions are implemented.

### .forestry folder

[Forestry.io](https://forestry.io) is a CMS for static site builders. Much of the customization that can be done via straight code and pull requests can be done somewhat GUI style through this CMS. A Forestry account has been set up for this website and via this CMS, pull requests are automatically accepted. This feature may be removed if desired.

### .migrations folder

Previously, the knoxdevs.com website used `json` files to represent data like bloggers. This is a folder that is completely unnecessary to the function of the website, but contains the `python` files used to convert the old `json` file to many `.yml` files, 1 for each blogger. At the time, this made more since than a separate repository for the work, at the cost of a few more bytes having to be cloned...

### assets folder

This folder contains all of the images (and potentially javascript files for future extension of this website) used by the website for logos, icons, and headshots. There is a README to explain the inner ordering structure that mirrors the `_data` folder.

Notice that this folder _does not_ have a `_` preceding the name. This folder is publically accessible from the website.

### api folder

This folder is an idea for the future to provide an api where one could easily queue all of the data stored in this repo in a developer friendly way. It is imagined that a `travis.ci` build tool could rebuild a combined `.yml` or `.json` file each time a push to `master` is done.
