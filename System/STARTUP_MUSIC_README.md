# 🎵 TencleOS Startup Music

## Melodia di Avvio Stile TempleOS

Musica di avvio per TencleOS usando i beep del PC speaker, ispirata alla leggendaria sigla di TempleOS.

---

## 🎼 Caratteristiche

- ✅ **PC Speaker Beeps** - Suoni autentici retrò
- ✅ **3 Melodie** - TencleOS, Breve, TempleOS Style
- ✅ **Suoni Sistema** - Boot, Success, Error
- ✅ **Puro Python** - Usa `winsound` (Windows nativo)
- ✅ **Personalizzabile** - Facile modificare le note

---

## 🚀 Come Usare

### Metodo 1: Avvio con Musica (Consigliato)
```bash
start_with_music.bat
```
Avvia TencleOS con la sequenza completa: logo + musica + caricamento

### Metodo 2: Solo Musica
```bash
python tencleos_startup_music.py
```
Riproduce solo la melodia TencleOS

### Metodo 3: Scelta Stile
```bash
python tencleos_startup_music.py tencleos    # Melodia completa
python tencleos_startup_music.py short       # Melodia breve (3 sec)
python tencleos_startup_music.py templeos    # Stile TempleOS originale
```

---

## 🎹 Melodie Disponibili

### 1. TencleOS (Default) - 5 secondi
Melodia originale riconoscibile per TencleOS
```
Do - Mi - Sol - Do alto
Sol - Mi - Do - Mi - Sol
Do alto - Si - Do alto
```

### 2. Short - 3 secondi
Versione breve per avvio rapido
```
Do - Sol - Do alto
Sol - Do alto
```

### 3. TempleOS Style - 4 secondi
Replica della melodia originale di TempleOS
```
Do alto - Re alto - Mi alto - Fa alto - Sol alto
Sol alto - Fa alto - Mi alto - Re alto - Do alto
```

---

## 🔊 Suoni Sistema

### Boot Sound
Triade ascendente veloce (1 secondo)
```python
TencleOSStartupMusic.play_boot_sound()
```

### Success Sound
Suono di successo finale
```python
TencleOSStartupMusic.play_success_sound()
```

### Error Sound
Beep di errore ripetuto
```python
TencleOSStartupMusic.play_error_sound()
```

---

## 📝 Uso nel Codice Python

```python
from tencleos_startup_music import TencleOSStartupMusic

# Riproduce melodia TencleOS
TencleOSStartupMusic.play_startup('tencleos')

# Riproduce melodia breve
TencleOSStartupMusic.play_startup('short')

# Riproduce stile TempleOS
TencleOSStartupMusic.play_startup('templeos')

# Suoni sistema
TencleOSStartupMusic.play_boot_sound()
TencleOSStartupMusic.play_success_sound()
TencleOSStartupMusic.play_error_sound()

# Beep personalizzati
TencleOSStartupMusic.play_beep_sequence([262, 330, 392, 523], duration=100)
```

---

## 🎨 Personalizzazione

### Modifica la Melodia

Apri `tencleos_startup_music.py` e modifica:

```python
TENCLEOS_MELODY = [
    ('C4', 150),  # Nota, Durata in ms
    ('E4', 150),
    ('G4', 150),
    # Aggiungi più note...
]
```

### Note Disponibili
```
C4 (Do) = 262 Hz
D4 (Re) = 294 Hz
E4 (Mi) = 330 Hz
F4 (Fa) = 349 Hz
G4 (Sol) = 392 Hz
A4 (La) = 440 Hz
B4 (Si) = 494 Hz
C5 (Do alto) = 523 Hz
# ... e tutte le ottave superiori
```

---

## 🔧 Requisiti

- **Windows**: Usa `winsound` (incluso in Python)
- **Python 3.6+**: Nessuna dipendenza esterna
- **PC Speaker**: La maggior parte dei PC moderni supporta i beep

### Se il PC Speaker Non Funziona

Alcuni PC moderni hanno il beep disabilitato. Per riattivarlo:

1. Apri Gestione Dispositivi
2. Vai su "Dispositivi di Sistema"
3. Trova "Beep" e abilitalo
4. Riavvia il PC

---

## 📊 Durata Suoni

| Suono | Durata | Note |
|-------|--------|------|
| TencleOS Melody | ~5 sec | Melodia completa |
| Short Melody | ~3 sec | Avvio rapido |
| TempleOS Style | ~4 sec | Stile originale |
| Boot Sound | ~1 sec | Triade veloce |
| Success Sound | ~0.5 sec | 3 note |
| Error Sound | ~0.5 sec | 2 beep bassi |

---

## 🎵 Demo Completa

Prova tutte le melodie e suoni:
```bash
python tencleos_startup_music.py demo
```

Oppure nel codice:
```python
from tencleos_startup_music import demo_all_melodies
demo_all_melodies()
```

---

## 💡 Tips & Tricks

### Volume
Il volume dei beep dipende dal volume di sistema Windows. Regolalo da:
- Icona volume nella taskbar
- Pannello di controllo → Suoni

### Personalizza Durata
Modifica i valori in millisecondi per note più lunghe/brevi:
```python
('C4', 300),  # Nota lunga (300ms)
('E4', 100),  # Nota breve (100ms)
```

### Aggiungi Pause
Usa `'REST'` per silenzi:
```python
('C4', 200),
('REST', 100),  # Pausa di 100ms
('E4', 200),
```

---

## 🎯 Integrazione con TencleOS

La musica è automaticamente integrata nel launcher:
1. `start_with_music.bat` avvia tutto
2. La musica suona durante il caricamento
3. Boot sound all'inizio
4. Melodia principale durante loading
5. Success sound alla fine

---

## 📜 Licenza

Stessa licenza di TencleOS - Usa liberamente!

---

## 🙏 Credits

- **Ispirato da**: TempleOS di Terry A. Davis
- **Creato per**: TencleOS v1.1.0
- **Tecnologia**: Python `winsound` module

---

## 🎉 Buon Ascolto!

**La melodia di TencleOS è ora pronta!** 🎵

Esegui `start_with_music.bat` e goditi l'esperienza completa di avvio stile TempleOS! 🚀
