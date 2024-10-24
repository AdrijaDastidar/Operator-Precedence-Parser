import numpy as np

grammar_rules = []
def grammarcheck(i):
    print(f"Enter the {i + 1}th grammar (production) you want to check: ")
    nonterminals = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    terminals = list("abcdefghijklmnopqrstuvwxyz")   

    b = list(input().split("->"))
    
    if len(b) != 2:
        print(f"Error: Invalid grammar format in production {i + 1}. Should be in 'LHS -> RHS' format.")
        return False
    
    lhs, Rhs = b
    lhs = lhs.strip()
    rhs = Rhs.strip()
    
    if not lhs or not rhs:
        print(f"Error: LHS or RHS is empty in production {i + 1}.")
        return False
    
    if lhs not in nonterminals:
        print(f"Error: LHS should be a non-terminal in production {i + 1}.")
        return False
    
    rhs_tokens = list(Rhs)
    for j in range(len(rhs_tokens) - 1):

        if rhs_tokens[j] in nonterminals and rhs_tokens[j + 1] in nonterminals:
            print(f"Error: Production '{lhs} -> {rhs}' contains consecutive non-terminals.")
            return False
    
    grammar_rules.append((lhs, rhs))
    return True

def stringcheck():
    a = list(input("Enter the operators used in the given grammar including the terminals: "))
    a.append('$')  
    print(a)

    terminals = list("abcdefghijklmnopqrstuvwxyz")   
    operators = list('(/*%+-)')  

    precedence_table = np.empty([len(a) + 1, len(a) + 1], dtype=str, order="C")

    for j in range(1, len(a) + 1):
        precedence_table[0][j] = a[j - 1]
        precedence_table[j][0] = a[j - 1]

    for i in range(1, len(a) + 1):
        for j in range(1, len(a) + 1):
            if (precedence_table[i][0] in terminals) and (precedence_table[0][j] in terminals):
                precedence_table[i][j] = ""
            elif (precedence_table[i][0] in terminals):
                precedence_table[i][j] = ">"
            elif (precedence_table[0][j] in terminals):
                precedence_table[i][j] = "<"
            elif (precedence_table[i][0] in operators) and (precedence_table[0][j] in operators):
                if operators.index(precedence_table[i][0]) <= operators.index(precedence_table[0][j]):
                    precedence_table[i][j] = ">"
                else:
                    precedence_table[i][j] = "<"
            elif precedence_table[i][0] == "$" and precedence_table[0][j] != "$":
                precedence_table[i][j] = "<"
            elif precedence_table[i][0] != "$" and precedence_table[0][j] == "$":
                precedence_table[i][j] = ">"
            else:
                precedence_table[i][j] = ""

    print("The Operator Precedence Relational Table\n=============================================")
    print(precedence_table)

    ip = list(input("Enter the string to be checked (non-terminals should be in lowercase): "))
    ip.append("$")  

    stack = ["$"]
    top = 0  
    i = 0  

    x = [row[0] for row in precedence_table] 
    y = list(precedence_table[0])  

    print("STACK\t\t\t\tINPUT STRING\t\tACTION")

    while True:
        if top >= len(stack) or i >= len(ip):
            print("Error: Stack or input pointer out of range.")
            print("String is not accepted")
            break
        
        if stack[top] =='S':
            row = x.index(stack[top-1]) 
        else: 
            row = x.index(stack[top])

        col = y.index(ip[i]) 

        if len(stack) == 2 and stack[0] == '$' and stack[1] == 'S' and ip[i] == '$':
            print(f"{'$'}\t{''.join(ip[i:])}\t\t\tString is accepted")
            break


        # Shift
        if (precedence_table[row][col] == '<') or (precedence_table[row][col] == '='):
            top += 1
            if top < len(stack):
                stack[top] = ip[i]
            else:
                stack.append(ip[i])
            action = f"Shift {ip[i]}"
            i += 1

        # Reduce
        elif precedence_table[row][col] == '>':
            reduced = False
            
            for rule in grammar_rules:
                lhs, rhs = rule
                rhs_tokens = rhs.split()
                if stack[top - len(rhs_tokens) + 1:top + 1] == rhs_tokens:
                    for _ in range(len(rhs_tokens)):
                        stack.pop()
                        top -= 1
                    stack.append(lhs)  
                    top += 1
                    action = f"Reduce to {lhs}"
                    reduced = True
                    break
            
            if not reduced:
                print(f"{''.join(stack)}\t{''.join(ip[i:])}\t\tString is not accepted")
                break
        else:
            print(f"{''.join(stack)}\t{''.join(ip[i:])}\t\tString is not accepted")
            break

        stack_display = ''.join(stack)
        input_display = ''.join(ip[i:])
        print(f"{stack_display:<20}\t\t{input_display:<20}\t{action}")

# Main program starts here
c = int(input("Enter the number of LHS variables: "))
grammar_accepted = True

for i in range(c):
    if grammarcheck(i):
        grammar_accepted = True
    else:
        grammar_accepted = False
        break

if grammar_accepted:
    print("Grammar is accepted")
    stringcheck()
else:
    print("Grammar is not accepted")
