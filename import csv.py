import csv
from tabulate import tabulate

csv.list_dialects()

lista = []
csv.Dialect.delimiter = ";"
booksfile = 'data/data/small-jobs.csv'
csv.Dialect.quotechar = "'"
fieldnames = ["title","street","city","country_code","address_text","marker_icon","workplace_type","company_name","company_url",
              "company_size","experience_level","published_at","remote_interview","open_to_hire_ukrainians","id","display_offer"]
input_file = csv.DictReader(open(booksfile, encoding='utf-8'), fieldnames = fieldnames, restval= 'Desconocido')
for row in input_file:
    lista.append(row["published_at"])
print(lista)

