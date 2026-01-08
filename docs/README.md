# TLang Website

Sito web ufficiale per TLang - Il linguaggio di programmazione con sintassi personalizzabile.

## Struttura

```
website/
├── index.html          # Homepage principale
├── style.css           # Stili CSS
├── script.js           # JavaScript interattivo
├── assets/            # Immagini e logo
│   └── tlang_logo.png
├── downloads/         # File scaricabili
│   ├── TLangIDE.exe
│   └── associate_tlang.bat
└── README.md          # Questo file
```

## Setup

1. Copia `TLangIDE.exe` nella cartella `downloads/`
2. Copia `associate_tlang.bat` nella cartella `downloads/`
3. Copia il logo TLang in `assets/tlang_logo.png`
4. Apri `index.html` con un browser

## Hosting

Per pubblicare online:

### Opzione 1: GitHub Pages (Gratis)
1. Crea un repository su GitHub
2. Carica tutti i file
3. Vai su Settings → Pages
4. Seleziona "main branch" come source
5. Il sito sarà disponibile su `https://tuousername.github.io/tlang`

### Opzione 2: Netlify (Gratis)
1. Vai su [netlify.com](https://netlify.com)
2. Trascina la cartella `website`
3. Il sito sarà online in pochi secondi

### Opzione 3: Vercel (Gratis)
1. Vai su [vercel.com](https://vercel.com)
2. Importa da GitHub o carica i file
3. Deploy automatico

## Features

- ✅ Design moderno e responsivo
- ✅ Syntax highlighting per il codice
- ✅ Documentazione completa
- ✅ Esempi interattivi
- ✅ Smooth scroll navigation
- ✅ Animazioni CSS
- ✅ Copy to clipboard per gli esempi
- ✅ Dark theme

## Personalizzazione

### Cambiare i colori
Modifica le variabili CSS in `style.css`:

```css
:root {
    --primary-color: #e67e22;    /* Colore principale */
    --secondary-color: #d35400;  /* Colore secondario */
    --dark-bg: #1e1e1e;          /* Background scuro */
}
```

### Aggiungere sezioni
Aggiungi nuove sezioni in `index.html` seguendo la struttura esistente.

### Modificare la navbar
Aggiungi link in `index.html` nella sezione `<ul class="nav-links">`.

## TODO

- [ ] Aggiungere sezione OS
- [ ] Integrare forum/community
- [ ] Aggiungere playground online
- [ ] Creare tutorial video
- [ ] Multi-language support

## Licenza

© 2025 TLang. Tutti i diritti riservati.
