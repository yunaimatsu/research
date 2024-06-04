import gensim.downloader as api

# Descargar el modelo Word2Vec
model = api.load('word2vec-google-news-300')

# Definir las palabras
palabras = ['gato', 'perro', 'pez']

# Calcular la distancia semántica entre las palabras
distancias = []
for i in range(len(palabras)):
    for j in range(i+1, len(palabras)):
        distancia = model.distance(palabras[i], palabras[j])
        distancias.append((palabras[i], palabras[j], distancia))

# Imprimir las distancias
for palabra1, palabra2, distancia in distancias:
    print(f"La distancia entre '{palabra1}' y '{palabra2}' es {distancia}")