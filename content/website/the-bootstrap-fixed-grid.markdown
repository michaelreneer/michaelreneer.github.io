Title: The Bootstrap Fixed Grid
Date: 2013-4-14
Tags: html5, css, bootstrap, responsive, fixed
Subtitle: implementing a responsive fixed grid
Summary: One of the first things I wanted to do with my blog - after exploring
         pelican - was to begin digging into some responsive layouts. I wanted
         a fixed-width design with various layouts and I wanted to test out a
         framework instead of build from scratch.

One of the first things I wanted to do with my blog - after exploring pelican -
was to begin digging into some responsive layouts. I wanted a fixed grid design
with various layouts and I wanted to test out a framework instead of build from
scratch.

Surprise, I ended up implementing [Bootstrap][]. Here is what I looked at:

Bootstrap seemed to be the most well adopted; it has a great community, great
documentation, and is actively supported. I didn't care for any of the UI
tools, but it was easy to build and exclude all the extras I didn't want.

[Foundation][] looked pretty good as well. Maybe a slightly smaller user base,
but still very supported and the documentation was there. Again, didn't want
the UI tools and there was a way to exclude them.

[Frameless][] also caught my eye. It ended up being less of a framework and
more of a strategy. But it was really interesting, and I may end up adopting a
fully customized approach since I am using so little of a framework that
doesn't do everything I want it to.

... so now you can view the site on your phone, tablet and computer.

Bootstrap ended up being very easy to implement. Checkout my [commit][]. It's
probably not worth going over the steps, as the documentation on
[Scaffolding][] really is clear. The only downside I have with the framework is
that it's not "[mobile first][]". Foundation is designed to be mobile first,
but it doesn't come with fixed-width layouts. [Bootstrap 3.0][] looks very
similar to the latest iteration of Foundation, in that it is being redesigned
with mobile in mind. I am pleased for now, and will likely take a look at
Foundation, Frameless, and Bootsrtrap 3.0 sometime in the furture.

[bootstrap]: http://twitter.github.io/bootstrap/ "Bootstrap"
[bootstrap 3.0]: http://thenextweb.com/dd/2013/03/10/heres-an-early-look-at-bootstrap-3-rewritten-to-be-mobile-friendly-from-the-start/ "Bootstrap 3.0"
[commit]: http://github.com/michaelreneer/michaelreneer.github.io/commit/9320672f46bd3334685ef7a6f064b09dfccaf9b0 "Commit"
[foundation]: http://foundation.zurb.com "Foundation"
[frameless]: http://framelessgrid.com "Frameless"
[mobile first]: http://www.lukew.com/ff/entry.asp?933 "Mobile First"
[scaffolding]: http://twitter.github.io/bootstrap/scaffolding.html "Scaffolding"
