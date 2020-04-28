import csv
from clasealumno import Alumno
class ManejadorAlu:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def testingAlu(self):
        arc=open('Alumnos.csv')
        reader=csv.reader(arc,delimiter=',')
        for fila in reader:
            alu=Alumno(fila[0],fila[1],fila[2],fila[3])
            self.unAlumno(alu)
        arc.close()
    def unAlumno(self,alumno):
        self.__lista.append(alumno)
    def __str__(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i].mostrardatos())
    def buscaAlu(self,año,div,cantmax):
        print('Alumno     Porcentaje')
        for i in range(len(self.__lista)):
            if(self.__lista[i].getAño()==año and self.__lista[i].getDivision()==div):
                if(self.__lista[i].getIna()>cantmax):
                  porcentaje=float(((self.__lista[i].getIna()*100/cantmax)))
                  print('{}       {}'.format(self.__lista[i].getNombre(),porcentaje))
          
