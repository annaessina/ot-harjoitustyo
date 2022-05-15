class Record:
    """Class that decribes new record object"""

    def __init__(self, number1: float, number2: float, add2: float, dist: float, mult: float, div: float, username: str):
        """Creates new object of Record-class

        Args:
            number1 (float): first entered number
            number2 (float): second entered number
            add2 (float): result of addition
            dist (float): result of distraction
            mult (float): result of multiplication
            div (float): result of division
            username (str): username of current user
        """
        self.number1 = number1
        self.number2 = number2
        self.add2 = add2
        self.dist = dist
        self.mult = mult
        self.div = div
        self.username = username