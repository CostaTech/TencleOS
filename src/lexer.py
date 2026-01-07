# LEXER - Analizzatore Lessicale
# Legge il codice e lo trasforma in token

from enum import Enum, auto
import config

class TokenType(Enum):
    """Tipi di token"""
    # Comandi (vengono da config.py)
    PRINT = auto()
    INPUT = auto()
    VAR = auto()
    IF = auto()
    ELSE = auto()
    ELIF = auto()
    WHILE = auto()
    FOR = auto()
    BREAK = auto()
    CONTINUE = auto()
    DEF = auto()
    RETURN = auto()
    IMPORT = auto()
    CLASS = auto()
    TRUE = auto()
    FALSE = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    
    # Tipi di dati
    NUMBER = auto()
    STRING = auto()
    IDENTIFIER = auto()
    
    # Operatori
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    EQUALS = auto()
    EQUAL_EQUAL = auto()
    NOT_EQUAL = auto()
    LESS = auto()
    GREATER = auto()
    LESS_EQUAL = auto()
    GREATER_EQUAL = auto()
    DOUBLE_LESS = auto()      # <<
    DOUBLE_GREATER = auto()   # >>
    
    # Delimitatori
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    DOT = auto()
    
    # Speciali
    NEWLINE = auto()
    EOF = auto()
    INVALID = auto()

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, line={self.line})"

class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.line = 1
        self.column = 1
        
        # Carica i comandi personalizzati da config.py
        self.keywords = config.get_keywords()
    
    def current_char(self):
        if self.pos >= len(self.code):
            return None
        return self.code[self.pos]
    
    def peek_char(self, offset=1):
        pos = self.pos + offset
        if pos >= len(self.code):
            return None
        return self.code[pos]
    
    def advance(self):
        if self.pos < len(self.code):
            if self.code[self.pos] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        if self.current_char() == '#':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
    
    def read_number(self):
        start_col = self.column
        num_str = ''
        has_dot = False
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.':
                if has_dot:
                    break
                has_dot = True
            num_str += self.current_char()
            self.advance()
        
        try:
            value = float(num_str) if has_dot else int(num_str)
            return Token(TokenType.NUMBER, value, self.line, start_col)
        except ValueError:
            return Token(TokenType.INVALID, num_str, self.line, start_col)
    
    def read_string(self):
        start_col = self.column
        quote_char = self.current_char()
        self.advance()
        
        string_value = ''
        while self.current_char() and self.current_char() != quote_char:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() == 'n':
                    string_value += '\n'
                elif self.current_char() == 't':
                    string_value += '\t'
                elif self.current_char():
                    string_value += self.current_char()
                self.advance()
            else:
                string_value += self.current_char()
                self.advance()
        
        if self.current_char() == quote_char:
            self.advance()
            return Token(TokenType.STRING, string_value, self.line, start_col)
        else:
            return Token(TokenType.INVALID, string_value, self.line, start_col)
    
    def read_identifier(self):
        start_col = self.column
        identifier = ''
        
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            identifier += self.current_char()
            self.advance()
        
        # Controlla se è un comando personalizzato
        token_type_str = self.keywords.get(identifier)
        if token_type_str:
            # Converti la stringa in TokenType enum
            token_type = TokenType[token_type_str]
        else:
            token_type = TokenType.IDENTIFIER
        return Token(token_type, identifier, self.line, start_col)
    
    def read_complex_command(self):
        """Legge comandi complessi con simboli (es: int << func >>, <<While>>! <on>)"""
        start_col = self.column
        command = ''
        start_pos = self.pos
        
        # Prova a matchare i comandi complessi
        for keyword, token_type_str in self.keywords.items():
            # Controlla se il codice corrente inizia con questo comando
            if self.code[self.pos:self.pos + len(keyword)] == keyword:
                # Avanza di tutta la lunghezza del comando
                for _ in range(len(keyword)):
                    self.advance()
                # Converti la stringa in TokenType enum
                token_type = TokenType[token_type_str]
                return Token(token_type, keyword, self.line, start_col)
        
        return None
    
    def tokenize(self):
        tokens = []
        
        while self.current_char() is not None:
            self.skip_whitespace()
            
            if self.current_char() is None:
                break
            
            # Commenti
            if self.current_char() == '#':
                self.skip_comment()
                continue
            
            # Newline
            if self.current_char() == '\n':
                tokens.append(Token(TokenType.NEWLINE, '\\n', self.line, self.column))
                self.advance()
                continue
            
            # Prova a leggere comandi complessi prima di tutto
            complex_token = self.read_complex_command()
            if complex_token:
                tokens.append(complex_token)
                continue
            
            # Numeri
            if self.current_char().isdigit():
                tokens.append(self.read_number())
                continue
            
            # Stringhe
            if self.current_char() in '"\'':
                tokens.append(self.read_string())
                continue
            
            # Identificatori e parole chiave semplici
            if self.current_char().isalpha() or self.current_char() == '_':
                tokens.append(self.read_identifier())
                continue
            
            # Operatori
            start_col = self.column
            char = self.current_char()
            
            # Operatori doppi
            if char == '=' and self.peek_char() == '=':
                self.advance()
                self.advance()
                tokens.append(Token(TokenType.EQUAL_EQUAL, '==', self.line, start_col))
                continue
            
            if char == '!' and self.peek_char() == '=':
                self.advance()
                self.advance()
                tokens.append(Token(TokenType.NOT_EQUAL, '!=', self.line, start_col))
                continue
            
            if char == '<' and self.peek_char() == '=':
                self.advance()
                self.advance()
                tokens.append(Token(TokenType.LESS_EQUAL, '<=', self.line, start_col))
                continue
            
            if char == '>' and self.peek_char() == '=':
                self.advance()
                self.advance()
                tokens.append(Token(TokenType.GREATER_EQUAL, '>=', self.line, start_col))
                continue
            
            # << e >>
            if char == '<' and self.peek_char() == '<':
                self.advance()
                self.advance()
                tokens.append(Token(TokenType.DOUBLE_LESS, '<<', self.line, start_col))
                continue
            
            if char == '>' and self.peek_char() == '>':
                self.advance()
                self.advance()
                tokens.append(Token(TokenType.DOUBLE_GREATER, '>>', self.line, start_col))
                continue
            
            # Operatori singoli
            single_char_tokens = {
                '+': TokenType.PLUS,
                '-': TokenType.MINUS,
                '*': TokenType.MULTIPLY,
                '/': TokenType.DIVIDE,
                '%': TokenType.MODULO,
                '=': TokenType.EQUALS,
                '<': TokenType.LESS,
                '>': TokenType.GREATER,
                '(': TokenType.LPAREN,
                ')': TokenType.RPAREN,
                '{': TokenType.LBRACE,
                '}': TokenType.RBRACE,
                '[': TokenType.LBRACKET,
                ']': TokenType.RBRACKET,
                ',': TokenType.COMMA,
                '.': TokenType.DOT,
                '!': TokenType.NOT,
            }
            
            if char in single_char_tokens:
                tokens.append(Token(single_char_tokens[char], char, self.line, start_col))
                self.advance()
                continue
            
            # Carattere non riconosciuto
            tokens.append(Token(TokenType.INVALID, char, self.line, start_col))
            self.advance()
        
        tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return tokens
