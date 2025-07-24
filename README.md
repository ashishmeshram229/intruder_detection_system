# Centralized Intruder Detection System

A simulated smart intruder detection system using Flask and Python. This version mimics sensor behavior and shows real-time alerts on a web UI, and sends email notifications on intrusion detection.

## Setup Instructions

### 1. Clone or unzip the project:
```bash
unzip intruder_detection_system_with_email.zip
cd intruder_detection_system
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure Email Settings:
Open `app.py` and replace the following variables with your actual email credentials:
```python
EMAIL_ADDRESS = 'youremail@example.com'     # Your email
EMAIL_PASSWORD = 'yourpassword'             # Your email password or app password
RECIPIENT_EMAIL = 'recipient@example.com'   # Recipient's email
```

For Gmail:
- If you have 2FA enabled, create an App Password at https://myaccount.google.com/apppasswords
- Or enable "Less secure apps" (not recommended for production)

### 4. Run the server:
```bash
python app.py
```

### 5. Open in browser:
```
http://127.0.0.1:5000/
```

## Features

- Simulated intrusion detection using random logic
- Real-time UI status updates every 3 seconds
- Logs all intrusion attempts to `alerts/alert_log.txt`
- Sends email alerts to a configured recipient when an intruder is detected

## Folder Structure

```
intruder_detection_system/
├── app.py
├── utils/
│   └── detector.py
├── templates/
│   └── index.html
├── static/
│   ├── css/style.css
│   └── js/script.js
├── alerts/
│   └── alert_log.txt
├── requirements.txt
└── README.md
```