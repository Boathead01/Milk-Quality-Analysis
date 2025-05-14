# Milk-Quality-Analysis

# Milk Quality Monitoring System using Raspberry Pi, pH & Temperature Sensors, and KMeans Clustering

## 📌 Overview

This project aims to assess milk quality by measuring **pH** and **temperature** using:

- **SEN0161 pH sensor**
- **DFRobot Analog Temperature sensor**

These sensors are interfaced with a **Raspberry Pi**, and the collected data is calibrated and used to classify the milk's quality using a **KMeans clustering model**.

---

## 🧰 Hardware Requirements

- Raspberry Pi
- SEN0161 pH Sensor
- DFRobot Analog Temperature Sensor
- ADS 1115 ADC (to read analog values from the sensors)
- Jumper wires
- Breadboard
- Power supply

---

## 🧪 Software & Libraries

- Python 3
- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib` (for visualization)
- `spidev` (for SPI communication)
- `RPi.GPIO`

Install required libraries:

```bash
pip install numpy pandas scikit-learn matplotlib
