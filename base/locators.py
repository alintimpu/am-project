
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# General locators for elements appearing across the site
class GeneralLocators:
    COOKIE_ACCEPT_BUTTON = (By.CSS_SELECTOR, "a[aria-label='dismiss cookie message']")


# Locators specific to search functionality
class SearchLocators:
    SEARCH_BOX = (By.CSS_SELECTOR, '[id="search_input_intro"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[class="search__button"]')
    SEARCH_RESULT_TITLES = (By.CSS_SELECTOR, '[class="media-object__heading__link bold breakword-for-long-text"]')

    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, '[id="no-results-msg-container"]')
    BROWSE_ALL_PAGE_TITLE = (By.CSS_SELECTOR, 'h1.browse-all-title') 


# Locators for filtering results
class FilterLocators:
    FILTER_OPTION = (By.CSS_SELECTOR, '[name="chk-box-war-&-conflict"]')
    APPLY_FILTERS =  (By.CSS_SELECTOR, '[id="filters"] [aria-label="Apply filters"]')
    APPLIED_COLLECTION_FILTER = (By.CSS_SELECTOR, '[data-testid="search-criteria-collections-group"]')


# Locators specific to timeline navigation
class TimelineLocators:
    DISCOVERY_AIDS_LINK = (By.CSS_SELECTOR, '[data-testid="site-main-menu"] [aria-label="Discovery Aids"]')
    BROWNINGS_HISTORY_LINK = (By.LINK_TEXT, "The Brownings: A Brief History")
    TIMELINE_LINK = (By.PARTIAL_LINK_TEXT, "Learn more")


# Locators for browsing collections
class BrowseLocators:
    EXPLORE_COLLECTIONS_LINK = (By.LINK_TEXT, "Explore the Collections")
    COLLECTION_LETTER_M = (By.CSS_SELECTOR, '[data-letter="M"]')
    COLLECTION_TITLE = (By.LINK_TEXT, "Manuscripts")

    # Header, results count, and asset title locators for collection details
    COLLECTION_HEADER = (By.CSS_SELECTOR, "div.wrapper.wrapper--flush > h1.heading.heading--tertiary.mark-highlightable") # Awful locator to improve for future stability
    COLLECTION_RESULTS_COUNT = (By.CSS_SELECTOR, '[class="media-list__top-pagination-info"]')
    COLLECTION_ASSET_TITLE = (By.CSS_SELECTOR, ".asset-title")


# Class to manage search-related actions
class SearchFunctions:
    def __init__(self, driver):
        self.driver = driver

    def handle_cookie_consent(self):
        # Dismiss the cookie consent banner if it appears
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(GeneralLocators.COOKIE_ACCEPT_BUTTON)
            ).click()
            print("Cookie consent dismissed.")
        except TimeoutException:
            print("No cookie banner found.")

    def open_quartex_site(self):
        # Navigate to the Quartex Published Site
        self.driver.get("https://demo.quartexcollections.com/")
        self.driver.maximize_window()


    def search_for_term(self, term):
        # Perform a search for a given term
        search_bar = self.driver.find_element(*SearchLocators.SEARCH_BOX)
        search_bar.send_keys(term)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(SearchLocators.SEARCH_BUTTON)
        ).click()

  
    def validate_search_results_with_title(self, search_results, expected_title):
        # Validate search results count and the presence of a specific title
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(SearchLocators.SEARCH_RESULT_TITLES)
        )
        results = self.driver.find_elements(*SearchLocators.SEARCH_RESULT_TITLES)

        # Validate the number of results
        actual_count = len(results)
        assert actual_count == search_results, f"Expected {search_results} results but found {actual_count}"
        print(f"Number of results matched: {actual_count}")

        # Validate the specific title is in the results
        titles = [result.text for result in results]    
        assert expected_title in titles, f"Expected title '{expected_title}' not found in results: {titles}"
        print(f"Title '{expected_title}' found in results.")


    def filter_by_collection(self, filtered_search_results):
        # Apply a filter and validate the filtered results count
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(FilterLocators.FILTER_OPTION)
        ).click()
        self.driver.find_element(*FilterLocators.APPLY_FILTERS).click()

        # Wait for filter results to load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FilterLocators.APPLIED_COLLECTION_FILTER)
        )

        # Validate the updated number of results
        results = self.driver.find_elements(*SearchLocators.SEARCH_RESULT_TITLES)
        actual_count = len(results)

        assert actual_count == filtered_search_results, (
            f"Expected {filtered_search_results} results but found {actual_count}"
        )
        print(f"Number of results matched: {actual_count}")


    def validate_no_results_message(self, expected_message):
        # Validate the no results message
        actual_message = self.driver.find_element(*SearchLocators.NO_RESULTS_MESSAGE).text
        assert actual_message == expected_message, (
            f"Expected message '{expected_message}' but found '{actual_message}'"
        )
        print(f"No results message validated: '{actual_message}'")


# Class for interacting with the timeline content block
class HeaderFunctions:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_timeline_content_block(self):
        # Navigate to the Timeline content block
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TimelineLocators.DISCOVERY_AIDS_LINK)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TimelineLocators.BROWNINGS_HISTORY_LINK)
        ).click()

    def click_timeline_link(self):
        # Click a hyperlink within the Timeline content block
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TimelineLocators.TIMELINE_LINK)
        ).click()

    def validate_new_tab(self, expected_url):
        # "Validate navigation to a new tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
        print(f"Successfully navigated to: {actual_url}")


class BrowseFunctions:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_explore_collections(self):
        # Navigate to the Explore the Collections page
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(BrowseLocators.EXPLORE_COLLECTIONS_LINK)
        ).click()

    # TODOUpdate to make it dynamic
    def browse_collections_by_letter(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BrowseLocators.COLLECTION_LETTER_M)
        ).click()
 
    def validate_collection_displayed(self, expected_collection):
        # Validate the collection title is displayed
        actual_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(BrowseLocators.COLLECTION_TITLE)
        ).text
        assert expected_collection in actual_title, (
            f"Expected collection '{expected_collection}', but got '{actual_title}'"
        )
        print(f"Collection '{expected_collection}' validated.")


    def navigate_to_collection(self):
        # Generate a dynamic locator for the collection and click
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BrowseLocators.COLLECTION_TITLE)
        ).click()



    def validate_collection_details(self, expected_collection, expected_results_count, expected_asset_title): 
        # Validate the header matches the chosen collection
        actual_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(BrowseLocators.COLLECTION_HEADER)
        ).text
        assert actual_header == expected_collection, f"Expected collection header '{expected_collection}', but got '{actual_header}'"
        print(f"Validated collection header: '{actual_header}'")


        # Wait until at least one search result is present
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(SearchLocators.SEARCH_RESULT_TITLES)
        )
        results = self.driver.find_elements(*SearchLocators.SEARCH_RESULT_TITLES)

        # Validate the number of results
        actual_count = len(results)
        assert actual_count == expected_results_count, f"Expected {expected_results_count} results but found {actual_count}"
        print(f"Number of results matched: {actual_count}")

        # Validate the title of an asset is visible
        titles = [result.text for result in results]
        assert expected_asset_title in titles, f"Expected title '{expected_asset_title}' not found in results: {titles}"
        print(f"Title '{expected_asset_title}' found in results.")






















