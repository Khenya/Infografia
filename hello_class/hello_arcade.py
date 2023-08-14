import arcade 

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hola Arcade"

def draw_shapes():
    # arcade.draw_circle_filled(300,300,90,arcade.color.CADMIUM_YELLOW)
    # arcade.draw_triangle_filled(400,300,0,0,90,100,arcade.color.DARK_RASPBERRY)
    arcade.draw_rectangle_filled(300,210,200,200,arcade.color.BLUE_BELL)
    arcade.draw_triangle_filled(200,310,400,310,300,500,arcade.color.BISTRE_BROWN)
    # arcade.draw_rectangle_filled(250,110,225,200,arcade.color.BISTRE_BROWN)

if __name__ == "__main__":
    # crear ventana
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

    # cambiara el color de fondo
    arcade.set_background_color(arcade.color.BLACK_OLIVE)

    arcade.start_render()

    draw_shapes()

    arcade.finish_render()

    arcade.run()
