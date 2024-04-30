# Ohjelmistotekniikka, harjoitustyö
This repository is for **Univeristy of Helsinki** course *Ohjelmistotekniikka* and its project work and exercises.

## Quiz Application
The project is a **quiz application**, where users are presented with various questions from different topics such as geography, cities, general knowledge, sports, and others. Each question has four answer options and one correct answer.

## Python version
The project has been built and tested with Python-version 3.10. It is possible that with older versions there might occur problmes.


## Releases
[Week 5 release](https://github.com/mikaelri/ot-harjoitustyo/releases/tag/week5) 
[Week 6 release](https://github.com/mikaelri/ot-harjoitustyo/releases/tag/week6)

## Documentation

[User Manual](https://github.com/mikaelri/ot-harjoitustyo/blob/main/quiz-app/documentation/user_manual.md)

[Requirements Specification](https://github.com/mikaelri/ot-harjoitustyo/blob/main/quiz-app/documentation/requirements_specification.md)

[Architecture](https://github.com/mikaelri/ot-harjoitustyo/blob/main/quiz-app/documentation/architecture.md)

[Change Log](https://github.com/mikaelri/ot-harjoitustyo/blob/main/quiz-app/documentation/change_log.md)

[Hour Tracker](https://github.com/mikaelri/ot-harjoitustyo/blob/main/quiz-app/documentation/hour_tracker.md)

## Installation instructions
Please note that you need to run the following commands inside the **quiz-app** folder.

1. Install the dependencies and requirements with command
```
poetry install
```

2. Create the database and initialize the questions for the quiz with command
```
poetry run invoke create
```

3. Start the application with command
```
poetry run invoke start
```
## Command line commands and testing the application

Please note that you need to run the following commands inside the **quiz-app** folder.

### Starting the application
The application can be started with command:
```
poetry run invoke start
```



### Testing
Activate the virtual environment inside the *quiz-app folder* before running the tests with command
```
poetry shell
```
Run the tests with command
```
poetry run invoke test
```

### Testing coverage
Run the tests when virtual environment is on and get coverage report with command
```
poetry run invoke coverage-report
```

This will create a coverage report to htmlcov folder, which can be opened from terminal after running the tests by clicking `htmlcov/index.html`


### Pylint
The file [.pylintrc](https://github.com/mikaelri/ot-harjoitustyo/blob/main/quiz-app/.pylintrc) has the defined pylint checks, which can be ran with command
```
poetry run invoke lint
```
