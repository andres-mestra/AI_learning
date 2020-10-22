

import json
import numpy as np 
#Importamos las funcion creada para calcular el puntaje de similitud, metodo de pearso
from compute_scores import pearson_score

#Definición de función para buscar los usuarios similares a el usuario indicado
def find_similar_users(dataset, user, num_users):
    if user not in dataset:
        raise TypeError('No se encontro el '+user+' en el conjunto de datos')
    #Calcula el puntaje de similitud respecto a cada usuario con el metodo de pearson
    scores = np.array([[x, pearson_score(dataset, user,x)] for x in dataset if x != user])

    #Ordena las puntuaciones
    scores_sorted = np.argsort(scores[:,1])[::-1]

    #Extrae las mejores puntuaciones 
    top_users = scores_sorted[:num_users]
    return scores[top_users]