class User:
    """Class for the users.

    Attributes:
        username:
            User's username as a string variable.
        password:
            User's password as a string variable.
    """

    def __init__(self, username: str, password: str):
        """Constructor for the class, data model of the User object.

        Args:
            username:
                User's username as a string variable.
            password:
                User's password as a string variable.
        """

        self.username = username
        self.password = password


class UserStats:
    """Class for the users' stats.

    Attributes:
        username:
            User's username as a string variable, identifier of the user.
        quiz_points:
            Points from the quiz for the user object.
        highscore:
            Highest score of the quiz for the user object.
    """

    def __init__(self, username: str, quiz_points: int = 0, highscore: int = 0):
        """Constructor for the class, data model of the UserStats object.

        Args:
            username:
                User's username as a string variable, identifier of the user.
            quiz_points:
                Points from the quiz for the user object.
            highscore:
                Highest score of the quiz for the user object.
        """
        self.username = username
        self.quiz_points = quiz_points
        self.highscore = highscore
