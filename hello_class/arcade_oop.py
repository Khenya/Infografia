import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hola Arcade"



class Hola(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        arcade.set_background_color(arcade.color.Gray)
    
    def on_draw(self):
        arcade.start_render()

        draw_shapes()
    
if __name__ == "__main__":
    app = Hola()
    arcade.run 