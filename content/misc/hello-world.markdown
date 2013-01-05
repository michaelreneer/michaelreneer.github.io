Title: Hello World
Date: 2012-12-9
Tags: blog, pelican
Subtitle: Bored + learning python = a blog written with pelican
Summary: <p>I have recently begun working professionally with Python and decided in order to truly have any fun, I needed to dive in with some of my free time. For some time now I have been interested in starting a blog. Being more interested in static site generation then WordPress configuration ... </p>

I have recently begun working professionally with [Python][] and decided in
order to truly have any *fun*, I needed to dive in with some of my free time.
For a while I have been interested in starting a blog. Being more keen on
static site generation then [WordPress][] configuration and wanting to learn
python - I started looking for a python solution for a personal blog.

After a few minutes of googling I gave [Hyde][] a try. Installed everything, got
everything working, building, got real excited, etc... and then decided it
wasn't for me. Not really sure what turned me off. Kept looking and found
[Pelican][] which had some great documentation and lot of activity on the
project. Now here you are reading a hello world blog entry written in
[Markdown][], built with pelican, and hosted on [GitHub][].

I am currently using OS X and the Terminal app. Here's what I did ...

Environment
----------

First install packages [pip][], [virtualenv][], and finally
[virtualenvwrapper][].

    :::console
    sudo easy_install pip
    sudo pip install virtualenv
    sudo pip install virtualenvwrapper

Update `~/.bash_profile` by adding.

    :::bash
    export WORKON_HOME=${HOME}/.virtualenvs
    export PROJECT_HOME=${HOME}/Documents/Developer
    export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
    source /usr/local/bin/virtualenvwrapper_lazy.sh
    export PIP_VIRTUALENV_BASE=${WORKON_HOME}
    export PIP_RESPECT_VIRTUALENV=true

Please read the [virtualenvwrapper reference][].

Pelican
----------

Create the virtual environment.

    :::console
    mkvirtualenv --no-site-packages michaelreneer.github.com

Setup the project.

    :::console
    mkdir ~/Documents/Developer/michaelreneer.github.com
    cd ~/Documents/Developer/michaelreneer.github.com
    setvirtualenvproject

Install packages.

    :::console
    pip install pelican Markdown

Run pelican quickstart

    :::console
    mkdir source
    cd source
    pelican-quickstart

**Most** of what I did so far can also be found directly from the
[pelican documentation][].

And we are done. You can 



[github]: http://github.com "GitHub"
[github pages]: http://pages.github.com "GitHub Pages"
[hyde]: http://hyde.github.com "Hyde"
[jekyll]: http://github.com/mojombo/jekyll "Jekyll"
[markdown]: http://daringfireball.net/projects/markdown/ "Markdown"
[pelican]: https://github.com/getpelican/pelican "Pelican"
[pelican documentation]: http://pelican.readthedocs.org/en/3.1.1/getting_started.html "Pelican Documentation"
[python]: http://www.python.org "Python"
[pip]: http://pypi.python.org/pypi/pip "pip"
[ruby]: http://www.ruby-lang.org "Ruby"
[virtualenv]: http://pypi.python.org/pypi/virtualenv "virtualenv"
[virtualenvwrapper]: http://pypi.python.org/pypi/virtualenvwrapper "virtualenvwrapper"
[virtualenvwrapper reference]: http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html "virtualenvwrapper goodies"
[wordpress]: http://wordpress.com "WordPress"
