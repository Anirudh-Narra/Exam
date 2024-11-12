from flask import Flask
from datetime import datetime
import os
import subprocess
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual name
    username = "Anirudh-Narra"
    
    # Set server time to IST
    india = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(india).strftime('%Y-%m-%d %H:%M:%S IST')
    
    # Get top command output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    # Display the data in HTML format
    return f"""
    <h1>System Information</h1>
    <p>Name: {name}</p>
    <p>User: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <h2>TOP output:</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
