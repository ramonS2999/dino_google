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
    def __init__(self, run_texture, jump_texture, pos, jump_sound):
        self.run_texture = run_texture
        self.jump_texture = jump_texture
        super().__init__(run_texture[0], pos)
        self.jump_sound = jump_sound
        self.velocity = 0
        self.gravity = 300
        self.jump_height = -400
        self.frame_index = 0

    def update(self, dt):
        # gravity
        self.velocity += self.gravity * dt
        self.pos.y += self.velocity * dt
        if self.pos.y > FLOOR_LINE:
            self.pos.y = FLOOR_LINE
            self.velocity = 0

        # jump input
        if is_key_pressed(rl.KEY_SPACE):
            self.velocity = self.jump_height
            play_sound(self.jump_sound)

        # animation
        self.frame_index += ANIMATION_SPEED * dt
        self.frame_index %= len(self.run_texture)

    def draw(self):
        self.texture = self.run_texture[int(self.frame_index)] if self.pos.y >= FLOOR_LINE else self.jump_texture
        super().draw()