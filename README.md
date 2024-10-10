# International Committee for Radionuclide Metrology

This repository contains the website of the International Committee for Radionuclide Metrology. The website is deployed directly from the root directory on the `main` branch, and is rebuilt automatically through a github Action [workflow](https://github.com/icrm-org/icrm-new/blob/main/.github/workflows/jekyll-gh-pages.yml) when new commits are pushed to `main`. 

## Updating the website

To maintain the integrity of the live website, it's essential to follow a structured editing process. Below is the recommended workflow for updating website content on GitHub:

1. Edit the markdown `.md` files, or create new ones.
2. Commit all changes to a new branch
3. Create a pull request for the new branch
4. Upon approval, merge into `main`

## Technical details

- The site is built with [Jekyll](https://jekyllrb.com/), using the [Just the Docs](https://just-the-docs.com/) theme.
- The website content is in Markdown `.md` files, which get converted into `.html` files by Jekyll.
- The website navigation structure (left sidebar) follows the hierachy of folders that contain `index.md` files.
- Custom styling can be added via the [custom.css](https://github.com/icrm-org/icrm-new/blob/main/_sass/custom/custom.scss) file.

## Building the web site locally

For changes beyond minor edits, merging pull requests directly into the main branch solely for development purposes—such as previewing website updates—is impractical. Website development typically involves an iterative trial-and-error process. To efficiently manage this, it’s recommended to work on a local clone of the repository. This approach allows you to build the website and view changes in your local browser during development.

### Development setup requirements

- Ruby
- Jekyll
- Just the Docs theme
- Prerequisites: gcc and make

### Quick setup instructions for linux:

1. Intall Ruby:

   ```bash
   git clone https://github.com/rbenv/rbenv.git ~/.rbenv`
   rbenv init
   rbenv install 3.3.5    # or any later version
   ```

2. Install Jekyll, bundler, and Just the Docs theme:

   ```bash
   gem install jekyll
   gem install bundler
   gem install just-the-docs
   ```
3. Clone the repository:

   ```bash
   git clone git@github.com:icrm-org/icrm-new.git
   cd icrm-new/
   ```

4. Install dependencies:

   ```
   bundle install
   ```

5. Build and serve the website locally:

   ```
   bundle exec jekyll serve
   ```

Open your web browser and navigate to [http://localhost:4000](http://localhost:4000). As long as the local web server is running, any changes you make to the content will be automatically reflected on the local website in real-time.
