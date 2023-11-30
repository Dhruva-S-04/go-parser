# go-parser

This project consists of a simple lex and yacc implementation in a single file. The purpose is to check the constructs such as `if`, `else if`, `else`, `for`, and `switch` in the Go programming language.

## Project Overview

The `go-parser` project aims to provide a basic parser for Go code, focusing on specific control flow constructs. The implementation uses lex and yacc to tokenize and parse the input code.

## Constructs Checked

The following control flow constructs are checked in the parser:

- `if`: Conditional statement.
- `else if`: Additional conditional statement.
- `else`: Default case when no previous conditions are met.
- `for`: Looping construct for iteration.
- `switch`: Conditional branching based on multiple cases.

## File Structure

The parser is implemented in a single file for simplicity and ease of understanding.

- `Project.py`: Contains the lex and yacc implementation for parsing Go code.

## Usage

To use the parser, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/go-parser.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd Project.py
   ```

3. **Run the Parser:**
   ```bash
   Run the python file
   ```

## Example

Here's a simple example of using the `go-parser`:

```go

    x := 10

    if x > 5 {
        a=a+b;
    } else if x == 5 {
        a=a-b;
    } else {
        a=a+1;
    }

    for i := 0; i < 5; i++ {
        a=a+1;
    }

    switch x {
    case 1:
        a=a+b;
    case 2:
        a=a-b;
    default:
        a+=1;
    }

```

