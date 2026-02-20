from machine import I2C, Pin
import time

# Note: Ensure you have the mpu6050 library uploaded to your board
try:
    from mpu6050 import MPU6050
except ImportError:
    print("Error: mpu6050 library not found. Please upload mpu6050.py to your device.")

# --- Configuration ---
I2C_ID = 0
SDA_PIN = 8
SCL_PIN = 9
FREQ = 400000
SAMPLE_RATE = 0.1 # Seconds

# Initialize I2C and Sensor
i2c = I2C(I2C_ID, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=FREQ)

def setup_sensor():
    try:
        devices = i2c.scan()
        if not devices:
            raise Exception("No I2C devices found! Check your wiring.")
        
        mpu = MPU6050(i2c)
        print(f"MPU-6050 initialized successfully at pins {SDA_PIN}, {SCL_PIN}")
        return mpu
    except Exception as e:
        print(f"Initialization Failed: {e}")
        return None

sensor = setup_sensor()

if sensor:
    print("Starting Stream... Press Ctrl+C to stop.")
    time.sleep(1) # Brief pause to let the user read the setup status

    try:
        while True:
            data = sensor.get_values()
            
            # Use ANSI escape code \033[H to move cursor to top-left 
            # and \033[J to clear screen for a "Dashboard" look
            print("\033[H\033[J") 
            print("=== MPU-6050 Real-Time Data ===")
            print(f" {'Category':<12} | {'X':>8} | {'Y':>8} | {'Z':>8}")
            print("-" * 45)
            
            # Formatted Accelerometer Data
            print(f" {'Accel (Raw)':<12} | {data['AcX']:>8} | {data['AcY']:>8} | {data['AcZ']:>8}")
            
            # Formatted Gyroscope Data
            print(f" {'Gyro (Raw)':<12} | {data['GyX']:>8} | {data['GyY']:>8} | {data['GyZ']:>8}")
            
            print("-" * 45)
            print(f" Sample Rate: {1/SAMPLE_RATE} Hz")
            
            time.sleep(SAMPLE_RATE)

    except KeyboardInterrupt:
        print("\nStream stopped by user.")
    except Exception as e:
        print(f"\nRuntime Error: {e}")