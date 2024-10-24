# Operator Precedence Parser

This repository contains an implementation of an **Operator Precedence Parser** using Python. The parser is designed to handle **Operator Precedence Grammars**, which are a subset of context-free grammars. These grammars are characterized by the absence of epsilon (ε) productions and adjacent non-terminals on the right-hand side of any production rule. This parser is useful for processing expressions in programming languages.

## Features

- **Grammar Validation**: The parser checks that the input grammar conforms to operator precedence rules.
- **Operator Precedence Table**: Generates a precedence table based on the provided terminals and operators.
- **Shift-Reduce Parsing**: Uses shift-reduce parsing to validate whether a given input string follows the grammar.
- **Error Handling**: Detects and reports errors in the grammar definitions and during parsing.

## Operator Precedence Grammar

An **Operator Precedence Grammar** satisfies the following conditions:

1. **No epsilon (ε) production rules**: The grammar cannot contain rules where the right-hand side is empty.
2. **No adjacent non-terminals**: There cannot be two non-terminal symbols next to each other on the right-hand side of any production rule.

These conditions allow for constructing a precedence table, which helps in parsing expressions.

## Advantages and Disadvantages

### Advantages

- Simple and easy to implement.
- Suitable for parsing expressions in programming languages.

### Disadvantages

- Managing operators like the minus sign (which may have different precedences in unary and binary forms) can be tricky.
- This parser can only handle a small subset of grammars.

## Operator Precedence Functions

Instead of storing the entire precedence table, the parser uses **precedence functions** that map terminal symbols to integers. These functions allow efficient numerical comparisons of operators without needing to store the full table.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/operator-precedence-parser.git
   ```

2. Ensure you have Python 3.x installed.

3. Install required libraries using pip:

   ```bash
   pip install numpy
   ```

## Usage

1. Start the script:

   ```bash
   python parser.py
   ```

2. Follow the on-screen prompts:

   - Input the number of production rules.
   - Enter each production in the format `LHS -> RHS`.
   - After validating the grammar, input the terminals and operators used in the grammar.
   - Provide the input string to be parsed.

### Example

Sample input for the parser:

```bash
Enter the number of LHS variables: 3
Enter the 1th grammar (production) you want to check: 
S -> i
Enter the 2th grammar (production) you want to check:
S -> S + S
Enter the 3th grammar (production) you want to check:
S -> S * S
Grammar is accepted
Enter the operators used in the given grammar including the terminals: +*i
['+', '*', 'i', '$']
The Operator Precedence Relational Table
=============================================
[['' '+' '*' 'i' '$']
 ['+' '>' '<' '<' '>']
 ['*' '>' '>' '<' '>']
 ['i' '>' '>' '' '>']
 ['$' '<' '<' '<' '']]
Enter the string to be checked (non-terminals should be in lowercase): i+i*i
STACK                           INPUT STRING            ACTION
$i                              +i*i$                   Shift i
$S                              +i*i$                   Reduce to S
$S+                             i*i$                    Shift +
$S+i                            *i$                     Shift i
$S+S                            *i$                     Reduce to S
$S+S*                           i$                      Shift *
$S+S*i                          $                       Shift i
$S+S*S                          $                       Reduce to S
$S+S                            $                       Reduce to S
$S                              $                       Reduce to S
$                               $                       String is accepted
```

## Code Structure

- `grammarcheck()`: Verifies that the input grammar is valid according to operator precedence rules.
- `stringcheck()`: Builds the operator precedence table, accepts input strings, and uses shift-reduce parsing to check their validity.
- **Main**: Drives the grammar validation and parsing process.

## Contribution

Feel free to fork this repository and submit pull requests if you'd like to contribute.

## License

This project is licensed under the MIT License.
