this is a program to test rect and flask together. 



# First, create your project folders:
mkdir my_project
cd my_project

# input your python files in the my_project directory!

## Set up Flask (the backend):
# Create a virtual environment (keeps your Python packages organized)
python -m venv venv

# Activate it (on Windows use: venv\Scripts\activate)
source venv/bin/activate

# Install what we need
pip install flask flask-cors

# Create app.py and paste the backend code from above

## Set up React (the frontend):
# In a new terminal, create a React app
npx create-react-app frontend
cd frontend

# Replace the contents of src/App.js with the frontend code from above


## Run both parts:
# In one terminal, run the Flask backend:
python app.py

# In another terminal, go to the frontend folder and run:
npm start