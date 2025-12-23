use pygame
use random
use builtins
use sys


pygame.init()
var len = builtins.len
var str = builtins.str

var sfondo = pygame.image.load("../System/Immagini/sfondo.png")
var uccello = pygame.image.load("../System/Immagini/uccello.png")
var base = pygame.image.load("../System/Immagini/base.png")
var gameover = pygame.image.load("../System/Immagini/gameover.png")
var tubo_giu = pygame.image.load("../System/Immagini/tubo.png")
var tubo_su = pygame.transform.flip(tubo_giu, off, on)

var font = pygame.font.SysFont("Comic Sans MS", 60, on)

var SCHERMO = pygame.display.set_mode([288, 512])
var FPS = 50
var VEL_AVANZ = 3
var largh_schermo = 288

var punti = 0
var fra_i_tubi = off
var uccellox = 60
var uccelloy = 150
var uccello_vely = 0
var basex = 0
var tubi = []
var game_over = off

<< CRT >>! >class< tubi_classe {
    << ! C>> New command: {} __init__(self) {
        self.x = 298
        self.y = random.randint(-75, 150)
    }
    
    << ! C>> New command: {} avanza(self) {
        self.x = self.x - VEL_AVANZ
    }
    
    << ! C>> New command: {} disegna(self) {
        SCHERMO.blit(tubo_giu, [self.x, self.y + 210])
        SCHERMO.blit(tubo_su, [self.x, self.y - 210])
    }
    
    << ! C>> New command: {} collisione(self, uccello, uccellox, uccelloy) {
        var tolleranza = 5
        var uccello_lato_dx = uccellox + uccello.get_width() - tolleranza
        var uccello_lato_sx = uccellox + tolleranza
        var tubi_lato_dx = self.x + tubo_giu.get_width()
        var tubi_lato_sx = self.x
        var uccello_lato_su = uccelloy + tolleranza
        var uccello_lato_giu = uccelloy + uccello.get_height() - tolleranza
        var gap_inizio = self.y + 110
        var gap_fine = self.y + 210
        
        << ! >func> if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx {
            << ! >func> if uccello_lato_su <= gap_inizio or uccello_lato_giu >= gap_fine {
                return on
            }
        }
        return off
    }
    
    << ! C>> New command: {} fra_i_tubi(self, img_uccello, pos_x) {
        << ! >func> if pos_x + img_uccello.get_width() > self.x and pos_x < self.x + tubo_giu.get_width() {
            return on
        }
        return off
    }
}

<< ! C>> New command: {} disegna_oggetti() {
    SCHERMO.blit(sfondo, [0, 0])
    for t in tubi {
        t.disegna()
    }
    SCHERMO.blit(uccello, [uccellox, uccelloy])
    SCHERMO.blit(base, [basex, 400])
    disegna_punti()
}

<< ! C>> New command: {} disegna_punti() {
    var testo = font.render(str(punti), on, [255, 255, 255])
    var larghezza_testo = testo.get_width()
    var pos_x = (288 - larghezza_testo) / 2
    SCHERMO.blit(testo, [pos_x, 10])
}

<< ! C>> New command: {} aggiorna() {
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
}

<< ! C>> New command: {} inizializza() {
    uccellox = 60
    uccelloy = 150
    uccello_vely = 0
    basex = 0
    tubi = []
    tubi.append(tubi_classe())
    punti = 0
    fra_i_tubi = off
    game_over = off
}

inizializza()

<<While>>! <on> on {
    for event in pygame.event.get() {
        << ! >func> if event.type == pygame.QUIT {
            pygame.quit()
            sys.exit()
        }
        << ! >func> if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE {
            uccellox = 60
            uccelloy = 150
            uccello_vely = 0
            basex = 0
            tubi = []
            tubi.append(tubi_classe())
            punti = 0
            fra_i_tubi = off
            game_over = off
        }
        << ! >func> if not game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_UP {
            uccello_vely = -10
        }
    }
    
    << ! >func> if not game_over {
        basex = basex - VEL_AVANZ
        << ! >func> if basex < -45 {
            basex = 0
        }
        
        uccello_vely = uccello_vely + 1
        uccelloy = uccelloy + uccello_vely
        
        for t in tubi {
            t.avanza()
        }
        
        << ! >func> if len(tubi) > 0 {
            var primo_tubo = tubi[0]
            << ! >func> if primo_tubo.x < -60 {
                tubi.pop(0)
            }
        }
        
        << ! >func> if len(tubi) > 0 {
            var ultimo_tubo = tubi[len(tubi) - 1]
            << ! >func> if ultimo_tubo.x < 150 {
                tubi.append(tubi_classe())
            }
        }
        
        var colpito = off
        for t in tubi {
            << ! >func> if t.collisione(uccello, uccellox, uccelloy) {
                colpito = on
                stop
            }
        }
        
        << ! >func> if colpito or uccelloy > 380 {
            game_over = on
        }
        
        << ! >func> if not fra_i_tubi {
            for tubo in tubi {
                << ! >func> if tubo.fra_i_tubi(uccello, uccellox) {
                    fra_i_tubi = on
                    stop
                }
            }
        } >> func << else {
            var trovato = off
            for tubo in tubi {
                << ! >func> if tubo.fra_i_tubi(uccello, uccellox) {
                    trovato = on
                    stop
                }
            }
            << ! >func> if not trovato {
                fra_i_tubi = off
                punti = punti + 1
            }
        }
    }
    
    disegna_oggetti()
    
    << ! >func> if game_over {
        SCHERMO.blit(gameover, [50, 180])
    }
    
    aggiorna()
}



