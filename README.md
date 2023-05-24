# Solita Dev Academy 

This project aims to complete the requirements set out by the Solita Dev Academy. 

The project aims to provide a backend to send CSV information to a Postgres Container, and display the database information on the front end. 

# Requirements

Docker 

Docker Compose 

Python3.9 with Requirements installed from requirements.txt

PIP

CSV Data provided by Solita: Make sure to add them to the directory named 'CSVData', this will need to make by you in the root directory. 
# Steps to Run 

Clone this repository, and place .env and secretVars.py in the Root Directory. 

1. First to Start up the Container RUN: 

docker-compose up -d 

2. Install PIP, and run:

pip3 install -r requirements.txt

3.  Run filesToDB.py 
python3 filesToDB.py


