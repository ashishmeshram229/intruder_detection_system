import random

def detect_motion():
    # Simulate motion detection (10% chance of intrusion)
    return "Intruder" if random.random() < 0.1 else "Safe"