
class Jeu:
    def __init__(self, name, image):
        self.__name = name
        self.__image = image
        self.__tags=set()
    
    @property 
    def tags(self):
        return self.__tags
    def addTags(self, tag):
        self.__tags.add(tag)
       
      
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        self.__name=newName
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, newimage):
        self.__image=newimage
    
    def __repr__(self):
        return f'{self.__name}: {self.__image}'
            
    def __eq__(self, __value: object):
        self.ç__name=__value.name


