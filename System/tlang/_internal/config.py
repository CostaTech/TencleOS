# ==========================================
# YOUR LANGUAGE COMMANDS CONFIGURATION
# ==========================================
# 
# HERE YOU CAN CUSTOMIZE ALL COMMANDS
# Just change the strings and the language will use your commands!

# ==========================================
# BASIC COMMANDS - CUSTOMIZE THESE
# ==========================================

# OUTPUT / INPUT
COMANDO_PRINT = "int << func >>"     # Print to screen: int << func >> ("Hello")
COMANDO_INPUT = "input"              # Get user input: var x = input()

# VARIABLES
COMANDO_VAR = "var"                  # Declare variable: var x = 10

# CONDITIONALS
COMANDO_IF = "<< ! >func> if"        # If statement: << ! >func> if x > 5 { ... }
COMANDO_ELSE = ">> func << else"     # Else statement: >> func << else { ... }
COMANDO_ELIF = "elif"                # Else if: elif x < 3 { ... }

# LOOPS
COMANDO_WHILE = "<<While>>! <on>"    # While loop: <<While>>! <on> x < 10 { ... }
COMANDO_FOR = "for"                  # For loop: for i in range(10) { ... }
COMANDO_BREAK = "stop"              # Exit loop: break
COMANDO_CONTINUE = "continue"        # Skip to next iteration: continue

# FUNCTIONS
COMANDO_DEF = "<< ! C>> New command: {" \
"}"                  # Define function: def myFunc(x, y) { ... }
COMANDO_RETURN = "return"            # Return value: return x + y

# IMPORT / MODULES
COMANDO_IMPORT = "use"               # Import module: use pygame

# BOOLEAN VALUES
COMANDO_TRUE = "on"                # Boolean true
COMANDO_FALSE = "off"              # Boolean false

# LOGICAL OPERATORS
COMANDO_AND = "and"                  # Logical AND: if x > 5 and y < 10
COMANDO_OR = "or"                    # Logical OR: if x == 1 or x == 2
COMANDO_NOT = "not"                  # Logical NOT: if not x

# OPERATORS (you can change them if you want different symbols)
OP_PLUS = "+"
OP_MINUS = "-"
OP_MULTIPLY = "*"
OP_DIVIDE = "/"
OP_EQUALS = "="
OP_EQUAL_EQUAL = "=="
OP_NOT_EQUAL = "!="
OP_LESS = "<"
OP_GREATER = ">"
OP_LESS_EQUAL = "<="
OP_GREATER_EQUAL = ">="

# DELIMITERS
LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"
LBRACKET = "["
RBRACKET = "]"
DOT = "."
COMMA = ","


# ==========================================
# FUNCTION TO GET ALL COMMANDS
# ==========================================
def get_keywords():
    """Returns the dictionary of all custom commands"""
    return {
        # Output/Input
        COMANDO_PRINT: 'PRINT',
        COMANDO_INPUT: 'INPUT',
        
        # Variables
        COMANDO_VAR: 'VAR',
        
        # Conditionals
        COMANDO_IF: 'IF',
        COMANDO_ELSE: 'ELSE',
        COMANDO_ELIF: 'ELIF',
        
        # Loops
        COMANDO_WHILE: 'WHILE',
        COMANDO_FOR: 'FOR',
        COMANDO_BREAK: 'BREAK',
        COMANDO_CONTINUE: 'CONTINUE',
        
        # Functions
        COMANDO_DEF: 'DEF',
        COMANDO_RETURN: 'RETURN',
        
        # Import
        COMANDO_IMPORT: 'IMPORT',
        
        # Boolean values
        COMANDO_TRUE: 'TRUE',
        COMANDO_FALSE: 'FALSE',
        
        # Logical operators
        COMANDO_AND: 'AND',
        COMANDO_OR: 'OR',
        COMANDO_NOT: 'NOT',
    }


# ==========================================
# EXAMPLES OF HOW TO CUSTOMIZE COMMANDS
# ==========================================
# 
# Want Italian commands? Change them like this:
# COMANDO_PRINT = "stampa"
# COMANDO_IF = "se"
# COMANDO_ELSE = "altrimenti"
# COMANDO_WHILE = "mentre"
#
# Want custom symbols? Like this:
# COMANDO_PRINT = "int << func >>"
# COMANDO_IF = "<< ? >>"
# COMANDO_WHILE = "<<loop>>! <on>"
#
# The language will automatically recognize your commands!
#
# NOTE: Currently implemented commands in lexer/parser/interpreter:
# - PRINT, IF, ELSE, WHILE, VAR (fully working)
# - INPUT, FOR, BREAK, CONTINUE, DEF, RETURN (need implementation)
# - To add more, tell me which command you want and I'll add it!


