def on_button_pressed_a():
    music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
        MelodyOptions.FOREVER)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
