def on_forever():
    images.icon_image(IconNames.SQUARE).show_image(0)
    if input.logo_is_pressed():
        images.icon_image(IconNames.SMALL_SQUARE).show_image(0)
basic.forever(on_forever)