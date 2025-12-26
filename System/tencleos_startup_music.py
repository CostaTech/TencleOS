"""
TencleOS Startup Music - TempleOS Style
========================================
Melodia di avvio con beep del PC speaker stile TempleOS retrò
Fallback con pygame se winsound non funziona
"""

import time
import sys

# Usa pygame per audio udibile dalle casse (non PC speaker)
AUDIO_METHOD = 'pygame'
try:
    import pygame
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
    print("🔊 Audio: pygame (suoni sintetici udibili)")
except ImportError:
    AUDIO_METHOD = 'none'
    print("ATTENZIONE: Nessun sistema audio disponibile!")
    print("Installa pygame: pip install pygame")

class TencleOSStartupMusic:
    """Classe per riprodurre la melodia di avvio TencleOS"""
    
    # Note musicali (frequenza in Hz)
    NOTES = {
        'C4': 262,   # Do
        'D4': 294,   # Re
        'E4': 330,   # Mi
        'F4': 349,   # Fa
        'G4': 392,   # Sol
        'A4': 440,   # La
        'B4': 494,   # Si
        'C5': 523,   # Do alto
        'D5': 587,   # Re alto
        'E5': 659,   # Mi alto
        'F5': 698,   # Fa alto
        'G5': 784,   # Sol alto
        'REST': 0    # Pausa
    }
    
    # Melodia TencleOS (ispirata a TempleOS ma originale)
    # Formato: (nota, durata_ms)
    TENCLEOS_MELODY = [
        # Intro ascendente (presentazione)
        ('C4', 150),
        ('E4', 150),
        ('G4', 150),
        ('C5', 300),
        ('REST', 100),
        
        # Tema principale (riconoscibile)
        ('G4', 200),
        ('E4', 200),
        ('C4', 200),
        ('E4', 200),
        ('G4', 400),
        ('REST', 100),
        
        # Finale trionfante
        ('C5', 200),
        ('B4', 200),
        ('C5', 400),
        ('REST', 200),
    ]
    
    # Melodia alternativa più breve (3 secondi)
    SHORT_MELODY = [
        ('C4', 150),
        ('G4', 150),
        ('C5', 300),
        ('REST', 100),
        ('G4', 200),
        ('C5', 400),
    ]
    
    # Melodia stile TempleOS originale (molto simile)
    TEMPLEOS_STYLE = [
        ('C5', 100),
        ('D5', 100),
        ('E5', 100),
        ('F5', 100),
        ('G5', 200),
        ('REST', 50),
        ('G5', 100),
        ('F5', 100),
        ('E5', 100),
        ('D5', 100),
        ('C5', 300),
    ]
    
    @classmethod
    def _beep(cls, freq, duration):
        """Riproduce un beep usando pygame per audio udibile"""
        # Usa sempre pygame per suoni dalle casse invece di PC speaker
        if AUDIO_METHOD == 'pygame':
            cls._beep_pygame(freq, duration)
        else:
            print(f"♪ {freq}Hz per {duration}ms")  # Visualizza invece di suonare
    
    @classmethod
    def _beep_pygame(cls, freq, duration):
        """Genera beep sintetico con pygame"""
        if AUDIO_METHOD != 'pygame':
            return
        
        import math
        import numpy as np
        
        # Genera onda sinusoidale
        sample_rate = 22050
        n_samples = int(sample_rate * duration / 1000.0)
        
        # Crea array di campioni
        buf = np.zeros((n_samples, 2), dtype=np.int16)
        max_sample = 2**(16 - 1) - 1
        
        for s in range(n_samples):
            t = float(s) / sample_rate
            buf[s][0] = int(round(max_sample * 0.3 * math.sin(2 * math.pi * freq * t)))
            buf[s][1] = buf[s][0]
        
        sound = pygame.sndarray.make_sound(buf)
        sound.play()
        time.sleep(duration / 1000.0)
    
    @classmethod
    def play_startup(cls, style='tencleos'):
        """
        Riproduce la melodia di avvio
        
        Args:
            style: 'tencleos', 'short', 'templeos'
        """
        if style == 'tencleos':
            melody = cls.TENCLEOS_MELODY
        elif style == 'short':
            melody = cls.SHORT_MELODY
        elif style == 'templeos':
            melody = cls.TEMPLEOS_STYLE
        else:
            melody = cls.TENCLEOS_MELODY
        
        print(f"🎵 Riproduzione con {AUDIO_METHOD}...")
        
        try:
            for note, duration in melody:
                if note == 'REST':
                    time.sleep(duration / 1000.0)
                else:
                    freq = cls.NOTES[note]
                    cls._beep(freq, duration)
        except Exception as e:
            print(f"Errore riproduzione audio: {e}")
            print("(Verifica che pygame sia installato: pip install pygame)")
    
    @classmethod
    def play_beep_sequence(cls, frequencies, duration=100, pause=50):
        """
        Riproduce una sequenza di beep personalizzata
        
        Args:
            frequencies: Lista di frequenze in Hz
            duration: Durata di ogni beep in ms
            pause: Pausa tra beep in ms
        """
        try:
            for freq in frequencies:
                if freq > 0:
                    cls._beep(freq, duration)
                time.sleep(pause / 1000.0)
        except Exception as e:
            print(f"Errore riproduzione: {e}")
    
    @classmethod
    def play_boot_sound(cls):
        """Suono breve di boot (1 secondo)"""
        try:
            # Triade ascendente veloce
            cls._beep(262, 100)  # Do
            cls._beep(330, 100)  # Mi
            cls._beep(392, 100)  # Sol
            cls._beep(523, 200)  # Do alto (più lungo)
        except Exception as e:
            print(f"Errore boot sound: {e}")
    
    @classmethod
    def play_success_sound(cls):
        """Suono di successo (caricamento completato)"""
        try:
            cls._beep(523, 100)  # Do alto
            cls._beep(659, 100)  # Mi alto
            cls._beep(784, 200)  # Sol alto
        except Exception as e:
            print(f"Errore success sound: {e}")
    
    @classmethod
    def play_error_sound(cls):
        """Suono di errore"""
        try:
            cls._beep(200, 200)  # Basso
            time.sleep(0.1)
            cls._beep(200, 200)  # Ripetuto
        except Exception as e:
            print(f"Errore error sound: {e}")


def demo_all_melodies():
    """Demo di tutte le melodie disponibili"""
    print("=== TencleOS Startup Music Demo ===\n")
    
    print("1. Melodia TencleOS completa...")
    TencleOSStartupMusic.play_startup('tencleos')
    time.sleep(1)
    
    print("\n2. Melodia breve (3 sec)...")
    TencleOSStartupMusic.play_startup('short')
    time.sleep(1)
    
    print("\n3. Stile TempleOS originale...")
    TencleOSStartupMusic.play_startup('templeos')
    time.sleep(1)
    
    print("\n4. Boot sound...")
    TencleOSStartupMusic.play_boot_sound()
    time.sleep(1)
    
    print("\n5. Success sound...")
    TencleOSStartupMusic.play_success_sound()
    time.sleep(1)
    
    print("\n6. Error sound...")
    TencleOSStartupMusic.play_error_sound()
    
    print("\n=== Demo completata! ===")


if __name__ == "__main__":
    # Test rapido
    print("TencleOS Startup Music - PC Speaker Beeps")
    print("==========================================\n")
    
    import sys
    
    if len(sys.argv) > 1:
        style = sys.argv[1]
        print(f"Riproduzione stile: {style}\n")
        TencleOSStartupMusic.play_startup(style)
    else:
        print("Riproduzione melodia TencleOS...\n")
        TencleOSStartupMusic.play_startup('tencleos')
        
        print("\n" + "="*50)
        print("Usa: python tencleos_startup_music.py [style]")
        print("Style: tencleos, short, templeos")
        print("="*50)
