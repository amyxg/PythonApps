# Collect Top Charting Songs from Several Pages into a csv File
# 10/20/2024
# CSC221 M4Pro
# Amy Santjer
import logging  # keeping track of what our program does
import csv
import requests  # get/request web pages
from bs4 import BeautifulSoup  # reading HTML content
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('m4pro_AmySantjer.log'),  # Save messages to a file
        logging.StreamHandler()  # Show messages in the console
    ]
)


def getSongsForYear(year):
    """
    Gets the top songs for a specific year from Wikipedia.
    Args:
        year: int
    Returns:
        A list of songs if successful, None if something goes wrong
    """
    url = f"https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{year}"
    try:
        # Try to get webpage
        logging.info("Getting data for year %d...", year)
        response = requests.get(url, timeout=10)
        # Check if we got the page successfully
        if response.status_code != 200:
            logging.error("Couldn't get the webpage for %d", year)
            return None
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the table with the songs
        tables = soup.find_all('table', {'class': 'wikitable'})
        if not tables:
            logging.error("Couldn't find the songs table for %d", year)
            return None
        songs = []
        table = tables[0]
        # Go through each row in the table
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all(['td', 'th'])
            # columns (rank, title, artist)
            if len(columns) >= 3:
                # Get and clean up the text from each column
                rank = columns[0].text.strip()
                title = columns[1].text.strip()
                artist = columns[2].text.strip()
                # Add this song to our list
                songs.append({
                    'year': str(year),
                    'rank': rank,
                    'title': title,
                    'artist': artist
                })
        logging.info("Found %d songs for %d", len(songs), year)
        return songs
    except Exception as error:
        logging.error("Error getting songs for %d: %s", year, str(error))
        return None


def saveSongFile(songs, filename):
    """
    Saves the list of songs to a CSV file.
    Args:
        songs: list (List of songs to save)
        filename: str (Name of the file to save to)
    Returns:
        True if successful, False if something goes wrong
    """
    try:
        if not songs:
            logging.error("No songs to save!")
            return False
        # Open the file and write the songs
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Define the columns for our CSV file
            fieldnames = ['year', 'rank', 'title', 'artist']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(songs)
        logging.info("Successfully saved %d songs to %s", len(songs), filename)
        return True
    except Exception as error:
        logging.error("Error saving to file: %s", str(error))
        return False


def main():
    """
    program to start: Get songs for a range of years and save them to a file
    """
    try:
        # Define which years we want to get
        start_year = 2020
        end_year = 2024
        output_file = f'm4Pro_{start_year}_{end_year}.csv'
        # Get songs for each year
        all_songs = []
        for year in range(start_year, end_year + 1):
            songs = getSongsForYear(year)
            if songs:
                all_songs.extend(songs)  # Add these songs to our main list
        # Save all songs to a file
        if all_songs:
            if saveSongFile(all_songs, output_file):
                print(f"Successfully saved {len(all_songs)} songs to {output_file}")
            else:
                print("Failed to save songs to file")
        else:
            print("No songs were found!")
    except Exception as error:
        print(f"The program encountered an error: {str(error)}")


if __name__ == "__main__":
    main()
