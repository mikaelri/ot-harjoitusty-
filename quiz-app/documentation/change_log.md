## Week3
- Added UI view
- Added and tested UserRepository class, which handles saving the new users to SQLite database
- Added and tested UserService class, which handles the user interface for creating a new user
- New user can be created and it is stored to database
- User can see user page after login
- User can logout
  
## Week4
- Added questions table, created initialized questions for the new table and tested the initialization of questions in database
- Added and tested QuestionRepository class, which handles saving the new questions to SQLite database
- Added and tested features for QuestionService class, which handles the user interface for the quiz app (created features as of now, might be necessary to add some more functions later, which will be also tested accordingly)
- User has a view to see all of the multiple choice questions and options (to be updated to show them question by question)
  
## Week5
- Added and tested new features for user playing the quiz for QuestionService and QuestionRepository classes (checking answers, adding points, getting points)
- User can see the questions one by one in random order and answer these, correct answer will increase the quiz points by +1 and incorrect does not increase, this is saved to the database.
- User can see the total points of the quiz once all of the questions are answered
  
## Week5
- User can see the current highscore before starting the quiz, which is replaced by quiz points if those will be higher.
- User can see highscores of the top 3 users in the same computer
- Added highscore column to the database and added and tested the related logic to question services and database changes to question repositories.