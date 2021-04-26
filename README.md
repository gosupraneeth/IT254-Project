# IT254-Project
Mini Project for the WEB DEV IT254

## Installations 

Install pip for your system 

Then run the below code to install the requirements for the project

````
pip install -r requirements.txt
````

## To load new data into database
To load new data by overwriting the present data run the below code
````
python manage.py runscript load_data
````
NOTE: Don't run this to test the application only use it if you want to upload new data

## How to run chatbot

To run the RASA Chatbot use the below command in **CHATBOT_RASA** directory
````
rasa run -m models --enable-api --cors "*" --debug
````
This command starts the local server *http://localhost:5005*


Parallelly run the below command to activate the actions for the bot
````
rasa run actions
````

## How to run the django project

Run the below command to start the local server *http://127.0.0.1:8000/* in the **MovieReview** directory
````python
python manage.py runserver
````
After starting this server, open the above link in browser to view the application.
>All the above commands should be run parallelly to use all the above features together and for full application.
