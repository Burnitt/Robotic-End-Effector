# Robotic End Effector System

A 3D-printed robotic end effector designed and programmed as part of 
a team project to automate warehouse order packaging. The system 
integrates a Python-based ordering pipeline with a physical gripper 
mechanism driven by a servo motor and operated via a Q-arm robot 
controlled by a Raspberry Pi 4.

**Timeline:** October – December 2025  
**Platform:** Python | Raspberry Pi 4 | Q-arm | CAD (PrusaSlicer)  
**Type:** Team project — personal contributions listed below

---

## Problem Statement

Global warehouses process thousands of packages daily and require 
systems that can package and organize items without manual labor, 
reducing operational costs and workplace injuries.

---

## System Overview

The team coded 7 functions covering the full ordering pipeline:
account creation, order retrieval, order verification, purchase 
history storage, receipt generation, item indication, and physical 
packing via the Q-arm.

The end effector was designed to attach to the Q-arm's servo motor 
and physically pick up items of varying shapes and sizes, dropping 
them into designated parcel locations based on scanner input.

---

## My Contributions

**Software**
- `sign_up()` — secure user authentication function using hashed 
  passwords (bcrypt) and unique UserID generation to manage warehouse 
  ordering data
- `pack_products()` — core packing function with helper functions 
  (`witchhat`, `bowl`) that take scanner input and direct the Q-arm 
  to pick up and deliver the correct items

**Hardware & CAD**
- Designed the main gear, sized to match the torque output of the 
  servo motor and supply it to the end effector
- Created the full assembly exploded view drawing, documenting part 
  positions, quantities, and part numbers
- Contributed to code integration and the testing plan

---

## Hardware

- Raspberry Pi 4
- Q-arm robot
- Servo motor
- 3D-printed end effector (PLA, PrusaSlicer)
- Main gear + sliding arm gripper mechanism

**Parts list:** End Effector Platform, Main Gear, Arms (×2), 
Sliders (×2), 92000A126 Passivated 18-8 SS Pan Head Screws (×4)

---

## CAD

![End effector physical model](https://github.com/user-attachments/assets/9bcbebda-e940-4277-97c5-a0c61a1e9c19)
![Main gear drawing](https://github.com/user-attachments/assets/4d70d485-f4b5-4c60-a6ab-be5ea6e78073)
![Assembly exploded view](https://github.com/user-attachments/assets/76511377-a703-48fd-b4f2-13b9e447628a)

> Demo video available on my [portfolio](https://bush-aurora-6f7.notion.site/Robotic-End-Effector-2da3afb3d1d581e6ac3df6b699bbd96e)

---

## Key Challenge

One week before the deadline, testing revealed the arm width was 
too wide, causing the effector to knock adjacent items during pickup. 
The team resolved this by shortening the arm width and increasing 
the length and depth of the arm tips to maintain contact with the 
target item without disturbing neighbors. Multiple reprints were 
required to land on the final geometry.

---

## Future Improvements

- Add precise Q-arm speed and direction control to compensate for 
  mechanical imperfections
- Reduce Q-arm travel by eliminating the home-position return after 
  each delivery cycle
- Implement a locking mechanism on the clamp — the servo motor 
  currently loses torque on contact, reducing grip force
- Widen item spacing in the platform design to reduce toppling 
  during packing
