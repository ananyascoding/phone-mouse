📱 Phone Mouse (WiFi Trackpad)

Turn your iPhone into a wireless trackpad for your laptop using a simple client-server system.

⸻

🚀 Features
	•	🖱️ Smooth cursor movement using touch gestures
	•	👆 Tap to click
	•	🔘 Left and right click buttons
	•	🌀 Two-finger scrolling
	•	🎚 Adjustable sensitivity
	•	📶 Connection status indicator

⸻

🧠 How It Works
	•	The iPhone acts as a touch controller via a web interface
	•	Touch data is sent over WiFi using HTTP requests
	•	A Python Flask server receives the data
	•	pyautogui controls the mouse on the laptop

⸻

📂 Project Structure

phone-mouse/
│
├── server.py          # Flask server (controls mouse)
├── test.html          # Web interface for phone
└── requirements.txt   # Python dependencies


⸻

🛠️ Setup Instructions

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/phone-mouse.git
cd phone-mouse


⸻

2. Install Dependencies

pip3 install -r requirements.txt


⸻

3. Run the Server (Laptop)

python3 server.py

You should see:

Running on http://192.168.1.5:5050


⸻

4. Start Web Interface

Open a new terminal and run:

python3 -m http.server 8000


⸻

5. Open on Your Phone

Make sure your phone and laptop are on the same WiFi.

On your iPhone (Safari), open:

http://192.168.1.5:8000/test.html


⸻

⚠️ Important Notes
	•	Enable Accessibility permissions for Terminal/Python on macOS
	•	Both devices must be on the same WiFi network
	•	Use Safari on iPhone for best compatibility
	•	If the server does not start, ensure port 5050 is not blocked

⸻

🎯 What This Project Demonstrates
	•	Client-server communication
	•	Real-time input handling
	•	Gesture recognition
	•	System-level automation using Python

⸻

🔥 Future Improvements
	•	Native iOS app (Swift)
	•	Keyboard input support
	•	Media controls (volume/play/pause)
	•	Multi-gesture shortcuts

⸻

👩‍💻 Author

Ananya Sharma
:::

⸻

⚠️ One small thing

Replace with your own IP if required!

