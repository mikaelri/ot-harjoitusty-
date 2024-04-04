# Ohjelmistotekniikka, harjoitustyö

This repository is for **Univeristy of Helsinki** course *Ohjelmistotekniikka* and its project work and exercises.

Link to the laskarit folder for exercises: [Laskarit](https://github.com/mikaelri/ot-harjoitustyo/tree/main/laskarit)

Please note that the repository will be updated during the spring of 2024.

## Quiz Application

The project is a **quiz application**, where users are presented with various questions from different topics such as geography, cities, general knowledge, sports, and others. Each question has four answer options and one correct answer.

## Requirements Specification

Link to the requirements specification [Vaatimusmaarittely](https://github.com/mikaelri/ot-harjoitustyo/tree/main/documentation/vaatimusmaarittely.md)

## Tracking of the working hours

Link to the requirements specification [tyoaikakirjanpito](https://github.com/mikaelri/ot-harjoitustyo/tree/main/documentation/tyoaikakirjanpito.md)

## Installation instructions
Install the dependencies and requirements with command
```
poetry install
```
## User guide and testing the application after installation

Create the database with command
```
poetry run invoke build
```

Start the application with command
```
poetry run invoke start
```

Run the tests with command
```
poetry run invoke coverage
```


