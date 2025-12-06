# INTERPRETER - Esecutore

from tlang_parser import *

class RuntimeError(Exception):
    pass

class BreakException(Exception):
    """Eccezione per break"""
    pass

class ContinueException(Exception):
    """Eccezione per continue"""
    pass

class ReturnException(Exception):
    """Eccezione per return"""
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self):
        self.variables = {}
    
    def visit_NumberNode(self, node):
        return node.value
    
    def visit_StringNode(self, node):
        return node.value
    
    def visit_BooleanNode(self, node):
        return node.value
    
    def visit_VariableNode(self, node):
        var_name = node.name
        
        if var_name not in self.variables:
            raise RuntimeError(f"Errore: variabile '{var_name}' non definita")
        
        return self.variables[var_name]
    
    def visit_BinaryOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = node.operator
        
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                raise RuntimeError("Errore: divisione per zero")
            return left / right
        elif op == '%':
            return left % right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
        else:
            raise RuntimeError(f"Errore: operatore '{op}' non supportato")
    
    def visit_LogicalOpNode(self, node):
        left = self.visit(node.left)
        op = node.operator
        
        if op == 'and':
            if not left:
                return False
            return self.visit(node.right)
        elif op == 'or':
            if left:
                return True
            return self.visit(node.right)
        else:
            raise RuntimeError(f"Errore: operatore logico '{op}' non supportato")
    
    def visit_UnaryOpNode(self, node):
        operand = self.visit(node.operand)
        op = node.operator
        
        if op == '-':
            return -operand
        elif op == '+':
            return +operand
        elif op == 'not':
            return not operand
        else:
            raise RuntimeError(f"Errore: operatore unario '{op}' non supportato")
    
    def visit_PrintNode(self, node):
        value = self.visit(node.expression)
        import sys
        sys.stdout.write(str(value) + '\n')
        sys.stdout.flush()
        return None
    
    def visit_InputNode(self, node):
        prompt = ""
        if node.prompt:
            prompt = str(self.visit(node.prompt))
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            try:
                return float(user_input)
            except ValueError:
                return user_input
    
    def visit_AssignNode(self, node):
        var_name = node.variable_name
        value = self.visit(node.expression)
        self.variables[var_name] = value
        return None
    
    def visit_AttributeAssignNode(self, node):
        """Assegnamento attributo: self.x = value"""
        obj = self.visit(node.object)
        attr_name = node.attribute
        value = self.visit(node.expression)
        
        # Se è istanza TLang
        if isinstance(obj, dict) and '__class_body__' in obj:
            obj[attr_name] = value
            return None
        
        # Altrimenti usa setattr Python
        try:
            setattr(obj, attr_name, value)
        except Exception as e:
            raise RuntimeError(f"Errore: impossibile settare attributo '{attr_name}': {e}")
        return None
    
    def visit_IfNode(self, node):
        condition = self.visit(node.condition)
        
        if condition:
            self.visit(node.then_block)
        else:
            # Controlla elif
            elif_executed = False
            for elif_cond, elif_body in node.elif_blocks:
                if self.visit(elif_cond):
                    self.visit(elif_body)
                    elif_executed = True
                    break
            
            # Se nessun elif è stato eseguito, esegui else
            if not elif_executed and node.else_block:
                self.visit(node.else_block)
        
        return None
    
    def visit_WhileNode(self, node):
        max_iterations = 10000000
        iterations = 0
        
        while self.visit(node.condition):
            iterations += 1
            if iterations > max_iterations:
                raise RuntimeError(
                    f"Errore: loop superato il limite di {max_iterations} iterazioni"
                )
            
            try:
                self.visit(node.body)
            except BreakException:
                break
            except ContinueException:
                continue
        
        return None
    
    def visit_ForNode(self, node):
        iterable = self.visit(node.iterable)
        
        # Se è un numero, crea un range
        if isinstance(iterable, (int, float)):
            iterable = range(int(iterable))
        
        for value in iterable:
            self.variables[node.variable] = value
            try:
                self.visit(node.body)
            except BreakException:
                break
            except ContinueException:
                continue
        
        return None
    
    def visit_BreakNode(self, node):
        raise BreakException()
    
    def visit_ContinueNode(self, node):
        raise ContinueException()
    
    def visit_FunctionDefNode(self, node):
        # Salva la funzione nel dizionario delle variabili
        self.variables[node.name] = ('function', node.params, node.body)
        return None
    
    def visit_ClassDefNode(self, node):
        # Salva la classe (nome e corpo)
        self.variables[node.name] = ('class', node.body)
        return None
    
    def visit_ReturnNode(self, node):
        value = None
        if node.expression:
            value = self.visit(node.expression)
        raise ReturnException(value)
    
    def visit_BlockNode(self, node):
        for statement in node.statements:
            self.visit(statement)
        return None
    
    def visit_ImportNode(self, node):
        """Import modulo Python"""
        module_name = node.module_name
        try:
            # Importa il modulo Python
            import importlib
            module = importlib.import_module(module_name)
            # Salva il modulo nelle variabili
            self.variables[module_name] = module
            return None
        except ImportError as e:
            raise RuntimeError(f"Errore: impossibile importare modulo '{module_name}': {e}")
    
    def visit_FunctionCallNode(self, node):
        """Chiamata funzione o creazione istanza classe"""
        # Valuta la funzione (può essere una variabile o un accesso attributo)
        function = self.visit(node.function)
        
        # Valuta gli argomenti
        args = [self.visit(arg) for arg in node.args]
        
        # Se è una classe TLang -> crea istanza
        if isinstance(function, tuple) and function[0] == 'class':
            _, class_body = function
            
            # Crea istanza (dizionario per attributi)
            instance = {'__class_body__': class_body, '__methods__': {}}
            
            # Estrai metodi dal corpo della classe
            for stmt in class_body.statements:
                if isinstance(stmt, FunctionDefNode):
                    instance['__methods__'][stmt.name] = (stmt.params, stmt.body)
            
            # Chiama __init__ se esiste
            if '__init__' in instance['__methods__']:
                params, body = instance['__methods__']['__init__']
                
                # Crea scope con self
                old_vars = self.variables.copy()
                self.variables['self'] = instance
                
                # Assegna parametri (salta self perché è già settato)
                if len(args) != len(params) - 1:
                    raise RuntimeError(f"Errore: __init__ richiede {len(params)-1} argomenti, ne sono stati passati {len(args)}")
                
                for param, arg in zip(params[1:], args):
                    self.variables[param] = arg
                
                # Esegui __init__
                try:
                    self.visit(body)
                except ReturnException:
                    pass
                
                # Ripristina scope
                self.variables = old_vars
            
            return instance
        
        # Se è un metodo bound (con self)
        if isinstance(function, tuple) and function[0] == 'bound_method':
            _, instance, params, body = function
            
            # Crea scope con self
            old_vars = self.variables.copy()
            self.variables['self'] = instance
            
            # Assegna parametri (salta self)
            if len(args) != len(params) - 1:
                raise RuntimeError(f"Errore: metodo richiede {len(params)-1} argomenti, ne sono stati passati {len(args)}")
            
            for param, arg in zip(params[1:], args):
                self.variables[param] = arg
            
            # Esegui metodo
            result = None
            try:
                self.visit(body)
            except ReturnException as e:
                result = e.value
            
            # Ripristina scope
            self.variables = old_vars
            return result
        
        # Se è una funzione TLang
        if isinstance(function, tuple) and function[0] == 'function':
            _, params, body = function
            
            # Crea nuovo scope (semplificato - salva scope precedente)
            old_vars = self.variables.copy()
            
            # Assegna parametri
            if len(args) != len(params):
                raise RuntimeError(f"Errore: funzione richiede {len(params)} argomenti, ne sono stati passati {len(args)}")
            
            for param, arg in zip(params, args):
                self.variables[param] = arg
            
            # Esegui corpo funzione
            result = None
            try:
                self.visit(body)
            except ReturnException as e:
                result = e.value
            
            # Ripristina scope
            self.variables = old_vars
            return result
        
        # Altrimenti è una funzione Python
        try:
            return function(*args)
        except Exception as e:
            raise RuntimeError(f"Errore nella chiamata funzione: {e}")
    
    def visit_AttributeAccessNode(self, node):
        """Accesso attributo/metodo di un oggetto"""
        obj = self.visit(node.object)
        attr_name = node.attribute
        
        # Se è un'istanza TLang
        if isinstance(obj, dict) and '__class_body__' in obj:
            # Controlla se è un metodo
            if attr_name in obj['__methods__']:
                params, body = obj['__methods__'][attr_name]
                # Ritorna funzione bound con self
                return ('bound_method', obj, params, body)
            # Altrimenti è un attributo
            if attr_name in obj:
                return obj[attr_name]
            raise RuntimeError(f"Errore: istanza non ha attributo '{attr_name}'")
        
        # Altrimenti usa getattr di Python
        try:
            return getattr(obj, attr_name)
        except AttributeError:
            raise RuntimeError(f"Errore: oggetto non ha attributo '{attr_name}'")
    
    def visit_ListNode(self, node):
        """Lista"""
        return [self.visit(elem) for elem in node.elements]
    
    def visit_IndexAccessNode(self, node):
        """Accesso indice di lista/array"""
        obj = self.visit(node.object)
        index = self.visit(node.index)
        
        try:
            return obj[int(index)]
        except (IndexError, KeyError) as e:
            raise RuntimeError(f"Errore: indice {index} non valido: {e}")
        except TypeError:
            raise RuntimeError(f"Errore: oggetto non supporta indicizzazione")
    
    def visit_ProgramNode(self, node):
        for statement in node.statements:
            self.visit(statement)
        return None
    
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)
    
    def generic_visit(self, node):
        raise RuntimeError(f"Errore: nodo {type(node).__name__} non implementato")
    
    def run(self, ast):
        try:
            self.visit(ast)
            return True
        except RuntimeError as e:
            print(f"ERRORE RUNTIME: {e}")
            return False
        except Exception as e:
            print(f"ERRORE INTERNO: {e}")
            import traceback
            traceback.print_exc()
            return False
