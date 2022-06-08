from picamera import PiCamera
from gpiozero import MotionSensor

camera = PiCamera()
pir = MotionSensor(17)

i = 0


def capture_video():
    pir.wait_for_motion()
    camera.start_recording(f'images/vid{i}.h264')
    pir.wait_for_no_motion()
    camera.stop_recording()


while True:
    capture_video()
    i += 1
