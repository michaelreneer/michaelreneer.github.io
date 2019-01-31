---
title: Goodbye Pelican, Hello Jekyll
subtitle: simpler and simpler
categories: website
tags: blog, jekyll, pelican
---

It was fun to use [Pelican](http://github.com/getpelican/pelican) to
learn [Python](http://www.python.org), but [Jekyll](http://jekyllrb.com) is
simply more integrated into [GitHub Pages](http://pages.github.com).

Install [Bundler](https://bundler.io/).

```bash
gem install --user-install bundler
```

Create a project.

```bash
mkdir "${HOME}/Documents/Developer/michaelreneer.github.io"
cd "${HOME}/Documents/Developer/michaelreneer.github.io"
```

Create a file named `Gemfile` containing the following...

```ruby
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
```

Install Ruby dependencies.

```bash
bundle install --path vendor/bundle
```

Create a Jekyll site.

```bash
bundle exec jekyll new . --force
```

Run Jekyll locally.

```bash
bundle exec jekyll serve
```

To publish your changes on your site, push your changes to the `master` branch
of your remote repository on GitHub. GitHub Pages will manage your site's build
process
