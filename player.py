import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED


class Player(CircleShape):
    
    PLAYER_SHOOT_COOLDOWN  = 0
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        # in the player class
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle())
        
    def update(self, dt):
        if Player.PLAYER_SHOOT_COOLDOWN  > 0:
            Player.PLAYER_SHOOT_COOLDOWN  -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.position += self.move(dt)
        if keys[pygame.K_s]:
            self.position -= self.move(dt)
        if keys[pygame.K_SPACE]:
            if Player.PLAYER_SHOOT_COOLDOWN  <= 0:
                self.shoot()
                Player.PLAYER_SHOOT_COOLDOWN  += 0.3
    
    def move(self, dt):
        return pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
    
    def shoot(self):
        print("Pew!")
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
        
        