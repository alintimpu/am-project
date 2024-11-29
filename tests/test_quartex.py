import sys
import os

# Dynamically add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from base.locators import SearchFunctions, HeaderFunctions, BrowseFunctions
import time


def test_basic_search():
    # Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
       # Create an instance of SearchFunctions
        search_functions = SearchFunctions(driver)
    
        # Open the Quartex Published Site
        search_functions.open_quartex_site()

        # Handle cookie consent banner if it appears
        search_functions.handle_cookie_consent()


        # Perform a search for the term "Brown"
        search_functions.search_for_term("Brown")

        # Validate that the search results match the expected count and contain a specific title
        search_functions.validate_search_results_with_title(
            search_results=34,
            expected_title="1 April 1875. Browning, Robert to Pollock, Lady."
        )

        # Apply a filter by collection and validate the filtered results
        search_functions.filter_by_collection(
            filtered_search_results=6
        )

        print("Great success!")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

def test_no_results_scenario():
    # Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        no_results_functions = SearchFunctions(driver)

        # Open the Quartex Published Site and maximize the window
        no_results_functions.open_quartex_site()

        # Perform a search for a term that will yield no results
        no_results_functions.search_for_term("Lorem Ipsum")

        # Validate that the "no results" message is displayed
        no_results_functions.validate_no_results_message(
            expected_message="Sorry, no results found that match your criteria."
        )

        print("No Results Test Passed")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()


def test_timeline_navigation():
    # Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        timeline_functions = HeaderFunctions(driver)

        # Open the Quartex Published Site and maximize the window
        timeline_functions.driver.get("https://demo.quartexcollections.com/")
        timeline_functions.driver.maximize_window()

        # Navigate to the Timeline content block
        timeline_functions.navigate_to_timeline_content_block()

        # Click on a hyperlink in the Timeline content block
        timeline_functions.click_timeline_link()

        # Validate that the user is navigated to the expected webpage in a new tab
        timeline_functions.validate_new_tab(
            expected_url="https://www.poetryfoundation.org/poets/robert-browning"
        )

        print("Timeline Navigation Test Passed")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()


def test_browse_and_view_collections():
    # Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        browse_functions = BrowseFunctions(driver)

        # Open the Quartex Published Site
        browse_functions.driver.get("https://demo.quartexcollections.com/")
        browse_functions.driver.maximize_window()

        # Navigate to the "Explore the Collections" page
        browse_functions.navigate_to_explore_collections()

        # Browse collections by the letter "M"
        browse_functions.browse_collections_by_letter()

        # Validate that the Manuscripts collection is displayed
        browse_functions.validate_collection_displayed(expected_collection="Manuscripts")

        # Click on the collection and validate its details including the header, number of results, and asset title
        browse_functions.navigate_to_collection()

        browse_functions.validate_collection_details(
            expected_collection="Manuscripts",
            expected_results_count=30,
            expected_asset_title="AM LAGERFEUER"
        )

        print("Browse Collections Test Passed")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    # Run the desired test(s) by uncommenting the relevant lines
    test_basic_search()
    test_no_results_scenario()
    test_timeline_navigation()
    test_browse_and_view_collections()