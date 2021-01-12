def puntuacion_palabras(array_de_palabras):
    puntuacion_final = 0
    for palabra in array_de_palabras:
        count = 0
        for letra in palabra:
            if letra.lower() in ['a','e','i','o','u']:
                count = count + 1
        if count % 2 == 0:
            puntuacion_final = puntuacion_final + 2
        else:
            puntuacion_final = puntuacion_final + 1
    return puntuacion_final
puntuacion_palabras(['amigos y estudiantes', 'programadores imparables', 'agradecidos con Dios'])