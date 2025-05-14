import sys
sys.path.insert(0,'DFRobot_ADS1115/RaspberryPi/Python/')
sys.path.insert(0,'GreenPonik_PH_Python/src/')


from DFRobot_ADS1115 import ADS1115
from GreenPonik_PH import GreenPonik_PH

ADS1115_REG_CONFIG_PGA_6_144V = 0x00  # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V = 0x02  # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V = 0x04  # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V = 0x06  # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V = 0x08  # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V = 0x0A  # 0.256V range = Gain 16

ads1115 = ADS1115()
ph = GreenPonik_PH()
ph.begin()

def read_ph():
    global ads1115
    global ph
    # Set the IIC address
    ads1115.set_addr_ADS1115(0x48)
    # Sets the gain and input voltage range.
    ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
    # Get the Digital Value of Analog of selected channel
    adc1 = ads1115.read_voltage(0)
    print("voltage = ",adc1)
    # Convert voltage to pH
    PH = ph.readPH(adc1['r'])
    print("PH:%.2f " % (PH))
    return PH

'''
def read_ph():
    global ads1115
    global ph
    # Set the IIC address
    ads1115.set_addr_ADS1115(0x48)
    # Sets the gain and input voltage range.
    ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
    
    # Average 50 readings to filter noise
    readings = []
    for _ in range(50):
        adc1 = ads1115.read_voltage(1)
        readings.append(adc1['r'])
    
    # Calculate average voltage
    avg_voltage = sum(readings) / len(readings)
    
    print(f"Raw average voltage: {avg_voltage:.4f} V")  # Debugging line to check voltage

    # Check if voltage is within a reasonable range (0V to 2V)
    if avg_voltage < 0 or avg_voltage > 2:
        print("Warning: Voltage is out of expected range (0V to 2V). Check sensor.")
        return None
    
    # Convert voltage to pH (ensure the conversion formula is correct for your sensor)
    PH = ph.readPH(avg_voltage)
    print("PH:%.2f " % (PH))
    return PH'''




while True:
    read_ph()
