import pymunk

# crear space
space = pymunk.Space()
space.gravity = (0,-981)

# creaer body
body = pymunk.Body()
body.position = (50,100)

# crear shape y acloparlo al body
poly = pymunk.Poly.create_box(body)
poly.mass = 10

# agregar los objetos a space 
space.add(body,poly)

print_option= pymunk.SpaceDebugDrawOptions()

# correr en 100 pasos
for _ in range(100):
    space.step(0.02)
    space.debug_draw(print_option)