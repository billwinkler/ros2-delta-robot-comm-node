# ROS2 Delta Robot Communication Node

🚧 **Work in Progress** 🚧  

This repository contains a **ROS2 node** that provides an interface between **user space** and **kernel space** for controlling a **delta-arm robot**. The goal is to enable communication between ROS2 and a **kernel module** running on a **Raspberry Pi**, which generates precise pulse signals for stepper motors.

## Overview

- The ROS2 node operates via **publish/subscribe (pub/sub)** messaging.
- It **subscribes** to delta-arm movement commands, which are published by a separate ROS2 module.
- Commands are sent to the **kernel module**, which directly controls the stepper motors.
- The **kernel module** is implemented separately and can be found here:  
  👉 [raspi-stepper-module](https://github.com/billwinkler/raspi-stepper-module)

## How It Works

1. **ROS2 Command Subscription:**  
   - The ROS2 node listens for incoming **delta-arm movement commands**.  
   - Each delta-arm command is an **array of motor commands**.  
   
2. **Motor Command Structure:**  
   - Each **motor command** contains:
     - **Motor ID**  
     - **Number of pulses** (to control the movement distance)  
     - **Rotation direction**  

3. **Kernel Module Communication:**  
   - The ROS2 node **relays** motor commands to the **kernel module** running on the Raspberry Pi.  
   - The kernel module then **generates step pulses** to move the delta-arm's motors.  

## Status

✅ Initial setup completed.  
🚧 Work in progress on pub/sub integration with ROS2.  
🔧 Further development needed for synchronization and control logic.  

## Future Goals

- Implement **real-time feedback** from the kernel module.
- Optimize pulse generation for smoother motion.
- Expand ROS2 interfaces to support dynamic command adjustments.

---


