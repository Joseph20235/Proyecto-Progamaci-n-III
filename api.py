import pandas as pd
from sodapy import Socrata
def consultar_datos(departamento, limite_registros):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit=limite_registros, departamento_nom=departamento)
    return results
