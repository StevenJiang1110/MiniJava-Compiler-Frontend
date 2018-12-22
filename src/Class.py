from ScopeMixin import ScopeMixin
from Symbol import Symbol


class Class(Symbol, ScopeMixin):

    def __init__(self, className, parentName, parentScope):
        Symbol.__init__(self, className)
