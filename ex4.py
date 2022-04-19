def on_forever():
    degrees = input.compass_heading()
    if degrees < 45 or degrees > 315:
        basic.show_string('N')
        basic.show_number(input.sound_level())
    elif degrees < 135:
        basic.show_string('E')
    elif degrees < 225:
        basic.show_string('S')
        basic.show_number(input.sound_level())
    elif degrees < 315:
        basic.show_string('W')
        basic.show_number(input.temperature())
        basic.show_number(input.light_level())
    else:
        basic.clear_screen()
basic.forever(on_forever)