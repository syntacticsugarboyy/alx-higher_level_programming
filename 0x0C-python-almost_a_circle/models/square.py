#!/usr/bin/python3
'''
    And now, the Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Square that inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' 
            Initializes a Square
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
            str
        '''
        s = '[Square] ({:d}) {:d}/{:d} - {:d}'
        return (s.format(self.id, self.__x, self.__y, self.__width))

    @property
    def size(self):
        '''
            Getter
        '''
        return self.size

    @size.setter
    def size(self, value):
        '''
            Sets size
        '''
        self.__width = value
        self.__height = value

	 def update(self, *args, **kwargs):
        '''
            Update
        '''
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
