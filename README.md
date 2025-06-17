# ShahroodRC

This repository provides a detailed overview of the ShahroodRC team's robot developed for the 2025 World Robot Olympiad in the Future Engineers category. The robot was conceptualized, designed, and built by a dedicated team of three students.

---

## Table of Contents

- [The Team](#the-team)
- [Our Path](#our-path)
- [Robot Components Overview](#robot-components-overview)
- [Mobility Management](#mobility-management)
- [Power and Sense Management](#power-and-sense-management)
- [Obstacle Management](#obstacle-management)
- [Robot Pictures](#robot-pictures)
- [License](#license)

---


## The Team

We are the ShahroodRC team, a group of students passionate about robotics, electronics, and programming, working toward the WRO 2025 competition in the Future Engineers category.

### Team Members:

- 👨‍💼 **Sepehr Yavarzadeh**: Project Manager and Software Engineer. At 16 years old, this is his third year participating in the WRO competition.  
- 🧑‍💻 **Amirparsa Saemi**: Lead Developer and Algorithm Designer. A 19-year-old computer science student with prior WRO experience.  
- 👩‍🔧 **Nikan Bashiri**: Mechanical and Electronics Specialist. He is 17 years old and in his fourth year participating in WRO.

### Coach:

- **Mr. Sadeghi**: The team’s 23-year-old coach with a B.Sc. in Computer Engineering. He is a certified Advanced LEGO Robotics Coach in Iran and supports both strategic and technical development for the team.

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
- **Use**: Used for object tracking and navigation
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


## Mobility Management

Our robot is built using LEGO components, primarily the **LEGO MINDSTORMS Education Core Set (Serial number 45544)**, along with additional **LEGO EV3 sets** and **wheels from the LEGO SPIKE Prime set** (Serial numbers 45678-1 and 45680-1). This setup ensures robust performance and maneuverability.

The robot’s dimensions are **19.5 cm (length)**, **13.5 cm (width)**, and **27 cm (height)**, optimized to fit within the competition's parking area. For mobility, we use a **differential drive system** powered by two motors at the rear axle, providing stable movement and steering control.

The robot's **mobility system** integrates the **powertrain**, **steering mechanism**, and **chassis**, working together to ensure smooth and efficient movement during the competition.


### 1. **Introduction to Mobility System**

   - **Overview of the mobility system**: This section explains the type of movement the robot performs, such as wheel-based movement, omnidirectional, or other mechanisms, and the reasoning behind choosing this system.
   - **Types of Movement**: Discusses how the robot moves (e.g., using four wheels, 360-degree rotation, independent control of each wheel, etc.).
   - **Design Choices**: Explains the design choices made for the mobility system, such as the number of wheels, their placement, and how they are connected to the motors.

---

### 2. **Motors and Actuators**

   - **Motor Types Used**: 
     - Discusses the types of motors used in the robot (DC, Servo, Stepper) and why these motors were chosen for the mobility system.
     - **Specifications**: Lists the specifications for each motor (e.g., speed, torque, voltage, etc.).
   - **Motor Control Mechanism**: Describes the method used to control the movement of the motors (e.g., motor controllers, specific algorithms for adjusting speed and precision).
   - **Motor Integration**: Explains how the motors are connected to other parts of the robot (e.g., wheels, arms, etc.).

---

### 3. **Sensor Integration for Mobility**

   - **Sensors for Navigation and Obstacle Avoidance**: Discusses the sensors used for detecting obstacles and aiding navigation (e.g., **Ultrasonic Sensors**, **IR sensors**, **LIDAR**, **Pixy Cam**, etc.).
   - **Real-time Feedback**: Describes how the robot processes the data received from sensors to adjust its movement in real-time.
   - **Sensor Fusion**: If multiple sensors are used, explains how the data from these sensors is combined to improve accuracy and performance.

---

### 4. **Mobility Control Algorithms**

   - **Control Algorithms**: Describes the algorithms used for controlling the robot’s mobility (e.g., **PID control**, **SLAM** for navigation, or other algorithms for controlling speed and direction).
   - **Navigation Techniques**: Explains the navigation techniques employed by the robot (e.g., **Dead Reckoning**, **Line-following**, etc.).
   - **Obstacle Avoidance**: Explains the algorithms used to avoid obstacles during movement (e.g., algorithms for obstacle avoidance and collision detection).

---

### 5. **Energy Management for Mobility**

- **Power Consumption**: The energy consumption for mobility is efficiently managed by the **LEGO EV3 Control Brick**, which regulates the power supplied to both the motors and sensors. The motors, which drive the robot's movement, and the sensors, which assist in navigation and obstacle detection, are powered directly through the EV3 system.

- **Battery and Power Supply**: The robot is powered by the official **LEGO EV3 Rechargeable Battery Pack**. This battery provides a stable power supply for all components, ensuring reliable operation throughout the competition. The EV3 system manages power distribution and ensures the motors and sensors receive the required voltage.

- **Energy Optimization**: To optimize energy usage and extend battery life during the competition, the robot’s power consumption is carefully balanced between motor usage and sensor operation. The **LEGO EV3 Control Brick** dynamically adjusts power distribution based on the robot’s activity, ensuring that energy is utilized efficiently and that the battery lasts for the duration of the event.

---

### 6. **System Integration for Mobility**

   - **Integration with Other Systems**: Explains how the mobility system integrates with other systems in the robot (e.g., sensors, processors, etc.).
   - **Control Unit**: Describes the control unit used for managing the mobility system (e.g., **LEGO EV3 Mindstorms Brick**, **Raspberry Pi**, **Arduino**, **ESP32**, etc.).

---

### 7. **Testing and Optimization**

   - **Testing the Mobility System**: Describes how the mobility system was tested under different conditions and simulated environments.
   - **Optimization for Efficiency**: Discusses how the mobility system was optimized for best performance in competitions.
   - **Challenges and Solutions**: Outlines any challenges faced during the design and testing phase, along with solutions implemented to overcome them.

---

### 8. **Conclusion**

   - **Summary of Mobility Features**: A summary of the key features of the mobility system and how they contribute to the robot's overall performance in competitions.
   - **Future Improvements**: Suggestions for future improvements in the mobility system, if needed.


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

| Port | Sensor             | Function                                  |
|------|--------------------|-------------------------------------------|
| 1    | Color Sensor       | Ground line detection                     |
| 2    | Ultrasonic Sensor  | Wall following / open challenge           |
| 3    | Ultrasonic Sensor  | Secondary wall following / open challenge |
| 4    | Pixy Cam           | Image processing / Obstacle detection     |

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
- **Dynamic Resource Allocation**: System resources are reassigned dynamically based on active tasks, such as switching between line-following and docking behaviors.

---

### 7. **Conclusion**

The ShahroodRC robot’s power and sensor systems demonstrate reliable hardware integration, clean custom wiring, and adaptive software routines. The direct EV3 port integration of the Pixy Cam without extra hardware shows that simple, well-tested solutions can achieve robust performance and maintain full compatibility for WRO 2025 challenges.


---

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
