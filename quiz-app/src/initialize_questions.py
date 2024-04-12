from database_connection import get_database_connection
from repositories.quiz_repository import QuizRepository
from entities.quiz import Quiz


def initialize_questions():

    connection = get_database_connection()
    quiz_repository = QuizRepository(connection)

    cursor = connection.cursor()
    cursor.execute("DELETE FROM questions")
    connection.commit()

    questions = [
        Quiz(None, "What is the largest planet in the Solar system",
             ["Mars", "Pluto", "Jupiter", "Venus"], 3),
        Quiz(None, "What is the capital of Finland", [
             "Helsinki", "Stockholm", "Oslo", "Turku"], 1),

    ]
    # To be updated with more questions

    for quiz in questions:
        quiz_repository.create_question(quiz)


if __name__ == "__main__":
    initialize_questions()
    print("Questions initialized for the quiz!")
