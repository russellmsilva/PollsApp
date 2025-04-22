# PollsApp
A web application used for testing/learning purposes. Largely based off of this [Django tutorial](https://docs.djangoproject.com/en/5.1/intro/tutorial01/).

## Features and Project Goals (Still in Development)

- **User Authentication**: Secure user login and registration system.
- **Poll Creation**: Users can create polls with multiple options.
- **Vote Casting**: Users can vote on polls and see real-time results.
- **Result Visualization**: Poll results are displayed in an easy-to-read format.
- **Admin Panel**: Admins can manage polls, users, and other application settings.
- **Responsive Design**: The application is optimized for both desktop and mobile devices.
- **Database Integration**: Uses SQLite for data storage and management.
- **Extensible Framework**: Built on Django, allowing for easy feature expansion.

## Installation

These installation instructions apply to Windows machines. They may need to be modified
for other operating systems.

1. Make sure the latest version of Python is installed.  
https://www.python.org/downloads/ 

2. Make sure the latest Sqlite3 tools package is installed.  
https://www.sqlite.org/download.html

3. Install and Configure Pipenv  
  
After cloning the repository, navigate to the repository using the terminal 
and run the following command:  

```bash
pipenv install django
```

Then run the following command to activate the virtual environment
```bash
pipenv shell
```

You can now input the standard command to start the server on port 8000
```bash
python manage.py runserver
```

4. Optional Step: VSCode Editor Configurations

If you are using VSCode, you can integrate the virtual environment into the VSCode 
editor by clicking "View" on the top, then "Command Palette", then "Python: Select Interpreter"
(you may need to search for this option in the search bar that is displayed). Now the virtual environment
python will be used instead of the global system wide python that is installed. 

You can then also configure the visual studio code debugger to run this virtual environment by 
clicking on the "Run and Debug" option in the left hand panel, creating a launch.json file from this
panel and choosing the "Django" Debug Configuration for the launch.json file. It is a good idea to add
a port argument of 9000 to the launch.json file so that this debugging server instance does not conflict 
with other server instances. You can now run the server with this launch file using the "Start Debugging" 
or "Run Without Debugging" option under "Run" (top of the IDE).

5. Database Configuration:  

Certain features of the application require the database to be setup. To set up the database for the 
application, you will need to create and apply migrations.  

Create migrations with the following command. This ensures migration files based on the project's models are generated:  
```bash
python manage.py makemigrations
```

Apply the generated migration files to the database with the following command. This ensures the necessary tables are created:  
```bash
python manage.py migrate
```
