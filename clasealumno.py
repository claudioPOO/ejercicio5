class Alumno:
    __nombre=''
    __año=''
    __divison=''
    __Cantinas=0
    cantMax=25
    cantTC=210
    def __init__(self,nombre,año,division,cantinas):
        self.__nombre=nombre
        self.__año=int(año)
        self.__division=int(division)
        self.__Cantinas=int(cantinas)
    def getAño(self):
        return self.__año
    def getDivision(self):
        return self.__division
    def getNombre(self):
        return self.__nombre
    def getIna(self):
        return self.__Cantinas
    def mostrardatos(self):
        print('{} {} {} {}'.format(self.__nombre,self.__año,self.__division,self.__Cantinas))
    @classmethod
    def getCnt(cls):
        return cls.cantMax
    @classmethod
    def setcantM(cls,tota):
        cls.cantMax=tota
        

