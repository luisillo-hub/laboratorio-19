ciudades = {
    "bogota":18,
    "cartagena":20,
    "medellin":24
}
ciudad_min=min(ciudades, key=ciudades.get)
temperatura_min=ciudades[ciudad_min]
print("La ciudad con temperatura mas baja",ciudad_min)
print("temperatura promedio",temperatura_min)