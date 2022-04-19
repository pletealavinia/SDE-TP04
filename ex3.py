def on_sound_loud():
    led.plot(0, 0)
    led.plot(1, 0)
    led.plot(2, 0)
    led.plot(3, 0)
    led.plot(4, 0)
input.on_sound(DetectedSound.LOUD, on_sound_loud)