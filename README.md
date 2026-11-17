# Real-World Autonomous Indoor Delivery Robot with SLAM-Based Navigation

## Project Overview

This project focuses on developing a compact indoor delivery robot capable of transporting small items between designated locations.

The robot uses a Raspberry Pi 5 as its main controller, an RPLIDAR A1 for environmental scanning, optical wheel encoders for movement estimation, and a differential-drive chassis for locomotion.

The software is developed using Python without relying on ROS. A Flask-based web interface is also implemented for browser-based manual control.

## Current Development Status

| Subsystem | Current status |
|---|---|
| Robot chassis assembly | Completed |
| Raspberry Pi and L298N integration | Tested |
| DC motor directional control | Tested |
| Flask browser control interface | Implemented and tested |
| RPLIDAR A1 scan acquisition | Tested |
| BreezySLAM map generation | Initial implementation |
| Optical wheel encoder detection | Tested |
| Encoder distance estimation | Preliminary calibration |
| Adjustable motor speed | Pending |
| Encoder-based movement control | Pending |
| Reliable SLAM mapping | Pending improvement |
| Autonomous navigation | Pending |
| Delivery compartment mechanism | Under design |
| Live camera monitoring | Under consideration |

## Hardware Components

- Raspberry Pi 5 (8 GB)
- RPLIDAR A1 2D LiDAR
- L298N dual H-bridge motor driver
- Two DC motors and wheels
- Two optical wheel encoder modules
- Two-wheel chassis with caster wheel
- Rechargeable 3.7 V batteries
- Proposed FS90R servo motor for delivery compartment investigation
- Proposed Raspberry Pi-compatible camera

## Software and Libraries

- Python
- Flask
- lgpio
- RPLIDAR Python library
- BreezySLAM
- Raspberry Pi OS

## Main Python Files

| File | Description |
|---|---|
| `motor_testing.py` | DC motor directional control |
| `web_control_ui.py` | Flask-based browser control interface |
| `slam_mapping.py` | LiDAR scan processing and initial SLAM map generation |
| `encoder_test.py` | Optical encoder signal counting |
| `encoder_distance_test.py` | Preliminary wheel distance estimation |

## Demonstration Evidence

- **Motor and web interface demonstration:** [Insert video link]
- **LiDAR scanning and initial map generation:** [Insert video link]

Additional photographs, terminal outputs and test results are available in the `evidence/` directory.

## Current Limitations

- Initial SLAM map quality requires improvement.
- Encoder calibration is preliminary.
- Motor speed control requires further development.
- Encoder feedback has not yet been integrated with motor control.
- Autonomous navigation has not yet been implemented successfully.
- Delivery compartment actuation and camera integration remain under development.

## Future Development Roadmap

1. Implement adjustable motor speed using PWM.
2. Improve wheel encoder calibration and movement estimation.
3. Improve LiDAR scan quality and SLAM mapping.
4. Develop and test the delivery compartment mechanism.
5. Integrate mapping and movement estimation.
6. Implement and evaluate autonomous navigation.
7. Integrate optional live camera monitoring.
8. Conduct full-system testing and evaluation.

## Repository Structure

```text
IMP_Delivery/
│
├── README.md
│
├── codes/
│   ├── lidar_test.py
│   ├── motor_testing.py
│   ├── web_control_ui.py
│   ├── slam_mapping.py
│   ├── encoder_test.py
│   └── encoder_distance_test.py
│
├── documents/
│   ├── project_report.docx
│   ├── logbook and gantt chart links
│   ├── gantt_chart.png
│   └── system_design.png
│
└── media_evidences/
    ├── 1st_RobotSketch.jpeg
    ├── IMP_Zhi YI_Gathered Parts.jpg
    ├── RaspberryPiConnection_with_GithubSSH.txt
    ├── Caster Wheel to Chassis Attacher.stl
    ├── LiDAR Testing w RoboStudio.mp4
    ├── Video_Motor_TestingwRaspberryPi.md
    ├── LiDAR Testing Video.md
    ├── LiDAR_Map Generation.jpg
    ├── slam_map.pgm
    ├── slam_map.png
    ├── Motor Control Testing Videos.md
    ├── robot controller initial ui.png
    ├── Robot_Bottom View_Encoders.jpg
    ├── Robot_Breadboard.jpg
    ├── Robot_Encoders.jpg
    ├── Robot_MotorDriver.jpg
    ├── TopView_Robot.jpg
    └── encoders/
```
