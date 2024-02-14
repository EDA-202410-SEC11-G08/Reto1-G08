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
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de ofertas. Crea una lista para la fehca de publicación, la oferta de trabajo, la empresa que da la oferta,
    pais de la oferta y ciudad de la oferta
    """
    catalog = {'Publicación': None,
               'Oferta': None,
               'Empresa': None,
               'Experticia': None,
               'País': None,
               'Ciudad': None}
    # Obtenidos de jobs.csv
    catalog['Publicación'] = lt.newList('ARRAY_LIST')   #ESTRUCTURA DE DATO ESCOGIDA AL AZAR CAMBIAR
    catalog['Oferta'] = lt.newList('ARRAY_LIST')
    catalog['Empresa'] = lt.newList('ARRAY_LIST')
    catalog['Experticia'] = lt.newList('ARRAY_LIST')
    catalog['País'] = lt.newList('SINGLE_LINKED')
    catalog['Ciudad'] = lt.newList('SINGLE_LINKED')
    # Obtenidos de employment_types.csv
    catalog['Tipos'] = lt.newList('SINGLE_LINKED')
    # Obtenidos de multilocations.csv
    catalog['Multi Locaciones'] = lt.newList('SINGLE_LINKED')
    # Obtenidos de skills.csv
    catalog['Habilidades'] = lt.newList('SINGLE_LINKED')
    return catalog

# Funciones para agregar informacion al modelo

def addDate(catalog, row):
    lt.addLast(catalog['Publicación'], row)
    return catalog

def addJob(catalog, row):
    lt.addLast(catalog['Oferta'], row)
    return catalog

def addCompany(catalog, row):
    lt.addLast(catalog['Empresa'], row)
    return catalog

def addExp(catalog, row):
    lt.addLast(catalog['Experticia'], row)
    return catalog

def addCountry(catalog, row):
    lt.addLast(catalog['País'], row)
    return catalog

def addCity(catalog, row):
    lt.addLast(catalog['Ciudad'], row)
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
    return lt.size(catalog['Oferta'])

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


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


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

def printTable(catalog, num):
    num += 1
    table = []
    header = ['Oferta','Empresa','Experticia','Publicación','País','Ciudad']
    table.append(header)

    for i in range(1,num+1):
        table.append([lt.getElement(catalog['Oferta'],i),
                        lt.getElement(catalog['Empresa'],i),
                        lt.getElement(catalog['Experticia'],i),
                        lt.getElement(catalog['Publicación'],i),
                        lt.getElement(catalog['País'],i),
                        lt.getElement(catalog['Ciudad'],i)])
    
    return table
