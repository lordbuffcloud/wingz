REM            __            ______
REM          /'__`\         /\  ___\
REM    __  _/\_\L\ \  __  __\ \ \__/   __  _
REM   /\ \/'\/_/_\_<_/\ \/\ \\ \___``\/\ \/'\
REM   \/>  </ /\ \L\ \ \ \_\ \\/\ \L\ \/>  </
REM   /\_/\_\\ \____/\/`____ \\ \____//\_/\_\
REM   \//\/_/ \/___/  `/___/> \\/___/ \//\/_/
REM                              /\___/
REM                               \/__/ crisking.me


# Wing Search: Traditional Wings Locator

## Overview
Wingz is a Python application designed to help users find the best traditional wings near their location. Utilizing the Google Places API, it searches for wing places based on a user-inputted zip code, evaluates them based on a set of criteria (like price level and rating), and recommends the top choice. The application features a graphical user interface (GUI) developed with Tkinter, making it user-friendly and accessible.

## Features
- **Zip Code Based Search:** Users can search for traditional wings by entering their zip code.
- **Real-Time Recommendations:** Dynamically fetches and recommends places based on user criteria.
- **Continuous Search:** Option to keep searching for wings every 12 hours.
- **User-Friendly GUI:** Easy-to-use graphical interface with visual feedback.

## Prerequisites
Before running Wing Search, ensure you have the following installed:
- Python (version 3.6 or later)
- pip (Python package installer)

## Dependencies
Wingz requires the following Python packages:
- `requests`: For making HTTP requests to the Google Places API.
- `tkinter`: For the GUI.
- `threading`: For running the search function in the background.
- `schedule`: For scheduling repeated searches.
- `time`: For time-related functions.

## Installation
1. **Install Python and pip:** Ensure Python and pip are installed on your system. Python installation typically includes pip.

2. **Clone the Repository or Download the Script:** Obtain a copy of the Wing Search script. If you're using git, you can clone the repository. Alternatively, download the script directly from the source.

3. **Install Dependencies:** Install the required Python packages by running the following command in your terminal or command prompt: pip install requests schedule


## Setting Up Google Places API Key
1. **Get a Google Places API Key:** Visit the [Google Cloud Platform Console](https://console.cloud.google.com/), create a project, and enable the Google Places API for that project. Generate an API key for accessing the API.

2. **Configure the Script:** Replace the placeholder API key in the script (`api_key = 'YOUR_API_KEY_HERE'`) with your actual Google Places API key.

## Running the Application
1. **Launch the Script:** Open a terminal or command prompt, navigate to the directory containing the Wing Search script, and run: python wingz.py
2. **Use the Application:** Upon launching, the application will display a window where you can:
- Enter a zip code.
- Click "Start Search" to begin the search for traditional wings.
- View real-time updates and recommendations in the output area.
- Click "Stop Search" to halt the search process.


## Note
- The Google Places API may incur charges based on your usage. Please review the [Google Places API pricing](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing) to understand potential costs and manage your API key accordingly.

## Troubleshooting
- **API Key Issues:** If you encounter errors related to the Google Places API, ensure your API key is correctly configured and has the necessary permissions enabled.
- **Dependency Errors:** Make sure all required packages are installed. If errors persist, try reinstalling the packages.

## Conclusion
Wingz simplifies the process of finding great traditional wings near you. With its easy-to-use interface and robust search functionality, it's an essential tool for wing enthusiasts. If you have any questions or encounter issues, please refer to the official documentation for the dependencies and the Google Places API.

