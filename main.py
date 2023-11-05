def on_button_pressed_a():
    personaje.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    personaje.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

personaje: game.LedSprite = None
game.set_score(0)
game.set_life(10)
objeto = game.create_sprite(randint(0, 4), 0)
personaje = game.create_sprite(2, 4)

def on_every_interval():
    objeto.change(LedSpriteProperty.Y, 1)
loops.every_interval(500, on_every_interval)

def on_forever():
    if objeto.get(LedSpriteProperty.Y) == 4:
        basic.pause(100)
        objeto.set(LedSpriteProperty.X, randint(0, 4))
        objeto.set(LedSpriteProperty.Y, 0)
    elif False:
        pass
basic.forever(on_forever)
