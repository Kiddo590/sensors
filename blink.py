from machine import Pin
from utime import sleep

# --- Configuration ---
LED_PIN = "LED"  # Internal LED for Pico W; use a GPIO number (e.g., 15) for external LEDs
DELAY_SECONDS = 0.5  # Faster blink rate for better responsiveness
counter = 0

# Initialize the pin
led = Pin(LED_PIN, Pin.OUT)

print(f"Starting LED sequence on pin: {LED_PIN}")
print("Press Ctrl+C to stop the program.")

try:
    while True:
        led.toggle()
        
        # Simple status update every 10 toggles
        counter += 1
        if counter % 10 == 0:
            print(f"Still blinking... (Cycles: {counter})")
            
        sleep(DELAY_SECONDS)

except KeyboardInterrupt:
    # This block catches the manual stop (Ctrl+C)
    print("\nStopping loop...")

finally:
    # Cleanup: Ensure the LED is off before the script exits
    led.off()
    print("LED turned off. System safe. Finished.")