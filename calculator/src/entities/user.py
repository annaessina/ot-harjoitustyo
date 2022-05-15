class User:
    """Class to describe a user

    Attributes:
        username = username
        password = password       
    """

    def __init__(self, username: str, password: str):
        """Constructor that creates an object of User-class

        Args:
            username (str): username
            password (str): password
        """
        self.username = username
        self.password = password
        
