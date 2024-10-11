# my-first-api-project
This i actually a project that helps you manage tasks that you have planed to do in future , gain info on how to use this from the provided readme file

The `README.txt` file contains detailed instructions to help you run both the `my_project.py` (Flask backend) and `request_api.py` (API request script). Here's a summary of what it includes:


1. **Prerequisites**: 
   - Python 3.x should be installed.
   - You'll need `pip` for managing dependencies.(pip is already installed along with python usually)
   - Install required libraries (`Flask`, `requests`) using `pip install -r requirements.txt`.

2. **Step 1: Install Dependencies**:
   - Navigate to your project folder and run the following code on command prompt:
     pip install -r requirements.txt
    

3. **Step 2: Run the Flask Application**:
   - To start the Flask server open command prompt where your project files are, run:
     python my_project.py
    
     most probablely,
   - The Flask server will be available at `http://127.0.0.1:5000/`.

4.1:**Step 3.1: Use Postman to Make an Api Request**:
   -The web app of postman dosent seem to support local severs
   -In case you have postman desktop agent downloaded you can make a request there and skip the next step

4.2:**Step 3.2: Use the API Request Script**:
   - Run the `request_api.py` script on an ide to interact with the API, providing the desired HTTP method and URL, along with JSON data for POST or PUT requests.
   - when you run your http request make sure that your path is /tasks
   -{'name': 'New Task','description': 'Task description','completed': False } this is how your JSON input should look

5. **Troubleshooting**:
   - Ensure that the Flask app is running before making API requests.
   - The URLs provided in `request_api.py` must point to the running Flask server.

