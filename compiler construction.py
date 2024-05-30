import re

# Define token classes
class Token:
    def __init__(self, tok_type, value):
        self.type = tok_type
        self.value = value

# Define token types
class TokenType:
    # Keywords
    IF = "IF"
    ELSE = "ELSE"
    FOR = "FOR"
    WHILE = "WHILE"
    BREAK = "BREAK"
    CONTINUE = "CONTINUE"
    RETURN = "RETURN"
    PRINT = "PRINT"
    READ = "READ"
    SHOW = "SHOW"
    DO = "DO"
    DEFAULT = "DEFAULT"
    FUNCTION = "FUNCTION"
    MAIN = "MAIN"
    TO = "TO"
    CON = "CON"
    INT = "INT"
    FL = "FL"
    CH = "CH"
    ST = "ST"
    
    # Relational operators
    LT = "LT"
    LTEQ = "LTEQ"
    GT = "GT"
    GTEQ = "GTEQ"
    EQ = "EQ"
    NET = "NET"
    
    # Logical operators
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    
    # Arithmetic operators
    PLUS = "PLUS"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    REM = "REM"
    INC = "INC"
    DEC = "DEC"
    
    # Assignment operator
    ASOP = "ASOP"
    
    # Data types
    IDENTIFIER = "IDENTIFIER"
    INTEGER_CONSTANT = "INTEGER_CONSTANT"
    REAL_CONSTANT = "REAL_CONSTANT"
    CHAR_CONSTANT = "CHAR_CONSTANT"
    STRING_CONSTANT = "STRING_CONSTANT"
    
    # Comments
    SINGLE_LINE_COMMENT = "SINGLE_LINE_COMMENT"
    MULTI_LINE_COMMENT = "MULTI_LINE_COMMENT"

# Define patterns
patterns = {
    # Keywords
    TokenType.IF: r'agar',
    TokenType.ELSE: r'nahi to',
    TokenType.FOR: r'mqsd k lya',
    TokenType.WHILE: r'jab tak',
    TokenType.BREAK: r'ruk jao',
    TokenType.CONTINUE: r'jari rkhyn',
    TokenType.RETURN: r'wapis',
    TokenType.PRINT: r'likhyn',
    TokenType.READ: r'prhyn',
    TokenType.SHOW: r'dikhayn',
    TokenType.DO: r'kryn',
    TokenType.DEFAULT: r'tay shuda',
    TokenType.FUNCTION: r'function',
    TokenType.MAIN: r'main',
    TokenType.TO: r'to',
    TokenType.CON: r'con',
    TokenType.INT: r'Int',
    TokenType.FL: r'Fl',
    TokenType.CH: r'Ch',
    TokenType.ST: r'St',
    
    # Relational operators
    TokenType.LT: r'<',
    TokenType.LTEQ: r'<=',
    TokenType.GT: r'>',
    TokenType.GTEQ: r'>=',
    TokenType.EQ: r'==',
    TokenType.NET: r'!=',
    
    # Logical operators
    TokenType.AND: r'&',
    TokenType.OR: r'\|',
    TokenType.NOT: r'!',
    
    # Arithmetic operators
    TokenType.INC: r'\+\+',  # Match ++ before +
    TokenType.DEC: r'--',    # Match -- before -
    TokenType.PLUS: r'\+',
    TokenType.SUB: r'-',
    TokenType.MUL: r'\*',
    TokenType.DIV: r'/',
    TokenType.REM: r'%',
    
    # Assignment operator
    TokenType.ASOP: r'=',
    
    # Data types
    TokenType.IDENTIFIER: r'[a-zA-Z][a-zA-Z0-9]*',
    TokenType.INTEGER_CONSTANT: r'\b\d+\b',
    TokenType.REAL_CONSTANT: r'\b\d+\.\d+\b',
    TokenType.CHAR_CONSTANT: r"'.'",
    TokenType.STRING_CONSTANT: r'"[^"]*"',
    
    # Comments
    TokenType.SINGLE_LINE_COMMENT: r'//.*',
    TokenType.MULTI_LINE_COMMENT: r'/\*(.|\n)*?\*/'
}

# Define lexer
class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
    
    def tokenize(self):
        token_regex = '|'.join(f'(?P<{tok}>{pat})' for tok, pat in patterns.items())
        for match in re.finditer(token_regex, self.text, re.MULTILINE):
            for name, value in match.groupdict().items():
                if value is not None:
                    self.tokens.append(Token(name, value))
                    break

# Sample usage
if __name__ == "__main__":
    # Ask user for file path and extension
    file_path = input("Please enter the full path of the file including its extension (e.g., C:\\path\\to\\your\\file.txt): ")

    # Read the file
    try:
        with open(file_path, "r") as file:
            text = file.read()
        
        # Tokenize
        lexer = Lexer(text)
        lexer.tokenize()
        
        # Print tokens in table format
        print("+---------------------+----------------------+")
        print("|        Lexeme       |         Token        |")
        print("+---------------------+----------------------+")
        for token in lexer.tokens:
            print(f"| {token.value.ljust(20)} | {token.type.ljust(20)} |")
        print("+---------------------+----------------------+")
    except Exception as e:
        print(f"Error: {e}")