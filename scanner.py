
# Define maximum token size
MAX_TOKEN_SIZE = 10000

# Enum-like labels for token types
KEYWORD = 'KEYWORD'
IDENTIFIER = 'IDENTIFIER'
NUMBER = 'NUMBER'
OPERATOR = 'OPERATOR'
SPECIAL = 'SPECIAL'
STRING = 'STRING'
COMMENT = 'COMMENT'
UNKNOWN = 'UNKNOWN'

# List of C keywords
keywords = {"int", "float", "if", "else", "while", "for", "return", "void", "char" , "scanf" ,"printf"}

# Function to check if a word is a keyword
def is_keyword(word):
    return word in keywords

# Function to classify a single character as a special symbol
def is_special(ch):
    return ch in {'{', '}', '(', ')', ';', ',', '[', ']'}

# Function to classify operators
def is_operator(ch):
    return ch in {'+', '-', '*', '/', '=', '<', '>', '%' , '&'}

# Scanner function
def scanner(code):
    i = 0
    tokens = []

    while i < len(code):
        # Skip whitespace
        if code[i].isspace():
            i += 1
            continue

        # Handle identifiers and keywords
        if code[i].isalpha() or code[i] == '_':
            j = i
            while j < len(code) and (code[j].isalnum() or code[j] == '_'):
                j += 1
            token = code[i:j]
            if is_keyword(token):
                tokens.append((KEYWORD, token))
            else:
                tokens.append((IDENTIFIER, token))
            i = j

        # Handle numbers
        elif code[i].isdigit():
            j = i
            while j < len(code) and (code[j].isdigit() or code[j] == '.'):
                j += 1
            token = code[i:j]
            tokens.append((NUMBER, token))
            i = j

        # Handle operators
        elif is_operator(code[i]) and not (code[i] == '/' and code[i + 1] == '/') and not (code[i] == '/' and code[i + 1] == '*'):
            j = i
            while j < len(code) and is_operator(code[j]):
                j += 1
            token = code[i:j]
            tokens.append((OPERATOR, token))
            i = j

        # Handle special characters
        elif is_special(code[i]):
            tokens.append((SPECIAL, code[i]))
            i += 1

        # Handle string literals
        elif code[i] == '"':
            j = i + 1
            while j < len(code) and code[j] != '"':
                j += 1
            j += 1  # Include closing quote
            token = code[i:j]
            tokens.append((STRING, token))
            i = j

        # Handle single-line comments
        elif code[i:i+2] == '//':
            j = i + 2
            while j < len(code) and code[j] != '\n':
                j += 1
            token = code[i:j]
            tokens.append((COMMENT, token))
            i = j

        # Handle multi-line comments
        elif code[i:i+2] == '/*':
            j = i + 2
            while j < len(code) - 1 and code[j:j+2] != '*/':
                j += 1
            j += 2  # Skip closing */
            token = code[i:j]
            tokens.append((COMMENT, token))
            i = j

        # Handle unknown characters
        else:
            tokens.append((UNKNOWN, code[i]))
            i += 1

    return tokens

# Example usage
print("Enter code to analyze:")
code = input()

# Run the scanner and print tokens
tokens = scanner(code)
for token in tokens:
    print(token)
