Phone Mouse (WiFi Trackpad)

Turn your iPhone into a wireless trackpad for your laptop using a simple client-server system.

⸻

Features
	•	Smooth cursor movement using touch gestures
	•	Tap to click
	•	Left and right click buttons
	•	Two-finger scrolling
	•	Adjustable sensitivity
	•	Connection status indicator

⸻

How It Works
	•	The iPhone acts as a touch controller via a web interface
	•	Touch input is sent over WiFi using HTTP requests
	•	A Python Flask server receives the data
	•	pyautogui controls the mouse on the laptop

⸻

Project Structure

phone-mouse/
│
├── server.py          # Flask server (mouse control)
├── test.html          # Web interface for phone
└── requirements.txt   # Python dependencies


⸻

Setup Instructions

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/phone-mouse.git
cd phone-mouse


⸻

2. Install Dependencies

pip3 install -r requirements.txt


⸻

3. Run the Server (Laptop)

python3 server.py

Expected output:

Running on http://192.168.1.5:5050


⸻

4. Start Web Interface

Open a new terminal and run:

python3 -m http.server 8000


⸻

5. Open on Your Phone

Ensure both devices are on the same WiFi network.

Open Safari on your iPhone and go to:

http://192.168.1.5:8000/test.html


⸻

Notes
	•	Grant Accessibility permissions to Terminal/Python on macOS
	•	Both devices must be connected to the same network
	•	Safari is recommended for best compatibility
	•	If needed, update the IP address based on your local network

⸻

What This Project Demonstrates
	•	Client-server communication
	•	Real-time input handling
	•	Gesture recognition
	•	System-level automation using Python

⸻

Future Improvements
	•	Native iOS application (Swift)
	•	Keyboard input support
	•	Media controls
	•	Advanced gesture shortcuts

⸻

Author

Ananya Sharma
:::

If you want next:
👉 I can help you add a demo section with screenshots/GIF — that’s what really makes recruiters notice it.
