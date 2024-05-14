from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)

json_data = [
    {
        "level": "error",
        "log_string": "Inside the Search API",
        "timestamp": "2023-09-15T08:00:00Z",
        "metadata": {
            "source": "log3.log"
        }
    },
    {
        "level": "error",
        "log_string": "Inside the Search API",
        "timestamp": "2023-09-15T08:00:00Z",
        "metadata": {
            "source": "log3.log"
        }
    }
]

@app.route('/')
def index():
    level = request.args.get('level')
    log_string = request.args.get('logString')
    timestamp = request.args.get('timestamp')
    source = request.args.get('source')

    data = []
    search_data = []
    
    log_folder = r'\Users\pande\Desktop\json'  # Raw string to handle backslashes properly
    
    if level or log_string or timestamp or source:
        for file_name in os.listdir(log_folder):
            file_path = os.path.join(log_folder, file_name)
            if os.path.isfile(file_path) and file_name.endswith('.log'):
                with open(file_path, 'r') as log_file:
                    for line in log_file:
                        try:
                            log_entry = json.loads(line.strip())
                            if (not level or log_entry.get('level') == level) and \
                               (not log_string or log_entry.get('log_string') == log_string) and \
                               (not timestamp or log_entry.get('timestamp') == timestamp) and \
                               (not source or log_entry.get('metadata', {}).get('source') == source):
                                search_data.append(log_entry)
                        except json.JSONDecodeError:
                            pass
        return render_template('index.html', data=search_data)
    else:
        for file_name in os.listdir(log_folder):
            file_path = os.path.join(log_folder, file_name)
            if os.path.isfile(file_path) and file_name.endswith('.log'):
                with open(file_path, 'r') as log_file:
                    for line in log_file:
                        try:
                            log_entry = json.loads(line.strip())
                            data.append(log_entry)
                        except json.JSONDecodeError:
                            pass
        return render_template('index.html', data=data)

@app.route('/upload')
def upload_file():
    level = request.args.get('level')
    log_string = request.args.get('logString')

    message = ["Oops! Enter valid value"]

    if level and log_string and level.strip() and log_string.strip():
        directory = r'\Users\pande\Desktop\json'  # Raw string to handle backslashes properly
        file_count = sum(1 for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item)))
        folder_count = sum(1 for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item)))
        count = file_count + folder_count + 1

        destination_path = os.path.join(directory, 'log' + str(count - 1) + '.log')

        current = datetime.now()

        log_message = {
            "level": level,
            "log_string": log_string,
            "timestamp": current.isoformat(),
            "metadata": {
                "source": 'log' + str(count - 1) + '.log'
            }
        }

        if not os.path.exists(destination_path):
            with open(destination_path, 'w') as log_file:
                log_file.write("Log File\n")

        with open(destination_path, 'a') as log_file:
            json.dump(log_message, log_file)

        message[0] = "Wooow.. Data inserted.."

    return render_template('index_data.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
