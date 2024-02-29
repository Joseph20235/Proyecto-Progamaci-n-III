from ui import solicitar_datos, imprimir_datos
from api import consultar_datos


def main():
    departamento, limite_registros = solicitar_datos()
    try:
        datos = consultar_datos(departamento, limite_registros)
        imprimir_datos(datos)
    except Exception as e:
        print("Error al procesar la consulta:", e)

if __name__ == "__main__":
    main()
