Class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setaddr__(self, name ,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            super().__setaddr__(name, value)
            #self.__dict__[name]=value

    def getArea(self):
        return self.width * self.height