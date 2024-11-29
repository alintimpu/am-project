## Quartex Test Automation

## Overview
This project contains an automated test suite for validating the functionality of the Quartex Published Site using Selenium WebDriver. The suite includes tests for search, filtering, timeline navigation, and browsing collections.

Detailed instructions and dependencies are provided below.


## Features
Basic Search: Validates the search functionality, including result count and title verification.

Filtering: Applies filters and validates filtered results.

Timeline Navigation: Navigates to timeline content and verifies navigation to a new tab.

Browse Collections: Browses collections by letter and validates the displayed collections and their details.

## Prerequisites
- Python 3.10 or later
- Google Chrome browser
- ChromeDriver (compatible with your installed Chrome version)
- Internet access for Selenium to load the website 

Python dependencies are listed in requirements.txt.


## Setup Instructions
1. Clone the repository:
    git clone https://github.com/alintimpu/am-project
2. Navigate to the correct path:
    cd am-project

## Create and activate a virtual environment:
python3 -m venv venv

source venv/bin/activate

## Install dependencies:
pip install -r requirements.txt

The dependencies include:
- selenium
- webdriver-manager

## Ensure chromedriver is installed and added to your PATH. To verify, run:
chromedriver --version


##  Running the UI tests:
1. Ensure that the virtual environment is active.
2. Navigate to the test directory:
    cd tests
3. Run the UI tests:
    python test_quartex.py

    Run Specific Tests: Uncomment the desired test(s) in the if __name__ == "__main__": section of test_quartex.py.

## Test Details
Basic Search - Validates search functionality with a specific term and verifies result count and title.

No Results Scenario - Ensures appropriate messaging is displayed when no search results are found.

Timeline Navigation - Verifies navigation to a timeline content block and new tab opening for specific content.

Browse Collections - Filters collections by letter, validates collections, and ensures asset details are correct.


## Notes
Ensure Google Chrome is installed on your system.

WebDriver Manager is used to handle the ChromeDriver version automatically.

If the test fails, check the CSS selectors or ensure that the website layout has not changed.
