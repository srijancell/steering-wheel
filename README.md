# Hand Steering Wheel(NEVER GAVE A DAMN AGAIN)

Hand Steering Wheel is a computer vision project that transforms hand movements into analog steering input using a webcam.

The project uses OpenCV and MediaPipe to track the position of the user's palm, converts the movement into a normalized steering value, and sends it to a virtual joystick through vJoy.

## Features

- Real-time hand tracking
- Analog steering input
- Palm-based steering control
- Calibration mode
- Dead zone implementation
- Steering visualization
- vJoy output for simulator compatibility

## Technologies

- Python
- OpenCV
- MediaPipe
- pyvJoy
- vJoy

## How It Works

1. Capture video from a webcam.
2. Detect the user's hand using MediaPipe.
3. Track the palm position.
4. Calibrate the center steering position.
5. Apply a dead zone to eliminate small unwanted movements.
6. Normalize hand movement into an analog steering value.
7. Send the steering value to a virtual joystick using vJoy.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/hand-steering-wheel.git
cd hand-steering-wheel
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Requirements

- opencv-python
- mediapipe
- pyvjoy

**vJoy** must also be installed separately.

## Future Improvements

- Steering smoothing
- Adjustable steering sensitivity
- Automatic calibration
- Multiple steering profiles
- Gesture-based throttle and brake
- Support for additional simulation games

## License

MIT License
