input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Forever)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.stopAllSounds()
})
basic.forever(function on_forever() {
    
})
