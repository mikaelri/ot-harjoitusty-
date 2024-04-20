# Requirements specification

## Purpose of the application
The project is a **quiz application**, where users are presented with various questions from different topics such as geography, cities, general knowledge, sports, and others. Each question has four answer options and one correct answer.

## Users and user roles
The project has only one user type, which is a *normal user* who can try to guess the correct answers.

It is possible that admin user is added to the application later. 

Admin user could add new questions to the quiz or handle user management.

## Planned functionalities

✅ Feature done<br>
⏳ Feature in progress<br>
❌ Feature or part of it not started

### Before login
* User can create a new user ✅ 
  * Application has requirements for username and password ✅
  
* User can login to the applicaiton ✅ 
  * Login is handled via a login form in the front page ✅
    * If the username is not created, message is displayed to the user ✅
    * If the username and or password is incorrect, message is displayed to the user✅
  
### After login
* User can start a new quiz ⏳
  * User sees the question (fixed/limited amount) and four options (generated randomly and in random order) ✅
  * User can select an option and submit it ✅
  * Application tells if the users answer was correct or wrong ❌
  * Application keeps score of the users points and at the end shows the total score ✅
* User can see highscores of the same users in same computer ❌
* User can logout ✅ 

## Further development

The following are some ideas for the future and further development for the application:
* Add admin user who can create new questions
* Use artificial intelligence to generate the questions
* Deleting the user account