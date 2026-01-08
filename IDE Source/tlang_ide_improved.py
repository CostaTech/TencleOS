"""
TLang IDE - Integrated Development Environment
Editor completo per il linguaggio TLang
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import sys
import io
import os
import threading
from contextlib import redirect_stdout, redirect_stderr

# Import TLang components
from lexer import Lexer, TokenType
from tlang_parser import Parser, ParseError
from interpreter import Interpreter, RuntimeError as TLangRuntimeError

class TLangIDE:
    def __init__(self, root, initial_file=None):
        self.root = root
        self.root.title("TLang IDE")
        self.root.geometry("1200x800")
        
        # *** AGGIUNGI ICON.ICO ***
        try:
            icon_path = os.path.join("TencleOS-GitHub", "System", "icon.ico")
            if not os.path.exists(icon_path):
                icon_path = os.path.join("System", "icon.ico")
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Impossibile caricare icon.ico: {e}")
        
        # File corrente
        self.current_file = None
        self.file_modified = False
        
        # *** TEMI DISPONIBILI ***
        self.themes = {
            "Dark": {
                "bg_dark": "#1e1e1e",
                "bg_editor": "#252526",
                "bg_toolbar": "#2d2d30",
                "fg_text": "#d4d4d4",
                "fg_keyword": "#569cd6",
                "fg_string": "#ce9178",
                "fg_comment": "#6a9955",
                "fg_number": "#b5cea8",
                "fg_linenumbers": "#858585"
            },
            "Light": {
                "bg_dark": "#ffffff",
                "bg_editor": "#ffffff",
                "bg_toolbar": "#f3f3f3",
                "fg_text": "#000000",
                "fg_keyword": "#0000ff",
                "fg_string": "#a31515",
                "fg_comment": "#008000",
                "fg_number": "#098658",
                "fg_linenumbers": "#858585"
            },
            "Monokai": {
                "bg_dark": "#272822",
                "bg_editor": "#272822",
                "bg_toolbar": "#1e1f1c",
                "fg_text": "#f8f8f2",
                "fg_keyword": "#f92672",
                "fg_string": "#e6db74",
                "fg_comment": "#75715e",
                "fg_number": "#ae81ff",
                "fg_linenumbers": "#75715e"
            },
            "Matrix": {
                "bg_dark": "#000000",
                "bg_editor": "#000000",
                "bg_toolbar": "#001100",
                "fg_text": "#00ff00",
                "fg_keyword": "#00ff00",
                "fg_string": "#00ff00",
                "fg_comment": "#008800",
                "fg_number": "#00ff00",
                "fg_linenumbers": "#008800"
            },
            "BASIC": {
                "bg_dark": "#0000aa",
                "bg_editor": "#0000aa",
                "bg_toolbar": "#000088",
                "fg_text": "#ffff55",
                "fg_keyword": "#ffffff",
                "fg_string": "#55ffff",
                "fg_comment": "#aaaaaa",
                "fg_number": "#55ff55",
                "fg_linenumbers": "#aaaaaa"
            }
        }
        
        self.current_theme = "Dark"
        
        # Tema colori (inizializzato con Dark)
        self.bg_dark = "#1e1e1e"
        self.bg_editor = "#252526"
        self.bg_toolbar = "#2d2d30"
        self.fg_text = "#d4d4d4"
        self.fg_keyword = "#569cd6"
        self.fg_string = "#ce9178"
        self.fg_comment = "#6a9955"
        self.fg_number = "#b5cea8"
        self.fg_linenumbers = "#858585"
        
        # *** AUTOCOMPLETE SETUP ***
        self.autocomplete_window = None
        self.autocomplete_list = None
        self.autocomplete_visible = False
        
        # TLang keywords for autocomplete
        self.tlang_keywords = [
            '<< ! C>> New command: nome(params)',
            'int << func >>',
            '<<While>>! <on>',
            '<< ! >func> if',
            '<< CRT >>! >class<',
            '>> func << else',
            'use',
            'var',
            '<<For>>! x <in> range',
            'in',
            'on',
            'off',
            'and',
            'or',
            'not',
            'elif',
            'stop',
            'continue',
            'return',
            'print',
            'input',
            'None'
        ]
        
        self.setup_ui()
        self.setup_menu()
        self.setup_bindings()
        self.setup_autocomplete()
        
        # Se viene passato un file, aprilo
        if initial_file and os.path.exists(initial_file):
            self.load_file(initial_file)
        else:
            self.new_file()
        
    def setup_ui(self):
        # Menu bar (creato in setup_menu)
        
        # Toolbar
        toolbar = tk.Frame(self.root, bg="#2d2d30", height=40)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Bottoni toolbar
        btn_new = tk.Button(toolbar, text="Nuovo", command=self.new_file, 
                           bg="#2d2d30", fg="white", relief=tk.FLAT, padx=10)
        btn_new.pack(side=tk.LEFT, padx=5, pady=5)
        
        btn_open = tk.Button(toolbar, text="Apri", command=self.open_file,
                            bg="#2d2d30", fg="white", relief=tk.FLAT, padx=10)
        btn_open.pack(side=tk.LEFT, padx=5, pady=5)
        
        btn_save = tk.Button(toolbar, text="Salva", command=self.save_file,
                            bg="#2d2d30", fg="white", relief=tk.FLAT, padx=10)
        btn_save.pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Frame(toolbar, width=2, bg="#3e3e42").pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        btn_run = tk.Button(toolbar, text="Esegui", command=self.run_code,
                           bg="#0e639c", fg="white", relief=tk.FLAT, padx=15,
                           font=("Arial", 10, "bold"))
        btn_run.pack(side=tk.LEFT, padx=5, pady=5)
        
        btn_debug = tk.Button(toolbar, text="Debug", command=self.debug_code,
                             bg="#4d4d30", fg="white", relief=tk.FLAT, padx=10)
        btn_debug.pack(side=tk.LEFT, padx=5, pady=5)
        
        btn_stop = tk.Button(toolbar, text="Stop", command=self.stop_execution,
                            bg="#b30000", fg="white", relief=tk.FLAT, padx=10)
        btn_stop.pack(side=tk.LEFT, padx=5, pady=5)
        
        # File label
        self.file_label = tk.Label(toolbar, text="Nuovo file", 
                                   bg="#2d2d30", fg="#888888", 
                                   font=("Arial", 9, "italic"))
        self.file_label.pack(side=tk.RIGHT, padx=10)
        
        # Main container
        main_container = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, 
                                       bg="#1e1e1e", sashwidth=5)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Editor
        editor_frame = tk.Frame(main_container, bg=self.bg_dark)
        main_container.add(editor_frame, width=800)
        
        # Line numbers
        line_frame = tk.Frame(editor_frame, bg="#1e1e1e")
        line_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.line_numbers = tk.Text(line_frame, width=4, padx=5, pady=10,
                                    bg="#1e1e1e", fg="#858585",
                                    font=("Consolas", 11),
                                    state=tk.DISABLED, relief=tk.FLAT)
        self.line_numbers.pack(fill=tk.BOTH, expand=True)
        
        # Editor
        self.editor = scrolledtext.ScrolledText(editor_frame, 
                                               wrap=tk.NONE,
                                               bg=self.bg_editor,
                                               fg=self.fg_text,
                                               insertbackground="white",
                                               font=("Consolas", 11),
                                               padx=10, pady=10,
                                               undo=True, maxundo=-1,
                                               relief=tk.FLAT)
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Right panel - Output & Debug
        right_panel = tk.Frame(main_container, bg=self.bg_dark)
        main_container.add(right_panel, width=400)
        
        # Tabs per output
        self.notebook = ttk.Notebook(right_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab Output
        output_frame = tk.Frame(self.notebook, bg=self.bg_dark)
        self.notebook.add(output_frame, text="Output")
        
        tk.Label(output_frame, text="Output Console", 
                bg="#2d2d30", fg="white", 
                font=("Arial", 10, "bold"), pady=5).pack(fill=tk.X)
        
        self.output_text = scrolledtext.ScrolledText(output_frame,
                                                     bg="#1e1e1e",
                                                     fg="#cccccc",
                                                     font=("Consolas", 10),
                                                     padx=10, pady=10,
                                                     state=tk.DISABLED,
                                                     relief=tk.FLAT)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tab Debug
        debug_frame = tk.Frame(self.notebook, bg=self.bg_dark)
        self.notebook.add(debug_frame, text="Debug")
        
        tk.Label(debug_frame, text="Informazioni Debug", 
                bg="#2d2d30", fg="white", 
                font=("Arial", 10, "bold"), pady=5).pack(fill=tk.X)
        
        self.debug_text = scrolledtext.ScrolledText(debug_frame,
                                                    bg="#1e1e1e",
                                                    fg="#d7ba7d",
                                                    font=("Consolas", 9),
                                                    padx=10, pady=10,
                                                    state=tk.DISABLED,
                                                    relief=tk.FLAT)
        self.debug_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tab Variabili
        vars_frame = tk.Frame(self.notebook, bg=self.bg_dark)
        self.notebook.add(vars_frame, text="Variabili")
        
        tk.Label(vars_frame, text="Variabili Runtime", 
                bg="#2d2d30", fg="white", 
                font=("Arial", 10, "bold"), pady=5).pack(fill=tk.X)
        
        self.vars_text = scrolledtext.ScrolledText(vars_frame,
                                                   bg="#1e1e1e",
                                                   fg="#4ec9b0",
                                                   font=("Consolas", 10),
                                                   padx=10, pady=10,
                                                   state=tk.DISABLED,
                                                   relief=tk.FLAT)
        self.vars_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Status bar
        self.status_bar = tk.Label(self.root, text="Pronto", 
                                  bg="#007acc", fg="white", 
                                  anchor=tk.W, padx=10, pady=3,
                                  font=("Arial", 9))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def setup_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Nuovo", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Apri...", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Salva", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Salva come...", command=self.save_file_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Esci", command=self.quit_ide)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Modifica", menu=edit_menu)
        edit_menu.add_command(label="Annulla", command=lambda: self.editor.edit_undo(), accelerator="Ctrl+Z")
        edit_menu.add_command(label="Ripeti", command=lambda: self.editor.edit_redo(), accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Taglia", command=lambda: self.editor.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        edit_menu.add_command(label="Copia", command=lambda: self.editor.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        edit_menu.add_command(label="Incolla", command=lambda: self.editor.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Autocomplete", command=self.show_autocomplete, accelerator="Ctrl+Space")
        
        # View menu (Temi)
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Visualizza", menu=view_menu)
        
        theme_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label="Tema", menu=theme_menu)
        
        for theme_name in self.themes.keys():
            theme_menu.add_command(
                label=theme_name,
                command=lambda t=theme_name: self.change_theme(t)
            )
        
        # Run menu
        run_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Esegui", menu=run_menu)
        run_menu.add_command(label="Esegui", command=self.run_code, accelerator="F5")
        run_menu.add_command(label="Debug", command=self.debug_code, accelerator="F6")
        run_menu.add_command(label="Stop", command=self.stop_execution, accelerator="F8")
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Aiuto", menu=help_menu)
        help_menu.add_command(label="Sintassi TLang", command=self.show_syntax_help)
        help_menu.add_command(label="Info IDE", command=self.show_about)
        
    def setup_bindings(self):
        # Keyboard shortcuts
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda e: self.save_file_as())
        self.root.bind("<F5>", lambda e: self.run_code())
        self.root.bind("<F6>", lambda e: self.debug_code())
        self.root.bind("<F8>", lambda e: self.stop_execution())
        self.root.bind("<Control-space>", lambda e: self.show_autocomplete())
        
        # Editor events
        self.editor.bind("<<Modified>>", self.on_text_change)
        self.editor.bind("<KeyRelease>", self.update_line_numbers)
        self.editor.bind("<MouseWheel>", self.sync_scroll)
        
        # Syntax highlighting
        self.editor.bind("<KeyRelease>", self.highlight_syntax)
        
        # Autocomplete triggers
        self.editor.bind("<KeyRelease>", self.on_key_release, add="+")
        
        # INVIO per autocomplete quando è visibile
        self.editor.bind("<Return>", self.on_editor_return, add="+")
        
    def on_text_change(self, event=None):
        if self.editor.edit_modified():
            self.file_modified = True
            self.update_title()
            self.editor.edit_modified(False)
    
    def update_line_numbers(self, event=None):
        line_count = self.editor.get("1.0", tk.END).count('\n')
        line_numbers_string = "\n".join(str(i) for i in range(1, line_count + 1))
        
        self.line_numbers.config(state=tk.NORMAL)
        self.line_numbers.delete("1.0", tk.END)
        self.line_numbers.insert("1.0", line_numbers_string)
        self.line_numbers.config(state=tk.DISABLED)
    
    def sync_scroll(self, event=None):
        self.line_numbers.yview_moveto(self.editor.yview()[0])
    
    def highlight_syntax(self, event=None):
        # Remove existing tags
        for tag in self.editor.tag_names():
            if tag.startswith("syntax_"):
                self.editor.tag_remove(tag, "1.0", tk.END)
        
        code = self.editor.get("1.0", tk.END)
        
        # Highlight keywords from config
        import config
        keywords = list(config.get_keywords().keys())
        
        for keyword in keywords:
            start = "1.0"
            while True:
                pos = self.editor.search(keyword, start, tk.END, nocase=False)
                if not pos:
                    break
                end = f"{pos}+{len(keyword)}c"
                self.editor.tag_add("syntax_keyword", pos, end)
                start = end
        
        # Highlight strings
        import re
        for match in re.finditer(r'"[^"]*"', code):
            start_idx = f"1.0+{match.start()}c"
            end_idx = f"1.0+{match.end()}c"
            self.editor.tag_add("syntax_string", start_idx, end_idx)
        
        # Highlight comments
        for match in re.finditer(r'#.*', code):
            start_idx = f"1.0+{match.start()}c"
            end_idx = f"1.0+{match.end()}c"
            self.editor.tag_add("syntax_comment", start_idx, end_idx)
        
        # Highlight numbers
        for match in re.finditer(r'\b\d+\.?\d*\b', code):
            start_idx = f"1.0+{match.start()}c"
            end_idx = f"1.0+{match.end()}c"
            self.editor.tag_add("syntax_number", start_idx, end_idx)
        
        # Configure tag colors
        self.editor.tag_config("syntax_keyword", foreground=self.fg_keyword, font=("Consolas", 11, "bold"))
        self.editor.tag_config("syntax_string", foreground=self.fg_string)
        self.editor.tag_config("syntax_comment", foreground=self.fg_comment, font=("Consolas", 11, "italic"))
        self.editor.tag_config("syntax_number", foreground=self.fg_number)
    
    def new_file(self):
        if self.file_modified:
            if not self.ask_save_changes():
                return
        
        self.editor.delete("1.0", tk.END)
        self.current_file = None
        self.file_modified = False
        self.clear_output()
        self.update_title()
        self.update_line_numbers()
        self.set_status("Nuovo file creato")
    
    def load_file(self, filename):
        """Carica un file nell'editor"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.editor.delete("1.0", tk.END)
            self.editor.insert("1.0", content)
            self.current_file = filename
            self.file_modified = False
            self.update_title()
            self.update_line_numbers()
            self.highlight_syntax()
            self.set_status(f"File aperto: {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile aprire il file:\n{e}")
    
    def open_file(self):
        if self.file_modified:
            if not self.ask_save_changes():
                return
        
        filename = filedialog.askopenfilename(
            title="Apri file TLang",
            filetypes=[("TLang Files", "*.tl"), ("All Files", "*.*")]
        )
        
        if filename:
            self.load_file(filename)
    
    def save_file(self):
        if self.current_file:
            return self.save_to_file(self.current_file)
        else:
            return self.save_file_as()
    
    def save_file_as(self):
        filename = filedialog.asksaveasfilename(
            title="Salva file TLang",
            defaultextension=".tl",
            filetypes=[("TLang Files", "*.tl"), ("All Files", "*.*")]
        )
        
        if filename:
            return self.save_to_file(filename)
        return False
    
    def save_to_file(self, filename):
        try:
            content = self.editor.get("1.0", tk.END)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.current_file = filename
            self.file_modified = False
            self.update_title()
            self.set_status(f"File salvato: {os.path.basename(filename)}")
            return True
        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile salvare il file:\n{e}")
            return False
    
    def ask_save_changes(self):
        result = messagebox.askyesnocancel(
            "Salvare modifiche?",
            "Il file contiene modifiche non salvate. Salvare?"
        )
        
        if result is True:
            return self.save_file()
        elif result is False:
            return True
        else:
            return False
    
    def run_code(self):
        self.clear_output()
        self.set_status("Esecuzione in corso...")
        self.notebook.select(0)  # Switch to output tab
        
        code = self.editor.get("1.0", tk.END)
        
        # Check if code contains input() - warn user
        if "input(" in code:
            self.append_output("ÔÜá´©Å ATTENZIONE: Il codice contiene input().\n", "warning")
            self.append_output("L'IDE potrebbe bloccarsi. Usa invece i file .bat per programmi con input.\n\n", "warning")
        
        # Run in separate thread to avoid blocking
        thread = threading.Thread(target=self._execute_code, args=(code,), daemon=True)
        thread.start()
    
    def _execute_code(self, code):
        # Capture stdout/stderr
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        try:
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                # Lexer
                lexer = Lexer(code)
                tokens = lexer.tokenize()
                
                # Check invalid tokens
                invalid_tokens = [t for t in tokens if t.type == TokenType.INVALID]
                if invalid_tokens:
                    for token in invalid_tokens:
                        self.root.after(0, self.append_output,
                            f"ÔØî ERRORE LESSICALE alla riga {token.line}, colonna {token.column}: "
                            f"carattere '{token.value}' non riconosciuto\n",
                            "error"
                        )
                    self.root.after(0, self.set_status, "Errore di sintassi")
                    return
                
                # Parser
                parser = Parser(tokens)
                ast = parser.parse()
                
                # Interpreter
                interpreter = Interpreter()
                interpreter.run(ast)
                
                # Show variables
                self.root.after(0, self.update_variables, interpreter.variables)
            
            # Show output
            output = stdout_capture.getvalue()
            if output:
                self.root.after(0, self.append_output, output, "output")
            
            errors = stderr_capture.getvalue()
            if errors:
                self.root.after(0, self.append_output, errors, "error")
            
            if not output and not errors:
                self.root.after(0, self.append_output, "Ô£à Esecuzione completata (nessun output)\n", "success")
            
            self.root.after(0, self.set_status, "Ô£à Esecuzione completata")
            
        except ParseError as e:
            self.root.after(0, self.append_output, f"ÔØî ERRORE DI SINTASSI:\n{e}\n", "error")
            self.root.after(0, self.set_status, "Errore di sintassi")
        except TLangRuntimeError as e:
            self.root.after(0, self.append_output, f"ÔØî ERRORE RUNTIME:\n{e}\n", "error")
            self.root.after(0, self.set_status, "Errore runtime")
        except Exception as e:
            self.root.after(0, self.append_output, f"ÔØî ERRORE:\n{e}\n", "error")
            self.root.after(0, self.set_status, "Errore")
    
    def debug_code(self):
        self.clear_debug()
        self.set_status("Debug in corso...")
        self.notebook.select(1)  # Switch to debug tab
        
        code = self.editor.get("1.0", tk.END)
        
        try:
            # Lexer debug
            self.append_debug("=== FASE 1: LEXER (Tokenizzazione) ===\n", "header")
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            
            self.append_debug(f"Token generati: {len(tokens)}\n\n", "info")
            for i, token in enumerate(tokens[:50]):  # Show first 50 tokens
                self.append_debug(f"{i+1}. {token}\n", "token")
            
            if len(tokens) > 50:
                self.append_debug(f"\n... e altri {len(tokens)-50} token\n", "info")
            
            # Check invalid
            invalid_tokens = [t for t in tokens if t.type == TokenType.INVALID]
            if invalid_tokens:
                self.append_debug("\nÔØî TOKEN INVALIDI TROVATI:\n", "error")
                for token in invalid_tokens:
                    self.append_debug(f"  Riga {token.line}, col {token.column}: '{token.value}'\n", "error")
                return
            
            # Parser debug
            self.append_debug("\n=== FASE 2: PARSER (Analisi Sintattica) ===\n", "header")
            parser = Parser(tokens)
            ast = parser.parse()
            
            self.append_debug(f"Nodi AST creati: {len(ast.statements)}\n\n", "info")
            for i, stmt in enumerate(ast.statements):
                self.append_debug(f"{i+1}. {stmt}\n", "ast")
            
            # Interpreter debug
            self.append_debug("\n=== FASE 3: INTERPRETER (Esecuzione) ===\n", "header")
            interpreter = Interpreter()
            interpreter.run(ast)
            
            self.append_debug(f"\nVariabili finali: {len(interpreter.variables)}\n", "info")
            for name, value in interpreter.variables.items():
                self.append_debug(f"  {name} = {value} ({type(value).__name__})\n", "var")
            
            self.append_debug("\nÔ£à Debug completato con successo!\n", "success")
            self.set_status("Ô£à Debug completato")
            
        except ParseError as e:
            self.append_debug(f"\nÔØî ERRORE DI SINTASSI:\n{e}\n", "error")
            self.set_status("Errore in debug")
        except Exception as e:
            self.append_debug(f"\nÔØî ERRORE:\n{e}\n", "error")
            import traceback
            self.append_debug(f"\nTraceback:\n{traceback.format_exc()}", "error")
            self.set_status("Errore in debug")
    
    def stop_execution(self):
        self.append_output("\nÔÅ╣´©Å Esecuzione interrotta\n", "warning")
        self.set_status("Esecuzione interrotta")
    
    def clear_output(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
    
    def clear_debug(self):
        self.debug_text.config(state=tk.NORMAL)
        self.debug_text.delete("1.0", tk.END)
        self.debug_text.config(state=tk.DISABLED)
    
    def append_output(self, text, tag="normal"):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        
        # Color coding
        colors = {
            "output": "#cccccc",
            "error": "#f48771",
            "success": "#4ec9b0",
            "warning": "#dcdcaa"
        }
        
        if tag in colors:
            start = self.output_text.index(f"end-{len(text)}c")
            self.output_text.tag_add(tag, start, tk.END)
            self.output_text.tag_config(tag, foreground=colors[tag])
        
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)
    
    def append_debug(self, text, tag="normal"):
        self.debug_text.config(state=tk.NORMAL)
        self.debug_text.insert(tk.END, text)
        
        # Color coding
        colors = {
            "header": "#569cd6",
            "info": "#dcdcaa",
            "token": "#9cdcfe",
            "ast": "#4ec9b0",
            "var": "#c586c0",
            "error": "#f48771",
            "success": "#4ec9b0"
        }
        
        if tag in colors:
            start = self.debug_text.index(f"end-{len(text)}c")
            self.debug_text.tag_add(tag, start, tk.END)
            self.debug_text.tag_config(tag, foreground=colors[tag])
        
        self.debug_text.see(tk.END)
        self.debug_text.config(state=tk.DISABLED)
    
    def update_variables(self, variables):
        self.vars_text.config(state=tk.NORMAL)
        self.vars_text.delete("1.0", tk.END)
        
        if variables:
            self.vars_text.insert(tk.END, "Variabili Runtime:\n\n")
            for name, value in variables.items():
                self.vars_text.insert(tk.END, f"{name:20} = {value}\n")
                self.vars_text.insert(tk.END, f"{'':20}   (tipo: {type(value).__name__})\n\n")
        else:
            self.vars_text.insert(tk.END, "Nessuna variabile definita")
        
        self.vars_text.config(state=tk.DISABLED)
    
    def set_status(self, message):
        self.status_bar.config(text=f"  {message}")
    
    def update_title(self):
        filename = os.path.basename(self.current_file) if self.current_file else "Nuovo file"
        modified = " *" if self.file_modified else ""
        self.root.title(f"TLang IDE - {filename}{modified}")
        self.file_label.config(text=f"{filename}{modified}")
    
    def show_syntax_help(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Sintassi TLang")
        help_window.geometry("600x500")
        help_window.configure(bg=self.bg_dark)
        
        help_text = scrolledtext.ScrolledText(help_window, 
                                              bg=self.bg_editor,
                                              fg=self.fg_text,
                                              font=("Consolas", 10),
                                              padx=20, pady=20)
        help_text.pack(fill=tk.BOTH, expand=True)
        
        import config
        
        syntax = f"""
SINTASSI TLANG - Guida Rapida
{'='*60}

COMANDI DISPONIBILI:
{'='*60}

Print:          {config.COMANDO_PRINT} ("testo")
Input:          {config.COMANDO_INPUT}()
Variabile:      {config.COMANDO_VAR} nome = valore

If/Else:        {config.COMANDO_IF} condizione {{ ... }}
                {config.COMANDO_ELIF} condizione {{ ... }}
                {config.COMANDO_ELSE} {{ ... }}

While:          {config.COMANDO_WHILE} condizione {{ ... }}
For:            {config.COMANDO_FOR} var in iterable {{ ... }}

Function:       << ! C>> New command: nome(parametri) {{
                    // corpo funzione
                }}
Return:         {config.COMANDO_RETURN} valore

Break:          {config.COMANDO_BREAK}
Continue:       {config.COMANDO_CONTINUE}

Import:         {config.COMANDO_IMPORT} modulo
Function Call:  funzione(arg1, arg2)
Attribute:      oggetto.attributo

Boolean:        {config.COMANDO_TRUE} / {config.COMANDO_FALSE}
Logic:          {config.COMANDO_AND} / {config.COMANDO_OR} / {config.COMANDO_NOT}

{'='*60}
ESEMPI:
{'='*60}

# Hello World
{config.COMANDO_PRINT} ("Hello, World!")

# Variabili
{config.COMANDO_VAR} x = 10
{config.COMANDO_VAR} nome = "Mario"

# Condizioni
{config.COMANDO_IF} x > 5 {{
    {config.COMANDO_PRINT} ("x ├¿ maggiore di 5")
}}

# Loop
{config.COMANDO_WHILE} x < 20 {{
    {config.COMANDO_PRINT} (x)
    x = x + 1
}}

# Funzione
<< ! C>> New command: saluta(nome) {{
    {config.COMANDO_PRINT} ("Ciao " + nome)
    {config.COMANDO_RETURN} on
}}

var risultato = saluta("TLang")

# Import e funzioni
{config.COMANDO_IMPORT} pygame
pygame.init()

{'='*60}
"""
        
        help_text.insert("1.0", syntax)
        help_text.config(state=tk.DISABLED)
    
    def setup_autocomplete(self):
        """Setup autocomplete window"""
        self.autocomplete_window = tk.Toplevel(self.root)
        self.autocomplete_window.withdraw()
        self.autocomplete_window.wm_overrideredirect(True)
        self.autocomplete_window.bind("<FocusOut>", lambda e: self.hide_autocomplete())
        
        # Header con istruzioni
        header = tk.Label(
            self.autocomplete_window,
            text="Premi INVIO per completare",
            bg="#007acc",
            fg="white",
            font=("Arial", 9, "bold"),
            pady=3
        )
        header.pack(fill=tk.X)
        
        # Listbox for suggestions
        self.autocomplete_list = tk.Listbox(
            self.autocomplete_window,
            bg="#252526",
            fg="#d4d4d4",
            selectbackground="#094771",
            selectforeground="white",
            font=("Consolas", 10),
            width=30,
            height=10,
            relief=tk.FLAT,
            borderwidth=2,
            highlightthickness=1,
            highlightbackground="#007acc"
        )
        self.autocomplete_list.pack()
        
        # Bind selection
        self.autocomplete_list.bind("<Return>", lambda e: self.insert_autocomplete())
        self.autocomplete_list.bind("<Double-Button-1>", lambda e: self.insert_autocomplete())
        self.autocomplete_list.bind("<Escape>", lambda e: self.hide_autocomplete())
        
        # Frecce per navigare
        self.autocomplete_list.bind("<Up>", self.autocomplete_navigate)
        self.autocomplete_list.bind("<Down>", self.autocomplete_navigate)
    
    def autocomplete_navigate(self, event):
        """Naviga nella lista autocomplete con le frecce"""
        return  # Lascia che Listbox gestisca la navigazione naturalmente
    
    def on_editor_return(self, event):
        """Gestisce INVIO nell'editor - completa se autocomplete è visibile"""
        if self.autocomplete_visible:
            self.insert_autocomplete()
            return "break"  # Blocca il normale comportamento di INVIO
        return None  # Lascia che INVIO funzioni normalmente
    
    def on_key_release(self, event=None):
        """Trigger autocomplete on key release"""
        # Ignore special keys
        if event.keysym in ('Shift_L', 'Shift_R', 'Control_L', 'Control_R', 
                            'Alt_L', 'Alt_R', 'Up', 'Down', 'Left', 'Right',
                            'Return', 'Escape', 'Tab'):
            return
        
        # Get current word
        current_word = self.get_current_word()
        
        # Auto-show if word has 2+ characters
        if len(current_word) >= 2:
            self.filter_autocomplete(current_word)
        else:
            self.hide_autocomplete()
    
    def get_current_word(self):
        """Get the word currently being typed"""
        try:
            cursor_pos = self.editor.index(tk.INSERT)
            line_start = self.editor.index(f"{cursor_pos} linestart")
            line_text = self.editor.get(line_start, cursor_pos)
            
            # Get last word
            words = line_text.split()
            if words:
                return words[-1]
            return ""
        except:
            return ""
    
    def filter_autocomplete(self, prefix):
        """Filter keywords by prefix and show autocomplete"""
        matches = [kw for kw in self.tlang_keywords if kw.lower().startswith(prefix.lower())]
        
        if matches:
            self.autocomplete_list.delete(0, tk.END)
            for match in matches:
                self.autocomplete_list.insert(tk.END, match)
            
            self.autocomplete_list.selection_set(0)
            self.position_autocomplete()
            self.autocomplete_window.deiconify()
            self.autocomplete_visible = True
        else:
            self.hide_autocomplete()
    
    def show_autocomplete(self):
        """Manually show autocomplete with all keywords"""
        self.autocomplete_list.delete(0, tk.END)
        for keyword in sorted(self.tlang_keywords):
            self.autocomplete_list.insert(tk.END, keyword)
        
        self.autocomplete_list.selection_set(0)
        self.position_autocomplete()
        self.autocomplete_window.deiconify()
        self.autocomplete_visible = True
        self.autocomplete_list.focus_set()
    
    def position_autocomplete(self):
        """Position autocomplete window below cursor"""
        try:
            cursor_pos = self.editor.index(tk.INSERT)
            bbox = self.editor.bbox(cursor_pos)
            
            if bbox:
                x = self.editor.winfo_rootx() + bbox[0]
                y = self.editor.winfo_rooty() + bbox[1] + bbox[3]
                self.autocomplete_window.geometry(f"+{x}+{y}")
        except:
            pass
    
    def hide_autocomplete(self):
        """Hide autocomplete window"""
        self.autocomplete_window.withdraw()
        self.autocomplete_visible = False
        self.editor.focus_set()
    
    def insert_autocomplete(self):
        """Insert selected autocomplete item"""
        try:
            selection = self.autocomplete_list.curselection()
            if selection:
                keyword = self.autocomplete_list.get(selection[0])
                
                # Get current word being typed
                current_word = self.get_current_word()
                
                if current_word:
                    # Calculate how much to complete (only the remaining part)
                    # Check if keyword starts with current_word
                    if keyword.lower().startswith(current_word.lower()):
                        # Insert only the remaining part
                        remaining = keyword[len(current_word):]
                        self.editor.insert(tk.INSERT, remaining)
                    else:
                        # If doesn't match, delete current word and insert full keyword
                        cursor_pos = self.editor.index(tk.INSERT)
                        start_pos = f"{cursor_pos} - {len(current_word)}c"
                        self.editor.delete(start_pos, cursor_pos)
                        self.editor.insert(tk.INSERT, keyword)
                else:
                    # No current word, just insert
                    self.editor.insert(tk.INSERT, keyword)
                
                self.hide_autocomplete()
        except Exception as e:
            print(f"Autocomplete error: {e}")
            self.hide_autocomplete()
    
    def change_theme(self, theme_name):
        """Cambia il tema dell'IDE"""
        if theme_name not in self.themes:
            return
        
        self.current_theme = theme_name
        theme = self.themes[theme_name]
        
        # Aggiorna colori
        self.bg_dark = theme["bg_dark"]
        self.bg_editor = theme["bg_editor"]
        self.bg_toolbar = theme["bg_toolbar"]
        self.fg_text = theme["fg_text"]
        self.fg_keyword = theme["fg_keyword"]
        self.fg_string = theme["fg_string"]
        self.fg_comment = theme["fg_comment"]
        self.fg_number = theme["fg_number"]
        self.fg_linenumbers = theme["fg_linenumbers"]
        
        # Applica tema all'UI
        try:
            # Editor
            self.editor.config(bg=self.bg_editor, fg=self.fg_text)
            
            # Line numbers
            self.line_numbers.config(bg=self.bg_dark, fg=self.fg_linenumbers)
            
            # Output panels
            self.output_text.config(bg=self.bg_dark)
            self.debug_text.config(bg=self.bg_dark)
            self.vars_text.config(bg=self.bg_dark)
            
            # Re-highlight syntax
            self.highlight_syntax()
            
            self.set_status(f"✨ Tema cambiato: {theme_name}")
        except Exception as e:
            print(f"Errore cambio tema: {e}")
    
    def show_about(self):
        messagebox.showinfo(
            "TLang IDE",
            "TLang IDE v2.0 - CON AUTOCOMPLETE E TEMI\n\n"
            "Integrated Development Environment\n"
            "per il linguaggio TLang\n\n"
            "✨ Caratteristiche:\n"
            "• Autocomplete stile VS Code (Ctrl+Space)\n"
            "• 5 Temi: Dark, Light, Monokai, Matrix, BASIC\n"
            "• Icona icon.ico integrata\n"
            "• Suggerimenti automatici durante la digitazione\n"
            "• Syntax highlighting\n"
            "• Debug mode\n\n"
            "Creato con Python e Tkinter\n"
            "© 2025"
        )
    
    def quit_ide(self):
        if self.file_modified:
            if not self.ask_save_changes():
                return
        
        self.root.quit()

def main():
    root = tk.Tk()
    
    # Controlla se ├¿ stato passato un file come argomento
    initial_file = None
    if len(sys.argv) > 1:
        initial_file = sys.argv[1]
    
    ide = TLangIDE(root, initial_file)
    root.mainloop()

if __name__ == "__main__":
    main()
