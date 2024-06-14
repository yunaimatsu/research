import torch
from transformers import BertTokenizer, BertModel
import pandas as pd
import os


# Define functions

def get_bert_model(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state
    cls_embeddings = embeddings[:, 0, :]
    return cls_embeddings

def calculate_cosine_similarity(vec1, vec2):
    cos_sim = torch.nn.functional.cosine_similarity(vec1, vec2)
    return cos_sim.item()

model_name = "bert-base-multilingual-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)


# Load the false-friends dataset

files = os.listdir('input')
for i, filename in enumerate(files):
    print(f"{i}: {filename}")

file_index = int(input("Please enter the index of the file you want to choose: "))
chosen_file = files[file_index]

false_friends_df = pd.read_csv(f'input/{chosen_file}')


# Calculate cosine similarity

results = []

for index, row in false_friends_df.iterrows():
    word1 = row['en']
    word2_es = row['es']
    word2_pt = row['pt']
    word2_fr = row['fr']

    embeddings1 = get_bert_model(word1, model, tokenizer)
    embeddings2_es = get_bert_model(word2_es, model, tokenizer)
    embeddings2_pt = get_bert_model(word2_pt, model, tokenizer)
    embeddings2_fr = get_bert_model(word2_fr, model, tokenizer)

    cos_sim_es = calculate_cosine_similarity(embeddings1, embeddings2_es)
    cos_sim_pt = calculate_cosine_similarity(embeddings1, embeddings2_pt)
    cos_sim_fr = calculate_cosine_similarity(embeddings1, embeddings2_fr)

    results.append([word1, word2_es, cos_sim_es, word2_pt, cos_sim_pt, word2_fr, cos_sim_fr])

results_df = pd.DataFrame(results, columns=['English', 'Spanish', 'Cosine_Similarity_ES', 'Portuguese', 'Cosine_Similarity_PT, French', 'Cosine_Similarity_FR'])
results_df.to_csv('output.csv', index=True)