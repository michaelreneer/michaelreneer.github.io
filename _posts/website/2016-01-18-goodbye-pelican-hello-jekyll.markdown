---
title: Goodbye Pelican, Hello Jekyll
subtitle: simpler and simpler
categories: website
tags: blog, jekyll, pelican
---

It was nice to use [Pelican][] as a way to learn [Python][], but [Jekyll][] is
simply more integrated into [GitHub Pages][].

## Ruby

First, install a ruby environment.

``` bash
\curl -sSL https://get.rvm.io | bash -s stable --ruby
rvm install 2.2
```

Begin using the environment.

``` bash
rvm use 2.2
```

Install [Bundler][].

``` bash
ruby install bundler
```

## Jekyll

Setup the project.

``` bash
cd ~/Documents/Developer/
jekyll new michaelreneer.github.io
cd ~/Documents/Developer/michaelreneer.github.io
```

Create repository called `Gemfile` containing the following...

``` ruby
source 'https://rubygems.org'
gem 'github-pages'
```

Install repository.

``` bash
bundle install
```

Run Jekyll.

``` bash
bundle exec jekyll serve
```

## GitHub

Locally, you will be able to view your site, but there is no need to push the
generated files to github. Github will generate the site for you if you push
the source to the `master` branch.

[github pages]: http://pages.github.com "GitHub Pages"
[bundler]: http:// "Bundler"
[jekyll]: http://jekyllrb.com "Jekyll"
[pelican]: http://github.com/getpelican/pelican "Pelican"
[python]: http://www.python.org "Python"
