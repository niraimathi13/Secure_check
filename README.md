# A Python SQL digital ledger for police post logs

To build an SQL based checkpost database with Python powered dashboard for the real time insights and alerts.

## Features

- Clean data processing - Handling missing values in Python
- SQL database intregation - Store and manage data in MySQL
- Real time dashboard - Streamlit dashboard for live vehicle logs and violation tracking
- Interactive search filter - Quickly find the records based on the driver's details
- Demographic analysis - Breakdown by driver age,gender,race and stop outcome
- Time based trends - Analyze the stop by hour,day,month
- Key metrices - Show the total stops,total warning,total arrest,drug related stops

## Technologies used

- Python 
- MySQL
- Streamlit

## Installation

📌Install Python

- Go to the official website:👉 https://www.python.org/downloads

- Download the latest version (Python 3.12.0)

- Run the downloaded .exe file

- ✅ Check the box that has "Add Python to PATH"

- Click Install now

💻Install Visual Studio Code

- Go to:👉 https://code.visualstudio.com/download

- Click "Download for Windows"

- Run the installer (VSCodeUserSetup-x64-x.x.x.exe)

- Accept the license agreement and continue

- On the "Select Additional Tasks" screen, ✅ check:

   -->"Add to PATH"

   -->"Register Code as an editor for supported file types"

   -->"Add 'Open with Code' to Windows Explorer context menu"

- Click Install

- Check "Launch Visual Studio Code" and click Finish

- Open VS Code and install the following extensions:

    --> Python (by Microsoft)

    -->Jupyter (for notebooks)

🧰 3. Download & Install XAMPP (MySQL+Apache)

- Go to:👉 https://www.apachefriends.org/index.html

- Click Download for Windows

- Run the installer (xampp-windows-x.x.x-installer.exe)

- Click Yes if prompted by User Account Control

- In the setup wizard:

  --> Select: Apache, MySQL, PHP, phpMyAdmin

- Choose a location (default: C:\xampp)

- Click Next --> Install

- Once installed, launch XAMPP Control Panel

- Start:

    -->✅ Apache

    -->✅ MySQL

- Visit http://localhost/phpmyadmin to access MySQL GUI

🐍Set Up Python Virtual Environment 

- In the project folder:

    -->python -m venv .venv

- .venv folder will be created. Then activate it:

    -->.venv\Scripts\activate.bat

📦Install required Python packages  

- Install the MySQL connector:

-->pip install mysql-connector-python

- Install Streamlit:

-->pip install streamlit

🚀Run the Streamlit app

- To launch the dashboard

    -->streamlit run police.py
    
## Business use cases

- Store all check post data in one central database for easier access across locations

- Find crime patterns by analyzing data with Python

- Automatically detect suspect vehicles using smart SQL filters

- Track how well each check post is working using data reports

- Log vehicle and officer details lively at each check post

## Screenshots

<img width="1920" height="1080" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/91252519-0663-4c29-866d-3eed94e225e0" />

<img width="1920" height="1080" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/cc73bd14-3b95-4442-9062-954a1de7a4ec" />

<img width="1920" height="1080" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/44788122-6bf1-4f6d-b013-4fc1e256fb51" />

<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/6540be2d-d45c-4f5c-a181-4ac687903b6c" />

<img width="1920" height="1080" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/259a5612-74fe-4f32-8761-ef19cc4eeca4" />

<img width="1920" height="1080" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/7aafdab8-29a5-4646-9fe3-4a2f8f0f5ef9" />

