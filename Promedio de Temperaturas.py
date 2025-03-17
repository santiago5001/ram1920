# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Quito (clima lluvioso)
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 14}
        ],
        # ... (Datos de las otras semanas de Quito)
    ],
    [   # Cuenca (chaparrones)
        [   # Semana 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 18}
        ],
        # ... (Datos de las otras semanas de Cuenca)
    ],
    [   # Ambato (lluvia moderada)
        [   # Semana 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 19}
        ],
        # ... (Datos de las otras semanas de Ambato)
    ]
]

def calcular_promedio_temperaturas(temperaturas):
    """
    Calcula el promedio de temperaturas para cada ciudad y semana.

    Args:
        temperaturas (list): Una lista de listas que contiene los datos de temperatura
                             para cada ciudad y semana.
    """

    # Nombres de las ciudades
    ciudades = ["Quito", "Cuenca", "Ambato"]

    # Iterar a través de las ciudades y sus datos de temperatura
    for ciudad_idx, ciudad in enumerate(temperaturas):
        # Iterar a través de las semanas de cada ciudad
        for semana_idx, semana in enumerate(ciudad):
            # Calcular la suma de las temperaturas de la semana
            suma_temperaturas = sum([dia["temp"] for dia in semana])

            # Calcular el promedio de temperaturas de la semana
            promedio = suma_temperaturas / len(semana)

            # Imprimir el promedio de temperaturas para la ciudad y semana actual
            print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")

# Llamar a la función para calcular y mostrar los promedios de temperatura
calcular_promedio_temperaturas(temperaturas)
print("Fin promedio de temperatura del tiempo ciudades")