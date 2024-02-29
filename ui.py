def solicitar_datos():
    departamento = input("Digite el nombre del departamento que desea consultar (en MAYUSCULAS): ")
    limite_registros = int(input("Digite el número de registros que desea obtener: "))
    return departamento, limite_registros

def imprimir_datos(datos):
    print("{:<20} {:<20} {:<10} {:<20} {:<10} {:<20}".format(
        'Ciudad de ubicación',
        'Nombre departamento',
        'Edad',
        'Tipo de contagio',
        'Estado',
        'Nombre del país'
    )
    )
    for registro in datos:
        print("{:<20} {:<20} {:<10} {:<20} {:<10} {:<20}".format(
            registro.get('ciudad_municipio_nom', ''),
            registro.get('departamento_nom', ''),
            registro.get('edad', ''),
            registro.get('fuente_tipo_contagio', ''),
            registro.get('estado', ''),
            registro.get('pais_viajo_1_nom', '')
        )
        )
