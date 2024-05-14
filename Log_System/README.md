## How to run the program
1. Install Python in your system
2. Install Flask using pip, Python's package installer.
   Open command prompt and run the command
	pip install Flask
3. Open the code files in python IDE.
4. Create a log directory and paste its path into the
   program in app.py file.
5. Run the Program and access the application using url
	'http://localhost:5000'
6. Now you can upload log files or search any 
   particular log data aor can retrieve all the log 
   data.
7. The log files are being saved in the created 
   directory.


## System design

The system consists of a Flask web application that 
serves HTML templates and handles user reqquests. 
It uses Python's 'json' module to parse JSON data from 
log files and 'os' module to interact with the system.

## Features Implemented
1. View log entries from log files.
2. Filter log entries by level, log string, timestamp &
   source.
3. Upload new log entries to log files.  
