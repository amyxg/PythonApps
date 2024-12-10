"""
Translate a date from mm/dd/yyyy to Month dd, yyyy format using flask
@author: amyxg

Steps for terminal
- python -m venv env (create virtual env, only IF there is no virtual env)
- source env/bin/activate (activate virtual env, should show (env)@amyxg ) 
- pip install Flask
- python dateConversion.py
"""
from flask import Flask, request, render_template # type: ignore
from datetime import datetime
import json
import os

app = Flask(__name__)

# Constants for file paths
LOG_FILE = "conversion_log.txt"
STATS_FILE = "usage_stats.json"

def init_stats():
    """
    Initialize usage statistics file if it doesn't exist.

    Parameters
    ----------
    None

    Returns
    -------
    dict
        Dictionary containing initial or loaded statistics data.
    """
    if not os.path.exists(STATS_FILE):
        stats = {"total_conversions": 0, "errors": 0, "last_used": None}
        save_stats(stats)
    return load_stats()

def load_stats():
    """
    Load usage statistics from JSON file.

    Parameters
    ----------
    None

    Returns
    -------
    dict
        Dictionary containing usage statistics data.
    """
    try:
        with open(STATS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"total_conversions": 0, "errors": 0, "last_used": None}

def save_stats(stats):
    """
    Save usage statistics to JSON file.

    Parameters
    ----------
    stats : dict
        Dictionary containing statistics to be saved.

    Returns
    -------
    None
    """
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=4)

def log_conversion(input_date, result):
    """
    Log conversion attempt with timestamp to file.

    Parameters
    ----------
    input_date : str
        Original date string provided by user.
    result : str
        Converted date string or error message.

    Returns
    -------
    None
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Input: {input_date} -> Output: {result}\n"
    
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

def dateToLabel(indate):
    """
    Exception handling and converting date to Month dd, yyyy format

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
    # check if vars are numeric, display error message if not an integer
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
    
    # output result in month dd, yyyy format
    return f"{monthNames[month-1]} {day:02d}, {year}"

@app.route("/", methods=['GET'])
def home():
    """
    Designated home page for users

    Returns
    -------
    html
        renders homepage.html page for user with usage statistics
    """
    stats = load_stats()
    return render_template('homepage.html', stats=stats)

@app.route("/dateToLabel", methods=['POST'])
def dateConverted():
    """
    Display results to users and log the conversion

    Returns
    -------
    html
        renders appropriate page based on user choice
    """
    if 'choice' in request.form:
        if request.form['choice'] == 'stop':
            return render_template('goodbye.html')
        # if yes, render the form again
        stats = load_stats()
        return render_template('homepage.html', stats=stats)
    
    dateString = request.form['userDate']
    convertedDate = dateToLabel(dateString)
    
    # Update statistics
    stats = load_stats()
    stats["last_used"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if convertedDate.startswith("Error"):
        stats["errors"] += 1
        log_conversion(dateString, convertedDate)
        save_stats(stats)
        return render_template('homepage.html', result=convertedDate, stats=stats)
    else:
        stats["total_conversions"] += 1
        result = f"{dateString} converted to Month dd, yyyy is {convertedDate}"
        log_conversion(dateString, convertedDate)
        save_stats(stats)
        return render_template('homepage.html', result=result, stats=stats)

if __name__ == "__main__":
    init_stats()
    app.run(debug=True)