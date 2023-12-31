from aka_food.core import Error


class AkaFoodError(Error):
    _message = None

    def __str__(self):
        if self._message is not None:
            return f'{self.__class__.__name__}: {self._message}'
        else:
            return f'{self.__class__.__name__}: ERROR '


class AkaFoodDbConnectionError(AkaFoodError):
    """ Cannot connect to DB """

    def __init__(self, *args):
        if args:
            self._message = f"DB connection error: {args[0]}"
        else:
            self._message = f"DB connection error"
