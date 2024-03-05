"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import mergesort as mes
from DISClib.Algorithms.Sorting import quicksort as qus
from DISClib.Algorithms.Sorting import customsort as cus
from DISClib.Algorithms.Sorting import heapsort as hes
from DISClib.Algorithms.Sorting import bogosort as bos
from datetime import datetime as date
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""
sort_algorithm = None
# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de ofertas. Crea una lista para la fehca de publicación, la oferta de trabajo, la empresa que da la oferta,
    pais de la oferta y ciudad de la oferta
    """
    catalog = {'Trabajos': None,
               'Tipos': None,
               'Multi Locaciones': None,
               'Habilidades': None}
    # Obtenidos de jobs.csv
    catalog['Trabajos'] = lt.newList('ARRAY_LIST')
    # Obtenidos de employment_types.csv
    catalog['Tipos'] = lt.newList('ARRAY_LIST')
    # Obtenidos de multilocations.csv
    catalog['Multi Locaciones'] = lt.newList('ARRAY_LIST')
    # Obtenidos de skills.csv
    catalog['Habilidades'] = lt.newList('ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al modelo
def addJob(catalog, row):
    lt.addLast(catalog['Trabajos'], row)
    return catalog

def addET(catalog,row):
    lt.addLast(catalog['Tipos'],row) #REVISAR NOMBRE DE KEY 'TIPOS'
    return catalog

def addML(catalog,row):
    lt.addLast(catalog['Multi Locaciones'], row)
    return catalog

def addSkills(catalog, row):
    lt.addLast(catalog['Habilidades'], row)
    return catalog

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass

def JobSize(catalog):
    return lt.size(catalog['Trabajos'])

def ETSize(catalog):
    return lt.size(catalog['Tipos'])

def MLSize(catalog):
    return lt.size(catalog['Multi Locaciones'])

def SkillSize(catalog):
    return lt.size(catalog['Habilidades'])

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

def selectDataSize(algo_opt):
    """
    Función para escoger el tipo de archivo con el que se ejecuta el programa
    """
    #Rta por defecto
    DataSize = 10
    Sizemsg = "Se escogió por defecto la opción 10 - small"
    
    if algo_opt == 1:
        DataSize = "10-por-"
        Sizemsg = "Se ha escogido el tamaño 10-por"
        
    elif algo_opt == 2:
        DataSize = "20-por-"
        Sizemsg = "Se ha escogido el tamaño 20-por"

    elif algo_opt == 3:
        DataSize = "30-por-"
        Sizemsg = "Se ha escogido el tamaño 30-por"

    elif algo_opt == 4:
        DataSize = "40-por-"
        Sizemsg = "Se ha escogido el tamaño 40-por"
        
    elif algo_opt == 5:
        DataSize = "50-por-"
        Sizemsg = "Se ha escogido el tamaño 50-por"
        
    elif algo_opt == 6:
        DataSize = "60-por-"
        Sizemsg = "Se ha escogido el tamaño 60-por"
        
    elif algo_opt == 7:
        DataSize = "70-por-"
        Sizemsg = "Se ha escogido el tamaño 70-por"
        
    elif algo_opt == 8:
        DataSize = "80-por-"
        Sizemsg = "Se ha escogido el tamaño 80-por"
        
    elif algo_opt == 9:
        DataSize = "90-por-"
        Sizemsg = "Se ha escogido el tamaño 90-por"
        
    elif algo_opt == 10:
        DataSize = "small-"
        Sizemsg = "Se ha escogido el tamaño small-"
        
    elif algo_opt == 11:
        DataSize = "meidum-"
        Sizemsg = "Se ha escogido el tamaño medium-"
        
    elif algo_opt == 12:
        DataSize = "large-"
        Sizemsg = "Se ha escogido el tamaño large-"
    return DataSize, Sizemsg
    
def selectSortAlgorithm(algo_opt):
    """selectSortAlgorithm permite seleccionar el algoritmo de ordenamiento
    para la lista de pokemon.

    Args:
        algo_opt (int): opcion de algoritmo de ordenamiento, las opciones son:
            1: Selection Sort
            2: Insertion Sort
            3: Shell Sort
            4: Merge Sort
            5: Quick Sort
            6: Heap Sort
            7: Bogo Sort
            8: Custom Sort (timsort o bucketsort)

    Returns:
        list: sort_algorithm (sort) la instancia del ordenamiento y
        algo_msg (str) el texto que describe la configuracion del ordenamiento
    """
    # respuestas por defecto
    sort_algorithm = 8
    algo_msg = "El algoritmo por defecto es TimSort"

    # selecciona el algoritmo de ordenamiento
    # opcion 1: Selection Sort
    if algo_opt == 1:
        sort_algorithm = ses
        algo_msg = "Seleccionó la configuración - Selection Sort"

    # opcion 2: Insertion Sort
    elif algo_opt == 2:
        sort_algorithm = ins
        algo_msg = "Seleccionó la configuración - Insertion Sort"

    # opcion 3: Shell Sort
    elif algo_opt == 3:
        sort_algorithm = shs
        algo_msg = "Seleccionó la configuración - Shell Sort"

    # opcion 4: Merge Sort
    elif algo_opt == 4:
        sort_algorithm = mes
        algo_msg = "Seleccionó la configuración - Merge Sort"

    # opcion 5: Quick Sort
    elif algo_opt == 5:
        sort_algorithm = qus
        algo_msg = "Seleccionó la configuración - Quick Sort"

    # opcion 6: Heap Sort
    elif algo_opt == 6:
        sort_algorithm = hes
        algo_msg = "Seleccionó la configuración - Heap Sort"

    # opcion 7: Bogo Sort
    elif algo_opt == 7:
        sort_algorithm = bos
        algo_msg = "Seleccionó la configuración - Bogo Sort"

    # opcion 8: Custom Sort, timsort o bucketsort
    elif algo_opt == 8:
        sort_algorithm = cus
        algo_msg = "Seleccionó la configuración - TimSort"
    # respuesta final: algoritmo de ordenamiento y texto de configuracion
    return sort_algorithm, algo_msg

def selectEDType(catalog, EDOp):
    """
    Función para escoger el tipo de archivo con el que se ejecuta el programa
    """
    #Rta por defecto
    EDType = 'SINGLE_LINKED'
    EDmsg = "Se escogió por defecto la opción 2 - SINGLE LINKED LIST"
    
    if EDOp == 1:
        EDType = 'ARRAY_LIST'
        EDmsg = "Se ha escogido: ARRAY LIST"
        
    elif EDOp == 2:
        EDType = 'SINGLE_LINKED'
        EDmsg = "Se ha escogido: SINGLE LINKED LIST"
    
    catalog['Trabajos'] = lt.newList(EDType)
    catalog['Tipos'] = lt.newList(EDType)
    catalog['Multi Locaciones'] = lt.newList(EDType)
    catalog['Habilidades'] = lt.newList(EDType)
    
    return EDmsg

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass
def cmp_ofertas_by_empresa_y_fecha (oferta1, oferta2):     
    """     Devuelve verdadero (True) si la empresa de la oferta1 es menor que en la oferta2,     
    en caso de que sean iguales se analiza la fecha de publicación de la oferta laboral,     
    de lo contrario devuelva falso (False).     
    Args:         
    oferta1: información de la primera oferta laboral que incluye          "company_name" y "published_at"         
    oferta1: información de la segunda oferta laboral que incluye          "company_name" y "published_at"  
    """
    if (oferta1["company_name"] < oferta2["company_name"]):
        return True
    elif (oferta1["company_name"] == oferta2["company_name"]):
         
        if (date.strptime(oferta1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") < date.strptime(oferta2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")):
            return True
        else: return False
    else: return False       
        
# Funciones de ordenamiento

def setJobSublist(catalog, size):
    """
    Crea una sublista de trabajos del porcentaje indicado
    """
    jobs = catalog["Trabajos"]

    if (float(size) <= 100) and (float(size) > 0):
        PercSize = round(lt.size(jobs)*float(size)/100 + 0.5)
        Percmsg = 'Se ha escogido', size,'%, ' + str(PercSize) + ' datos'
    else: 
        Percmsg = 'Se escogió 100% por defecto'
        PercSize = 100
        
    catalog["Trabajos sublist"] = lt.subList(jobs, 1, PercSize)
    return catalog, Percmsg

def sortJobs(catalog):
    sorted_jobs = catalog["Trabajos sublist"]
    sorted_jobs = sort_algorithm.sort(sorted_jobs, cmp_ofertas_by_empresa_y_fecha)
    return sorted_jobs 

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def printTableJobs(catalog, num):
    num += 1
    table1 = []
    table2 = []
    header = ['Oferta','Empresa','Experticia','Publicación','País','Ciudad']
    table1.append(header)
    table2.append(header)
    jobs1 = lt.subList(catalog['Trabajos'], 1, num)
    jobs2 = lt.subList(catalog['Trabajos'], lt.size(catalog['Trabajos'])-num, num)

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
