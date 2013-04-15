Title: Objective-C Style Guide
Date: 2013-3-2
Tags: ios, style
Subtitle: reading code can be difficult
Summary: <p>Reading code can be difficult. Maybe you didn't write it; maybe seventeen people touched it before you. My preference is to conform to whatever style is currently being used when joining a project. In the absence of...</p>

Reading code can be difficult. Maybe you didn't write it; maybe seventeen people
touched it before you. My preference is to conform to whatever style is
currently being used when joining a project. In the absence of that:

Consistent. Clean. Easy to read. Short.

Dot Notation
----------

- Use dot notation to access properties.
- Use message notation to call a method.

Whitespace
----------

- Use spaces not tabs.
- Do not wrap lines.
- Use new lines before blocks of code.
- Do not open braces on a new line.

Structure
----------

- Only define the public interface in the header.
- Only `#import` the superclass, adopted protocols, and enums in the header.
- Don't declare methods in the private interface.
- Don't put two semicolons on the same line.
- Use #pragma marks to logically group code.

Naming
----------

- Use descriptive variable names.
- Use self describing method names.
- Use class name prefixes.

Comments
----------

- Use descriptive variable and method names to explain code not comments.
- Use `TODO:` `FIXME:` `!!!:` and `???:` when writing comments.

Variables
----------

- Asterisks of pointers belong with the variable not the type.

@property
----------

- Use properties.
- Do not declare iVars.
- Only access iVars directly during initialization.

Booleans
----------

- Use `YES` or `NO` not `true` or `false`.
- Do not compare to methods or properties that return `BOOL`
