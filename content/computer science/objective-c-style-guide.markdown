Title: Objective-C Style Guide
Date: 2013-3-2
Tags: objective-c, ios, osx, style
Subtitle: reading code should not be difficult
Summary: Understanding an algorithm or some bit code can be difficult, but
         reading it should not be. This means that a coding style should be
         agreed on and used. It also means that when working with someone
         elses code, it's more important to be consistent than creative.

Understanding an algorithm or some bit code can be difficult, but reading it
should not be. This means that a coding style should be agreed on and used. It
also means that when working with someone elses code, it's more important to
be consistent than creative. When I find myself owning code or maintaining
a codebase written in `objective-c` I prefer the following style:

Consistent. Clean. Easy. Short.

Whitespace
----------

- Use spaces, not tabs.
- Do not wrap lines.
- Do not open braces on a new line.
- Use whitespace to group logical blocks of code.

Structure
----------

- Use dot notation to access properties.
- Use message notation to call a method.
- Do not `#import` in the header, except the superclass, protocols, and enums.
- Import root frameworks, not files from those frameworks.
- Do not declare methods in the private interface.
- Do not put two semicolons on the same line.
- Use #pragma marks to logically group code.

Declarations
----------

- Do not declare iVars.
- Do not put a space between the dereferencing oporator (asterisks) and the
    variable.
- Do not put a space between protocol and the type.
- Do not accessing iVars, except in `-init`, `-dealloc`, or accessor.
- Use namespace prefix for functions.

Naming
----------

- Use descriptive property names.
- Use descriptive method names.
- Use namespace prefix for classes.

Comments
----------

- Prefer self describing code to comments where possible.
- Use `TODO:` `FIXME:` `!!!:` and `???:` where appropriate.

Expressions
----------

- Use literals.
- Use `YES` or `NO` not `true` or `false`.
- Use explicit comparisons, except for `BOOL` type's.
