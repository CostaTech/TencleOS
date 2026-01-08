# PARSER - Analizzatore Sintattico

from lexer import Token, TokenType

# ===== NODI AST =====

class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Number({self.value})"

class StringNode(ASTNode):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"String({self.value!r})"

class VariableNode(ASTNode):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Var({self.name})"

class BinaryOpNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    def __repr__(self):
        return f"BinOp({self.left} {self.operator} {self.right})"

class UnaryOpNode(ASTNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
    def __repr__(self):
        return f"UnaryOp({self.operator}{self.operand})"

class PrintNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression
    def __repr__(self):
        return f"Print({self.expression})"

class AssignNode(ASTNode):
    def __init__(self, variable_name, expression):
        self.variable_name = variable_name
        self.expression = expression
    def __repr__(self):
        return f"Assign({self.variable_name} = {self.expression})"

class IfNode(ASTNode):
    def __init__(self, condition, then_block, elif_blocks=None, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.elif_blocks = elif_blocks or []
        self.else_block = else_block
    def __repr__(self):
        return f"If({self.condition})"

class InputNode(ASTNode):
    def __init__(self, prompt=None):
        self.prompt = prompt
    def __repr__(self):
        return "Input()"

class ForNode(ASTNode):
    def __init__(self, variable, iterable, body):
        self.variable = variable
        self.iterable = iterable
        self.body = body
    def __repr__(self):
        return f"For({self.variable} in {self.iterable})"

class BreakNode(ASTNode):
    def __repr__(self):
        return "Break()"

class ContinueNode(ASTNode):
    def __repr__(self):
        return "Continue()"

class FunctionDefNode(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    def __repr__(self):
        return f"FunctionDef({self.name})"

class ReturnNode(ASTNode):
    def __init__(self, expression=None):
        self.expression = expression
    def __repr__(self):
        return f"Return({self.expression})"

class BooleanNode(ASTNode):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Boolean({self.value})"

class LogicalOpNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    def __repr__(self):
        return f"LogicalOp({self.left} {self.operator} {self.right})"

class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f"While({self.condition})"

class ImportNode(ASTNode):
    def __init__(self, module_name):
        self.module_name = module_name
    def __repr__(self):
        return f"Import({self.module_name})"

class FunctionCallNode(ASTNode):
    def __init__(self, function, args):
        self.function = function
        self.args = args
    def __repr__(self):
        return f"FunctionCall({self.function})"

class AttributeAccessNode(ASTNode):
    def __init__(self, object, attribute):
        self.object = object
        self.attribute = attribute
    def __repr__(self):
        return f"AttributeAccess({self.object}.{self.attribute})"

class ListNode(ASTNode):
    def __init__(self, elements):
        self.elements = elements
    def __repr__(self):
        return f"List({len(self.elements)} elements)"

class IndexAccessNode(ASTNode):
    def __init__(self, object, index):
        self.object = object
        self.index = index
    def __repr__(self):
        return f"IndexAccess({self.object}[{self.index}])"

class ClassDefNode(ASTNode):
    def __init__(self, name, methods):
        self.name = name
        self.methods = methods
    def __repr__(self):
        return f"ClassDef({self.name}, {len(self.methods)} methods)"

class BlockNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements
    def __repr__(self):
        return f"Block({len(self.statements)} statements)"

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements
    def __repr__(self):
        return f"Program({len(self.statements)} statements)"


# ===== PARSER =====

class ParseError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]
    
    def peek_token(self, offset=1):
        pos = self.pos + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return self.tokens[-1]
    
    def advance(self):
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
    
    def expect(self, token_type):
        token = self.current_token()
        if token.type != token_type:
            raise ParseError(
                f"Errore di sintassi alla riga {token.line}, colonna {token.column}: "
                f"atteso {token_type}, trovato {token.type}"
            )
        self.advance()
        return token
    
    def skip_newlines(self):
        while self.current_token().type == TokenType.NEWLINE:
            self.advance()
    
    def parse_primary(self):
        self.skip_newlines()
        token = self.current_token()
        
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        
        if token.type == TokenType.STRING:
            self.advance()
            return StringNode(token.value)
        
        if token.type == TokenType.TRUE:
            self.advance()
            return BooleanNode(True)
        
        if token.type == TokenType.FALSE:
            self.advance()
            return BooleanNode(False)
        
        if token.type == TokenType.LBRACKET:
            return self.parse_list()
        
        if token.type == TokenType.IDENTIFIER:
            name = token.value
            self.advance()
            node = VariableNode(name)
            
            # Gestione chiamate funzione, accesso attributi, indicizzazione
            while True:
                if self.current_token().type == TokenType.LPAREN:
                    # Chiamata funzione: func()
                    self.advance()
                    args = []
                    if self.current_token().type != TokenType.RPAREN:
                        args.append(self.parse_expression())
                        while self.current_token().type == TokenType.COMMA:
                            self.advance()
                            args.append(self.parse_expression())
                    self.expect(TokenType.RPAREN)
                    node = FunctionCallNode(node, args)
                elif self.current_token().type == TokenType.DOT:
                    # Accesso attributi: obj.attr
                    self.advance()
                    attr_token = self.expect(TokenType.IDENTIFIER)
                    node = AttributeAccessNode(node, attr_token.value)
                elif self.current_token().type == TokenType.LBRACKET:
                    # Indicizzazione: list[0]
                    self.advance()
                    index = self.parse_expression()
                    self.expect(TokenType.RBRACKET)
                    node = IndexAccessNode(node, index)
                else:
                    break
            
            return node
        
        if token.type == TokenType.INPUT:
            return self.parse_input_statement()
        
        if token.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr
        
        if token.type in (TokenType.PLUS, TokenType.MINUS):
            op = token.value
            self.advance()
            operand = self.parse_primary()
            return UnaryOpNode(op, operand)
        
        if token.type == TokenType.NOT:
            self.advance()
            operand = self.parse_primary()
            return UnaryOpNode('not', operand)
        
        raise ParseError(
            f"Errore di sintassi alla riga {token.line}: "
            f"espressione non valida"
        )
    
    def parse_list(self):
        self.expect(TokenType.LBRACKET)
        elements = []
        
        if self.current_token().type != TokenType.RBRACKET:
            elements.append(self.parse_expression())
            while self.current_token().type == TokenType.COMMA:
                self.advance()
                elements.append(self.parse_expression())
        
        self.expect(TokenType.RBRACKET)
        return ListNode(elements)
    
    def parse_multiplication(self):
        left = self.parse_primary()
        
        while self.current_token().type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            op = self.current_token().value
            self.advance()
            right = self.parse_primary()
            left = BinaryOpNode(left, op, right)
        
        return left
    
    def parse_addition(self):
        left = self.parse_multiplication()
        
        while self.current_token().type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token().value
            self.advance()
            right = self.parse_multiplication()
            left = BinaryOpNode(left, op, right)
        
        return left
    
    def parse_comparison(self):
        left = self.parse_addition()
        
        comparison_ops = (
            TokenType.EQUAL_EQUAL, TokenType.NOT_EQUAL,
            TokenType.LESS, TokenType.GREATER,
            TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL
        )
        
        if self.current_token().type in comparison_ops:
            op = self.current_token().value
            self.advance()
            right = self.parse_addition()
            left = BinaryOpNode(left, op, right)
        
        return left
    
    def parse_logical(self):
        left = self.parse_comparison()
        
        while self.current_token().type in (TokenType.AND, TokenType.OR):
            op = 'and' if self.current_token().type == TokenType.AND else 'or'
            self.advance()
            right = self.parse_comparison()
            left = LogicalOpNode(left, op, right)
        
        return left
    
    def parse_expression(self):
        return self.parse_logical()
    
    def parse_print_statement(self):
        """Parse: COMANDO_PRINT(expression) - es: int << func >> (expression)"""
        self.expect(TokenType.PRINT)
        self.expect(TokenType.LPAREN)
        
        # Supporta multipli argomenti separati da virgola
        expressions = []
        if self.current_token().type != TokenType.RPAREN:
            expressions.append(self.parse_expression())
            while self.current_token().type == TokenType.COMMA:
                self.advance()  # salta la virgola
                expressions.append(self.parse_expression())
        
        self.expect(TokenType.RPAREN)
        
        # Se c'è un solo argomento, ritorna come prima per compatibilità
        if len(expressions) == 1:
            return PrintNode(expressions[0])
        else:
            # Per multipli argomenti, crea un nodo che li stampa tutti
            return PrintNode(expressions)
    
    def parse_input_statement(self):
        """Parse: COMANDO_INPUT() - es: input()"""
        self.expect(TokenType.INPUT)
        self.expect(TokenType.LPAREN)
        prompt = None
        if self.current_token().type != TokenType.RPAREN:
            prompt = self.parse_expression()
        self.expect(TokenType.RPAREN)
        return InputNode(prompt)
    
    def parse_assignment(self):
        # Può essere una variabile semplice o un accesso attributo (self.x)
        if self.current_token().type == TokenType.IDENTIFIER:
            first_part = self.current_token().value
            self.advance()
            
            # Se c'è un punto, è un accesso attributo
            if self.current_token().type == TokenType.DOT:
                self.advance()
                if self.current_token().type != TokenType.IDENTIFIER:
                    raise ParseError("Atteso nome attributo dopo '.'")
                attr_name = self.current_token().value
                self.advance()
                
                # Supporta anche più livelli (self.x.y)
                full_path = f"{first_part}.{attr_name}"
                while self.current_token().type == TokenType.DOT:
                    self.advance()
                    if self.current_token().type != TokenType.IDENTIFIER:
                        raise ParseError("Atteso nome attributo dopo '.'")
                    full_path += f".{self.current_token().value}"
                    self.advance()
                
                self.expect(TokenType.EQUALS)
                expression = self.parse_expression()
                return AssignNode(full_path, expression)
            else:
                # Assegnazione semplice
                self.expect(TokenType.EQUALS)
                expression = self.parse_expression()
                return AssignNode(first_part, expression)
        else:
            raise ParseError(f"Atteso identificatore nell'assegnazione")
    
    def parse_if_statement(self):
        self.expect(TokenType.IF)
        condition = self.parse_expression()
        self.skip_newlines()
        then_block = self.parse_block()
        
        elif_blocks = []
        else_block = None
        
        self.skip_newlines()
        while self.current_token().type == TokenType.ELIF:
            self.advance()
            elif_condition = self.parse_expression()
            self.skip_newlines()
            elif_body = self.parse_block()
            elif_blocks.append((elif_condition, elif_body))
            self.skip_newlines()
        
        if self.current_token().type == TokenType.ELSE:
            self.advance()
            self.skip_newlines()
            else_block = self.parse_block()
        
        return IfNode(condition, then_block, elif_blocks, else_block)
    
    def parse_while_statement(self):
        """Parse: COMANDO_WHILE condition { body }"""
        self.expect(TokenType.WHILE)
        condition = self.parse_expression()
        self.skip_newlines()
        body = self.parse_block()
        return WhileNode(condition, body)
    
    def parse_for_statement(self):
        """Parse: COMANDO_FOR variable in iterable { body }"""
        self.expect(TokenType.FOR)
        
        if self.current_token().type != TokenType.IDENTIFIER:
            raise ParseError(f"Atteso nome variabile dopo for")
        var_name = self.current_token().value
        self.advance()
        
        # Cerca 'in' (può essere una keyword o identificatore)
        if self.current_token().type == TokenType.IDENTIFIER and self.current_token().value == 'in':
            self.advance()
        else:
            raise ParseError(f"Atteso 'in' nel for loop")
        
        iterable = self.parse_expression()
        self.skip_newlines()
        body = self.parse_block()
        
        return ForNode(var_name, iterable, body)
    
    def parse_function_def(self):
        """Parse: COMANDO_DEF name(params) { body }"""
        self.expect(TokenType.DEF)
        
        if self.current_token().type != TokenType.IDENTIFIER:
            raise ParseError(f"Atteso nome funzione")
        func_name = self.current_token().value
        self.advance()
        
        self.expect(TokenType.LPAREN)
        params = []
        while self.current_token().type != TokenType.RPAREN:
            if self.current_token().type != TokenType.IDENTIFIER:
                raise ParseError(f"Atteso nome parametro")
            params.append(self.current_token().value)
            self.advance()
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        self.expect(TokenType.RPAREN)
        
        self.skip_newlines()
        body = self.parse_block()
        
        return FunctionDefNode(func_name, params, body)
    
    def parse_class_def(self):
        """Parse: << CRT >>! >class<ClassName { methods }"""
        self.expect(TokenType.CLASS)
        
        if self.current_token().type != TokenType.IDENTIFIER:
            raise ParseError(f"Atteso nome classe")
        class_name = self.current_token().value
        self.advance()
        
        self.skip_newlines()
        self.expect(TokenType.LBRACE)
        self.skip_newlines()
        
        methods = []
        while self.current_token().type != TokenType.RBRACE:
            if self.current_token().type == TokenType.EOF:
                raise ParseError("Errore: classe non chiusa, manca }")
            
            # Salta newline
            if self.current_token().type == TokenType.NEWLINE:
                self.advance()
                continue
            
            # Ogni metodo inizia con DEF (che corrisponde a << ! C>> New command:)
            if self.current_token().type == TokenType.DEF:
                method = self.parse_function_def()
                methods.append(method)
            else:
                # Token non riconosciuto dentro la classe
                raise ParseError(f"Errore: token inaspettato dentro la classe: {self.current_token().type}")
        
        self.expect(TokenType.RBRACE)
        return ClassDefNode(class_name, methods)
    
    def parse_block(self):
        self.expect(TokenType.LBRACE)
        self.skip_newlines()
        
        statements = []
        while self.current_token().type != TokenType.RBRACE:
            if self.current_token().type == TokenType.EOF:
                raise ParseError("Errore: blocco non chiuso, manca }")
            
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        
        self.expect(TokenType.RBRACE)
        return BlockNode(statements)
    
    def parse_import_statement(self):
        """Parse: COMANDO_IMPORT module_name"""
        self.expect(TokenType.IMPORT)
        
        if self.current_token().type != TokenType.IDENTIFIER:
            raise ParseError(f"Atteso nome modulo dopo import")
        module_name = self.current_token().value
        self.advance()
        
        return ImportNode(module_name)
    
    def parse_statement(self):
        self.skip_newlines()
        token = self.current_token()
        
        if token.type in (TokenType.EOF, TokenType.RBRACE):
            return None
        
        # Skip << ! >func> markers before statements
        if token.type == TokenType.DOUBLE_LESS:
            # Skip the marker tokens (<<, !, >func>)
            while self.current_token().type not in (TokenType.IF, TokenType.WHILE, TokenType.FOR, TokenType.EOF):
                self.advance()
                if self.pos >= len(self.tokens):
                    break
            token = self.current_token()
            
            # Check EOF again after skipping
            if token.type == TokenType.EOF:
                return None
        
        if token.type == TokenType.PRINT:
            return self.parse_print_statement()
        
        if token.type == TokenType.IF:
            return self.parse_if_statement()
        
        if token.type == TokenType.WHILE:
            return self.parse_while_statement()
        
        if token.type == TokenType.FOR:
            return self.parse_for_statement()
        
        if token.type == TokenType.DEF:
            return self.parse_function_def()
        
        if token.type == TokenType.CLASS:
            return self.parse_class_def()
        
        if token.type == TokenType.IMPORT:
            return self.parse_import_statement()
        
        if token.type == TokenType.BREAK:
            self.advance()
            return BreakNode()
        
        if token.type == TokenType.CONTINUE:
            self.advance()
            return ContinueNode()
        
        if token.type == TokenType.RETURN:
            self.advance()
            expr = None
            if self.current_token().type not in (TokenType.NEWLINE, TokenType.EOF, TokenType.RBRACE):
                expr = self.parse_expression()
            return ReturnNode(expr)
        
        if token.type == TokenType.IDENTIFIER:
            # Controlla se è un'assegnazione (var = o self.attr =)
            if self.peek_token().type == TokenType.EQUALS:
                return self.parse_assignment()
            elif self.peek_token().type == TokenType.DOT:
                # Potrebbe essere self.x = valore
                # Salva posizione e prova a parsare come assegnazione
                saved_pos = self.pos
                try:
                    # Prova a parsare come assegnazione attributo
                    return self.parse_assignment()
                except:
                    # Se fallisce, ripristina e tratta come expression
                    self.pos = saved_pos
                    expr = self.parse_expression()
                    return expr
            else:
                # Chiamata di funzione standalone o altra expression
                expr = self.parse_expression()
                return expr
        
        if token.type == TokenType.VAR:
            self.advance()
            return self.parse_assignment()
        
        raise ParseError(
            f"Errore di sintassi alla riga {token.line}: "
            f"statement non riconosciuto (token: {token.type})"
        )
    
    def parse(self):
        statements = []
        self.skip_newlines()
        
        while self.current_token().type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        
        return ProgramNode(statements)
