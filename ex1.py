def on_forever():
    if input.button_is_pressed(Button.B):
        basic.show_number(input.temperature()) #display the temperature
    if input.logo_is_pressed():
        basic.show_number(input.light_level())
basic.forever(on_forever)
