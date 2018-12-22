class Symbol(object):
    def __init__(self, name, type = None):
        self.name = name
        if type:
            self.type = type
