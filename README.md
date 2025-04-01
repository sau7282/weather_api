# Weather API Data Collector

This API pulls weather data from OpenWeather and stores it in CSV, XML, and Excel file formats.

## Features
- Fetches real-time weather data from OpenWeather API.
- Stores weather data in multiple formats:
  - CSV
  - XML
  - Excel (.xlsx)
- Can be extended to support additional data formats.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sau7282/weather_api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd weather_api
   ```
3. Install dependencies (if required):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script to fetch and store weather data:
```bash
python app.py
```

## Configuration
Make sure to set up your OpenWeather API key in an environment variable or a configuration file before running the script.

## Output
- **CSV**: Stored as `weather_data.csv`
- **XML**: Stored as `weather_data.xml`
- **Excel**: Stored as `weather_data.xlsx`

## Contributing
Feel free to contribute by creating pull requests or reporting issues.
