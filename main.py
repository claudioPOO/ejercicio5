from manejadoralu import ManejadorAlu
from clasealumno import Alumno

def  opcion0 (alumno):
    print( "Adiós" )
def  opcion1 (alumno):
   año=int(input('Año '))
   div=int(input('Division '))
   cant=int(Alumno.getCnt())
   alumno.buscaAlu(año,div,cant)
def  opcion2 (alumno):
    print(Alumno.getCnt())
    nueva=int(input('Cantidad de inasistencias maximas '))
    Alumno.setcantM(nueva)

switcher = {
    0 : opcion0,
    1 : opcion1,
    2 : opcion2,  
}

def switch (argumento,alumno):
    func  =  switcher.get ( argumento , lambda : print ( "Opción incorrecta" ))
    func (alumno)

if __name__ == '__main__':
 alumno=ManejadorAlu()
 alumno.testingAlu()
 alumno.__str__()
 bandera='falso'
 while bandera=='falso':
     print('')
     print ( "      Menu" )
     print ( " 0 Salir" )
     print ( " 1 Listado y porcentaje" )
     print ( ' 2 Modificar cantidad maxima de inasistencias')
     opcion =  int ( input ( "Ingrese una opción:" ))
     switch(opcion,alumno)
     op=(input('Desea Continuar? '))
     if(op=='no'):
         bandera='verdadero'
 
