import requests

def obtener_datos(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

datos = obtener_datos("https://jsonplaceholder.typicode.com/todos/1")

if datos:
    print(datos)
else:
    print("Error al obtener los datos.")
