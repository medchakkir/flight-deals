# Flight Deals Tracker

A Python application that helps you track and find the best flight deals to your desired destinations. The application uses the Amadeus API for flight searches and Sheety API for managing destination data, making it easy to monitor and compare flight prices.

## Features

- Automated flight price tracking
- IATA code lookup for cities
- Integration with Amadeus Flight Search API
- Google Sheets integration via Sheety API
- Price comparison and deal notifications
- Easy-to-use data management system

## Requirements

- Python 3.x
- Required Python packages:
  - requests
  - twilio
  - pprint

## Installation

1. Clone this repository:

```bash
git clone https://github.com/<username>/flight-deals.git
cd flight-deals
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Create a `.env` file in the root directory
   - Add your API keys:
     ```
     AMADEUS_API_KEY=your_amadeus_api_key
     AMADEUS_API_SECRET=your_amadeus_api_secret
     SHEETY_ENDPOINT=your_sheety_endpoint
     ```

## Project Structure

- `main.py`: Main application entry point
- `flight_search.py`: Handles flight search functionality using Amadeus API
- `data_manager.py`: Manages data operations and Google Sheets integration
- `flight_data.py`: Defines flight data structures
- `notification_manager.py`: Handles price alerts and notifications

## Usage

1. Run the main application:

```bash
python main.py
```

2. The application will:
   - Fetch destination data from your Google Sheet
   - Look up IATA codes for cities without them
   - Search for flight deals using the Amadeus API
   - Update the sheet with new flight information
   - Send notifications for good deals (if configured)

## API Integration

### Amadeus API

The application uses the Amadeus API for flight searches. You'll need to:

1. Sign up for an Amadeus API account
2. Get your API key and secret
3. Configure the credentials in your environment variables

### Sheety API

The application uses Sheety to manage destination data in Google Sheets:

1. Create a Google Sheet with your desired destinations
2. Set up Sheety to connect to your sheet
3. Configure the Sheety endpoint in your environment variables

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
