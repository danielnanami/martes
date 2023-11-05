input.onButtonPressed(Button.A, function () {
    personaje.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    personaje.change(LedSpriteProperty.X, 1)
})
let personaje: game.LedSprite = null
game.setScore(0)
game.setLife(10)
let objeto = game.createSprite(randint(0, 4), 0)
personaje = game.createSprite(2, 4)
loops.everyInterval(500, function () {
    objeto.change(LedSpriteProperty.Y, 1)
})
basic.forever(function () {
    if (objeto.get(LedSpriteProperty.Y) == 4) {
        basic.pause(100)
        objeto.set(LedSpriteProperty.X, randint(0, 4))
        objeto.set(LedSpriteProperty.Y, 0)
    } else if (false) {
    	
    } else {
    	
    }
})
