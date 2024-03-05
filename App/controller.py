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
 """

import config as cf
import model
import time
import csv
import datetime as date

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
Route = None

def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control


# Funciones para la carga de datos

def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    jobs = loadJobs(catalog)
    empType = loadEmploymentTypes(catalog)
    multiLoc = loadMultiLocations(catalog)
    skills = loadSkills(catalog)
    # TODO INCLUIR FUNCION PARA TRANSFORMAR TODAS LAS FECHAS Y CAMBIAR FUNCION DE COMPARACION AL IMPLEMENTAR
    return jobs, empType, multiLoc, skills


def loadJobs(catalog):
    """
    Carga csv jobs
    """
    datefile = cf.data_dir + Route + 'jobs.csv'
    input_file = csv.DictReader(open(datefile, encoding='utf-8'), restval= 'Desconocido', delimiter= ";")
    for row in input_file:
        model.addJob(catalog,row)
    return model.JobSize(catalog)

# Falta extrar info de las filas y añadirlas al catalogo general
def loadEmploymentTypes(catalog):
    """
    Carga csv employment_types
    """
    tagsfile = cf.data_dir + 'small-employments_types.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for row in input_file:  
        model.addET(catalog, row)
    return model.ETSize(catalog)

def loadMultiLocations(catalog):
    """
    Carga csv multilocations
    """
    tagsfile = cf.data_dir + 'small-multilocations.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for row in input_file:
        model.addML(catalog,row)
    return model.MLSize(catalog)

def loadSkills(catalog):
    """
    Carga csv skills
    """
    tagsfile = cf.data_dir + 'small-skills.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for row in input_file:
        model.addSkills(catalog,row)
    return model.SkillSize(catalog)

def     loadTableJobs(control, num):
    catalog = control['model']
    return model.printTableJobs(catalog,num)

def setDataSize(SizeOp):
    """
    Configura que csv se utilizara para la carga de datos
    """
    ans = model.selectDataSize(SizeOp)
    DataSize = ans[0]
    data_msg = ans[1]
    return data_msg, DataSize

def setEDType(control, EDOp):
    """
    Configura que csv se utilizara para la carga de datos
    """
    catalog = control['model']
    EDmsg = model.selectEDType(catalog, EDOp)
    return EDmsg

def setSortAlgorithm(algo_opt):
    """
    Configura el algoritmo de ordenamiento que se va a utilizar en el
    modelo y retorna un mensaje que informa al usuario.
    """
    # TODO nuevo del lab 5 (Parte 2)
    ans = model.selectSortAlgorithm(algo_opt)
    # TODO mirar ojo!!!!
    algorithm = ans[0]
    model.sort_algorithm = algorithm
    algoritm_msg = ans[1]
    return algoritm_msg

# Funciones de ordenamiento
def sortJobs(control):
    """
    Ordena las ofertas por empresa y si es igual, por fecha. Se calcula el tiempo de ordenamiento
    """
    # incluir resutlado en la toma de tiempos
    start_time = get_time()
    sorted_books = model.sortJobs(control["model"])
    end_time = get_time()
    delta = delta_time(start_time, end_time)
    return sorted_books, delta

def setJobSublist(control, size):
    """
    Retorna una sublista de trabajos
    """
    catalog = control["model"]
    ans = model.setJobSublist(catalog, size)
    control["model"] = ans[0]
    Percmsg = ans[1]
    return control, Percmsg

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
