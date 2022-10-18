let distance = 0
basic.forever(function () {
    distance = sonar.ping(
    DigitalPin.P0,
    DigitalPin.P1,
    PingUnit.Centimeters
    )
    basic.pause(1)
    while (distance < 45) {
        pins.servoWritePin(AnalogPin.P2, 90)
        music.playTone(988, music.tempo())
        basic.showIcon(IconNames.Sad)
        basic.pause(100)
        pins.servoWritePin(AnalogPin.P2, 0)
        break;
    }
    basic.showIcon(IconNames.Happy)
})
