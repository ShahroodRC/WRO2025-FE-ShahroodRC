# ShahroodRC

This repository provides a detailed overview of the ShahroodRC team's robot developed for the 2025 World Robot Olympiad in the Future Engineers category. The robot was conceptualized, designed, and built by a dedicated team of three students.

---

## Table of Contents

- [The Team](#the-team)
- [Our Path](#our-path)
- [Robot Components Overview](#robot-components-overview)
- [Mobility Management](#mobility-management)
-	[Power and Sense Management](#power-and-sense-management)
- [Obstacle Management](#obstacle-management)
- [Robot Pictures](#robot-pictures)
- [License](#license)

---


## The Team

We are the ShahroodRC team, a group of students passionate about robotics, electronics, and programming, working toward the WRO 2025 competition in the Future Engineers category.

### Team Members:

- 👨‍💼 **Sepehr Yavarzadeh**: The team's programmer and manager. At 16 years old, this is his third year participating in the WRO competition.  
- 🧑‍💻 **Amirparsa Saemi**: Amirparsa is the team’s main programmer. A 19-year-old computer science student, he has previous experience competing in the WRO.  
- 👩‍🔧 **Nikan Bashiri**: Nikan is the group's mechanic and electronics expert. He is 17 years old and is in his fourth year participating in WRO.

### Coach:
- **Mr X**: Coach of the team.

> In this project, we aimed to combine creativity, teamwork, and technical knowledge to build an efficient robot for the challenges of WRO 2025.

---

## Our Path

### Robot Development Process Explanation

This project involves the design and construction of a robot for a competition, during which various stages were undertaken to select and implement the most suitable hardware and software. Initially, we used the Arduino Uno as the main platform, which had both advantages and drawbacks. We faced issues with camera quality and simultaneous control of sensors and motors, leading to the decision to explore other hardware options.

### Development Stages

- **Using Arduino Uno**:
    Initially, we chose the Arduino Uno for controlling the robot. Due to its simplicity in programming and extensive support for sensors and motors, it seemed like a suitable option.
    However, one of the primary issues with using the Arduino Uno was the poor quality of the cameras, which significantly impacted the robot's performance in the competition.

- **Switching to ESP32**:
    After encountering issues with the Arduino Uno, we decided to move to the ESP32. This board, with its more powerful processing capabilities and advanced features such as Wi-Fi and Bluetooth, seemed like a better fit.
    However, with the ESP32, a new issue arose: the inability to control sensors and motors simultaneously. This limitation made it impossible for the robot to operate effectively in real-time, negatively affecting the competition results.

- **Adopting Raspberry Pi Zero**:
    Ultimately, we opted for the Raspberry Pi Zero. This platform was chosen due to its higher processing power, better camera support, and the ability to handle more complex operations.
    The Raspberry Pi Zero allowed us to use sensors, motors, and cameras simultaneously while performing complex processing tasks in real-time. However, during the development process, we encountered a significant issue: we burned out two Raspberry Pi Zero boards. This mishap led us to reconsider our hardware platform.

- **Switching to LEGO EV3**:
    After burning out two Raspberry Pi Zero boards, we decided to switch to LEGO EV3 for our robot's control system. This decision was strongly influenced by the fact that all three team members had prior experience with the LEGO EV3 platform and had successfully participated in the WRO competition using it in the previous year. Our familiarity with EV3 allowed us to quickly progress and resolve issues that would have otherwise taken longer to address. Given the stability and ease of use of the EV3, we determined it was the most suitable platform for our robot in the 2025 competition.

### Challenges and Issues:
- In the early stages, the main issue with Arduino Uno was the poor quality of the cameras, which prevented accurate visual data processing.
- The ESP32 introduced a new challenge related to simultaneous control of sensors and motors, which hindered the robot's performance in more complex environments.
- The Raspberry Pi Zero was able to resolve these problems, but we encountered hardware failures when two Raspberry Pi Zero boards were damaged, forcing us to change direction.
- Ultimately, LEGO EV3 provided a stable and well-understood platform, allowing us to make rapid progress toward the competition.

### Conclusion:
In the end, by choosing the LEGO EV3 platform, we were able to significantly enhance the robot's performance. This decision allowed us to resolve earlier issues, streamline development, and capitalize on our team's existing experience with the platform. LEGO EV3 provided the right balance of stability, simplicity, and power for the challenges of the WRO 2025.

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
      <li>Power: 9V (battery pack)</li>
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


## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
