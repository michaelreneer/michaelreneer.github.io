status: draft
Title: Data Structures
Date: 2013-5-19
Tags: computer science, data structure, abstract data type
Subtitle: the building blocks

[&#x21d0; Table Of Contents][]

## Data Structures {: #data_structures}

[Contiguous][] data structures are based on arrays and are composed of a single
block of memory. [Linked][] data structures are based on pointers and are
composed of distinct blocks of memory referenced by pointers.

Because a contiguous data structure is allocated with a defined size it can
become nessissary to resize the structure as items are inserted or deleted.
For example, a [dynamic array][] might resize itself by allocating a new larger
block of memory; copying data from the old block to the new one; and releasing
the old block of memory.

Items can be inserted in or deleted from a linked data structure without
reallocating the structure.

#### Array {: #array }

- Contiguous
- Constant time indexing
- Linear time insert, delete, and search

#### Singly Linked List {: #singly_linked_list }

    typedef struct Node {
        void *object;
        struct Node *next;
    } Node;

- Linked
- Constant time insert and delete
- Linear time indexing and search

#### Doubly Linked List {: #doubly_linked_list }

    typedef struct Node {
        void *object;
        struct Node *next;
        struct Node *previous;
    } Node;

- Linked
- Constant time insert and delete
- Linear time indexing and search

#### Hash Table {: #hash_table }

A hash table combines a [hash function][] and a dynamic array to represent a
list of key-value pairs.

- Contiguous
- Constant time search, insert, and delete (average)
- Linear time search, insert, and delete (worse)

The worst case, linear time performance complexities, represent the scenario
where every item added the the hash table hases to the same key. When using a
*good* hash function, a hash table has a constant time search, insert, and
delete performance complexity.

#### Binary Search Tree {: #binary_search_tree }

- Linked
- Logarithmic time index, search, insert, and delete (average)
- Linear time index, search, insert, and delete (worst)

The wosrt case, linear time performance complexities, represent the scenario
where the tree is unbalanced and the items have been added in an order that
creates a degerate tree. A degenerate tree has only one child per parent and
has a performance complxity similar to that of a linked list. A
[balanced binary tree][] has a logarithmic time index, search, insert, and
delete performance complexity.

#### Suffix Tree {: #suffix_tree }

- Linked

#### Binary Heap {: #binary_heap }

- Contiguous
- Constant time max
- Logarithmic time insert, delete

| Data Structure     | Indexing  | Search    | Insertion  | Deletion  |
|:-------------------|:----------|:----------|:-----------|:----------|
| Array              | O(1)      | O(1)      | O(*n*)     | O(*n*)    |
| Singly Linked List | O(*n*)    | O(*n*)    | O(1)       | O(1)      |
| Doubly Linked List | O(*n*)    | O(*n*)    | O(1)       | O(1)      |
| Hash Table         | O(1)*     | O(1)*     | O(1)*      | O(1)*     |
| Binary Search Tree | O(log n)* | O(log n)* | O(log n)*  | O(log n)* |
| Suffix Tree        |           |           |            |           |

| Data Structure     | Max   | Insertion | Deletion |
|:-------------------|:------|:----------|:---------|
| Binary Heap        | O(1)  | O(log n)  | O(log n) |

## Abstract Data Types {: #abstract_data_types}

#### List {: #list }

<!-- TODO: content -->

#### Stack {: #stack }

- implemented with linked list
- operations: push, pop, top

- last in first out

<!-- TODO: content -->

#### Queue {: #queue }

- implemented with linked list with a pointer to tail or circlular linked list
- operations: enqueue, dequeue, first, last

- first in first out

<!-- TODO: content -->

#### Deque {: #deque }

<!-- TODO: content -->

#### Dictionary {: #dictionary }

- implemented with hash table
- operations: set, get, remove

- Also known as Map

<!-- TODO: content -->

#### Set {: #set }

- balanced binary serach tree
- unique objects

<!-- TODO: content -->

#### Priority Queue {: #priority_queue }

- implemented with binary heap

<!-- TODO: content -->

#### Tree {: #tree }

<!-- TODO: content -->

| Data Structure     | Indexing | Search | Insertion | Deletion |
|:-------------------|:---------|:-------|:----------|:---------|
| List               |          |        |           |          |
| Stack              |          |        |           |          |
| Deque              |          |        |           |          |
| Dictionary         |          |        |           |          |
| Set                |          |        |           |          |
| Priority Queue     |          |        |           |          |
| Tree               |          |        |           |          |

[&#x21d0; Table Of Contents][]

[&#x21d0; table of contents]: ../study-guide/#basic_c_data_types "Table Of Contents"
[balanced binary tree]: http:// "Balanced Binary Tree"
[contiguous]: http:// "Contiguous"
[dynamic array]: http:// "Dynamic Array"
[hash function]: http:// "Hash Function"
[linked]: http:// "Linked"
[the algorithm design manual]: http://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1848000693/ "The Algorithm Design Manual"
