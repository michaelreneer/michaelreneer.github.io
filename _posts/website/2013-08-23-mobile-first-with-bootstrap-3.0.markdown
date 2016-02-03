---
title: Mobile First With Bootstrap 3.0
subtitle: mobile >> desktop
categories: website
tags: html5, css, bootstrap, responsive, mobile first
---

[Bootstrap 3.0][] was [released][] a couple of weeks ago and there is plenty of
information on thier blog about what this new version brings to the table,
improvements, how to migrate, etc ... My experience migrating to Bootstrap 3.0
has been super positive, which probably isn't much perspective when I am only
using the grid system and some utilities, but: give credit where credit's due.

It was a three step program.

1. Remove [Normalize][]. It is now being pulled directly into Bootstrap.
2. Replace `span6` with `col-sm-6`.
3. Refactor my css media queries to be from a mobile first perspective. I only
    have differently layouts for phone and not phone. My base style represented
    the not phone layout and I used media queries to override that style in a
    few places for the phone layout. All I did in this step was refactor my
    media queries so that the base style represented the phone layout and the
    media queries override that style in order to support the not phone layout.
    Note that this likely sounds more complicated than it is.

Done. Checkout my [commit][].

[bootstrap 3.0]: http://getbootstrap.com "Bootstrap 3.0"
[commit]: http://github.com/michaelreneer/michaelreneer.github.io/commit/348321845c5928285e768ed84c04dadb508df0ca "Commit"
[normalize]: http://necolas.github.io/normalize.css/ "Normalize"
[released]: http://blog.getbootstrap.com/2013/08/19/bootstrap-3-released/ "Bootstrap 3.0 Released"
