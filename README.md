Great, here's the `README.md` based on the information provided.

# Meeting-Mojo-Crawler


## ⚠️ Disclaimer / Warning!
This repository/project is intended for Educational Purposes ONLY.
The project and corresponding python script should not be used for any purpose other than learning. Please do not use it for any other reason than to learn about webscrapping. Make sure you adhere to the terms and conditions of the site!

## Overview

Before attending a business conference, networking is crucial. Connecting with relevant attendees beforehand not only maximizes the conference experience but also helps you to meet potential collaborators, clients, and investors. However, navigating the participants list on the event's platform can be time-consuming. That's where Meeting-Mojo-Crawler comes into play.

This Python script scrapes the participants' list from a conference using the Meeting-Mojo platform and exports all available data into an Excel file. This tool extracts various data points including company profile, company ticker, company type, company website, financial summary, investment & licensing (in/out), keywords, participants' name, participants' description, other sector, pipeline, presentation time and location, sector, sponsor level, year founded, country, name, team, and url. These details can then be used for pre-conference networking and planning.

## Installation

1. Clone this repository: `git clone https://github.com/ahaake/Meeting-Mojo-Crawler.git`
2. Change into the directory: `cd Meeting-Mojo-Crawler`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

To use this project, follow these steps:

1. Make sure you're a registered participant for the event (you should have a ticket and a profile in the system).
2. Launch the event's site and inspect it to get the curl command in bash format. You can do this by using the network inspect tool of your browser and looking for the "https://XXXX.meeting-mojo.com/search" request. XXXX stands for your event shortcode.
3. Copy the curl command and convert it into Python dictionary format using this tool: "https://curlconverter.com/python/"
4. Replace the `headers` and `cookies` in the Python script with your own.
5. Run the script with `python your_script.py` and wait for it to complete.

At the end, you'll find an Excel file `export_participants.xlsx` in the same directory with the extracted data.

## Contributions

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Please make sure to update the tests as appropriate.

## License

This project is licensed under the MIT License. See the `LICENSE.md` file for details.

## Contact

For any questions or discussions, feel free to open an issue or submit a pull request.

Please note: This script should be used responsibly and ethically, and only with proper permissions. Misuse of this script could potentially violate privacy rights or terms of service of the Meeting-Mojo platform. Please make sure you understand the implications and are in compliance with all relevant rules and regulations.