status: draft
Title: Big O Notation
Date: 2013-6-8
Tags: computer science, algorithm, big o notation, complexity, performance
Subtitle: 

[&#x21d0; Table Of Contents][]

[Big O notation][] is used in computer science to describe the worse case
complexity or performance of an [algorithm][].

http://bigocheatsheet.com

#### Constant - O(1) {: #constant }

An algorithm whose complexity will remain constant regardless of *n*.

- Accessing an index of an array.
- Determining if an integer is even.

#### Logarithmic - O(log *n*) {: #logarithmic }

An algorithm whose complexity will grow logarithmically with *n*.

- [Binary Search][]

#### Linear - O(*n*) {: #linear }

An algorithm whose complexity will grow linearly with *n*.

- Finding an item in an unsorted array.
- Adding all the items in an array.

#### Linearithmic - O(*n* log *n*) {: #linearithmic }

Most efficient sorting algorithms have a linearithmic complexity.
Described as performing a O(log *n*) operation for every item.

- [Quicksort][]*
- [Mergesort][]
- [Heapsort][]

#### Quadratic - O(*n*<sup>2</sup>) {: #quadratic }

An algorithm whose complexity will grow quadratically with *n*.
Described as performing *n* operations for every item.

- [Insertion Sort][]
- [Selection Sort][]
- [Bubble Sort][]

#### Exponential - O(2<sup>*n*</sup>) {: #exponential }

An algorithm whose complexity will grow exponentially with *n*.

- Solving the [Traveling Salesman Problem][] with [dynamic programming][].

#### Factorial - O(*n*!) {: #factorial }

An algorithm whose complexity will grow factorially with *n*.
Described as performing an operation for all permutations of *n*.

- Solving the [Traveling Salesman Problem][] using brute force.

#### Operation Comparison {: #operation_comparison }

| Big-O              | 10 Operations | 100 Operations  |
|:-------------------|:--------------|:----------------|
| O(1)               | 1             | 1               |
| O(log *n*)         | 3             | 7               |
| O(*n*)             | 10            | 100             |
| O(*n* log *n*)     | 30            | 700             |
| O(*n*<sup>2</sup>) | 100           | 10000           |
| O(2<sup>*n*</sup>) | 1024          | 2<sup>100</sup> |
| O(*n*!)            | 3628800       | 100!            |

#### Amortized Analysis {: #amortized_analysis }

Average complexity of an operation over a large *n*.

- Adding an item to a dynamic array.

#### Domination {: #domination }

[&#x21d0; Table Of Contents][]

[&#x21d0; table of contents]: ../study-guide/#basic_c_data_types "Table Of Contents"
[big o notation]: http:// "Big O Notation"
[algorithm]: http:// "Algorithm"
[binary search]: http:// "Binary Search"
[quicksort]: http:// "Quicksort"
[mergesort]: http:// "Mergesort"
[heapsort]: http:// "Heapsort"
[insertion sort]: http:// "Insertion Sort"
[selection sort]: http:// "Selection Sort"
[bubble sort]: http:// "Bubble Sort"
[traveling salesman problem]: http://en.wikipedia.org/wiki/Travelling_salesman_problem "Traveling Salesman Problem"
[dynamic programming]: http:// "Dynamic Programming"
