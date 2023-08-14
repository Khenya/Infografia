import arcade
import random
from app_objects import Tank, Enemy

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tank"
SPEED = 10

def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.rot_speed = 0.5
        self.speed = 10
        # primer tanque
        self.tank = Tank(200, 300, get_random_color())
        # segundo tanque 
        self.tank2 = Tank(600, 300, get_random_color())        
        # enemigos
        self.enemies = [
            Enemy(
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(0, SCREEN_HEIGHT),
                random.randrange(10, 50)
            )
            for _ in range(10)
        ]
        self.puntos1 = 0
        
        self.puntos2 = 0

    # primer tanque disparar 
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.tank.shoot(20)

    def on_key_press(self, symbol: int, modifiers: int):
        # primer tanque
        if symbol == arcade.key.UP:
            self.tank.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tank.speed = -SPEED

        if symbol == arcade.key.LEFT:
            self.tank.angular_speed = 1.5
        if symbol == arcade.key.RIGHT:
            self.tank.angular_speed = -1.5

        # segundo tanque
        if symbol == arcade.key.W:
            self.tank2.speed = SPEED
        if symbol == arcade.key.S:
            self.tank2.speed = -SPEED

        if symbol == arcade.key.A:
            self.tank2.angular_speed = 1.5
        if symbol == arcade.key.D:
            self.tank2.angular_speed = -1.5

        # disparar segundo tanke 
        if symbol == arcade.key.SPACE:
            self.tank2.shoot(20)

    def on_key_release(self, symbol: int, modifiers: int):
        # primer tanke
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.tank.speed = 0

        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.tank.angular_speed = 0

        # segundo tanke
        if symbol in (arcade.key.W, arcade.key.S):
            self.tank2.speed = 0

        if symbol in (arcade.key.A, arcade.key.D):
            self.tank2.angular_speed = 0

    def on_update(self, delta_time: float):
        self.tank.update(delta_time)
        self.tank2.update(delta_time)
        for e in self.enemies:
            if  e.detect_collision(self.tank):
                self.puntos1 += e.puntos_ganados
                e.puntos_ganados = 0
            elif e.detect_collision(self.tank2):
                self.puntos2 += e.puntos_ganados
                e.puntos_ganados = 0
        
    def on_draw(self):
        arcade.start_render()
        self.tank.draw()
        self.tank2.draw()
        for e in self.enemies:
            e.draw()

            # puntos tanke 1
            arcade.draw_text(f'Puntos Tanke 1: {self.puntos1 }', 10, 10, arcade.color.WHITE, 14)
        
            # puntos tanke 2
            arcade.draw_text(f'Puntos Tanke 2: {self.puntos2 }  ', 600, 10, arcade.color.WHITE, 14)


    
if __name__ == "__main__":
    app = App()
    arcade.run()
