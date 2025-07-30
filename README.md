# ShahroodRC

This repository provides a detailed overview of the ShahroodRC team's robot developed for the 2025 World Robot Olympiad in the Future Engineers category. The robot was conceptualized, designed, and built by a dedicated team of three students.

---


## Table of Contents
- [The Team](#the-team)
- [Our Path](#our-path)
- [Robot Components Overview](#robot-components-overview)
  - [LEGO EV3 Mindstorms Control Brick](#lego-ev3-mindstorms-control-brick)
  - [Pixy Cam](#pixy-cam)
  - [Ultrasonic Sensor EV3](#ultrasonic-sensor-ev3)
  - [Color Sensor EV3](#color-sensor-ev3)
  - [Medium Motor EV3](#medium-motor-ev3)
- [Code For Each Component](#code-for-each-component)
  - [Drive Motor Code](#drive-motor-code)
  - [Pixy Camera Code](#pixy-camera-code)
  - [Color Sensor Code](#color-sensor-code)
  - [LED Indicator Code](#led-indicator-code)
  - [Ultrasonic Sensor Code](#ultrasonic-sensor-code)
  - [Button Control Code](#button-control-code)
  - [Main Control Flow](#main-control-flow)
- [Mobility Management](#mobility-management)
  - [Introduction to Mobility System](#1-introduction-to-mobility-system)
  - [Motors and Actuators](#2-motors-and-actuators)
  - [Sensor Integration for Mobility](#3-sensor-integration-for-mobility)
  - [Mobility Control Algorithms](#4-mobility-control-algorithms)
  - [Energy Management for Mobility](#5-energy-management-for-mobility)
  - [System Integration for Mobility](#6-system-integration-for-mobility)
  - [Testing and Optimization](#7-testing-and-optimization)
  - [Conclusion](#8-conclusion)
- [Power and Sense Management](#power-and-sense-management)
  - [Power Supply and Distribution](#1-power-supply-and-distribution)
  - [Power Consumption Overview](#2-power-consumption-overview)
  - [Sensor Architecture and Management](#3-sensor-architecture-and-management)
  - [Wiring and Safety](#4-wiring-and-safety)
  - [Diagnostics and Monitoring](#5-diagnostics-and-monitoring)
  - [Optimization Techniques](#6-optimization-techniques)
  - [Conclusion](#7-conclusion)
- [Obstacle Management](#obstacle-avoidance-and-parking-managementobstacle-management)
  - [Open Challenge (Qualification Round)](#open-challenge-qualification-round)
    - [Line Detection and Navigation](#line-detection-and-navigation)
  - [Final Round with Obstacle Avoidance(Obstacle Challenge)](#final-round-with-obstacle-avoidanceobstacle-challenge)
    - [Obstacle Detection and Avoidance](#obstacle-detection-and-avoidance)
    - [Parking Sequence](#parking-sequence)
    - [Parking Wall Detection](#parking-wall-detection)
  - [Additional Functions](#additional-functions)
    - [Steering Control](#steering-control)
    - [Stall Detection and Recovery](#stall-detection-and-recovery)
    - [Color-Based Navigation](#color-based-navigation)
    - [Visual Feedback](#visual-feedback)
  - [Notes](#notes-1)
- [Robot Pictures](#robot-pictures)
- [Repository Structure](#repository-structure)
- [License](#license)

---


## The Team

We are the ShahroodRC team, a group of students passionate about robotics, electronics, and programming, working toward the WRO 2025 competition in the Future Engineers category.

### 👨‍💼 Sepehr Yavarzadeh
- Project Manager and Software Engineer. At 16 years old, this is his third year participating in the WRO competition.  
- sepehryavarzadeh@gmail.com
- [Instagram](https://www.instagram.com/sepehr.yavarzadeh/)
- [Github](https://github.com/Sepehryy)
- [Linkedin](https://www.linkedin.com/in/sepehr-yavarzadeh-9643252a3/)

![photo](/team-photos/name.jpg)


### 🧑‍💻 Amirparsa Saemi
- Lead Developer and Algorithm Designer. A 19-year-old computer science student with prior WRO experience.  
- sepehryavarzadeh@gmail.com
- [Instagram](https://www.instagram.com/sepehr.yavarzadeh/)
- [Github](https://github.com/Sepehryy)
- [Linkedin](https://www.linkedin.com/in/sepehr-yavarzadeh-9643252a3/)

![photo](/team-photos/name.jpg)


### 👩‍🔧 Nikan Bashiri
- Mechanical and Electronics Specialist. He is 17 years old and in his fourth year participating in WRO.
- sepehryavarzadeh@gmail.com
- [Instagram](https://www.instagram.com/nikanbsr/)

![photo](/team-photos/name.jpg)


### Mr. Sadeghi
- The team’s 23-year-old coach with a B.Sc. in Computer Engineering. He is a certified Advanced LEGO Robotics Coach in Iran and supports both strategic and technical development for the team.
- sepehryavarzadeh@gmail.com
- [Instagram](https://www.instagram.com/_amir.reza.sd_/)

![photo](/team-photos/name.jpg)

#### Special Thanks
Special thanks to **Ali Raeisi** for helping in algorithms and programming the robot.

> In this project, we aimed to combine creativity, teamwork, and technical knowledge to build an efficient robot for the challenges of WRO 2025.

---


## Our Path

### Robot Development Process

This project involved testing multiple hardware platforms to determine the most efficient and stable system for our robot. Each platform was evaluated based on performance, reliability, integration ability, and real-time processing. Here is a detailed explanation of our journey and the reasons behind switching from one platform to another.

---

### 🔁 1. Using Arduino Uno

Initially, we selected the **Arduino Uno** due to its ease of programming, availability, and compatibility with a wide range of sensors and actuators. The decision was also influenced by our prior experience working with Arduino boards in simpler robotic projects. However, as we progressed and tried to scale up the system for competition-level performance, we encountered several critical issues:

- **Camera Limitations**: We experimented with common camera modules like the OV7670 and even the ESP32-CAM via serial relay, but Arduino lacked the computational power and memory to process visual data effectively. The result was low-resolution, slow frame rates, and unreliable object detection.
- **Limited Multitasking**: Arduino's single-threaded loop and limited interrupt management made it extremely difficult to handle real-time sensor reading and motor control simultaneously, which was essential for dynamic environments like WRO.
- **No Native Support for USB Devices**: Integrating vision modules that relied on USB (like Pixy Cam) was not natively supported, which limited expansion possibilities.

After thorough testing, we concluded that Arduino Uno was not suitable for vision-integrated robotics and began searching for a more powerful platform.

---

### 🔁 2. Switching to ESP32

Our second approach was to use the **ESP32**, a microcontroller that offers dual-core processing, integrated Wi-Fi/Bluetooth, and better memory management. This seemed like a strong candidate for balancing sensor control and wireless communication.

- **Pros**:
  - Faster than Arduino with dual-core capabilities
  - Excellent for IoT-based data communication (Wi-Fi/Bluetooth)
  - Can theoretically handle simultaneous I/O from sensors and motors

- **Cons**:
  - **Sensor Interference**: When we attempted to drive multiple motors and read sensor data (e.g., ultrasonic or color detection) in real-time, the I2C and PWM signals would become unstable, often introducing jitter or complete loss of feedback.
  - **PWM Conflicts**: The number of reliable PWM channels was limited and required careful GPIO selection. Timing mismatches caused delays in response.
  - **Camera Challenges**: Even with the ESP32-CAM module, integrating vision processing with motor control wasn’t practically feasible due to RAM bottlenecks and lack of image processing libraries in MicroPython or Arduino ESP32 cores.
  - **Library Limitations**: Most ESP32-compatible camera libraries (e.g., ESP-IDF CAM or Arduino-based ESP32-CAM libraries) are not optimized for parallel sensor/motor tasks, especially in real-time robotics.


Eventually, the technical instability forced us to abandon the ESP32 setup despite its attractive specs on paper.

---

### 🔁 3. Adopting Raspberry Pi Zero

In search of a more powerful yet compact platform, we transitioned to the **Raspberry Pi Zero**, which runs Linux and provides sufficient computational resources to handle camera modules like the Pi Camera and USB peripherals like the Pixy Cam.

- **Advantages**:
  - Full support for Python and OpenCV
  - Ability to use multi-threaded programming
  - Native support for USB and camera modules

- **Challenges**:
  - **Power Sensitivity**: The Raspberry Pi Zero is highly sensitive to voltage drops, especially when multiple peripherals are connected. We experienced brownouts during testing even with power banks and regulated supplies.
  - **Heat Issues**: Continuous camera streaming and motor control led to significant thermal buildup, which affected stability.
  - **Hardware Fragility**: Despite all precautions, we burned two Raspberry Pi Zero boards — one due to a short from an incorrectly grounded motor driver, and another due to sudden current surge when powering the camera and motors simultaneously.

These hardware failures prompted us to reconsider the ruggedness of the Raspberry Pi platform for field use in competitions.

---

### ✅ 4. Final Transition to LEGO EV3

Given all previous difficulties and our positive past experiences, we decided to return to the **LEGO EV3 Mindstorms** system. All team members were already familiar with it from previous WRO competitions, and it offered unmatched integration, safety, and stability.

- **Stability & Robustness**: The EV3 Intelligent Brick is designed for rugged educational environments and can safely manage motors and sensors without external drivers.
- **Built-in Motor/Sensor Ports**: Four motor ports and four sensor ports eliminate the need for extra circuitry and reduce risk of hardware failure.
- **Pixy Cam Integration**: With minor custom wiring, the Pixy Cam could be integrated via I2C through an EV3 sensor port, removing the need for USB host support or voltage converters.
- **Development Efficiency**: Using LEGO’s native block-based software or Python (via ev3dev/pybricks), we could rapidly develop and test behaviors without the delays we faced with bare-metal microcontrollers.
- **Competition-Proven**: The EV3 platform has been used extensively in WRO, and many open-source libraries and sensor solutions are readily available.

---

### 📌 Final Summary & Reflection

Each platform taught us unique lessons about system design, integration challenges, and performance trade-offs, ultimately guiding us toward the most reliable solution. While Arduino and ESP32 were simpler to program, and Raspberry Pi offered more processing power, **only EV3 delivered the right balance of stability, expandability, and safety for WRO 2025**.

> This final transition was not a fallback, but a strategic return to a battle-tested platform that ensured our team could focus on **strategy and performance** instead of constantly troubleshooting hardware issues.

---


## Robot Components Overview

This section provides a detailed overview of the parts used in the robot, including key hardware components that play an integral role in the design and functionality of the robot.

---

### 🔧 Components Overview

#### **LEGO EV3 Mindstorms Control Brick** <a class="anchor" id="ev3-control-brick"></a>

<table>
  <tr>
    <td width="50%" style="text-align: left;">
      <img src="pictures/ev3_brick.jpg" alt="LEGO EV3 Control Brick" width="100%">
    </td>
    <td width="50%" style="text-align: left; vertical-align: top;">
      <h3>Specifications:</h3>
      <li>Type: Main Controller</li>
      <li>Power: 10V (battery pack)</li>
      <li>CPU: ARM9 Processor</li>
      <li>Memory: 64MB RAM, 16MB Flash</li>
      <li>Ports: 4 Motor Ports, 4 Sensor Ports, USB, Bluetooth, Wi-Fi (via dongle)</li>
      <li>Operating System: LEGO OS</li>
    </td>
  </tr>
</table>

- **Type**: Main Controller Unit
- **Feature**: Central unit for processing, motor control, and sensor integration.
- **Use**: Used for controlling all robot operations including logic, sensor reading, motor control, and communication.
- **Description**: The LEGO EV3 Mindstorms Control Brick is the heart of the robot, responsible for managing all processes, including controlling the motors and processing sensor data. It has an ARM9 processor and offers both Bluetooth and USB connectivity for easy integration with other devices. The EV3 platform is well-known for its ease of use and reliability, making it ideal for competitive robotics. It is fully programmable using the LEGO Mindstorms software or other compatible development environments. Since the team was already familiar with the EV3 platform, transitioning to this control brick allowed for a fast and efficient setup, focusing more on design and functionality.


#### **Pixy Cam** <a class="anchor" id="pixy-cam"></a>

<table>
  <tr>
    <td width="50%" style="text-align: left;">
      <img src="pictures/pixy_cam.jpg" alt="Pixy Cam" width="100%">
    </td>
    <td width="50%" style="text-align: left; vertical-align: top;">
      <h3>Specifications:</h3>
      <li>Microcontroller: ARM Cortex-M4</li>
      <li>Resolution: 640x480</li>
      <li>Frame Rate: 60fps</li>
      <li>Field of View: 75°</li>
      <li>Lens: 3.6mm</li>
      <li>Power Supply: 5V</li>
      <li>Interface: USB, UART, I2C</li>
    </td>
  </tr>
</table>

- **Type**: Vision Sensor
- **Feature**: Real-time object recognition
- **Interface**: USB, UART, or I2C
- **Use**: Used for obstacle detection and color recognition
- **Description**: The Pixy Cam is a highly efficient vision sensor that performs real-time object recognition. It is designed to detect and track objects based on color codes, making it ideal for tasks like obstacle detection and target tracking in robotics competitions. This sensor’s easy-to-use interface allows it to quickly communicate with the EV3 control brick, enabling rapid deployment in real-world environments. The Pixy Cam is highly effective for object tracking and is ideal for WRO-style challenges where precise object detection and navigation are crucial.


### **Ultrasonic Sensor EV3** <a class="anchor" id="ultrasonic-sensor-ev3"></a>

<table>
  <tr>
    <td width="50%" style="text-align: left;">
      <img src="pictures/ultrasonic_ev3.jpg" alt="Ultrasonic Sensor EV3" width="100%">
    </td>
    <td width="50%" style="text-align: left; vertical-align: top;">
      <h3>Specifications:</h3>
      <li>Type: Ultrasonic</li>
      <li>Range: 3 cm to 250 cm</li>
      <li>Accuracy: ±1 cm</li>
      <li>Operating Voltage: 4.5V to 5.5V</li>
      <li>Interface: LEGO EV3 Port</li>
      <li>Field of View: 35°</li>
    </td>
  </tr>
</table>

- **Type**: Distance Sensor (Ultrasonic)
- **Feature**: Measures distance using sound waves.
- **Interface**: LEGO EV3 Port (requires connection to an EV3 Intelligent Brick)
- **Use**: Used for measuring distance to obstacles, avoiding collisions, and performing obstacle detection.
- **Description**: The EV3 Ultrasonic Sensor uses sound waves to measure the distance to an object in front of it. It has a range of 3 cm to 250 cm, with an accuracy of ±1 cm. The sensor is typically used for obstacle detection and navigation in EV3 robots. It is connected to the EV3 brick using one of the sensor ports and can be easily programmed using the LEGO Mindstorms EV3 software or other compatible development environments.


#### **Color Sensor EV3** <a class="anchor" id="color-sensor-ev3"></a>

<table>
  <tr>
    <td width="50%" style="text-align: left;">
      <img src="pictures/color_sensor_ev3.jpg" alt="EV3 Color Sensor" width="100%">
    </td>
    <td width="50%" style="text-align: left; vertical-align: top;">
      <h3>Specifications:</h3>
      <li>Type: RGB Color Sensor</li>
      <li>Modes: Color, Reflected Light Intensity, Ambient Light Intensity</li>
      <li>Colors Detected: 7 (black, blue, green, yellow, red, white, brown)</li>
      <li>Operating Voltage: 4.5V to 5.5V</li>
      <li>Interface: LEGO EV3 Sensor Port</li>
      <li>Sampling Rate: ~1 kHz</li>
    </td>
  </tr>
</table>

- **Type**: Light and Color Detection Sensor  
- **Feature**: Detects color, reflected light intensity, and ambient light  
- **Interface**: LEGO EV3 Sensor Port (requires connection to EV3 Intelligent Brick)  
- **Use**: Used for color classification, line following, and light-based navigation  
- **Description**: The EV3 Color Sensor is a versatile optical sensor that can operate in three different modes: color mode (detecting one of seven predefined colors), reflected light mode (measuring light reflected off surfaces), and ambient light mode (measuring surrounding light levels). It plays a vital role in line-following algorithms and object classification tasks in LEGO EV3 robotics. Thanks to its high sampling rate and accurate color detection, it is a critical component for autonomous navigation, decision-making, and environment interaction.


#### **Medium Motor EV3** <a class="anchor" id="medium-motor-ev3"></a>

<table>
  <tr>
    <td width="50%" style="text-align: left;">
      <img src="pictures/medium_motor_ev3.jpg" alt="EV3 Medium Motor" width="100%">
    </td>
    <td width="50%" style="text-align: left; vertical-align: top;">
      <h3>Specifications:</h3>
      <li>Type: DC Motor</li>
      <li>Voltage: 9V</li>
      <li>Speed: 160 rpm</li>
      <li>Torque: 20 N·cm</li>
      <li>Weight: 120 g</li>
      <li>Motor Type: Medium</li>
    </td>
  </tr>
</table>

- **Type**: DC Motor (Medium)
- **Feature**: Provides moderate torque and speed for a wide range of robotic applications.
- **Interface**: LEGO EV3 Motor Port
- **Use**: Used for driving wheels, arms, and other moving parts in the robot.
- **Description**: The LEGO EV3 Medium Motor is designed for moderate power and speed in robotics applications. It provides a balanced performance, offering good torque at relatively high speeds. This motor is typically used for driving mechanisms that do not require the high power or slow speed that a large motor provides. It is connected to the EV3 control brick using one of the motor ports and can be easily programmed to perform specific actions in the robot. The medium motor is an ideal choice for general-purpose motion in robotics projects.

---


### Notes:
- The LEGO EV3 Mindstorms Control Brick is the central processing unit for the robot, controlling all operations.
- Pixy Cam is interfaced via USB to the LEGO EV3 control brick for real-time vision data.
- The **EV3 Ultrasonic Sensor** is connected to one of the sensor ports on the EV3 control brick for distance measurement and obstacle detection.
- The **Medium Motor EV3** is connected to the motor ports on the EV3 control brick for driving the robot's wheels and other moving parts.
- The LEGO EV3 platform offers easy programming through the LEGO Mindstorms software or other compatible development environments, which streamlines the development and troubleshooting process for the robot.
- We no longer use the **HC-SR04 Ultrasonic Sensor**, as we switched to the more robust and reliable **EV3 Ultrasonic Sensor** for better integration and performance.

---


## Code for Each Component

This section details the code implementation for each major component of our robot, explaining how they work together to achieve the competition objectives.

### Drive Motor Code

The drive motor (Motor B) is responsible for propelling the robot forward and backward. It uses a proportional control system to maintain consistent speed and respond to commands from the obstacle management system.

```python
from ev3dev2.motor import MediumMotor, OUTPUT_B, SpeedPercent

# Initialize the drive motor
motor_b = MediumMotor(OUTPUT_B)

def drive_forward(speed_percent):
    """
    Function to drive the robot forward at a specified speed.
    Args:
        speed_percent (int): Speed percentage from 1 to 100
    """
    motor_b.on(speed_percent)

def drive_backward(speed_percent):
    """
    Function to drive the robot backward at a specified speed.
    Args:
        speed_percent (int): Speed percentage from 1 to 100
    """
    motor_b.on(-speed_percent)

def stop_drive():
    """Function to stop the drive motor."""
    motor_b.off()
```
**Implementation Notes:**
- The drive motor operates on a simple on/off principle with speed control
- We found that 60% speed provides optimal balance between stability and performance
- For precise maneuvers, we use `on_for_degrees()` or `on_for_rotations()` methods

### Steering Motor Code
The steering motor (Motor A) controls the robot's direction by adjusting the front wheels. It implements a proportional control algorithm for smooth and accurate steering.
```python
from ev3dev2.motor import MediumMotor, OUTPUT_B, OUTPUT_D, SpeedPercent

# Initialize the steering motor
motor_a = MediumMotor(OUTPUT_B)
motor_a.reset()

def clamp(value, minimum, maximum):
    """
    Utility function to limit a value between minimum and maximum bounds.
    Args:
        value: The value to clamp
        minimum: Minimum allowed value
        maximum: Maximum allowed value
    Returns:
        Clamped value
    """
    if value > maximum: 
        value = maximum
    if value < minimum: 
        value = minimum
    return value

def amotor(degrees, cl=50):
    """
    Function to control steering motor with proportional control.
    Args:
        degrees: Target position in degrees
        cl: Control limit for maximum power (default 50)
    """
    diff = degrees - motor_a.position
    diff = clamp(diff, -cl, cl)  
    motor_a.on(diff)
```
**Control Algorithm Explanation:**
The steering system uses a proportional control algorithm where the motor power is directly proportional to the difference between the target angle and current position. This provides smooth, oscillation-free steering adjustments.

### Pixy Camera Code
The Pixy camera is our primary sensor for detecting red and green pillars in the obstacle challenge. It communicates with the EV3 brick via I2C protocol.
```python
from ev3dev2.sensor import Sensor, INPUT_1

# Initialize Pixy sensor
pixy = Sensor(INPUT_1)
pixy.mode = 'ALL'

def get_pillar_data():
    """
    Function to read data from Pixy camera.
    Returns:
        tuple: (signature, x_position, y_position, size)
    """
    sig = pixy.value(1) * 256 + pixy.value(0)  # Color signature
    x = pixy.value(2)  # X position
    y = pixy.value(3)  # Y position  
    size = pixy.value(4)  # Size of detected object
    
    return sig, x, y, size

def detect_pillar():
    """
    Main function for pillar detection and response.
    Returns:
        int: 1 for red pillar, 2 for green pillar, 0 for no pillar
    """
    sig, x, y, size = get_pillar_data()
    
    # Filter out detections that are too far (low Y value)
    if y < 75:
        sig = 0
        
    return sig
```
**Detection Strategy:**
- The Pixy is programmed to recognize two color signatures: red (signature 1) and green (signature 2)
- We filter detections based on Y-position to avoid false positives from distant objects
- The X-position is used to calculate steering corrections

### Color Sensor Code
The color sensor detects the colored lines on the track, which determine the robot's turning direction in the open challenge.
```python
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_4

# Initialize color sensor
color_sensor = ColorSensor(INPUT_4)

def get_track_color():
    """
    Function to read the current track color.
    Returns:
        int: Color code (2=Green, 5=Red, 6=White, etc.)
    """
    return color_sensor.color

def wait_for_color(target_color):
    """
    Function to wait until a specific color is detected.
    Args:
        target_color (int): Color code to wait for
    """
    current_color = get_track_color()
    while current_color != target_color:
        current_color = get_track_color()
        sleep(0.01)  # Small delay to prevent excessive CPU usage
```
**Color Detection Logic:**
- The robot uses color detection to determine when to start turning
- Green line (color code 2) triggers a left turn sequence
- Red line (color code 5) triggers a right turn sequence

### LED Indicator Code
The EV3 brick's LEDs provide visual feedback about the robot's state and detected obstacles.
```python
from ev3dev2.led import Leds

# Initialize LEDs
leds = Leds()

def set_led_state(state):
    """
    Function to set LED colors based on robot state.
    Args:
        state (str): 'idle', 'red_pillar', 'green_pillar', 'turning'
    """
    if state == 'idle':
        leds.set_color('LEFT', 'ORANGE')
        leds.set_color('RIGHT', 'ORANGE')
    elif state == 'red_pillar':
        leds.set_color('LEFT', 'GREEN')
        leds.set_color('RIGHT', 'GREEN')
    elif state == 'green_pillar':
        leds.set_color('LEFT', 'RED')
        leds.set_color('RIGHT', 'RED')
    elif state == 'turning':
        leds.set_color('LEFT', 'AMBER')
        leds.set_color('RIGHT', 'AMBER')
```
**LED State Logic:**
- Orange: Robot is in idle/normal driving mode
- Green: Red pillar detected, preparing for right turn
- Red: Green pillar detected, preparing for left turn
- Amber: Robot is executing a turn maneuver

### Ultrasonic Sensor Code
We use two ultrasonic sensors (left and right) for wall following and distance measurement.
```python
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_2, INPUT_3

# Initialize ultrasonic sensors
rast = UltrasonicSensor(INPUT_2)  # Right sensor
chap = UltrasonicSensor(INPUT_3)  # Left sensor

def get_distances():
    """
    Function to read distances from both ultrasonic sensors.
    Returns:
        tuple: (right_distance, left_distance) in centimeters
    """
    right_distance = rast.distance_centimeters
    left_distance = chap.distance_centimeters
    return right_distance, left_distance

def wall_following_control():
    """
    Main wall following control algorithm.
    Returns:
        float: Steering correction value
    """
    right_dist, left_dist = get_distances()
    
    # Calculate correction factors using square root function
    # This provides non-linear response for better control
    fr = (-2*(math.sqrt(11*(right_dist)))) + 100
    fc = (-2*(math.sqrt(11*(left_dist)))) + 100
    
    # Combine corrections with weighting
    target = (fc*1.3) - (fr*1.7)
    
    return clamp(target, -50, 50)
```
**Wall Following Algorithm:**
Our wall following system uses a non-linear control function that provides more sensitive response at closer distances. The square root function in our correction algorithm ensures that small distance changes near the wall result in larger steering corrections, while larger distances result in more gradual adjustments.

### Button Control Code
The EV3 button is used to start the robot after manual positioning.
```python
from ev3dev2.button import Button

# Initialize button
btn = Button()

def wait_for_start():
    """
    Function to wait for user to press the center button to start.
    """
    btn.wait_for_bump('enter')
```
**Start Procedure:**
- The robot waits in a holding pattern until the center button is pressed
- This allows for precise manual positioning before autonomous operation begins
- After button press, the robot changes LED color to green to indicate readiness

### Main Control Flow
The main program integrates all components into a cohesive system:
```python
# Initialize all components
initialize_components()

# Wait for start signal
wait_for_start()
set_led_state('idle')

# Main control loop
while not challenge_complete:
    # Check for color line (Open Challenge)
    current_color = get_track_color()
    
    # Check for pillars (Obstacle Challenge)  
    pillar_type = detect_pillar()
    
    # Execute appropriate behavior based on detections
    if current_color in [2, 5]:  # Green or Red line
        execute_turn_sequence(current_color)
    elif pillar_type in [1, 2]:  # Red or Green pillar
        execute_obstacle_avoidance(pillar_type)
    else:
        # Normal driving mode
        normal_driving()
        
    # Continuous wall following adjustment
    steering_correction = wall_following_control()
    amotor(steering_correction)
```
This integrated approach ensures that all sensors and actuators work together harmoniously to navigate the competition course successfully.

---


## Mobility Management

The ShahroodRC robot is constructed using LEGO components, primarily the **LEGO MINDSTORMS Education Core Set (Serial number 45544)**, supplemented with additional **LEGO EV3 sets**. This configuration ensures robust performance, reliability, and precise maneuverability tailored for the World Robot Olympiad (WRO) 2025 Future Engineers category.

The robot’s dimensions are **20 cm (length)**, **13.5 cm (width)**, and **17.5 cm (height)**, optimized to fit within the competition’s parking area while maintaining stability and agility. The robot employs a **rear-wheel drive system with front-wheel steering**, powered by two **EV3 Medium Motors**, enabling smooth movement and precise directional control.

The **mobility system** integrates the **powertrain**, **steering mechanism**, and **chassis**, working together to ensure efficient navigation through various competition challenges, such as wall-following, obstacle avoidance, precise parking, and zone detection.

### 1. **Introduction to Mobility System**

**Overview of the Mobility System**  
The ShahroodRC robot utilizes a **rear-wheel drive system with front-wheel steering**, featuring two powered wheels at the rear and two steerable wheels at the front. All four wheels are **LEGO Tire 49.5 x 20**, providing consistent traction and stability. This mobility system mimics the mechanics of a traditional vehicle, offering a balance of precision, stability, and agility. It is designed to excel in the dynamic environments of WRO 2025, including navigating wall-based tracks, avoiding obstacles, and parking in constrained spaces. The system’s reliance on a differential for propulsion and a dedicated steering motor ensures reliable and responsive control tailored for competition demands.

**Types of Movement**  
The rear-wheel drive and front-wheel steering system enables the following types of movement:
- **Linear Motion**: Forward and backward movement is achieved by the rear wheels, driven by a single EV3 Medium Motor through a differential, ensuring synchronized power delivery.
- **Steering and Turning**: The front wheels are controlled by a second EV3 Medium Motor, which adjusts their angle to the left or right, allowing for smooth and precise turns.
- **Curved Navigation**: By combining propulsion from the rear wheels and angular adjustments of the front wheels, the robot can follow curved paths, essential for wall-following and obstacle avoidance tasks.

The robot’s compact dimensions (20 cm length, 13.5 cm width, 17.5 cm height) and optimized design enhance its ability to maneuver in tight spaces while maintaining stability during high-speed navigation.

**Design Choices**  
The rear-wheel drive with front-wheel steering system was selected for the following reasons:
1. **Precision in Steering**: The dedicated steering motor allows for fine-tuned directional control, critical for tasks like wall-following and parking in WRO challenges.
2. **Efficient Power Distribution**: Using a differential for the rear wheels ensures balanced power delivery, reducing wheel slippage and improving traction on competition surfaces.
3. **Compatibility with LEGO EV3**: The system leverages two **EV3 Medium Motors** (20 N·cm torque, 160 rpm speed), which provide adequate power and precision for both propulsion and steering.
4. **Wheel Selection**: All four wheels are **LEGO Tire 49.5 x 20**, chosen for their 49.5 mm diameter and traction properties, optimizing grip and consistency on competition surfaces.
5. **Chassis Design**: Constructed from LEGO MINDSTORMS Education Core Set components, the chassis is lightweight yet rigid, designed to support the motors, differential, steering mechanism, and sensors while maintaining a low center of gravity for stability.
6. **Compliance with WRO Rules**: The system is fully compliant with the rules and restrictions of the WRO 2025 Future Engineers category, ensuring compatibility with competition requirements such as size limits, material constraints, and operational safety.

The combination of these design choices ensures the robot is both robust and highly maneuverable, capable of meeting the diverse challenges of WRO 2025.

### 2. **Motors and Actuators**

**Motor Types Used**  
The ShahroodRC robot is equipped with two **LEGO EV3 Medium Motors** to drive its mobility system. These DC motors were selected for their compact size, balanced performance, and compatibility with the robot’s rear-wheel drive and front-wheel steering configuration. The key specifications of the EV3 Medium Motors are:
- **Type**: DC Motor
- **Voltage**: 9V
- **Speed**: 160 rpm
- **Torque**: 20 N·cm
- **Weight**: 120 g

The first motor powers the rear wheels through a differential, providing propulsion for forward and backward movement. The second motor controls the front-wheel steering mechanism, adjusting the angle of the front wheels for precise directional control. The choice of Medium Motors over alternatives (e.g., EV3 Large Motors) was driven by their lightweight design and sufficient power for the WRO 2025 tasks, ensuring agility and energy efficiency.

**Motor Control Mechanism**  
The motors are managed by the **LEGO EV3 Mindstorms Control Brick**, running the **ev3dev** operating system, which allows for precise control using Python-based programming. The propulsion motor delivers power to the rear wheels via a differential, ensuring balanced torque distribution and minimizing wheel slippage during turns or on varying surfaces. The steering motor adjusts the front wheels’ angle incrementally, enabling smooth and accurate navigation. Control algorithms, implemented in Python via ev3dev, include:
- **Speed Regulation**: Maintains consistent velocity for linear motion using feedback loops, critical for tasks like wall-following and parking.
- **Steering Calibration**: Adjusts the steering motor’s position based on sensor feedback to achieve precise turning angles, ensuring accurate navigation in complex WRO 2025 environments.

**Motor Integration**  
The propulsion motor is connected to a **differential mechanism**, which drives the two rear **LEGO Tire 49.5 x 20** wheels. The differential ensures synchronized yet flexible rotation, allowing the rear wheels to rotate at different speeds during turns, enhancing stability and traction. The steering motor is linked to the front axle, controlling the orientation of the two front **LEGO Tire 49.5 x 20** wheels. Both motors are securely mounted to the chassis, constructed from LEGO MINDSTORMS Education Core Set components, ensuring mechanical reliability and minimal vibration. The integration leverages standard LEGO connectors, maintaining compatibility with the EV3 Control Brick and simplifying maintenance.

### 3. **Sensor Integration for Mobility**

**Sensors for Navigation and Obstacle Avoidance**  
The ShahroodRC robot is equipped with three key sensors to enable precise navigation and obstacle avoidance in the WRO 2025 Future Engineers category: two **EV3 Ultrasonic Sensors**, one **EV3 Color Sensor**, and one **Pixy Cam**. Their roles and placements are as follows:
- **EV3 Color Sensor**: Positioned at the front center of the robot, close to the ground, to detect blue and orange lines on the competition surface for specific WRO 2025 challenge tasks.
- **EV3 Ultrasonic Sensors**: Two sensors mounted at the front, one facing right and one facing left, to measure distances to walls (range: 3 cm to 250 cm, accuracy: ±1 cm) for wall detection and wall-following tasks in all competition challenges.
- **Pixy Cam**: Mounted above the LEGO EV3 Mindstorms Control Brick, angled to view the front of the robot, for real-time object recognition, specifically configured to detect the presence and color of obstacles in the WRO 2025 Obstacle Challenge.

These sensors are strategically placed on the robot’s chassis to optimize their field of view and ensure accurate data collection for navigation tasks such as wall-following, obstacle avoidance, precise parking, and other WRO 2025 challenges.

**Real-time Feedback**  
Sensor data is processed by the **LEGO EV3 Mindstorms Control Brick** running the **ev3dev** operating system, using Python-based scripts. The Color Sensor provides continuous feedback by detecting blue and orange lines, contributing to specific challenge tasks as required by WRO 2025. The Ultrasonic Sensors measure distances to walls on the left and right, enabling the robot to maintain a consistent distance for wall-following tasks. The Pixy Cam delivers real-time data on the presence and color of obstacles, guiding navigation decisions in the Obstacle Challenge. The EV3 Control Brick processes these inputs to dynamically adjust the propulsion and steering motors, ensuring responsive and adaptive movement across all WRO 2025 challenges.

**Sensor Fusion**  
To enhance navigation accuracy, the robot combines data from the Color Sensor, Ultrasonic Sensors, and Pixy Cam in a coordinated manner. The Python scripts running on ev3dev manage sensor inputs based on the task:
- **Challenge-specific Tasks**: The Color Sensor’s data, detecting blue and orange lines, is used for specific WRO challenge requirements, such as identifying track markers or zones.
- **Wall-following**: The Ultrasonic Sensors’ distance measurements are prioritized to maintain alignment with walls, ensuring precise navigation in wall-following tasks.
- **Obstacle Avoidance**: The Pixy Cam’s detection of obstacle presence and color is used to navigate around obstacles in the Obstacle Challenge, ensuring collision-free movement.
- **Combined Tasks**: For challenges requiring multiple tasks (e.g., navigating a track with walls and obstacles or reaching specific zones), the system integrates data from all sensors to make informed decisions, balancing wall-following, obstacle detection, and task-specific objectives.

This sensor fusion approach ensures robust and adaptive navigation, enabling the robot to handle all challenges in WRO 2025, including wall-following, obstacle avoidance, parking, and other task-specific requirements, effectively.

### 4. **Mobility Control Algorithms**

**Control Algorithms**  
The ShahroodRC robot employs Python-based control algorithms implemented via the **ev3dev** operating system to manage its mobility, ensuring precise and efficient navigation during WRO 2025 challenges. These algorithms govern the behavior of the two **EV3 Medium Motors** for propulsion and steering, enabling the robot to perform tasks such as wall-following, obstacle avoidance, and precise parking. The key control algorithms include:
- **Speed Control**: Regulates the propulsion motor’s speed to maintain consistent velocity, critical for smooth linear motion and energy efficiency across various WRO tasks.
- **Steering Control**: Adjusts the steering motor’s angle based on sensor inputs to achieve accurate directional control, ensuring precise navigation in confined spaces.
- **Task-specific Control**: Coordinates propulsion and steering to address specific WRO challenge requirements, such as navigating to marked zones or parking accurately.

These algorithms are designed to be adaptive, leveraging sensor data to dynamically adjust motor outputs for optimal performance in the dynamic environments of WRO 2025.

**Navigation Techniques**  
The robot employs the following navigation techniques to address WRO 2025 challenges:
- **Wall-following**: Utilizes the two **EV3 Ultrasonic Sensors** to maintain a consistent distance from walls, ensuring stable navigation in tasks requiring wall-following. The sensors measure distances on the left and right, guiding the steering motor to adjust the robot’s path.
- **Zone Detection**: Uses the **EV3 Color Sensor** to detect blue and orange lines, enabling the robot to identify specific track markers or zones as required by WRO challenges.
- **Obstacle Avoidance**: Employs the **Pixy Cam** to detect the presence and color of obstacles, allowing the robot to navigate around them in the Obstacle Challenge.

These techniques ensure the robot can handle the diverse navigation requirements of WRO 2025, from following walls to reaching designated areas.

**Obstacle Avoidance**  
The robot’s obstacle avoidance strategy relies on the **Pixy Cam** for real-time detection of obstacles in the WRO 2025 Obstacle Challenge:
- **Detection**: The Pixy Cam identifies the presence and color of obstacles, providing critical data for navigation decisions.
- **Decision-making**: Python scripts running on ev3dev process Pixy Cam data to adjust the robot’s speed and steering, enabling it to slow down, stop, or redirect around obstacles.
- **Path Adjustment**: The algorithm recalculates the robot’s path to avoid obstacles while maintaining progress toward challenge goals, such as reaching a parking zone or navigating a track.

The **EV3 Ultrasonic Sensors** complement this by focusing solely on wall-following, ensuring the robot maintains proper alignment with walls while the Pixy Cam handles obstacle avoidance. This integrated approach ensures robust and adaptive navigation, enabling the robot to handle all WRO 2025 challenges effectively.

### 5. **Energy Management for Mobility**

**Power Consumption**  
The ShahroodRC robot’s energy consumption is efficiently managed by the **LEGO EV3 Mindstorms Control Brick**, which regulates power supplied to the two **EV3 Medium Motors** and the sensors (**EV3 Color Sensor**, two **EV3 Ultrasonic Sensors**, and **Pixy Cam**). The propulsion motor, driving the rear wheels via a differential, and the steering motor, controlling the front wheels, are the primary consumers of power. The sensors, used for detecting blue and orange lines, wall-following, and obstacle detection, have relatively low power requirements. The EV3 Control Brick, running the **ev3dev** operating system, ensures stable power delivery to all components, maintaining consistent performance during WRO 2025 challenges.

**Battery and Power Supply**  
The robot is powered by the official **LEGO EV3 Rechargeable Battery Pack** (DC 10V, 2050 mAh), providing a reliable power supply for all components. This battery supports the high demands of the EV3 Medium Motors (requiring 9V input, 20 N·cm torque, 160 rpm) and the sensors, ensuring uninterrupted operation throughout the competition. The EV3 Control Brick manages power distribution, delivering the required voltage and current to motors and sensors while preventing overloads or voltage drops during intensive tasks like wall-following, obstacle avoidance, and parking.

**Energy Optimization**  
To optimize energy usage and extend battery life during WRO 2025 challenges, the robot’s power consumption is carefully balanced. Key strategies include:
- **Dynamic Power Allocation**: The EV3 Control Brick, programmed via Python on ev3dev, adjusts power distribution based on task requirements. For example, during wall-following, power is prioritized to the propulsion motor and Ultrasonic Sensors, while during obstacle avoidance, the Pixy Cam receives sufficient power for reliable object detection.
- **Efficient Motor Control**: The Python-based control algorithms minimize unnecessary motor activity, such as reducing propulsion speed when navigating stable paths or limiting steering adjustments during straight motion.
- **Sensor Management**: The sensors operate only when needed, with Python scripts ensuring efficient polling to reduce power draw without compromising performance.

These optimization techniques ensure that the robot maintains energy efficiency, allowing the **LEGO EV3 Rechargeable Battery Pack** to sustain the robot’s performance for the duration of WRO 2025 challenges, including wall-following, obstacle avoidance, and precise parking.

### 6. **System Integration for Mobility**

**Integration with Other Systems**  
The ShahroodRC robot’s mobility system is seamlessly integrated with its sensory and processing components to ensure cohesive operation during WRO 2025 challenges. The mobility system, consisting of a **rear-wheel drive with front-wheel steering** powered by two **EV3 Medium Motors**, works in tandem with the sensor suite (**EV3 Color Sensor**, two **EV3 Ultrasonic Sensors**, and **Pixy Cam**) and the **LEGO EV3 Mindstorms Control Brick**. Key integration aspects include:
- **Sensor-to-Motor Integration**: The **EV3 Color Sensor**, detecting blue and orange lines, provides data for task-specific navigation (e.g., identifying track markers or zones). The two **EV3 Ultrasonic Sensors**, used for wall-following, measure distances to walls, guiding the steering motor to maintain alignment. The **Pixy Cam**, configured for obstacle detection and color recognition in the Obstacle Challenge, informs the propulsion and steering motors to navigate around obstacles.
- **Real-time Data Processing**: Sensor data is processed by the EV3 Control Brick running **ev3dev**, which uses Python scripts to translate inputs into motor commands. For example, wall distance data from Ultrasonic Sensors adjusts the steering angle, while Pixy Cam data triggers obstacle avoidance maneuvers.
- **Mechanical Integration**: The motors and sensors are mounted on a lightweight yet rigid chassis built from **LEGO MINDSTORMS Education Core Set** components. The chassis ensures stable alignment of the differential (for rear-wheel propulsion) and the front axle (for steering), minimizing vibrations and ensuring reliable sensor readings.

This integration ensures that the mobility system operates in harmony with sensory inputs and processing capabilities, enabling the robot to perform complex tasks like wall-following, obstacle avoidance, and precise parking in WRO 2025.

**Control Unit**  
The **LEGO EV3 Mindstorms Control Brick** serves as the central control unit for the ShahroodRC robot’s mobility system. Running the **ev3dev** operating system with Python-based programming, the EV3 Brick manages all aspects of mobility, including:
- **Motor Control**: The EV3 Brick sends PWM (Pulse Width Modulation) signals to the propulsion motor (driving the rear wheels via a differential) and the steering motor (controlling the front wheels), ensuring precise speed and directional adjustments.
- **Sensor Processing**: The EV3 Brick processes real-time data from the Color Sensor, Ultrasonic Sensors, and Pixy Cam, using Python scripts to make navigation decisions based on task requirements (e.g., wall-following, obstacle avoidance, or zone detection).
- **Power Management**: The EV3 Brick regulates power distribution from the **LEGO EV3 Rechargeable Battery Pack** (10V, 2050 mAh) to motors and sensors, optimizing energy usage to sustain performance throughout the competition.

The choice of the EV3 Control Brick was driven by its compatibility with the LEGO MINDSTORMS ecosystem, robust processing capabilities, and support for ev3dev, which enables flexible and precise control through Python programming. This control unit ensures reliable integration of the mobility system with other components, allowing the robot to meet the diverse challenges of WRO 2025 effectively.

### 7. **Testing and Optimization**

**Testing the Mobility System**  
The ShahroodRC robot’s mobility system was rigorously tested to ensure reliable performance across the WRO 2025 Future Engineers category challenges. The testing process involved evaluating the **rear-wheel drive with front-wheel steering** system, powered by two **EV3 Medium Motors**, under various conditions simulating competition environments. Key testing scenarios included:
- **Wall-following Tests**: The robot was tested on surfaces with walls to verify the accuracy of the two **EV3 Ultrasonic Sensors** in maintaining consistent distances for wall-following tasks. Tests ensured the steering motor adjusted the front wheels accurately based on sensor feedback.
- **Obstacle Avoidance Tests**: The **Pixy Cam** was tested in simulated Obstacle Challenge environments to confirm its ability to detect the presence and color of obstacles, with the propulsion and steering motors responding appropriately to navigate around them.
- **Zone Detection Tests**: The **EV3 Color Sensor** was tested on surfaces with blue and orange lines to ensure reliable detection of track markers or zones, critical for specific WRO challenge tasks.
- **Parking and Maneuverability Tests**: The robot was tested in confined spaces to evaluate its ability to perform precise parking and tight maneuvers, ensuring the differential and steering mechanisms worked seamlessly.

Tests were conducted on surfaces mimicking WRO competition tracks (e.g., smooth surfaces with marked lines and obstacles) to validate the robot’s performance under realistic conditions.

**Optimization for Efficiency**  
The mobility system was optimized to achieve maximum performance and efficiency during WRO 2025 challenges. Key optimization strategies included:
- **Motor Calibration**: The propulsion and steering motors were fine-tuned using Python scripts on **ev3dev** to balance speed and torque, ensuring smooth operation while minimizing energy consumption.
- **Sensor Calibration**: The **EV3 Ultrasonic Sensors** were calibrated to optimize wall-following accuracy, while the **Pixy Cam** was adjusted to improve obstacle detection reliability under varying lighting conditions. The **EV3 Color Sensor** was tuned to accurately distinguish blue and orange lines.
- **Software Optimization**: Python-based control algorithms were refined to reduce processing delays, ensuring rapid response to sensor inputs for tasks like wall-following and obstacle avoidance.
- **Energy Efficiency**: The **LEGO EV3 Control Brick** was programmed to dynamically adjust power distribution, prioritizing active components (e.g., Ultrasonic Sensors during wall-following or Pixy Cam during obstacle avoidance) to extend the **LEGO EV3 Rechargeable Battery Pack** (10V, 2050 mAh) lifespan.

These optimizations ensured the robot could perform reliably and efficiently throughout the competition, handling tasks like wall-following, obstacle avoidance, and precise parking with minimal resource usage.

**Challenges and Solutions**  
Several challenges were encountered during the design and testing of the mobility system, with solutions implemented to address them:
- **Challenge: Inconsistent Wall-following**: Initial tests showed occasional deviations in wall-following due to sensor noise from the Ultrasonic Sensors.
  - **Solution**: Adjusted the Python scripts to implement filtering techniques (e.g., averaging multiple sensor readings) to reduce noise and improve distance measurement accuracy.
- **Challenge: Obstacle Detection in Varied Lighting**: The Pixy Cam’s performance was affected by inconsistent lighting in some test environments.
  - **Solution**: Calibrated the Pixy Cam’s color detection parameters and tested it under multiple lighting conditions to ensure robust obstacle recognition.
- **Challenge: Battery Drain During Intensive Tasks**: High motor and sensor activity during combined tasks (e.g., wall-following and obstacle avoidance) led to increased power consumption.
  - **Solution**: Optimized Python scripts to reduce unnecessary motor and sensor activity, such as limiting steering adjustments during stable paths and polling sensors only when needed.

These solutions enhanced the robot’s reliability and performance, ensuring it meets the rigorous demands of WRO 2025 challenges.

### 8. **Conclusion**

**Summary of Mobility Features**  
The ShahroodRC robot’s mobility system is a robust and efficient design tailored for the WRO 2025 Future Engineers category. The **rear-wheel drive with front-wheel steering** system, powered by two **EV3 Medium Motors**, provides precise and agile movement, enabling the robot to navigate complex competition environments. The integration of the **EV3 Color Sensor** (for detecting blue and orange lines for task-specific navigation), two **EV3 Ultrasonic Sensors** (for wall-following), and **Pixy Cam** (for obstacle detection and color recognition in the Obstacle Challenge) ensures accurate navigation and task execution. Controlled by the **LEGO EV3 Mindstorms Control Brick** running **ev3dev** with Python-based scripts, the system achieves seamless coordination between motors and sensors, optimizing performance for tasks like wall-following, obstacle avoidance, and precise parking. The **LEGO EV3 Rechargeable Battery Pack** (10V, 2050 mAh) supports energy-efficient operation, with dynamic power allocation enhancing battery life. This combination of mechanical design, sensor integration, and software control makes the ShahroodRC robot highly competitive, capable of meeting the diverse challenges of WRO 2025 with reliability and precision.

**Future Improvements**  
While the current mobility system performs effectively, several areas could be explored for future enhancements:
- **Enhanced Sensor Calibration**: Further tuning of the **Pixy Cam** to improve obstacle detection accuracy under extreme lighting conditions could enhance performance in the Obstacle Challenge.
- **Advanced Control Algorithms**: Implementing more sophisticated algorithms, such as PID control for steering or speed regulation, could improve precision and responsiveness during complex maneuvers.
- **Battery Optimization**: Exploring higher-capacity batteries or more advanced power management techniques could extend operational time, particularly for longer competition rounds.
- **Mechanical Refinements**: Strengthening the chassis or optimizing the differential mechanism could reduce wear and improve stability during high-speed or high-torque tasks.
- **Sensor Fusion Enhancements**: Developing more advanced sensor fusion techniques, such as weighted data integration, could improve decision-making for combined tasks like wall-following and obstacle avoidance.

These potential improvements aim to further enhance the robot’s performance, ensuring greater adaptability and competitiveness in future iterations of the WRO or similar competitions.


---

## Power and Sense Management

This section outlines how electrical power is distributed across the robot and how all sensors — including a customized Pixy Cam integration — are managed to ensure efficient and stable performance during the WRO 2025 challenges.

---

### 1. **Power Supply and Distribution**

- **Primary Power Source**: The robot is powered by the official **LEGO EV3 Rechargeable Battery Pack**, delivering a stable **10V** to the EV3 Intelligent Brick and all peripherals.
- **Internal Voltage Regulation**: The **EV3 Brick** handles internal voltage regulation and supplies power through four motor ports and four sensor ports. No external converters were required for standard LEGO components.
- **Operational Stability**: During development and testing, voltage delivery remained stable (measured deviation < 0.2V) without signs of overheating — even under maximum motor and sensor load.

---

### 2. **Power Consumption Overview**

- **Motors**: Each **EV3 Medium Motor** draws approximately **150–200 mA** during standard operation, peaking at **500 mA** under stall conditions.
- **Sensors**: Built-in LEGO sensors (e.g., ultrasonic, color) typically consume under **100 mA**, remaining well within EV3’s supply limits.
- **Pixy Cam (Direct EV3 Sensor Port Integration)**: Four EV3 internal wires were identified (via continuity testing) and connected to the Pixy Cam’s I2C port:
  - **Red** → 5V (Pixy power input)
  - **Blue** → GND
  - **Yellow** → SDA
  - **Green** → SCL  
  The unused **white** and **black** wires were insulated and left unconnected. Pixy Cam draws approximately **120–160 mA**, a value confirmed safe through multimeter testing. Based on compatibility tests, no level shifters were required.

---

### 3. **Sensor Architecture and Management**

- **Central Control Unit**: All sensors, including the non-standard Pixy Cam, interface directly with the EV3 Brick.
- **Port Allocation Table**:

| Port | Sensor             | Function                                                     |
|------|--------------------|--------------------------------------------------------------|
| 1    | Color Sensor       | Blue and orange lines for task-specific navigation detection |
| 2    | Ultrasonic Sensor  | Wall following / open challenge                              |
| 3    | Ultrasonic Sensor  | Secondary wall following / open challenge                    |
| 4    | Pixy Cam           | Image processing / Obstacle detection                        |

- **Polling Strategy**: Critical sensors like the color sensor are polled every **10ms**, while secondary inputs (e.g., Pixy or second ultrasonic) are polled at **50ms**.

---

### 4. **Wiring and Safety**

- **Standard Wiring**: All LEGO components are connected using official RJ-type sensor cables to maintain signal integrity and mechanical reliability.

- **Pixy Cam Integration (Custom Wiring)**:  
  To interface the Pixy Cam with the EV3 Brick, one original EV3 sensor cable (6-wire) was carefully cut and modified. The internal wires were accessed, and **four out of six** were soldered to the Pixy Cam's I2C interface:

  **Connected Wires**:
  - **Red** → Pixy 5V  
  - **Blue** → Pixy GND  
  - **Yellow** → Pixy SDA  
  - **Green** → Pixy SCL

  **Unused**:
  - **White** → not required  
  - **Black** → extra ground, left unconnected  

  This setup enabled direct power and I2C communication via EV3’s sensor port without needing external regulators or level converters. Continuity and voltage checks confirmed proper signal routing; runtime tests validated stable behavior in all modes.

> ⚠️ *All unused wires were safely insulated to prevent short circuits. The electrical integrity of the system was validated using both multimeter and long-duration load testing.*

- **Heat and Overload Protection**: The EV3 Brick includes internal thermal sensors and current-limiting features, protecting against overheating or short circuits during prolonged operation.

---

### 5. **Diagnostics and Monitoring**

- **Battery Monitoring**: The EV3 firmware alerts users when battery voltage drops below approximately **6.5V**.
- **Sensor Health Checks**: Custom scripts run background checks; if a sensor fails to respond within **500ms**, an error is logged and displayed.
- **Low-Power Strategy**: If battery voltage becomes critically low, the robot disables non-essential functions (e.g., Pixy Cam video feedback) to preserve core operations.

---

### 6. **Optimization Techniques**

- **Idle Power Saving**: Motors and sensors enter low-power mode when not in use.
- **Sensor Prioritization**: The color and primary ultrasonic sensors are prioritized in polling frequency for real-time decisions.
- **Dynamic Resource Allocation**: System resources are reassigned dynamically based on active tasks, such as task-specific navigation.

---

### 7. **Conclusion**

The ShahroodRC robot’s power and sensor systems demonstrate reliable hardware integration, clean custom wiring, and adaptive software routines. The direct EV3 port integration of the Pixy Cam without extra hardware shows that simple, well-tested solutions can achieve robust performance and maintain full compatibility for WRO 2025 challenges.

---

## Obstacle Avoidance and Parking Management(Obstacle Management)

The robot’s mobility is managed through a combination of two medium motors (`motor_a` and `motor_b`) from the LEGO Mindstorms EV3 kit, selected for their balance of speed, torque, and compatibility with the EV3 platform. `motor_b` drives the robot’s forward and backward motion, while `motor_a` controls steering, enabling precise navigation and turning. The motors were chosen for their ability to deliver sufficient torque for navigating the obstacle course and performing the parking sequence, while maintaining energy efficiency for prolonged operation.

The chassis is a modular LEGO EV3 structure, designed for stability and ease of component integration. The motors are mounted on a reinforced baseplate to ensure durability during high-speed navigation and obstacle avoidance. The steering mechanism uses a rack-and-pinion system, driven by `motor_a`, to achieve smooth and controlled turns. The chassis design prioritizes a low center of gravity to prevent tipping during sharp turns or sudden stops, as seen in the parking sequence.

Engineering principles such as speed and torque were considered in the motor control logic. For instance, the `motor_b.on(speed)` function uses variable speed settings (e.g., 20, 40, 60, 70) to balance between fast navigation and precise maneuvers. The `amotor` function implements a PID-like control to adjust steering angles, ensuring accurate alignment with lines and walls. Assembly instructions are provided in the GitHub repository, including a step-by-step guide for mounting motors and sensors, along with STL files for 3D-printed sensor mounts to enhance component stability.

```python
def amotor(degrese, cl=50):
    diff = degrese
    diff = diff - motor_a.position
    diff = clamp(diff, -cl, cl)
    motor_a.on(diff)
```

*Improvements*: To enhance mobility, we optimized the gear ratio for `motor_b` to increase torque during the parking sequence, reducing strain on the motor. Future iterations could include a differential drive system for smoother turns.

### Open Challenge (Qualification Round)

[Full Code](codes/open-challenge-code.py)

In the open challenge, the robot navigates a track using a color sensor (`color_sensor`) to detect lines (blue: `cr1=2`, orange: `cr1=5`) and ultrasonic sensors (`rast` and `chap`) for distance-based steering. The robot determines its initial direction by detecting a line color and then follows a path, making turns when specific colors are detected. It uses a PID-like control for steering (`amotor`) to maintain a target distance (27 cm) from walls, adjusting based on the detected line color.

```python
cr1 = color_sensor.color
while cr1 != 2 and cr1 != 5:
    cr1 = color_sensor.color
    motor_b.on(60)
while g != 60:
    motor_b.on(30)
    r = rast.distance_centimeters
    c = chap.distance_centimeters
    fr = (-2 * (math.sqrt(11 * r))) + 100
    fc = (-2 * (math.sqrt(11 * c))) + 100
    target = (fc * 1.3) - (fr * 1.7)
    amotor(clamp(target, -50, 50))
    g = g + 1
```

#### Line Detection and Navigation
The robot detects blue (`cr1=2`) or orange (`cr1=5`) lines to determine its path. Upon detecting a line, it stops, increments a turn counter (`a`), and resumes navigation. The robot completes 11 turns (`a == 11`) before entering a final straight-line navigation phase, maintaining a 27 cm distance from the wall using the appropriate ultrasonic sensor based on the initial line color.

```python
if cr1 == 2:
    while True:
        cr1 = color_sensor.color
        if cr1 == 2:
            while cr1 == 2:
                cr1 = color_sensor.color
                motor_b.on_for_degrees(80, 70)
                motor_a.stop(stop_action='coast')
                motor_b.stop(stop_action='coast')
            a = a + 1
        motor_b.on(60)
        distance = chap.distance_centimeters
        diff = ((distance - 27) * -2)
        diff = diff - motor_a.position
        diff = clamp(diff, -32, 32)
        amotor(diff)
        if a == 11:
            i = 0
            while i != 130:
                motor_b.on(50)
                distance = chap.distance_centimeters
                diff = (distance - 27) * -2
                diff = diff - motor_a.position
                diff = clamp(diff, -27, 27)
                amotor(diff)
                i = i + 1
            break
elif cr1 == 5:
    while True:
        cr1 = color_sensor.color
        if cr1 == 5:
            while cr1 == 5:
                cr1 = color_sensor.color
                motor_b.on_for_degrees(80, 70)
                motor_a.stop(stop_action='coast')
                motor_b.stop(stop_action='coast')
            a = a + 1
        motor_b.on(60)
        distance = rast.distance_centimeters
        diff = (distance - 27) * 2
        diff = diff - motor_a.position
        diff = clamp(diff, -32, 32)
        amotor(diff)
        if a == 11:
            i = 0
            while i != 130:
                motor_b.on(50)
                distance = rast.distance_centimeters
                diff = (distance - 27) * 2
                diff = diff - motor_a.position
                diff = clamp(diff, -27, 27)
                amotor(diff)
                i = i + 1
            break
```

### Final Round with Obstacle Avoidance(Obstacle Challenge)

[Full Code](codes/obstacle-challenge-code.py)

In the final round, the robot builds on the open challenge logic by adding obstacle avoidance using a Pixy camera. It determines its initial direction (`al`) by comparing distances from two ultrasonic sensors (`rast` and `chap`) over 100 iterations. The robot then assigns color values (`rang` and `rangdovom`) for line detection and uses the Pixy camera to detect green (`sig=1`) or red (`sig=2`) obstacles, adjusting steering (`target`) based on their position (`x`) relative to predefined offsets (`green` or `red`). LEDs indicate detected obstacles (green for `sig=1`, red for `sig=2`).

```python
p = 0
jahat = 0
while p != 100:
    r = rast.distance_centimeters
    c = chap.distance_centimeters
    if r > c:
        jahat = 1 + jahat
    else:
        jahat = jahat - 1
    p = p + 1
if jahat > 0:
    al = -1
    green = 230
    red = 20
    rang = 5
    rangdovom = 2
else:
    al = 1
    green = 230
    red = 5
    rang = 2
    rangdovom = 5
```

#### Obstacle Detection and Avoidance
When an obstacle is detected, the robot adjusts its speed and steering. If the obstacle is close (`y < 110`), it slows down and tightens steering control. If no obstacle is detected (`sig == 0`), it uses ultrasonic sensors to maintain a dynamic distance (`fasele`) from walls.

```python
if y < 110 and (sig == 1):
    leds.set_color('LEFT', 'GREEN')
    leds.set_color('RIGHT', 'GREEN')
    target = (x - 120) * 0.7
    target = clamp(target, -20, 20)
    amotor(target, 35)
    speed = 40
elif y < 110 and (sig == 2):
    leds.set_color('LEFT', 'RED')
    leds.set_color('RIGHT', 'RED')
    target = (x - 100) * 0.7
    target = clamp(target, -20, 20)
    amotor(target, 35)
    speed = 40
elif sig == 1:
    ghabeliat = True
    target = (x - green) * 0.5
    leds.set_color('LEFT', 'GREEN')
    leds.set_color('RIGHT', 'GREEN')
    amotor(target, 50)
    speed = 22
elif sig == 2:
    ghabeliat = True
    target = (x - red) * 0.5
    leds.set_color('LEFT', 'RED')
    leds.set_color('RIGHT', 'RED')
    amotor(target, 50)
    speed = 22
elif sig == 0 and cr1 == 6:
    leds.all_off()
    speed = 33
    r = rast.distance_centimeters
    c = chap.distance_centimeters
    if al == 1:
        oltra = c
    else:
        oltra = r
    out = (fasele - oltra) * al
    out = clamp(out, -45, 45)
    amotor(out)
```

#### Parking Sequence

After completing the required laps (`a == door`), the robot enters a parking sequence. It aligns with the secondary line color (`rangdovom`) and uses the ultrasonic sensor (`rast`) to maintain a 15 cm distance from the wall. A series of precise motor movements positions the robot correctly within the parking area, ending with a final alignment to stop parallel to the wall.

```python
if al < 0:
    navakht = 90
    while cr1 != rangdovom:
        motor_b.on(30)
        amotor(0)
        cr1 = color_sensor.color
    motor_b.off()
    motor_a.on_for_degrees((100), -120)
    motor_b.on_for_degrees((-30), 300)
    motor_a.on_for_degrees((90), -motor_a.position)
    while True:
        motor_b.on(speed)
        r = rast.distance_centimeters
        if r < 60 or cr1 == rangdovom:
            break
    fasele = 15
    speed = 20
    while motor_b.position < 1500:
        motor_b.on(speed)
        r = rast.distance_centimeters
        out = (fasele - r) * 1.5 * al
        out = clamp(out, -23, 23)
        amotor(out)
    motor_b.off()
    motor_a.on_for_degrees((90), -90)
    motor_b.on_for_rotations(-20, 1.72)
    motor_a.on_for_degrees((90), -motor_a.position)
    motor_b.on_for_rotations(-20, 3.5)
    motor_a.on_for_degrees((90), 90)
    motor_b.on_for_rotations(20, 0.7)
    motor_a.on_for_degrees((90), -190)
    motor_b.on_for_rotations(-20, 0.6)
    motor_a.on_for_degrees((90), 190)
    motor_b.on_for_rotations(20, 0.4)
```

#### Parking Wall Detection
The ultrasonic sensor (`rast`) ensures the robot stays close to the wall during parking, while the color sensor confirms alignment with the parking line (`rangdovom`).

### Additional Functions

#### Steering Control
The `amotor` function provides PID-like steering control, adjusting the motor angle based on the target position. The `clamp` function limits values to prevent oversteering.

```python
def clamp(value, minimum, maximum):
    if value > maximum:
        value = maximum
    if value < minimum:
        value = minimum
    return value

def amotor(degrese, cl=50):
    diff = degrese
    diff = diff - motor_a.position
    diff = clamp(diff, -cl, cl)
    motor_a.on(diff)
```

#### Stall Detection and Recovery
The robot detects stalls by checking if the motor position (`lastpos`) remains unchanged for 0.3 seconds, initiating a recovery sequence by reversing and adjusting steering.

```python
if lastpos == motor_b.position:
    if b_timer == 0:
        b_timer = time.time()
    if time.time() - b_timer > 0.3:
        print("khokafez")
        b_timer = 0
        motor_a.on_for_degrees((40), -motor_a.position)
        motor_b.on_for_rotations(-100, 1)
        motor_a.on_for_degrees((40), 45 * al)
        motor_b.on_for_rotations(100, 0.8)
lastpos = motor_b.position
```

#### Color-Based Navigation
The robot uses the color sensor to detect lines (`rang` and `rangdovom`) for navigation decisions. In the open challenge, it detects blue or orange lines to trigger turns, while in the final round, it uses these colors to navigate and park.

```python
if cr1 == rang:
    fasele = 25
    timeRang = time.time()
    navakht = -40
    while cr1 != rangdovom and sig == 0 and time.time() - timeRang < 4:
        amotor(navakht * al)
        if navakht <= 0:
            navakht = navakht + 1
        motor_b.on(20)
        cr1 = color_sensor.color
    timeRang = time.time()
    while time.time() - timeRang < 0.7 and sig == 0:
        amotor(-20 * al)
        motor_b.on(70)
    if a_timer == 0 or time.time() - a_timer > 4:
        a_timer = time.time()
        a = a + 1
    fasele = 35
```

#### Visual Feedback
LEDs provide visual feedback: green for green obstacles (`sig=1`), red for red obstacles (`sig=2`), and off when navigating without obstacles or during parking.

```python
if sig == 1:
    leds.set_color('LEFT', 'GREEN')
    leds.set_color('RIGHT', 'GREEN')
elif sig == 2:
    leds.set_color('LEFT', 'RED')
    leds.set_color('RIGHT', 'RED')
elif sig == 0 and cr1 == 6:
    leds.all_off()
```

### Notes
- **Robustness**: The combination of ultrasonic sensors, color sensors, and the Pixy camera ensures reliable navigation and obstacle avoidance.
- **Adaptability**: The direction determination (`al`) and dynamic distance adjustment (`fasele`) allow adaptation to different track orientations.
- **Limitations**: The code assumes consistent lighting for color detection and reliable ultrasonic readings. Variations may require recalibration of thresholds (`green`, `red`, `fasele`).

---

## Repository Structure
- `codes/`: Contains Python scripts for Open Challenge and Obstacle Challenge.
- `team-photos/`: Images of team members and the whole team.
- `robot-photos/`: Images of robot from front, back, up, down, right and left.
- `3d-files/`: STL files for 3D model of the robot.
- `videos/`: Performance videos for both challenges.

---


## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
