import torch
from transformers import BertTokenizer, BertModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_bert_embeddings(text, model, tokenizer):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    # Get the hidden states from the BERT model
    outputs = model(**inputs)
    # Take the mean of the token embeddings to represent the text
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.squeeze()  # Add this line to remove the extra dimension

def find_closest_words(vector, word_embeddings, word_list, n=5):
    # Reshape the vector to 2D
    vector = vector.cpu().detach().numpy().reshape(1, -1)
    word_embeddings = word_embeddings.cpu().detach().numpy()
    # Calculate cosine similarities between the vector and all word embeddings
    similarities = cosine_similarity(vector, word_embeddings)
    # Get the indices of the highest similarities
    closest_indices = np.argsort(similarities[0])[::-1][:n]
    return [word_list[i] for i in closest_indices]

# Load BERT model and tokenizer
model_name = "bert-base-multilingual-cased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# Words for the semantic calculation
words = ["Tokyo", "Japan", "Spain"]

# Get embeddings for each word
embeddings = {}
for word in words:
    embeddings[word] = get_bert_embeddings(word, model, tokenizer)

# Perform vector arithmetic: Tokyo - Japan + Spain
result_vector = embeddings["Tokyo"] - embeddings["Japan"] + embeddings["Spain"]

# For the purpose of finding the closest word, get embeddings for a list of common words
# Here, we use a simplified list of words for demonstration. In practice, you'd use a larger vocabulary.
common_words = ["Madrid", "Barcelona", "Japan", "Spain", "Tokyo", "France", "Germany"]
common_word_embeddings = torch.stack([get_bert_embeddings(word, model, tokenizer) for word in common_words])

# Find the closest word to the result vector
# Find the closest words to the result vector
closest_words = find_closest_words(result_vector, common_word_embeddings, common_words, n=5)

print(f"The words closest to 'Tokyo - Japan + Spain' are: {closest_words}")