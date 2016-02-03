Title: Basic C Data Types
Date: 2013-5-9
Tags: computer science, c, data type
Subtitle: beginning with the basics

[&#x21d0; Table Of Contents][]

## Bit {: #bit}

A [bit][] is a unit of information having a value of 0 or 1; a [byte][] is 8
bits. [Binary][] is a base 2 numeral system typically using a bit to represent a
value, [decimal][] is base 10, and [hexadecimal][] is base 16.

| Binary | Decimal | Hexdecimal |
|:-------|:--------|:-----------|
| 0000   | 0       | 0          |
| 0001   | 1       | 1          |
| 0010   | 2       | 2          |
| 0011   | 3       | 3          |
| 0100   | 4       | 4          |
| ...    | ...     | ...        |
| 1111   | 15      | f          |

Note that *n* bits yields 2<sup>*n*</sup> possible values. This means that the
8 bits in a byte can be used to represent the values from 0 to 255.

## Integer {: #integer}

The standard header for integer types is `limits.h`.

| Type               | Bits | Value                                        |
|:-------------------|:-----|:---------------------------------------------|
| char               | 8    |                                              |
| signed char        | 8    |                 -127 to 127                  |
| unsigned char      | 8    |                    0 to 255                  |
| short int          | 16   |               -32767 to 32767                |
| unsigned short int | 16   |                    0 to 65535                |
| int                | 16   |               -32767 to 32767                |
| unsigned int       | 16   |                    0 to 65535                |
| long int           | 32   |          -2147483647 to 2147483647           |
| unsigned long int  | 32   |                    0 to 4294967295           |
| long long          | 64   | -9223372036854775807 to 9223372036854775807  |
| unsigned long long | 64   |                    0 to 18446744073709551615 |

The requirements being that `short` and `int` are at least 16 bits; `long` is
at least 32 bits; and `short` is smaller than `int` which is smaller that
`long`.

## Floating Point {: #floating_point}

The standard header for floating point types is `float.h`.

| Type        | Bits |
|:------------|:-----|
| float       | 32   |
| double      | 64   |
| long double | 64   |

The requirements being that `float` is smaller than `double` which is smaller
than `long double`.

## Boolean {: #boolean}

The standard header for the boolean type is `stdbool.h`.

In it's simplest form, boolean can be represented with either 0 or 1, a single
bit. In some languages bool is an `int`, in others the `bool` type is not
defined. Often the value 0 or NULL is considered false and any other value
true.

## Pointer {: #pointer}

A pointer is a variable that contains the address of another variable.

<!-- TODO: content -->

## Array {: #array}

<!-- TODO: content -->

## Struct {: #struct}

<!-- TODO: content -->

Most of this information is from [The C Programming Language][] or the
wikipedia page [C Standard Library][].

[&#x21d0; Table Of Contents][]

[&#x21d0; table of contents]: ../study-guide/#basic_c_data_types "Table Of Contents"
[binary]: http://en.wikipedia.org/wiki/binary "Binary"
[bit]: http://en.wikipedia.org/wiki/bit "Bit"
[byte]: http://en.wikipedia.org/wiki/byte "Byte"
[c standard library]: http://en.wikipedia.org/wiki/c_standard_library "C Standard Library"
[decimal]: http://en.wikipedia.org/wiki/decimal "Decimal"
[hexadecimal]: http://en.wikipedia.org/wiki/hexadecimal "Hexadecimal"
[the c programming language]: http://www.amazon.com/c-programming-language-2nd-ed/dp/0131103709/ "The C Programming Language"
