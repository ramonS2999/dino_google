from settings import *
from sprites import Sprite, Dino

class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, DINO_NAME)
        init_audio_device()
        set_target_fps(FPS)
        self.dino = Dino(
            load_texture(join("assets", "dino", "run0.png")), 
            Vector2(100, FLOOR_LINE),
            load_sound(join("audio", "jump.wav"))
        )

    def update(self):
        self.dino.update()

    def draw(self):
        begin_drawing()
        clear_background(RAYWHITE)
        draw_line_ex(
            Vector2(0, FLOOR_LINE + 120), 
            Vector2(WINDOW_WIDTH, FLOOR_LINE + 120),
            10,
            MAIN_COLOR
        )

        self.dino.draw()

        end_drawing()

    def run(self):
        while not window_should_close():
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()