"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback
import threading


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def print_menu():
    print("commit")
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Escoger algoritmo de ordenamiento")
    print("11- Ordenar datos")
    print("0- Salir")


def loadData(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    jobs, empType, multiLoc, skills = controller.loadData(control)
    return jobs, empType, multiLoc, skills


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

    
def printSortResults(sort_jobs, sample):     # TODO completar funcion para imprimir resultados sort lab 5     
    size = lt.size(sort_jobs)     
    if size <= sample*2:         
        print("Las", size, "ofertas ordenadas son:")         
        for job in lt.iterator(sort_jobs):             
            print('Oferta: ' + job['title'] + ' Empresa: ' + job['company_name'] + 
                  ' Experticia: ' + job['experience_level'] + 
                    ' Publicación: ' + job['published_at'] + ' País: '+ job['country_code'] + ' Ciudad: ' + job['city'])      
    else:    
             
        print("Las", sample, "primeras ofertas ordenadas son:")         
        i = 1
                 
        while i <= sample:             
            job = lt.getElement(sort_jobs, i)             
            print('Oferta: ' + job['title'] + ' Empresa: ' + job['company_name'] + 
                  ' Experticia: ' + job['experience_level'] + 
                    ' Publicación: ' + job['published_at'] + ' País: '+ job['country_code'] + ' Ciudad: ' + job['city'])             
            i += 1  
            
        print("Las", sample, "últimas ofertas ordenadas son:")         
        i = size - sample + 1        
        
        while i <= size:            
            job = lt.getElement(sort_jobs, i)           
            print('Oferta: ' + job['title'] + ' Empresa: ' + job['company_name'] + 
                  ' Experticia: ' + job['experience_level'] + 
                    ' Publicación: ' + job['published_at'] + ' País: '+ job['country_code'] + ' Ciudad: ' + job['city'])             
            i += 1 
# Se crea el controlador asociado a la vista
control = newController()
# Variables utiles para el programa
EDOPStr = """Seleccione el tipo de estructura para guardar los datos:
                1. ARRAY LIST
                2. SINGLE LINKED LIST
"""
SizeOpStr = """Seleccione el tamaño de CSV a cargar:
                 1. 10-por ||
                 2. 20-por ||
                 3. 30-por ||
                 4. 40-por ||
                 5. 50-por ||
                 6. 60-por ||
                 7. 70-por ||
                 8. 80-por ||
                 9. 90-por ||
                 10. small ||
                 11. medium||
                 12. large ||
                 """
                 
SortOp = """Seleccione el algoritmo de ordenamiento:
                1. Selection Sort ||
                 2. Insertion Sort ||
                 3. Shell Sort ||
                 4. Merge Sort ||
                 5. Quick Sort ||
                 6. Heap Sort ||
                 7. Bogo Sort ||
                 8. TimSort (custom):"""


# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            # Definir el tipo de ED donde se cargan los archivos
            print('Como desea guardar los datos?\n')
            EDOp = input(EDOPStr)
            EDOp = int(EDOp)
            EDmsg = controller.setEDType(control, EDOp)
            print(EDmsg)
            
            # Definir que archivos csv se van a utilizar para cargar datos
            print("Que datos desea cargar?\n")
            SizeOp = input(SizeOpStr)
            SizeOp = int(SizeOp)
            Sizemsg, DataSize = controller.setDataSize(SizeOp)      
            controller.Route = DataSize    
            print(Sizemsg) 
            
            # Presenta la cantidad de datos cargados
            print("Cargando información de los archivos ....\n")
            jobs, empType, multiLoc, skills = loadData(control)
            print('Ofertas cargadas: '+ str(jobs))
            print('Tipos de empleos cargados '+ str(empType))
            print('Multilocaciones cargadas '+ str(multiLoc))
            print('Habilidades cargadas '+ str(skills))
            
            num = input('Cuantas ofertas desea visualizar ')
            table1, table2 = controller.loadTableJobs(control, int(num)-1)
            print('Primeras ' + str(num) + " Ofertas")
            print(tabulate(table1))
            print('Ultimas ' + str(num) + " Ofertas")
            print(tabulate(table2))
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)
        
        elif int(inputs) == 10:
            algo_opt = input(SortOp)
            algo_opt = int(algo_opt)
            algo_msg = controller.setSortAlgorithm(algo_opt)
            print(algo_msg)
        
        elif int(inputs) == 11:
            print("Ordenando las ofertas ....")         
            result = controller.sortJobs(control)         
            sortedJobs = result[0]         
            DeltaTime = f"{result[1]:.3f}"         
            print("Para", jobs, "elementos, el tiempo es:",               
              str(DeltaTime), "[ms]")         
            sample = input("Cuantas ofertas desea visualizar?\n")
            printSortResults(sortedJobs, int(sample))


        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
