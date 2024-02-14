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

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


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
    
    return jobs, empType, multiLoc, skills


def loadJobs(catalog):
    """
    Carga csv jobs
    """
    datefile = cf.data_dir + 'data/small-jobs.csv'
    input_file = csv.DictReader(open(datefile, encoding='utf-8'), restval= 'Desconocido')
    for row in input_file:
        
        model.addDate(catalog, row['published_at'])    
        model.addJob(catalog, row['title'])   
        model.addCompany(catalog, row['company_name'])
        model.addExp(catalog, row['experience_level'])
        model.addCountry(catalog, row['country_code'])
        model.addCity(catalog, row['city'])
        
    return model.JobSize(catalog)

# Falta extrar info de las filas y añadirlas al catalogo general
def loadEmploymentTypes(catalog):
    """
    Carga csv employment_types
    """
    tagsfile = cf.data_dir + 'data/small-employments_types.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    return model.ETSize(catalog)

def loadMultiLocations(catalog):
    """
    Carga csv multilocations
    """
    tagsfile = cf.data_dir + 'data/small-multilocations.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    return model.MLSize(catalog)

def loadSkills(catalog):
    """
    Carga csv skills
    """
    tagsfile = cf.data_dir + 'data/small-skills.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    return model.SkillSize(catalog)

def loadTable(control, num):
    catalog = control['model']
    return model.printTable(catalog,num)
# Funciones de ordenamiento

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
