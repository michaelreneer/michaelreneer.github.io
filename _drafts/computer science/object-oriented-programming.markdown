status: draft
Title: Object Oriented Programming
Date: 2013-6-30
Tags: computer science, oop, design patterns
Subtitle: 

[&#x21d0; Table Of Contents][]

## Polymorphism {: #polymorphism}

- Polymorphism is a programming language feature that allows values of
    different data types to be handled using a uniform interface.
- Polymorphism describes a pattern in object oriented programming in which
    classes have different functionality while sharing a common interface.
    - Ad-Hoc polymorphism = same method name different arguements
    - Subtype polymorphism = supertype as the method arguement
    - Parametric polymorphism = If the goal is to separate algorithms from
        types at compile type, C may do it by macros. Here's sample code
        implementing binary tree with node creation and insertion:

<!-- TODO: content -->

## Design Patterns {: #design_patterns}

#### Singleton {: #singleton}

> Ensure a class only has one instance, and provide a global point of access
> to it.

<!-- TODO: content -->

#### Abstract Factory {: #abstract_factory}

> Provide an interface for creating families of related or dependent objects
> without specifying their concreet classes.

- Class Clusters in Cocoa. Initializing an NSArray may return a different
    underlying object depending on if you know the size ...

    <!-- TODO: content -->

#### Adapter {: #adapter}

> Convert the interface of a class into another interface clients expect.
> Adapter lets classes work together that couldn't otheriseze becaue of
> imcompatible interfaces.

- Wrapper on a third party library.

<!-- TODO: content -->

#### Bridge {: #bridge}

> Decouple an abstraction from its implementation so that the two can vary
> independently.

- break up the class hierarchy and the interface hierarchy

<!-- TODO: content -->

#### Visitor {: #visitor}

> Represent an operation to be performed on the elements of an object
> structure. Visitor lets you define a new operation without changing the
> classes of the elements on which it operates.

- helps to seperate an algorithm from an object structure on which it operates

<!-- TODO: content -->

#### Command {: #command}

> Encapsulate a request as an object, thereby letting you parameterize clients
> with different requests, queue or log reqeusts and support undoable
> operations.

- In cocoas this is action-target pattern

<!-- TODO: content -->

#### Proxy {: #proxy}

> Provide a surrogate or placeholder for another object to control access to
> it.

- Only load an image on demand.

<!-- TODO: content -->

#### Observer {: #observer}

> Define a one-to-many dependency between objects so that when one object
> changes state, all it's dependents are notifited and updated automatically.

- Notifications.

<!-- TODO: content -->

[&#x21d0; Table Of Contents][]

[&#x21d0; table of contents]: ../study-guide/#basic_c_data_types "Table Of Contents"
