class AbstraceFactory(object):
    def getSize(self):
        return Size()
    
    def getColour(self):
        return Colour()

class Size(AbstraceFactory):
    @staticmethod
    def sizeFactory(type):
        if type == 'A4':
            return A4()
        if type == 'A3':
            return A3()

class A4(Size):
    def __init__(self):
        print('A4 \'s size: 297mm * 420mm')

class A3(Size):
    def __init__(self):
        print('A3 \'s size: 297mm * 420mm')

class Colour(AbstraceFactory):
    @staticmethod
    def colorFactory(type):
        if type == 'White':
            return White()
        if type == 'Color':
            return Color()

class White(Colour):
    def __init__(self):
        print('this is a white papper')

class Color(Colour):
    def __init__(self):
        print('this is a color papper')

if __name__ == '__main__':
    abstractFactory = AbstraceFactory()
    types = Size.__subclasses__()
    for type in types:
        size = abstractFactory.getSize().sizeFactory(type.__name__)
    types = Colour.__subclasses__()
    for type in types:
        colour = abstractFactory.getColour().colorFactory(type.__name__)
