# guc-overflow
## Overview

Web app that helps gucians ask questions reltaed to courses and other topics, have polls for cancelling quizzes or having an event.

---
## Usage
1. clone repo into your local machine.
2. Change working directory into the top level of the repo that you have just cloned. (hint: you have to be on the same level where          manage.py file is)
3. To create the docker container that our project will be running on execute the following command:
    docker-compose build
4. To create the postgresql database you need to run the following command:
    docker-compose run web python manage.py migrate
  This will create your database.
5. To start the server:
    docker-compose up
6. To access the server you will need to go to "http://localhost:8000/"
