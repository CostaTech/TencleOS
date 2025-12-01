# TLANG - Il tuo linguaggio di programmazione personalizzato

import sys
from lexer import Lexer, TokenType
from tlang_parser import Parser, ParseError
from interpreter import Interpreter, RuntimeError as TLangRuntimeError

def run_code(code, debug=False):
    if debug:
        print("===== CODICE =====")
        print(code)
        print("\n===== ESECUZIONE =====\n")
    
    try:
        # Fase 1: Lexing
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        # Controlla token invalidi
        invalid_tokens = [t for t in tokens if t.type == TokenType.INVALID]
        if invalid_tokens:
            for token in invalid_tokens:
                print(f"ERRORE LESSICALE alla riga {token.line}, colonna {token.column}: "
                      f"carattere '{token.value}' non riconosciuto")
            return False
        
        # Fase 2: Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Fase 3: Interpretazione
        interpreter = Interpreter()
        success = interpreter.run(ast)
        
        if debug:
            print(f"\n===== VARIABILI FINALI =====")
            print(interpreter.variables)
        
        return success
        
    except ParseError as e:
        print(f"ERRORE DI SINTASSI: {e}")
        return False
    except TLangRuntimeError as e:
        print(f"ERRORE RUNTIME: {e}")
        return False
    except Exception as e:
        print(f"ERRORE: {e}")
        if debug:
            import traceback
            traceback.print_exc()
        return False

def run_file(filename, debug=False):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        
        return run_code(code, debug)
        
    except FileNotFoundError:
        print(f"ERRORE: File '{filename}' non trovato")
        return False
    except Exception as e:
        print(f"ERRORE lettura file: {e}")
        return False

def repl():
    print("=" * 50)
    print("TLANG - Linguaggio Personalizzato")
    print("=" * 50)
    print("Comandi REPL:")
    print("  exit/quit - Esci")
    print("  vars      - Mostra variabili")
    print("  clear     - Pulisci variabili")
    print("=" * 50)
    print()
    
    interpreter = Interpreter()
    
    while True:
        try:
            line = input(">>> ")
            
            if line.strip() in ('exit', 'quit'):
                print("Arrivederci!")
                break
            
            if line.strip() == 'vars':
                if interpreter.variables:
                    print("Variabili:")
                    for name, value in interpreter.variables.items():
                        print(f"  {name} = {value}")
                else:
                    print("Nessuna variabile")
                continue
            
            if line.strip() == 'clear':
                interpreter.variables.clear()
                print("Variabili pulite")
                continue
            
            if not line.strip():
                continue
            
            lexer = Lexer(line)
            tokens = lexer.tokenize()
            
            invalid_tokens = [t for t in tokens if t.type == TokenType.INVALID]
            if invalid_tokens:
                for token in invalid_tokens:
                    print(f"Errore: carattere '{token.value}' non riconosciuto")
                continue
            
            parser = Parser(tokens)
            ast = parser.parse()
            
            for statement in ast.statements:
                try:
                    interpreter.visit(statement)
                except TLangRuntimeError as e:
                    print(f"Errore: {e}")
                    break
        
        except ParseError as e:
            print(f"Errore di sintassi: {e}")
        except KeyboardInterrupt:
            print("\nUsa 'exit' per uscire")
        except EOFError:
            print("\nArrivederci!")
            break
        except Exception as e:
            print(f"Errore: {e}")

def main():
    if len(sys.argv) == 1:
        repl()
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        if filename in ('-h', '--help'):
            print("TLang - Linguaggio Personalizzato")
            print("\nUso:")
            print("  python tlang.py              - REPL interattiva")
            print("  python tlang.py file.tlang   - Esegui file")
            print("  python tlang.py -d file.tlang - Debug")
            return
        run_file(filename)
    elif len(sys.argv) == 3 and sys.argv[1] in ('-d', '--debug'):
        run_file(sys.argv[2], debug=True)
    else:
        print("Uso: python tlang.py [file]")

if __name__ == "__main__":
    main()
