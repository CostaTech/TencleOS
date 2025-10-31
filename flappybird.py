# 🐍 Importo le Librerie
import pygame
import random

# 🚀 Inizializzo PyGame
pygame.init()

# 🎨 Carico le Immagini
sfondo = pygame.image.load('Immagini/sfondo.png')
uccello = pygame.image.load('Immagini/uccello.png')
base = pygame.image.load('Immagini/base.png')
gameover = pygame.image.load('Immagini/gameover.png')
tubo_giu = pygame.image.load('Immagini/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)

# 🖋️ Font per il punteggio
font = pygame.font.SysFont('Comic Sans MS', 60, bold=True)


# ⚙️ Costanti Globali
SCHERMO = pygame.display.set_mode((288, 512))
FPS = 50
VEL_AVANZ = 3

# 🧮 Variabili Globali
punti = 0
fra_i_tubi = False

# 🧱 Classe Tubi
class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150)

    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ
        SCHERMO.blit(tubo_giu, (self.x,self.y+210))
        SCHERMO.blit(tubo_su, (self.x,self.y-210))

    def collisione(self, uccello, uccellox, uccelloy):
        tolleranza = 5
        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox+tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x
        uccello_lato_su = uccelloy+tolleranza
        uccello_lato_giu = uccelloy+uccello.get_height()-tolleranza
        tubi_lato_su = self.y+110
        tubi_lato_giu = self.y+210
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                hai_perso()

    def fra_i_tubi(self, img_uccello, pos_x):
        if pos_x + img_uccello.get_width() > self.x and pos_x < self.x + tubo_giu.get_width():
            return True
        return False

# 🎭 Funzione per disegnare gli oggetti
def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    for t in tubi:
        t.avanza_e_disegna()
    SCHERMO.blit(uccello, (uccellox,uccelloy))
    SCHERMO.blit(base, (basex,400))
    disegna_punti()

# 🧾 Funzione per disegnare il punteggio
def disegna_punti():
    testo = font.render(str(punti), True, (255,255,255))
    larghezza_testo = testo.get_width()
    SCHERMO.blit(testo, ((288 - larghezza_testo) // 2, 10))

# 🔄 Funzione per aggiornare lo schermo
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

# 🧨 Funzione per inizializzare il gioco
def inizializza():
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    global punti, fra_i_tubi
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    tubi = []
    tubi.append(tubi_classe())
    punti = 0
    fra_i_tubi = False

# 💥 Funzione per gestire la sconfitta
def hai_perso():
    SCHERMO.blit(gameover, (50,180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()

# 🐣 Inizializzo Variabili
inizializza()

### 🔁 Ciclo Principale ###
while True:
    # 🏃 Avanzamento Base
    basex -= VEL_AVANZ
    if basex < -45: basex = 0

    # 🌌 Gravità
    uccello_vely += 1
    uccelloy += uccello_vely

    # 🎮 Comandi
    for event in pygame.event.get():
        if ( event.type == pygame.KEYDOWN and event.key == pygame.K_UP ):
            uccello_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()

    # ➕ Aggiunta nuovi tubi
    if tubi[-1].x < 150: tubi.append(tubi_classe())

    # 🧠 Gestione punteggio
    if not fra_i_tubi:
        for tubo in tubi:
            if tubo.fra_i_tubi(uccello, uccellox):
                fra_i_tubi = True
                break
    else:
        trovato = False
        for tubo in tubi:
            if tubo.fra_i_tubi(uccello, uccellox):
                trovato = True
                break
        if not trovato:
            fra_i_tubi = False
            punti += 1

    # 💥 Collisione con i tubi
    for t in tubi:
        t.collisione(uccello, uccellox, uccelloy)

    # 🧱 Collisione con la base
    if uccelloy > 380:
        hai_perso()

    # 🖼️ Disegno e Aggiorno
    disegna_oggetti()
    aggiorna()

