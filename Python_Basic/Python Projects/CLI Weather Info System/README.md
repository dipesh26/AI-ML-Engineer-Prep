# 🌦️ Weather Info System

A simple and effective command-line Weather Info System built using Python and OpenWeatherMap API. This tool provides real-time weather information like temperature, humidity, pressure, wind speed, and wind direction for any city around the world.

---

## 📌 Features

- Get real-time weather data by entering any city name
- Handles incorrect or invalid inputs gracefully
- Displays clean, readable weather output with emojis
- Prevents crashes with smart error handling
- Lightweight and easy to run in terminal

---

## 🚀 Technologies Used

| Technology   | Purpose                      |
|--------------|-------------------------------|
| Python 3     | Core programming language     |
| `requests`   | To make API calls             |
| OpenWeatherMap API | Real-time weather data |

---

## ⚙️ How to Use

### 1. Download the Project

- Extract the ZIP file to your local machine

### 2. Install Dependencies

Make sure Python is installed. Then open a terminal in the project folder and run:

```bash
pip install requests
```

### 3. Get Your API Key

- Go to **[OpenWeatherMap](https://openweathermap.org)**
- Sign up and generate your free **API key**

### 4. Run the Script

Edit the file to add your API key:

```bash
API_Key = "your_api_key_here"
```

Then run the script:

```bash
weather_info_system.py
```

### 5. Sample Output

```bash
Enter city name (or type 'exit' to quit): Mumbai

📍 Weather Info for Mumbai, IN:
🌡️ Temperature     : 30.4°C
💧 Humidity        : 78%
🔽 Pressure        : 1012 hPa
🌥️ Condition       : haze
💨 Wind Speed      : 3.1 m/s
🧭 Wind Direction  : 240°
```

### 🔐 API & Security

This project requires an active **[OpenWeatherMap](https://openweathermap.org)** API key. Make sure not to share or upload your personal API key in public repositories.

### 👨‍💻 Owner & Maintainer
Made with ❤️ by **Dipesh Mahajan**

### 📃 License
- This project is open-source and free to use for learning and non-commercial purposes

### ⭐️ Show Your Support
If this project helped you, give it a ⭐️