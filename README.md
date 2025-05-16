# Milk-Quality-Analysis

# Milk Quality Monitoring System using Raspberry Pi, pH & Temperature Sensors, and KMeans Clustering

## 📌 Overview

This project aims to assess milk quality by measuring **pH** and **temperature** using:

- **SEN0161 pH sensor**
- **DS18B20 Temperature Sensor**

These sensors are interfaced with a **Raspberry Pi**, and the collected data is calibrated and used to classify the milk's quality using a **KMeans clustering model**.

---

## 🧰 Hardware Requirements

- Raspberry Pi
- SEN0161 pH Sensor
- DS18B20 Temperature Sensor
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
