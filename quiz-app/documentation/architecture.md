## Project overall, high-level structure

![Overall structure](./pictures/overalldiagram.png)

## Project packaging class structure
Ui uses the classes from services layer (UserServices, QuestionServices) for the application logic.

Services uses classes from repositories layer (UserRepository, QuestionRepository) to get the user and question data to application logic and for processing it. Services is also using Entities classes i.e. for user login.

Repositories uses entities classes in data processing.

Entities are the data models, representing the data structure in the application.<br>
Entities class User can have multiple questions as well as the Questions class can have multiple users.

![Packaging structure](./pictures/packagingdiagram.png)