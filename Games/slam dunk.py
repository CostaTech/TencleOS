#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gioco di Basket 2D - Pygame
Compatibile con PC e Android (PyDroid 3)
"""

import pygame
import math
import sys

# Inizializzazione pygame
pygame.init()

# Costanti
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
DARK_ORANGE = (200, 100, 0)
RED = (220, 20, 60)
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 235)
DARK_RED = (139, 0, 0)

# Fisica
GRAVITY = 0.5
DAMPING = 0.7  # Coefficiente di rimbalzo

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.vx = 0
        self.vy = 0
        self.is_dragging = False
        self.prev_x = x
        self.prev_y = y
        self.is_shot = False
        self.velocity_history = []  # Per calcolare velocità media
        
    def draw(self, screen):
        # Disegna palla arancione
        pygame.draw.circle(screen, ORANGE, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, DARK_ORANGE, (int(self.x), int(self.y)), self.radius, 3)
        # Linee sulla palla
        pygame.draw.line(screen, DARK_ORANGE, 
                        (int(self.x - self.radius), int(self.y)), 
                        (int(self.x + self.radius), int(self.y)), 2)
        pygame.draw.line(screen, DARK_ORANGE, 
                        (int(self.x), int(self.y - self.radius)), 
                        (int(self.x), int(self.y + self.radius)), 2)
        
    def start_drag(self, mouse_x, mouse_y):
        distance = math.sqrt((mouse_x - self.x)**2 + (mouse_y - self.y)**2)
        if distance <= self.radius and not self.is_shot:
            self.is_dragging = True
            self.prev_x = self.x
            self.prev_y = self.y
            self.velocity_history = []
            return True
        return False
        
    def update_drag(self, mouse_x, mouse_y):
        if self.is_dragging:
            # Muovi la palla con il dito/mouse
            dx = mouse_x - self.x
            dy = mouse_y - self.y
            
            # Salva velocità per calcolare il lancio
            self.velocity_history.append((dx, dy))
            if len(self.velocity_history) > 5:  # Mantieni solo le ultime 5 velocità
                self.velocity_history.pop(0)
            
            self.prev_x = self.x
            self.prev_y = self.y
            self.x = mouse_x
            self.y = mouse_y
            
    def release(self):
        if self.is_dragging:
            # Calcola velocità media dalle ultime posizioni
            if len(self.velocity_history) > 0:
                avg_vx = sum(v[0] for v in self.velocity_history) / len(self.velocity_history)
                avg_vy = sum(v[1] for v in self.velocity_history) / len(self.velocity_history)
                self.vx = avg_vx * 1.2  # Fattore di potenza
                self.vy = avg_vy * 1.2
            else:
                self.vx = 0
                self.vy = 0
                
            self.is_dragging = False
            self.is_shot = True
            self.velocity_history = []
    
    def update(self):
        if self.is_shot:
            # Applica gravità
            self.vy += GRAVITY
            
            # Aggiorna posizione
            self.x += self.vx
            self.y += self.vy
            
            # Rimbalzo sui bordi
            if self.x - self.radius < 0:
                self.x = self.radius
                self.vx = -self.vx * DAMPING
            elif self.x + self.radius > SCREEN_WIDTH:
                self.x = SCREEN_WIDTH - self.radius
                self.vx = -self.vx * DAMPING
                
            if self.y + self.radius > SCREEN_HEIGHT:
                self.y = SCREEN_HEIGHT - self.radius
                self.vy = -self.vy * DAMPING
                self.vx *= 0.95  # Attrito
                
                # Se la palla si ferma in basso, resetta
                if abs(self.vy) < 1 and abs(self.vx) < 1:
                    return True  # Segnala di resettare
        return False

class Basket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 10
        self.rim_thickness = 5
        self.backboard_width = 10
        self.backboard_height = 100
        
    def draw(self, screen):
        # Tabellone (ora DIETRO il canestro, sulla destra)
        backboard_x = self.x + self.width - self.backboard_width // 2
        pygame.draw.rect(screen, WHITE, 
                        (backboard_x, 
                         self.y - self.backboard_height // 2, 
                         self.backboard_width, self.backboard_height))
        pygame.draw.rect(screen, BLACK, 
                        (backboard_x, 
                         self.y - self.backboard_height // 2, 
                         self.backboard_width, self.backboard_height), 2)
        
        # Canestro (ora va verso SINISTRA, verso la palla)
        pygame.draw.rect(screen, RED, 
                        (self.x, self.y, self.width, self.rim_thickness))
        pygame.draw.rect(screen, DARK_RED, 
                        (self.x, self.y, self.width, self.rim_thickness), 2)
        
        # Rete (linee semplici)
        net_lines = 8
        for i in range(net_lines):
            x_pos = self.x + (self.width * i / net_lines)
            pygame.draw.line(screen, RED, 
                           (int(x_pos), self.y), 
                           (int(x_pos), self.y + 30), 2)
        
    def check_score(self, ball):
        # Controlla se la palla passa attraverso il canestro dall'alto
        ball_bottom = ball.y + ball.radius
        ball_top = ball.y - ball.radius
        
        # La palla deve passare dall'alto verso il basso
        if (ball.x > self.x and ball.x < self.x + self.width and
            ball_top < self.y and ball_bottom > self.y and ball.vy > 0):
            return True
        return False

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Gioco di Basket 2D")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Font
        try:
            self.font = pygame.font.SysFont("Comic Sans MS", 60)
        except:
            # Fallback se Comic Sans non è disponibile
            self.font = pygame.font.Font(None, 60)
        
        # Oggetti di gioco
        self.ball = Ball(SCREEN_WIDTH // 4, SCREEN_HEIGHT - 100)
        self.basket = Basket(SCREEN_WIDTH - 150, 150)
        self.score = 0
        self.scored_this_shot = False
        
    def reset_ball(self):
        self.ball = Ball(SCREEN_WIDTH // 4, SCREEN_HEIGHT - 100)
        self.scored_this_shot = False
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                self.ball.start_drag(mouse_x, mouse_y)
                
            elif event.type == pygame.MOUSEMOTION:
                if self.ball.is_dragging:
                    mouse_x, mouse_y = event.pos
                    self.ball.update_drag(mouse_x, mouse_y)
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                self.ball.release()
                
    def update(self):
        # Aggiorna palla
        should_reset = self.ball.update()
        
        # Controlla punteggio
        if not self.scored_this_shot and self.basket.check_score(self.ball):
            self.score += 2
            self.scored_this_shot = True
        
        # Resetta se la palla esce dallo schermo o si ferma
        if should_reset or self.ball.y > SCREEN_HEIGHT + 50:
            self.reset_ball()
            
    def draw(self):
        # Sfondo
        self.screen.fill(SKY_BLUE)
        
        # Disegna pavimento
        pygame.draw.rect(self.screen, (101, 67, 33), 
                        (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
        
        # Disegna oggetti
        self.basket.draw(self.screen)
        self.ball.draw(self.screen)
        
        # Disegna punteggio
        score_text = self.font.render(f"Punti: {self.score}", True, WHITE)
        score_shadow = self.font.render(f"Punti: {self.score}", True, BLACK)
        self.screen.blit(score_shadow, (22, 22))
        self.screen.blit(score_text, (20, 20))
        
        # Istruzioni se non ha ancora tirato
        if not self.ball.is_shot and not self.ball.is_dragging:
            instruction_font = pygame.font.Font(None, 30)
            inst_text = instruction_font.render("Tieni premuto sulla palla e trascinala, poi rilascia per tirare!", True, WHITE)
            inst_shadow = instruction_font.render("Tieni premuto sulla palla e trascinala, poi rilascia per tirare!", True, BLACK)
            text_rect = inst_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
            shadow_rect = inst_shadow.get_rect(center=(SCREEN_WIDTH // 2 + 2, SCREEN_HEIGHT - 28))
            self.screen.blit(inst_shadow, shadow_rect)
            self.screen.blit(inst_text, text_rect)
        
        pygame.display.flip()
        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()