# Summarize.py
import os
from datetime import datetime

# Function to find the latest file based on the filename date in the 'results' folder
def find_latest_file():
    folder = 'results'
    files = [f for f in os.listdir(folder) if f.startswith("MSM_") and f.endswith(".txt")]
    
    # If no file exists, return None
    if not files:
        return None

    # Sort files by the date in their filename (assuming 'MSM_dd_mm_yyyy.txt' format)
    files.sort(key=lambda f: datetime.strptime(f[4:-4], "%d_%m_%Y"), reverse=True)
    latest_file = files[0]
    
    return os.path.join(folder, latest_file)

# Function to read content from the latest file
def read_latest_file(latest_file):
    with open(latest_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
