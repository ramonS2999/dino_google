from settings import *

class Sprite:
    def __init__(self, texture, pos):
        self.texture = texture
        self.pos = pos

    def draw(self):
        draw_texture_ex(
            self.texture, 
            self.pos, 
            0, 
            SCALE, 
            WHITE
        )

class Dino(Sprite):
    def __init__(self, texture, pos, jump_sound):
        super().__init__(texture, pos)
        self.jump_sound = jump_sound
        self.velocity = 0
        self.gravity = 0.8
        self.jump_height = -28

    def update(self):
        self.velocity += self.gravity
        self.pos.y += self.velocity
        if self.pos.y > FLOOR_LINE:
            self.pos.y = FLOOR_LINE
            self.velocity = 0
        if is_key_pressed(rl.KEY_SPACE):
            self.velocity -= self.jump_height
            play_sound(self.jump_sound)