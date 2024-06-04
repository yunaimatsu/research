from gensim.models import Word2Vec
import gensim.downloader as api

# Read the document
with open('es_1.txt', 'r') as file:
    text = file.read()

# Preprocess the text
sentences = [line.split() for line in text.split('\n')]

# Train a Word2Vec model
model = Word2Vec(sentences=sentences, vector_size=100, window=5, min_count=1, workers=4)

# Perform word calculations
vector = model.wv['español']  # Get vector for 'computer'
similar_words = model.wv.most_similar('español')  # Get words most similar to 'computer'
print(similar_words)

# # Word calculation example: (king - man) + woman = ?
# result = model.wv.most_similar(positive=['woman', 'king'], negative=['man'])
# print(result)