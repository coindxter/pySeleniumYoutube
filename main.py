import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Setup Chrome options (e.g., disable notifications)
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Provide the path to ChromeDriver
driver_path = "/path/to/chromedriver"
service = Service(driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Class period playlists as tuples of playlist titles
class_1B = (
    "Student 1 Playlist Title",
    "Student 2 Playlist Title",
    # Add more playlist titles as needed
)

class_2B = (
    "Student 1 Playlist Title",
    "Student 2 Playlist Title",
    # Add more playlist titles as needed
)

class_3B = (
    "Student 1 Playlist Title",
    "Student 2 Playlist Title",
    # Add more playlist titles as needed
)

class_4B = (
    "Student 1 Playlist Title",
    "Student 2 Playlist Title",
    # Add more playlist titles as needed
)

class_5B = (
    "Student 1 Playlist Title",
    "Student 2 Playlist Title",
    # Add more playlist titles as needed
)

class_6B = (
    "Student 1 Playlist Title",
    "Student 2 Playlist Title",
    # Add more playlist titles as needed
)

class_7B = (
    "Student 1 Playlist Title",
    "Student 2 Playlist Title",
    # Add more playlist titles as needed
)

class_8B = (
    "Student 1 Playlist Title",
    "Student 2 Playlist Title",
    # Add more playlist titles as needed
)

# List of class periods (each corresponding to one of the tuples)
class_periods = [class_1B, class_2B, class_3B, class_4B, class_5B, class_6B, class_7B, class_8B]

# Function to search and play a playlist by title
def search_and_play_playlist(playlist_title):
    # Open YouTube's homepage
    driver.get("https://www.youtube.com/")
    
    # Wait for the page to load
    time.sleep(3)
    
    # Find the search bar element and input the playlist title
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.clear()
    search_box.send_keys(playlist_title)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for search results to load
    time.sleep(3)
    
    # Find the first result that is a playlist and click on it
    try:
        playlist_link = driver.find_element(By.XPATH, "//a[contains(@href, '/playlist')]")
        playlist_link.click()
        
        # Wait for the playlist page to load
        time.sleep(3)
        
        # Play the playlist
        play_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Play all']")
        play_button.click()
    except Exception as e:
        print(f"Could not find playlist '{playlist_title}' due to: {e}")

# Function to manage class periods
def manage_class_periods(class_periods, duration):
    for i, class_period in enumerate(class_periods, start=1):
        print(f"Playing a playlist from class period {i}B")
        
        # Pick a random playlist title from the given class period
        playlist_title = random.choice(class_period)
        
        # Search for and play the playlist
        search_and_play_playlist(playlist_title)
        
        # Sleep for the duration of the class period (in seconds)
        time.sleep(duration)
        
        # After the duration ends, refresh to stop the current playlist
        driver.refresh()

# Main function
if __name__ == "__main__":
    try:
        # Assume each class period is 45 minutes (2700 seconds)
        class_duration = 45 * 60
        
        # Play random playlists for all class periods
        manage_class_periods(class_periods, class_duration)
    
    finally:
        # Close the driver when done
        driver.quit()