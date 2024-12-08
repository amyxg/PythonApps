"""
Translate a date from mm/dd/yyyy to Month dd, yyyy format using flask
@author: amyxg

Steps for terminal
- python -m venv env (create virtual env)
- source env/bin/activate (activate virtual env, should show (env)@amyxg ) 
- pip install Flask
- python dateConversion.py
"""
from flask import Flask, request, render_template

app = Flask(__name__)

# Global vars
monthNames = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]

@app.route("/", methods=['GET'])
def home():
    return render_template('homepage.html')


@app.route("/dateToLabel", methods=['POST'])
def dateConverted():
    userInput = ""
    while userInput != "stop":
        
        # requesting userDate from homepage.html
        dateString = request.form['userDate']

        # split string into list of strings, ex: "mm", "dd", "yyyy"
        month, day, year  = dateString.split("/")
        if len(month, day, year ) != 3:
            return render_template('homepage.html', result="Error: Incorrect format for date. Must be in mm/dd/yyyy format")
        
        # check if month, day, and year are numeric, display error message if not an interger
        if not (month.isdigit() and day.isdigit() and year.isdigit()):
            return render_template('homepage.html', result="Error: month (mm), day (dd), and year (yyyy) must be numbers")

        # define all vars from string to int
        month = int(month)
        day = int(day)
        year = int(year)

        if month < 1 or month > 12:
            errorMonthMsg = f"Error: {month} (mm) was not a valid month. Month should between 1 and 12."
            return render_template('homepage.html', result=errorMonthMsg)
        
        # accounting for leap years and max number of days in each month, Ex. Feb has 28 days
        maxNumDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if day < 1 or day > maxNumDays[month - 1]:
            errorDayMsg = f"Error: {day} (dd) was not a valid day. Day should be between 1 and {maxNumDays[month - 1]} for month {month}"
            return render_template('homepage.html', result=errorDayMsg)
        
        if year < 1000 or year > 9999:
            errorYearMsg = f"Error: {year} (yyyy) was not a valid year. Year should be between 1000 and 9999"
            return render_template('homepage.html', result=errorYearMsg)
        
        # if all conditions passes, convert that date!
        convertedDate = f"{dateString} converted to Month dd, yyyy is {monthNames[month-1]} {day:02d}, {year}"
        return render_template('homepage.html', result=convertedDate)

    
if __name__ == "__main__":
    app.run(debug=True)