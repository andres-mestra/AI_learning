import json
import numpy as np


#Definimos una función para calcular la puntuación euclidiana entre usuarios de entrada
#Si los usuarios no estan en los datos, arroja error
def euclidean_score(dataset,user1, user2):
    if user1 not in dataset:
        raise TypeError('Cannot find '+user1+' in the dataset')
        
    if user2 not in dataset:
        raise TypeError('Cannot find '+user2+' in the dataset')
        
    #Peliculas clasificadas por ambos usuarios
    common_movies = {}
    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1
    
    #Extracción de las peliculas clasificadas por los usuarios
    if len(common_movies) == 0:
        return 0
    
    #Calcular las diferencias cuadráticas entre las clasificaciones y para calcular la Euclídea Puntuación
    squared_diff = []
    for item in dataset[user1]:
        if item in dataset[user2]:
            squared_diff.append(np.square(dataset[user1][item] - dataset[user2][item]))
    
    return 1 / (1 + np.sqrt(np.sum(squared_diff)))





#Funcion para calcular la puntuación de Pearson

def pearson_score(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('Cannot find '+user1+' in the dataset')
        
    if user2 not in dataset:
        raise TypeError('Cannot find '+user2+' in the dataset')
    common_movies = {}
    
    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1
    
    num_ratings = len(common_movies)
    if num_ratings == 0:
        return 0
    #Calcular la suma de calificaciones de todas las películas que han sido calificadas por ambos usuarios
    user1_sum = np.sum([dataset[user1][item] for item in common_movies ])
    user2_sum = np.sum([dataset[user2][item] for item in common_movies ])
    
    #Calcular la suma de los cuadrados de las calificaciones de todas las películas que han sido calificadas por ambos usuarios
    user1_squared_sum = np.sum([np.square(dataset[user1][item]) for item in common_movies])
    user2_squared_sum = np.sum([np.square(dataset[user2][item]) for item in common_movies])
    
    #Calcular la suma de productos de las clasificaciones de las películas comunes
    sum_of_products = np.sum([dataset[user1][item] * dataset[user2][item] for item in common_movies])
    
    # Calculate the Pearson correlation score
    Sxy = sum_of_products - (user1_sum * user2_sum / num_ratings)
    Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
    Syy = user2_squared_sum - np.square(user2_sum) / num_ratings
    
    if Sxx * Syy == 0:
        return 0
    return Sxy / np.sqrt(Sxx * Syy)