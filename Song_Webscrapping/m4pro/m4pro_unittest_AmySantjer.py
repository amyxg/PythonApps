# This program will test m4Pro_Webscrapping_AmySantjer functions (2)
# 10/20/2024
# CSC221 M4Pro
# Amy Santjer

import unittest
from M4Pro_Webscrapping_AmySantjer import getSongsForYear, saveSongFile

class Testm4Pro_Webscrapping_AmySantjer(unittest.TestCase):
    """
    Test cases for our m4Pro_Webscrapping_AmySantjer functions.
    """

    def test_getSongsForYear(self):
        """
        Test getting songs for a valid year.
        """
        
        songs = getSongsForYear(2023) # Try to get songs for 2023, can input any year(YYYY) to check
        
        # Check if we got any songs
        self.assertIsNotNone(songs)
        # Check if we got a reasonable number of songs
        self.assertGreater(len(songs), 0)
        # Check if each song has all required information
        for song in songs:
            self.assertTrue('year' in song)
            self.assertTrue('rank' in song)
            self.assertTrue('title' in song)
            self.assertTrue('artist' in song)

    def test_getSongsBadYear(self):
        """
        Test getting songs for an invalid year.
        """
        songs = getSongsForYear(1600) # Try to get songs for a year that won't have data
        self.assertIsNone(songs)

    def testSaveSongs(self):
        """
        Test saving songs to a csv file.
        """
        # Create some test songs to put in csv file later 
        test_songs = [
            {'year': '2024', 'rank': '1', 'title': 'SongAlpha', 'artist': 'Alpha Artist'},
            {'year': '2024', 'rank': '2', 'title': 'SongBeta', 'artist': 'Beta Artist'}
        ]
        
        # Try to save the songs in csv file
        result = saveSongFile(test_songs, 'unittest_Output.csv')
        self.assertTrue(result)

    def testSaveEmptySongs(self):
        """
        Test trying to save when we have no songs.
        """

        result = saveSongFile([], 'unittest_Output.csv')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)