Copy

🌧️ Weather Rain Alert System
A Python automation project that checks the weather forecast
and sends an email notification when rain is expected.

📋 About
This project calls the OpenWeatherMap API to check the next
4 hours of weather forecast for Virginia Beach, VA. If any
hour shows rain conditions it automatically sends an email
alert so you never get caught without an umbrella!

✨ Features
☁️ Checks next 4 hours of weather forecast
🌧️ Detects all types of rain and storms
📧 Sends automatic email alert when rain detected
☀️ Confirms when no rain expected
🔒 Secure API key handling with environment variables
🖥️ Example Output
# If rain detected:
Rain alert sent! ☔

# If no rain:
No rain expected today! ☀️
🛠️ Built With
Python 3
Requests library
OpenWeatherMap API
smtplib (built into Python)
python-dotenv
🚀 How to Run
Make sure Python is installed
Install required libraries:
pip install requests python-dotenv
Clone this repository:
git clone https://github.com/alexisn1989/weather-rain-alert
Create .env file with your credentials:
OWM_API_KEY=your_openweathermap_key
MY_EMAIL=your_gmail
MY_PASSWORD=your_gmail_app_password
Run the program:
python main.py
📁 Project Structure
weather-rain-alert/
├── main.py    ← main program
└── .env       ← credentials (never push to GitHub!)
🔑 API Setup
Sign up free at openweathermap.org
Copy your API key
Add to .env file
Gmail App Password setup:
Go to myaccount.google.com
Security → App Passwords
Generate password for Python
📦 Requirements
requests
python-dotenv
smtplib (built into Python)
💡 What I Learned
Calling weather APIs with parameters
Parsing nested JSON responses
Weather condition codes
Sending automated emails with smtplib
Environment variables for security
Boolean logic for condition checking
Loops for checking multiple data points
👨‍💻 Author
Alexi — Aspiring Python Developer
Currently completing Angela Yu's 100 Days of Code bootcamp
📍 Virginia Beach, VA | Open to remote opportunities
🔗 LinkedIn: your-linkedin-url
🐙 GitHub: github.com/alexisn1989

