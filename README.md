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

- Go to:👉 https://code.visualstudio.com/

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
    
