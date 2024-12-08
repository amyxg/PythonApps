# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:37:06 2024

@author: amyxg
"""

def dateToLabel(indate):
    """
    

    Parameters
    ----------
    indate : string
        string of user input for date.

    Returns
    -------
    str
        converted date from mm/dd/yyyy to month dd, yyyy format.

    """
    monthNames = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]
    
    # split string into list of strings, ex: "mm", "dd", "yyyy"
    fields = indate.split("/")
    if len(fields) != 3:
        return "Error: Incorrect format for date. Must be in mm/dd/yyyy format"
    
    month, day, year = fields
    # check if vars are numeric, display error message if not an interger
    if not (month.isdigit() and day.isdigit() and year.isdigit()):
        return "Error: month (mm), day (dd), and year (yyyy) must be numbers"
    
    # define all vars from string to int
    month = int(month)
    day = int(day)
    year = int(year)
    
    
    if month < 1 or month > 12:
        return f"Error: {month} (mm) was not a valid month. Month should between 1 and 12."
    
    # accounting for leap years and max number of days in each month, Ex. Feb has 28 days
    maxNumDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > maxNumDays[month - 1]:
        return f"Error: {day} (dd) was not a valid day. Day should be between 1 and {maxNumDays[month - 1]} for month {month}"
    
    
    if year < 1000 or year > 9999:
        return f"Error: {year} (yyyy) was not a valid year. Year should be between 1000 and 9999"
    
    return f"{monthNames[month-1]} {day:02d}, {year}"