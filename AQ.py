# Paso 1: Ejemplos positivos (socios activos)
positivos = [
    {"edad": 25, "frecuencia_asistencia": "frecuente", "plan_contratado": "premium"},
    {"edad": 32, "frecuencia_asistencia": "frecuente", "plan_contratado": "premium"},
    {"edad": 45, "frecuencia_asistencia": "frecuente", "plan_contratado": "premium"},
]

# Paso 2: Ejemplos negativos (socios no activos)
negativos = [
    {"edad": 25, "frecuencia_asistencia": "ocasional", "plan_contratado": "básico"},
    {"edad": 32, "frecuencia_asistencia": "ocasional", "plan_contratado": "estándar"},
    {"edad": 38, "frecuencia_asistencia": "rara", "plan_contratado": "básico"},
]

# Paso 3: Inducción de reglas
regla = {}

atributos = []
ejemplo = positivos[0]
for clave in ejemplo:
    atributos.append(clave)

for atributo in atributos:
    valores_pos = []
    valores_neg = []

    for ej in positivos:
        valor = ej[atributo]
        if valor not in valores_pos:
            valores_pos.append(valor)

    for ej in negativos:
        valor = ej[atributo]
        if valor not in valores_neg:
            valores_neg.append(valor)

    valores_validos = []
    for valor in valores_pos:
        encontrado = False
        for v in valores_neg:
            if valor == v:
                encontrado = True
                break
        if not encontrado:
            valores_validos.append(valor)

    if len(valores_validos) > 0:
        regla[atributo] = valores_validos

# Paso 4: Mostrar la regla inducida
print("Regla inducida para identificar a un 'Socio Activo':")
for atributo in regla:
    print("-", atributo, "debe ser uno de:", regla[atributo])
