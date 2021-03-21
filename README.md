# IT254-Project
Mini Project for the WEB DEV IT254

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
>All the above commands should be run parallelly to use all the about features together.
