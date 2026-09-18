from settings import *
from sprites import Dino, MovingSprite
from custom_timer import Timer

class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, DINO_NAME)
        init_audio_device()
        self.import_assets()
        self.sprites = []
        self.bg_sprites = []
        self.dino = Dino(
            self.assets['player_run'],
            self.assets['player_jump'],
            Vector2(100, FLOOR_LINE),
            self.audio['jump']
        )
        self.sprites.append(self.dino)
        self.timers = {
            'obstacle': Timer(3, self.spawn_obstacle, True, True),
            'cloud': Timer(5, self.spawn_cloud, True, True),
            'floor': Timer(2, self.spawn_floor, True, True),
            'floor_lines': Timer(0.2, self.spawn_floor_lines, True, True),
        }

    def import_assets(self):
        self.assets = {
            'player_run': [load_texture(join("assets", "dino", f"run{i}.png")) for i in range(2)],
            'player_jump': load_texture(join("assets", "dino", "jump.png")),
            'cacti': [load_texture(join("assets", "cactii", f"cactus{i}.png")) for i in range(4)],
            'clouds': [load_texture(join("assets", "clouds", f"cloud{i}.png")) for i in range(4)],
            'floor': [load_texture(join("assets", "floor", f"floor{i}.png")) for i in range(4)],
        }

        self.audio = {
            'jump': load_sound(join("audio", "jump.wav")),
        }

    def spawn_floor(self):
        sprite = MovingSprite(
            choice(self.assets['floor']),
            Vector2(WINDOW_WIDTH, FLOOR_LINE + 40),
            300
        )
        self.bg_sprites.append(sprite)
        self.timers['floor'].duration = get_random_value(1, 3)

    def spawn_cloud(self):
        sprite = MovingSprite(
            choice(self.assets['clouds']),
            Vector2(WINDOW_WIDTH, FLOOR_LINE - randint(160, 240)),
            randint(80, 120)
        )
        self.bg_sprites.append(sprite)

    def spawn_obstacle(self):
        sprite = MovingSprite(
            choice(self.assets['cacti']),
            Vector2(WINDOW_WIDTH, FLOOR_LINE + randint(-10, 10)),
            300
        )
        self.sprites.append(sprite)
 
    def spawn_floor_lines(self):
        image = gen_image_color(randint(2, 8), 2, MAIN_COLOR)
        texture = load_texture_from_image(image)
        sprite = MovingSprite(
            texture,
            Vector2(WINDOW_WIDTH, FLOOR_LINE + 160 + randint(-10, 30)),
            300
        )
        self.bg_sprites.append(sprite)

    def update(self, dt):
        for sprite in self.sprites + self.bg_sprites:
            sprite.update(dt)
        for timer in self.timers.values():
            timer.update()

    def draw(self):
        begin_drawing()
        clear_background(RAYWHITE)
        draw_line_ex(
            Vector2(0, FLOOR_LINE + 120), 
            Vector2(WINDOW_WIDTH, FLOOR_LINE + 120),
            10,
            MAIN_COLOR
        )

        for sprite in self.bg_sprites:
            sprite.draw()
        for sprite in self.sprites:
            sprite.draw()

        end_drawing()

    def run(self):
        while not window_should_close():
            dt = get_frame_time()
            self.update(dt)
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()