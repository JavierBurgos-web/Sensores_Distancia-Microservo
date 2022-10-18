distance = 0

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    basic.pause(1)
    while distance < 10:
        pins.servo_write_pin(AnalogPin.P2, 90)
        music.play_tone(988, music.tempo())
        basic.show_icon(IconNames.SAD)
        basic.pause(100)
        pins.servo_write_pin(AnalogPin.P2, 0)
        break
    music.stop_melody(MelodyStopOptions.FOREGROUND)
    basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
