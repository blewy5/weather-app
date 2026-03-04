# Weather App

A simple command-line weather application written in Python.
The program fetches current weather data for a selected city and displays it in the terminal.

---

## Requirements

* Python 3.8+
* Internet connection
* API key for a weather service (for example OpenWeather)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/blewy5/weather-app.git
cd weather-app
```

2. (Optional but recommended) Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

3. Install dependencies (if `requirements.txt` is present):

```bash
pip install -r requirements.txt
```

---

## Configuration

Edit the `config.py` file and set your API key and other settings required by the application, for example:

```python
API_KEY = "YOUR_API_KEY"
```

---

## Run the application

```bash
python main.py
```

---

## How it works

The application runs in the terminal and allows you to:

* enter a city name,
* download current weather data from an external API,
* display basic information such as temperature and weather conditions.

---

## Project structure

* `main.py` – application entry point
* `cli.py` – command-line interface logic
* `core.py` – main application logic
* `config.py` – configuration (API key, endpoints, etc.)

---

## Author

Bartek Lewandowski

---

## License

This project is released under the MIT license.
