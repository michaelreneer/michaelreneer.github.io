Title: Objective-C Coding Guidelines
Date: 2013-3-2
Tags: objective-c, ios, osx, style
Subtitle: reading code should not be difficult
Summary: Understanding an algorithm or some bit code can be difficult, but
         reading it should not be. This means that a coding style should be
         agreed on and used. It also means that when working with someone
         elses code, it's more important to be consistent than creative.

Understanding an algorithm or some bit code can be difficult, but reading it
should not be. This means that a coding guideline should be agreed on and used.
It also means that when working with someone elses code, it is more important
to be consistent than creative. When I find myself owning code in `objective-c`
I prefer to follow Apple's exisiting [Coding Guidelines for Cocoa][] augmented
with the following style:

Consistent. Clean. Easy. Short.

## Whitespace

- Use spaces, not tabs.
- Do not wrap lines.
- Do not open braces on a new line.
- End files with a newline.
- Use whitespace to group logical blocks of code.

## Structure

- Do not `#import` in the header, except the superclass, protocols, and enums.
- Import root frameworks, not files from those frameworks.
- Use #pragma marks to logically group code.

## Naming

- Use descriptive property names.
- Use descriptive method names.
- Use namespace prefix for classes.

## Comments

- Prefer self describing code to comments where possible.
- Use `TODO:` `FIXME:` `!!!:` and `???:` where appropriate.

## Declarations

- Do not declare iVars.
- Do not declare methods in the private interface.
- Do not put a space between the dereferencing oporator (asterisk) and the
    variable.
- Do not put a space between the type and the protocol it conforms to.
- Do not accessing iVars, except in `-init`, `-dealloc`, or the accessors for
    it's property.
- Use namespace prefix for functions.

## Expressions

- Use dot notation to access properties.
- Use message notation to call a method.
- Use literals.
- Use `YES` or `NO` not `true` or `false`.
- Use explicit comparisons, except for `BOOL` type's.

This is a living document.

[coding guidelines for cocoa]: http://developer.apple.com/library/mac/#documentation/cocoa/conceptual/codingguidelines/codingguidelines.html "Coding Guidelines For Cocoa"

