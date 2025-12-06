"""
TencleOS Launcher con Musica di Avvio
======================================
Avvia TencleOS con la melodia stile TempleOS
"""

import os
import sys
import time
from tencleos_startup_music import TencleOSStartupMusic

def clear_screen():
    """Pulisce lo schermo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    """Stampa il logo ASCII"""
    logo = """
    ████████╗███████╗███╗   ██╗ ██████╗██╗     ███████╗ ██████╗ ███████╗
    ╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝
       ██║   █████╗  ██╔██╗ ██║██║     ██║     █████╗  ██║   ██║███████╗
       ██║   ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══╝  ██║   ██║╚════██║
       ██║   ███████╗██║ ╚████║╚██████╗███████╗███████╗╚██████╔╝███████║
       ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
    """
    print(logo)

def animated_loading(duration=2):
    """Barra di caricamento animata"""
    print("\n    Loading TencleOS", end="")
    steps = 20
    for i in range(steps):
        time.sleep(duration / steps)
        print(".", end="", flush=True)
    print(" Done!\n")

def startup_sequence():
    """Sequenza di avvio completa con musica"""
    clear_screen()
    
    # 1. Logo
    print_logo()
    print("    ⚡ The Operating System in TLang ⚡")
    print("    Version 1.1.0 - Built with Python & Tkinter\n")
    
    # 2. Messaggio iniziale
    print("    [BOOT] Initializing TencleOS...")
    time.sleep(0.5)
    
    # 3. Avvia musica in parallelo
    print("    [BOOT] Starting audio system...")
    TencleOSStartupMusic.play_boot_sound()
    time.sleep(0.3)
    
    # 4. Caricamento
    print("    [BOOT] Loading kernel...")
    time.sleep(0.3)
    print("    [BOOT] Mounting filesystem...")
    time.sleep(0.3)
    print("    [BOOT] Starting TLang interpreter...")
    time.sleep(0.3)
    
    # 5. Melodia principale durante caricamento
    print("    [BOOT] Initializing system services...")
    TencleOSStartupMusic.play_startup('tencleos')
    
    # 6. Completamento
    print("    [OK] TencleOS ready!")
    TencleOSStartupMusic.play_success_sound()
    
    print("\n" + "="*70)
    time.sleep(1)

def main():
    """Funzione principale"""
    try:
        # Esegui sequenza di avvio con musica
        startup_sequence()
        
        # Avvia OS TLang
        print("\n    Starting TencleOS interface...\n")
        time.sleep(1)
        
        # Esegui il file TLang dell'OS
        os.system("python tlang/tlang_runner.py os.tl")
        
    except KeyboardInterrupt:
        print("\n\n    [EXIT] TencleOS shutdown.")
        sys.exit(0)
    except Exception as e:
        print(f"\n    [ERROR] Startup failed: {e}")
        TencleOSStartupMusic.play_error_sound()
        sys.exit(1)

if __name__ == "__main__":
    main()
