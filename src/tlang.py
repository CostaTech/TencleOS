#!/usr/bin/env python3
# TLang - Interprete Principale

import sys
from lexer import Lexer
from tlang_parser import Parser
from interpreter import Interpreter

def run_file(filename, debug=False):
    """Esegue un file .tl/.tlang"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Errore: file '{filename}' non trovato")
        return False
    except Exception as e:
        print(f"Errore durante la lettura del file: {e}")
        return False
    
    # Lexer
    lexer = Lexer(code)
    try:
        tokens = lexer.tokenize()
        if debug:
            print("=== TOKENS ===")
            for token in tokens:
                print(token)
            print()
    except Exception as e:
        print(f"Errore nel lexer: {e}")
        return False
    
    # Parser
    parser = Parser(tokens)
    try:
        ast = parser.parse()
        if debug:
            print("=== AST ===")
            print(ast)
            print()
    except Exception as e:
        print(f"Errore nel parser: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Interpreter
    interpreter = Interpreter()
    try:
        if debug:
            print("=== ESECUZIONE ===")
        success = interpreter.run(ast)
        return success
    except Exception as e:
        print(f"Errore nell'interprete: {e}")
        import traceback
        traceback.print_exc()
        try:
            input("\nPremi INVIO per chiudere...")
        except:
            pass
        return False

def run_repl():
    """REPL interattiva"""
    print("TLang - Linguaggio Personalizzato")
    print("Digita 'exit' per uscire\n")
    
    interpreter = Interpreter()
    
    while True:
        try:
            code = input(">>> ")
            if code.strip().lower() == 'exit':
                break
            
            if not code.strip():
                continue
            
            # Lexer
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            
            # Parser
            parser = Parser(tokens)
            ast = parser.parse()
            
            # Interpreter
            interpreter.run(ast)
            
        except KeyboardInterrupt:
            print("\nUscita...")
            break
        except Exception as e:
            print(f"Errore: {e}")

def main():
    if len(sys.argv) == 1:
        # Modalità REPL
        run_repl()
    elif sys.argv[1] in ('-h', '--help'):
        print("TLang - Linguaggio Personalizzato")
        print()
        print("Uso:")
        print("  python tlang.py              - REPL interattiva")
        print("  python tlang.py file.tlang   - Esegui file")
        print("  python tlang.py -d file.tlang - Debug")
    elif sys.argv[1] == '-d':
        # Modalità debug
        if len(sys.argv) < 3:
            print("Errore: specifica un file da eseguire")
            sys.exit(1)
        filename = sys.argv[2]
        success = run_file(filename, debug=True)
        sys.exit(0 if success else 1)
    else:
        # Esegui file
        filename = sys.argv[1]
        success = run_file(filename, debug=False)
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
