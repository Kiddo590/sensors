from machine import I2C, Pin
from mpu6050 import MPU6050
import time

# S3 Default I2C Pins: SDA=8, SCL=9
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

# Initialize sensor
sensor = MPU6050(i2c)

print("Starting MPU-6050 Stream...")

while True:
    data = sensor.get_values()
    # Scannable formatted string
    print(f"Accel: {data['AcX']:>6} | Gyro: {data['GyX']:>6}")
    time.sleep(0.1)