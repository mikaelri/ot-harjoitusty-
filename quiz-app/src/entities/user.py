class User:
    """Class for the users.

    Attributes:
        username:
            user's username as a string variable
        password:
            user's password as a string variable
    """

    def __init__(self, username: str, password: str):
        """Constructor for the class.
        Args:
            username:
                user's username as a string variable
            password:
                user's password as a string variable
        """
        self.username = username
        self.password = password


class UserStats:
    """Class for the users' stats.

    Attributes:
        username:
            identifier for the user
        quiz_points:
            points from the quiz for the user
    """

    def __init__(self, username: int, quiz_points: int = 0):
        """Constructor for the users' stats.

        Args:
            username:
                identifier for the user
            quiz_points:
                points from the quiz for the user
        """
        self.user_id = username
        self.quiz_points = quiz_points
