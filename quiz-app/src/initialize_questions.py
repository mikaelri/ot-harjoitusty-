from sqlite3 import DatabaseError
from database_connection import get_database_connection
from repositories.question_repository import QuestionRepository
from entities.quiz import Quiz


def initialize_questions(connection=None, question_repository=None) -> object:

    if connection is None:
        connection = get_database_connection()

    if question_repository is None:
        question_repository = QuestionRepository(connection)

    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM questions")
        connection.commit()

        questions = [
            Quiz(None, "What is the largest planet in the Solar system?",
                 ["Mars", "Pluto", "Jupiter", "Venus"], 3),

            Quiz(None, "What is the capital of Australia?", [
                "Perth", "Sidney", "Canberra", "Melbourne"], 3),

            Quiz(None, "Who won the icehockey World cup in 1995?", [
                "USA", "Sweden", "Finland", "Canada"], 3),

            Quiz(None, "In what year Finland participated in the football European cup?", [
                "1992", "2002", "2022", "2021"], 4),

            Quiz(None, "In what year Finland won the Eurovision song contest?", [
                "1996", "1998", "2012", "2006"], 4),

            Quiz(None, "What is the largest lake in Finland?", [
                "Päijänne", "Saimaa", "Oulujärvi", "Inarijärvi"], 2),
        ]

        for quiz in questions:
            question_repository.create_question(quiz)
        print('Questions initialized for the quiz')

    except DatabaseError as error:
        print(f'Error: {error}')
        connection.rollback()


if __name__ == "__main__":
    initialize_questions()
