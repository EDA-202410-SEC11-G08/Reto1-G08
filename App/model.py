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
sort_algorithm = cus #SE SELECCIONA TIMSORT COMO ALGORITMO POR DEFECTO
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

def sortCountryExperience(catalog, pais, experiencia): # REQUERIMIENTO 1
    """
    Función que soluciona el requerimiento 1
    Ingresar catalogo
    Ingresar codigo de país
    Ingresar experiencia
    
    Lista con todos los trabajos de ese país y experiencia, la cantidad de visualización se resuelve 
    en la impresión de datos
    
    """
    # TODO: Realizar el requerimiento 1
    jobs = catalog["Trabajos"]
    jobsf = lt.newList("ARRAY_LIST")
    for job in lt.iterator(jobs): #Revisar cada oferta de trabajo
        if (cmp_pais_experiencia(job, pais, experiencia) == True):
            lt.addLast(jobsf, job) #Añadir a la nueva lista filtrada si coincide con los criterios
    jobsfsize = lt.size(jobsf)
    if jobsfsize != 0:
        jobsf = sort_algorithm.sort(jobsf, cmp_fecha_publicacion)
        catalog['REQ1'] = jobsf
    return catalog, jobsfsize  
    

def sortCompanyCity(catalog, empresa, ciudad): # REQUERIMIENTO 2
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    jobs = catalog["Trabajos"]
    jobsf = lt.newList("ARRAY_LIST")
    for job in lt.iterator(jobs): #Revisar cada oferta de trabajo
        if (cmp_ciudad_empresa(job, empresa, ciudad) == True):
            lt.addLast(jobsf, job) #Añadir a la nueva lista filtrada si coincide con los criterios
    jobsfsize = lt.size(jobsf)
    if jobsfsize != 0:
        jobsf = sort_algorithm.sort(jobsf, cmp_fecha_publicacion)
        catalog['REQ2'] = jobsf
    return catalog, jobsfsize 

def sortCompanyDateExperience(catalog, empresa, fecha_inicial, fecha_final): # REQUERIMIENTO 3
    """
    Función que soluciona el requerimiento 3
    """
    jobs = catalog["Trabajos"]
    jobsf = lt.newList("ARRAY_LIST")
    for job in lt.iterator(jobs): #Revisar cada oferta de trabajo
        if (cmp_empresa_fecha(job, empresa, fecha_inicial, fecha_final) == True):
            lt.addLast(jobsf, job) #Añadir a la nueva lista filtrada si coincide con los criterios
    jobsfsize = lt.size(jobsf)
    if jobsfsize != 0:
        jobsf = sort_algorithm.sort(jobsf, cmp_fecha_pais)
        catalog['REQ3'] = jobsf
    return catalog, jobsfsize 


def cmp_empresa_fecha(job, empresa, fecha_inicial, fecha_final):
    """
    Compara si la empresa y la fecha de la oferta de trabajo coinciden con los criterios.
    La fecha de la oferta de trabajo debe estar en el rango [fecha_inicial, fecha_final].
    """
    fecha_oferta = date.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    fecha_inicial = date.strptime(fecha_inicial, '%Y-%m-%d')
    fecha_final = date.strptime(fecha_final, '%Y-%m-%d')

    return job['company_name'] == empresa and fecha_inicial <= fecha_oferta <= fecha_final

def cmp_fecha_pais(offer1, offer2):
    """
    Compara la fecha y el país de las ofertas de trabajo.
    Primero compara las fechas, y si son iguales, entonces compara los países.
    """
    date1 = date.strptime(offer1["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date2 = date.strptime(offer2["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")

    if date1 != date2:
        return date1 < date2
    else:
        return offer1['country_code'] < offer2['country_code']


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def sortCityDate(catalog, ciudad, fecha1, fecha2):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    jobs = catalog["Trabajos"]
    jobsf = lt.newList('ARRAY_LIST')
    empresas = {} #Diccionario con nombre de empresa y # de ofertas
    ofertasmax = 0
    empresamax = None
    empresamin = None
    
    for job in lt.iterator(jobs): #Revisar cada oferta de trabajo
        if  (cmp_ciudad_fecha(job, ciudad, fecha1, fecha2) == True): 
            lt.addLast(jobsf, job) #Añadir a la nueva lista filtrada si coincide con los criterios
            
            if job['company_name'] in empresas: #Contador de ofertas por empresa para saber maximo y minimo
                empresas[job['company_name']] += 1 
                if ofertasmax < empresas[job['company_name']]: #Identificar maximo 
                    ofertasmax = empresas[job['company_name']]
                    empresamax = job['company_name']                    
            else:
                empresas[job['company_name']] = 1
    
    for empresa in empresas: # INCLUIR DENTRO DE 1 CICLO FOR NO 2
        if empresas[empresa] <= ofertasmax:
            ofertasmin = empresas[empresa]
            empresamin = empresa
    
    max = (empresamax, ofertasmax)
    if lt.size(jobsf) == 1:
        min = max
    else:
        min = (empresamin, ofertasmin)
    
    jobsfsize = lt.size(jobsf)
    if jobsfsize != 0:
        jobsf = sort_algorithm.sort(jobsf, cmp_fecha_empresa)
        catalog['REQ5'] = jobsf
        
    return catalog, jobsfsize, max, min


def classifyCitiesWithMostJobOffers(N, country_code, experience_level, start_date, end_date): #REQUERIMIENTO 6
    try:
        city_data = loadCityDataFromFile()

        # Ordenar las ciudades por el número de ofertas (de mayor a menor) y luego por el promedio de salario
        sorted_cities = sorted(city_data, key=lambda x: (x['total_offers'], x['average_salary']), reverse=True)

        # Preparar la respuesta con los datos requeridos
        response = {
            "total_cities": len(city_data),
            "total_companies": sum(city['total_companies'] for city in city_data),
            "total_offers": sum(city['total_offers'] for city in city_data),
            "average_salary": sum(city['average_salary'] for city in city_data) / len(city_data),
            "city_with_most_offers": sorted_cities[0]['city_name'],
            "city_with_least_offers": sorted_cities[-1]['city_name'],
            "cities_list": sorted_cities[:N] if len(sorted_cities) > N else sorted_cities
        }

        return response
    except Exception as e:
        # Manejo de errores
        raise e

def loadCityDataFromFile(filename):
    """
    Carga los datos de las ciudades desde un archivo CSV
    """
    city_data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city_data.append({
                "city_name": row['city_name'],
                "total_offers": int(row['total_offers']),
                "average_salary": float(row['average_salary']),
                "total_companies": int(row['total_companies'])
            })
    return city_data


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(offers):
    """
    Calcula el salario promedio de las ofertas con rango salarial
    """
    total_salary = sum((offer["min_salary"] + offer["max_salary"]) / 2 for offer in offers if offer["min_salary"] is not None and offer["max_salary"] is not None)
    num_salary_offers = sum(1 for offer in offers if offer["min_salary"] is not None and offer["max_salary"] is not None)
    if num_salary_offers > 0:
        return total_salary / num_salary_offers
    return None

def country_stats(offers, currency_conversion):
    """
    Calcula las estadísticas de los países y ordena por promedio salarial
    """
    country_data = {}
    for offer in offers:
        country = offer["country"]
        if country not in country_data:
            country_data[country] = {
                "total_offers": 0,
                "total_companies": 0,
                "total_salary_offers": 0,
                "total_fixed_salary_offers": 0,
                "total_no_salary_offers": 0,
                "total_skills": 0,
                "average_salary": None
            }
        country_data[country]["total_offers"] += 1
        if offer["min_salary"] is not None and offer["max_salary"] is not None:
            country_data[country]["total_salary_offers"] += 1
        elif offer["fixed_salary"] is not None:
            country_data[country]["total_fixed_salary_offers"] += 1
        else:
            country_data[country]["total_no_salary_offers"] += 1
        country_data[country]["total_companies"] = len(set(offer["company"] for offer in offers))
        country_data[country]["total_skills"] += offer["skills"]
    
    for country in country_data:
        if country_data[country]["total_salary_offers"] > 0:
            country_data[country]["average_salary"] = calculate_average_salary(offers)
    
    sorted_countries = sorted(country_data.items(), key=lambda x: (x[1]["average_salary"] is None, x[1]["average_salary"]), reverse=True)
    return [{"country": country[0], **country[1]} for country in sorted_countries]

def highest_lowest_salary_countries(country_stats):
    """
    Encuentra el país con el salario promedio más alto y más bajo
    """
    highest_salary_country = None
    lowest_salary_country = None
    for country in country_stats:
        if country["average_salary"] is not None:
            if highest_salary_country is None or country["average_salary"] > highest_salary_country["average_salary"]:
                highest_salary_country = country
            if lowest_salary_country is None or country["average_salary"] < lowest_salary_country["average_salary"]:
                lowest_salary_country = country
    return highest_salary_country, lowest_salary_country

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
        DataSize = "medium-"
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
    
def cmp_pais_experiencia (oferta, pais, experiencia): #Criterio de filtrado REQUERIMIENTO 1
    """ Devuelve verdadero (True) si la empresa de la oferta pertenece al país y experiencia seleccionados
        """
    if (oferta["country_code"] == pais) and (oferta["experience_level"] == experiencia):
        return True
    else: return False
    
def cmp_fecha_publicacion(oferta1, oferta2): #Criterio de ordenamiento de RQ 1 - Fecha de menor a mayor (mas viejo a nuevo)
    if (date.strptime(oferta1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") < date.strptime(oferta2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")):
        return True
    else: return False

def cmp_ciudad_empresa(oferta, empresa, ciudad ): #Criterio de filtrado RQ2
    if (oferta['city'] == ciudad) and (oferta['company_name'] == empresa):
        return True
    else: return False
    
def cmp_ciudad_fecha(oferta, ciudad, fecha1, fecha2): #Criterio de filtrado de RQ 5
    if ((oferta['city'] == ciudad) 
        and (date.strptime(oferta["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") >= date.strptime(fecha1,"%Y-%m-%d"))
        and (date.strptime(oferta["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") <= date.strptime(fecha2,"%Y-%m-%d"))):
        return True
    else: return False

def cmp_fecha_empresa(oferta1, oferta2): #Criterio ordenamiento RQ 5 - Fecha menor a mayor, si igual, nombre de empresa de A-Z
    if (date.strptime(oferta1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") < date.strptime(oferta2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")):
        return True
    elif (date.strptime(oferta1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") == date.strptime(oferta2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")):
        if (oferta1["company_name"] < oferta2["company_name"]):
            return True
        else: return False
    else: return False

 # Funciones de ordenamiento

def setJobSublist(catalog, size):
    """
    Crea una sublista de trabajos del porcentaje indicado
    """
    jobs = catalog["Trabajos"]

    if (float(size) < 100) and (float(size) > 0):
        PercSize = round(lt.size(jobs)*float(size)/100 + 0.5)
        Percmsg = 'Se ha escogido', size,'%, ' + str(PercSize) + ' datos'
    else: 
        Percmsg = 'Se escogió 100% por defecto'
        PercSize = lt.size(jobs)
        
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
