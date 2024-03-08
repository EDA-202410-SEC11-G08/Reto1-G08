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
    print("\nBienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("Funciones para Lab 5-----------------")
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

def print_req_1(list, num):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    table = []
    header = ['Publicación','Oferta','Empresa','Experticia','País','Ciudad','Tamaño','Ubicación','Contratar Ucranianos']
    table.append(header)
    jobs = lt.subList(list, lt.size(list)-num, num)

    for job in lt.iterator(jobs):
        table.append([job['published_at'],
        job['title'],
        job['company_name'],
        job['experience_level'],
        job['country_code'],
        job['city'],
        job['company_size'],
        job['workplace_type'],
        job['open_to_hire_ukrainians']])
        
    return table


def print_req_2(list, num):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    table = []
    header = ['Publicación','País','Ciudad','Empresa','Oferta','Experticia','Formato de aplicación','Tipo']
    table.append(header)
    jobs = lt.subList(list, lt.size(list)-num, num)

    for job in lt.iterator(jobs):
        table.append([job['published_at'],
        job['country_code'],
        job['city'],
        job['company_name'],
        job['title'],
        job['experience_level'],
        job['company_url'],
        job['workplace_type']])
        
    return table



def print_req_3(list, num):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    table = []
    header = ['Publicación','Oferta','Experticia','Ciudad','País','Tamaño','Ubicación','Contratar Ucranianos']
    table.append(header)
    jobs = lt.subList(list, lt.size(list)-num, num)

    for job in lt.iterator(jobs):
        table.append([job['published_at'],
        job['title'],
        job['experience_level'],
        job['city'],
        job['country_code'],
        job['company_size'],
        job['workplace_type'],
        job['open_to_hire_ukrainians']])
        
    return table

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(list, num):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    table1 = []
    table2 = []
    header = ['Publicación','Oferta','Empresa','Tamaño','Ubicación']
    table1.append(header)
    table2.append(header)
    jobs1 = lt.subList(list, 1, num)
    jobs2 = lt.subList(list, lt.size(list)-num, num)

    for job in lt.iterator(jobs1):
        table1.append([job['published_at'],
        job['title'],
        job['company_name'],
        job['company_size'],
        job['workplace_type']])  

    for job in lt.iterator(jobs2):
        table2.append([job['published_at'],
        job['title'],
        job['company_name'],
        job['company_size'],
        job['workplace_type']])      
        
    return table1, table2


def classifyCitiesWithMostJobOffers(control): #REQUERIMIENTO 6
    try:
        N = int(input("Ingrese el número de ciudades para consulta: "))
        country_code = input("Ingrese el código del país (opcional, dejar en blanco para consultar todas las ciudades): ")
        experience_level = input("Ingrese el nivel de experiencia de las ofertas (junior, mid o senior): ")
        start_date = input("Ingrese la fecha inicial del periodo a consultar (formato YYYY-MM-DD): ")
        end_date = input("Ingrese la fecha final del periodo a consultar (formato YYYY-MM-DD): ")

        result = controller.classifyCitiesWithMostJobOffers(control, N, country_code, experience_level, start_date, end_date)
        
        # Presenta el resultado al usuario de acuerdo con el formato especificado en el requerimiento
        print("Total de ciudades:", result["total_cities"])
        print("Total de empresas:", result["total_companies"])
        print("Total de ofertas publicadas:", result["total_offers"])
        if country_code:
            print("Promedio del salario ofertado:", result["average_salary"])
        print("Ciudad con mayor cantidad de ofertas:", result["city_with_most_offers"])
        print("Ciudad con menor cantidad de ofertas:", result["city_with_least_offers"])
        print("Listado de ciudades:")
        print(tabulate(result["cities_list"], headers="keys"))
    except Exception as e:
        print("Ocurrió un error al clasificar las ciudades con mayor número de ofertas de trabajo:", e)

def print_req_7(control, maxreq7, minreq7, size, promedio):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    i = 0
    print("El total de ofertas de empleo:",size[0]) #Total de ofertas en los paises seleccionados
    print("Número de ciudades donde se ofertó en los países resultantes", size[1])
    print("País con mayor cantidad de ofertas:",maxreq7[0][0],",",maxreq7[0][1])
    print("Ciudad con mayor cantidad de ofertas:",maxreq7[1][0],",",maxreq7[1][1])
    exp = ["junior","mid","senior"]
    for lvl in exp:
        print("\nPara",lvl,"----------------------")
        print("Número de habilidades:",size[2][i])
        print("La habilidad más solicitada es",maxreq7[3][0][i],"-",maxreq7[3][1][i])
        print("La habilidad menos solicitada es",minreq7[1][0][i],"-",minreq7[1][1][i])
        print("Nivel promedio de habilidades",promedio[i])
        print("Conteo de empresas que publicaron una oferta en este nivel:",size[3+i])
        print("Empresa con mayor número de ofertas:",maxreq7[2][0][i],"-", maxreq7[2][1][i])
        print("Empresa con menor número de ofertas:",minreq7[0][0][i],"-", minreq7[0][1][i])        
        print("Número de empresas con una o más sedes:", size[6][i])
        i += 1

    
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(country_stats, highest_salary_country, lowest_salary_country):
    """
    Imprime el resultado del Requerimiento 8
    """
    print("Estadísticas Generales:")
    print(f"Total de empresas: {country_stats['total_companies']}")
    print(f"Total de ofertas de empleo: {country_stats['total_offers']}")
    print(f"Número de países: {len(country_stats)}")
    # Otras estadísticas generales
    print("Lista de países por promedio salarial:")
    for country in country_stats:
        print(f"- {country['country']}: Promedio Salarial: {country['average_salary']}")
    print("Países con Mayor y Menor Oferta Salarial:")
    print(f"Mayor Oferta Salarial: {highest_salary_country['country']}")
    print(f"Menor Oferta Salarial: {lowest_salary_country['country']}")


def printTableJobs(list, num):
    table1 = []
    table2 = []
    header = ['Oferta','Empresa','Experticia','Publicación','País','Ciudad']
    table1.append(header)
    table2.append(header)
    jobs1 = lt.subList(list, 1, num)
    jobs2 = lt.subList(list, lt.size(list)-num, num)

    for job in lt.iterator(jobs1):
        table1.append([job['title'],
        job['company_name'],
        job['experience_level'],
        job['published_at'],
        job['country_code'],
        job['city']])

    for job in lt.iterator(jobs2):
        table2.append([job['title'],
        job['company_name'],
        job['experience_level'],
        job['published_at'],
        job['country_code'],
        job['city']])
        
    return table1, table2
    

    
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
Req1OP = """Seleccione un nivel de experiencia
                junior
                mid
                senior
"""
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
        if int(inputs) == 1: #CARGA DE DATOS ------------------------------------------------------------------------------------------------
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
            table1, table2 = printTableJobs(control["model"]["Trabajos"], int(num))
            print('Primeras ' + str(num) + " Ofertas")
            print(tabulate(table1))
            print('Ultimas ' + str(num) + " Ofertas")
            print(tabulate(table2))
            
        elif int(inputs) == 2: #REQUERIMIENTO 1 ---------------------------------------------------------------------------------------------
            pais = input('Por cúal país desea filtrar?\nIngresar código de país\n')
            experiencia = input (Req1OP)
            ans = controller.setCountryExperience(control, pais, experiencia)
            control = ans[0]
            req1size = ans[1]
            DeltaTime = f"{ans[2]:.3f}"         

            if req1size == 0:
                print("País o experiencia invalido")
            else: 
                print("Para filtrar y organizar", req1size, "ofertas, el tiempo es:", str(DeltaTime), "[ms]")                
                num = input('Cuantas ofertas desea visualizar ')
                table = print_req_1(control['model']['REQ1'], int(num))             
                print('Ultimas ' + str(num) + " Ofertas")
                print(tabulate(table))           

        elif int(inputs) == 3: #REQUERIMIENTO 2 ---------------------------------------------------------------------------------------------
            empresa = input('Cúal empresa desea filtrar?\n')
            ciudad = input('Cúal ciudad desea filtrar?\n')
            
            ans = controller.setCompanyCity(control, empresa, ciudad)
            control = ans[0]
            req2size = ans[1]
            DeltaTime = f"{ans[2]:.3f}"         

            if req2size == 0:
                print("Empresa o ciudad invalida")
            else: 
                print("Para filtrar y organizar", req2size, "ofertas, el tiempo es:", str(DeltaTime), "[ms]")                
                num = input('Cuantas ofertas desea visualizar ')
                table = print_req_2(control['model']['REQ2'], int(num))             
                print('Ultimas ' + str(num) + " Ofertas")
                print(tabulate(table))            

        elif int(inputs) == 4: # Requerimiento 3 --------------------------------------------------------------------------------------------
            empresa = input('¿Cuál empresa desea filtrar?\n')
            fecha_inicial = input('Ingrese la fecha inicial (formato "%Y-%m-%d")\n')
            fecha_final = input('Ingrese la fecha final (formato "%Y-%m-%d")\n')
    
            ans = controller.setCompanyDateExperience(control, empresa, fecha_inicial, fecha_final)
            control = ans[0]
            req3size = ans[1]
            DeltaTime = f"{ans[2]:.3f}"         

            if req3size == 0:
                print("Empresa o rango de fechas inválido")
            else: 
                print("Para filtrar y organizar", req3size, "ofertas, el tiempo es:", str(DeltaTime), "[ms]")                
                num = input('¿Cuántas ofertas desea visualizar? ')
                table = print_req_3(control['model']['REQ3'], int(num))             
                print('Últimas ' + str(num) + " Ofertas")
                print(tabulate(table))

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6: #REQUERIMIENTO 5 ---------------------------------------------------------------------------------------------

            ciudad = input("Que ciudad desea consultar?\n")
            fecha1 = input("En que fecha desea iniciar? formato YYYY-MM-DD\n")
            fecha2 = input("En que fecha desea terminar? formato YYYY-MM-DD\n")
            
            ans = controller.setCityDate(control, ciudad, fecha1, fecha2) #FILTRADO Y ORGANIZAR
            control = ans[0]
            req5size = ans[1]
            DeltaTime = f"{ans[2]:.3f}"  
            maxreq5, minreq5 = ans[3], ans[4]    
            
            if req5size == 0: #Si la lista regresa vacia, hubo problemas de filtrado
                print("Ciudad o fechas invalidas")   
            else:
                print("Se encontraron", req5size,"ofertas entre las fechas", fecha1,"y",fecha2)
                print("Para filtrar y organizar", req5size, "ofertas, el tiempo es:", str(DeltaTime), "[ms]")  #Cantidad de ofertas   
                print("La empresa con mayor ofertas es",maxreq5[0],"con",str(maxreq5[1]),"ofertas")
                print("La empresa con menor ofertas es",minreq5[0],"con",str(minreq5[1]),"ofertas")
                
                num = input('Cuantas ofertas desea visualizar ')
                table1, table2 = print_req_5(control['model']['REQ5'], int(num))             
                print('Primeras ' + str(num) + " Ofertas")
                print(tabulate(table1))
                print('Ultimas ' + str(num) + " Ofertas")
                print(tabulate(table2))

        elif int(inputs) == 7:
            classifyCitiesWithMostJobOffers(control)

        elif int(inputs) == 8: # REQUERIMIENTO 7 --------------------------------------------------------------------------------------
            num = input('Cuantos paises desea consultar?')
            fecha1 = input("En que fecha desea iniciar? formato YYYY-MM-DD\n")
            fecha2 = input("En que fecha desea terminar? formato YYYY-MM-DD\n")
            
            ans = controller.req_7(control, fecha1, fecha2, num)
            control = ans[0]
            size = ans[1]
            DeltaTime = f"{ans[2]:.3f}"  
            maxreq7, minreq7 = ans[3], ans[4]            
            promedio = ans[5]
            print("El Tiempo es:", str(DeltaTime), "[ms]")  #Cantidad de ofertas   
            print_req_7(control, maxreq7, minreq7, size, promedio)

        elif int(inputs) == 9:
            print_req_8(control)
        
        elif int(inputs) == 10:
            algo_opt = input(SortOp)
            algo_opt = int(algo_opt)
            algo_msg = controller.setSortAlgorithm(algo_opt)
            print(algo_msg)
        
        elif int(inputs) == 11:
            
            size = input("Que porcentaje de datos desea ver?")
            size = float(size)
            ans = controller.setJobSublist(control, size)
            control = ans[0]
            Percmsg = ans[1]
            print(Percmsg)
            
            print("Ordenando las ofertas ....")         
            result = controller.sortJobs(control)         
            sortedJobs = result[0]         
            DeltaTime = f"{result[1]:.3f}"         
            print("Para", lt.size(sortedJobs), "elementos, el tiempo es:",               
              str(DeltaTime), "[ms]")        
             
            num = input('Cuantas ofertas desea visualizar ')
            table1, table2 = printTableJobs(sortedJobs, int(num))             
            print('Primeras ' + str(num) + " Ofertas")
            print(tabulate(table1))
            print('Ultimas ' + str(num) + " Ofertas")
            print(tabulate(table2))


        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
