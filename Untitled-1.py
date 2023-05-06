from pygame import *
 
 
class GameSprite(sprite.Sprite):
    def __init__(self, object_image, object_x, object_y, object_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(object_image), (size_x, size_y))
        self.speed = object_speed
        self.rect = self.image.get_rect()
        self.rect.x = object_x
        self.rect.y = object_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
    def move_hero(self):
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 620:
            self.rect.x += self.speed
 

fon = GameSprite('fon.jpg', 0, 0, 0, 700, 500)
t1 = GameSprite('storona.png', 10, 50, 3, 10, 100) 
t2 = GameSprite('storona.png', 600, 50, 3, 10, 100)
 
 
window = display.set_mode((700, 500))
display.set_caption('Shooter')

 
 
clock = time.Clock()
FPS = 60
 
 
 
game = True


while game:
    keys_pressed = key.get_pressed()
    fon.reset()
    t1.reset()
    t2.reset()
    t1.move_hero()
    for e in event.get():
        if e.type == QUIT:
            game = False

 
    display.update()
    clock.tick(FPS)
        
        
