# Ohjelmistotekniikka, harjoitustyö

This repository is for **Univeristy of Helsinki** course *Ohjelmistotekniikka* and its project work and exercises.

Please note that the repository will be updated during the spring of 2024.

## Quiz Application

The project is a **quiz application**, where users are presented with various questions from different topics such as geography, cities, general knowledge, sports, and others. Each question has four answer options and one correct answer.

## Documentation

Link to the [Requirements Specification](https://github.com/mikaelri/ot-harjoitustyo/blob/main/quiz-app/documentation/requirements_specification.md)

Link to the [Hour Tracker](https://github.com/mikaelri/ot-harjoitustyo/blob/main/quiz-app/documentation/hour_tracker.md)

Link to the  [Change Log](https://github.com/mikaelri/ot-harjoitustyo/blob/main/quiz-app/documentation/change_log.md)

## Installation instructions
Install the dependencies inside the *quiz-app* folder and requirements with command
```
poetry install
```
## User guide and testing the application after installation

Create the database with command inside *the quiz-app folder*
```
poetry run invoke build
```

Start the application with command inside *the quiz-app folder*
```
poetry run invoke start
```

Run the tests and get coverage report with command inside *the quiz-app folder*
```
poetry run invoke coverage-report
```


