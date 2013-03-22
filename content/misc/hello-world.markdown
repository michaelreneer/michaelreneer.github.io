Title: Hello World
Date: 2012-12-9
Tags: blog, pelican
Subtitle: Bored + learning python = a blog written with pelican
Summary: <p>I have recently begun working professionally with Python and decided in order to truly have any fun, I needed to dive in with some of my free time. For a while I have been interested in starting a blog. Being more keen on static site generation then WordPress configuration ...</p>

I have recently begun working professionally with [Python][] and decided in
order to truly have any *fun*, I needed to dive in with some of my free time.
For a while I have been interested in starting a blog. Being more keen on
static site generation than [WordPress][] configuration and wanting to learn
python - I started looking for a python solution for a personal blog.

After a few minutes of googling I gave [Hyde][] a try. Installed everything, got
everything working, building, got real excited, etc... and then decided it
wasn't for me. Not really sure what turned me off. Kept looking and found
[Pelican][] which had some great documentation and lot of activity on the
project. Now here you are reading a hello world blog entry written in
[Markdown][], built with pelican, and hosted on [GitHub][].

I am currently using OS X and the Terminal app. Here's what I did...

Environment
----------

First install packages [pip][], [virtualenv][], and [virtualenvwrapper][].

    :::console
    sudo easy_install pip
    sudo pip install virtualenv
    sudo pip install virtualenvwrapper

Update `~/.bash_profile` by adding:

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

Run pelican quickstart.

    :::console
    pelican-quickstart

Please read the [pelican documentation][].

GitHub
----------

I also experimented a little with how the project lives in GitHub and locally.
To start, the static html in the `master` branch of the project named
`USERNAME.github.com` is served up as your user page. Free hosting.

I first tried organizing the source that generated the html as a subdirectory in
the `master` branch. This was nice because I had only one branch to manage; but
because everything was in one branch, managing pull requests would be more
complicated since I would only want to merge changes that updated the source.

So I ended up pushing the source to the `source` branch and the content to the
`master` branch. This way I can automatically decline all pull requests to
the `master` branch. Locally, I have each branch cloned into a different
directory named for the branch.

I will eventually script the process so that immediately after I
push to the `source` branch, my pelican build runs, copies its output to the
`master` branch, and finished by pushing the `master` branch. Eliminating any
branch switching antics.

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
