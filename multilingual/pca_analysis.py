import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import torch
from transformers import BertTokenizer, BertModel
import pandas as pd
import os

import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap


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

embed_1 = []
embed_es = []
embed_pt = []
embed_fr = []

for index, row in false_friends_df.iterrows():
    word1 = row['en']
    word2_es = row['es']
    word2_pt = row['pt']
    word2_fr = row['fr']

    embeddings1 = get_bert_model(word1, model, tokenizer)
    embeddings2_es = get_bert_model(word2_es, model, tokenizer)
    embeddings2_pt = get_bert_model(word2_pt, model, tokenizer)
    embeddings2_fr = get_bert_model(word2_fr, model, tokenizer)

    embed_1.append(embeddings1)
    embed_es.append(embeddings2_es)
    embed_pt.append(embeddings2_pt)
    embed_fr.append(embeddings2_fr)


# Convert the lists to numpy arrays
embed_1 = torch.cat(embed_1).detach().numpy()
embed_es = torch.cat(embed_es).detach().numpy()
embed_pt = torch.cat(embed_pt).detach().numpy()
embed_fr = torch.cat(embed_fr).detach().numpy()

# Step 1: Standardize the data
scaler = StandardScaler()
data_scaled_1 = scaler.fit_transform(embed_1)
data_scaled_es = scaler.fit_transform(embed_es)
data_scaled_pt = scaler.fit_transform(embed_pt)
data_scaled_fr = scaler.fit_transform(embed_fr)

# Step 2: Perform PCA
pca = PCA(n_components=3)
data_pca_1 = pca.fit_transform(data_scaled_1)
data_pca_es = pca.fit_transform(data_scaled_es)
data_pca_pt = pca.fit_transform(data_scaled_pt)
data_pca_fr = pca.fit_transform(data_scaled_fr)

# Now data_pca contains your reduced data with shape (n_samples, 3)

# Optional: Print the explained variance ratio
#print("Explained variance ratio:", pca.explained_variance_ratio_)

# Optional: Print the cumulative explained variance ratio
#print("Cumulative explained variance ratio:", np.cumsum(pca.explained_variance_ratio_))

# Step 4: Create the 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the scatter points
scatter = ax.scatter(data_pca_1[:, 0], data_pca_1[:, 1], data_pca_1[:, 2], label='English', alpha=0.5)   
scatter = ax.scatter(data_pca_es[:, 0], data_pca_es[:, 1], data_pca_es[:, 2], label='Spanish', alpha=0.5)
scatter = ax.scatter(data_pca_pt[:, 0], data_pca_pt[:, 1], data_pca_pt[:, 2], label='Portuguese', alpha=0.5)
scatter = ax.scatter(data_pca_fr[:, 0], data_pca_fr[:, 1], data_pca_fr[:, 2], label='French', alpha=0.5) 

# Set labels for each axis
ax.set_xlabel('First Principal Component')
ax.set_ylabel('Second Principal Component')
ax.set_zlabel('Third Principal Component')

# Add a legend
ax.legend()

# Set a title for the plot
ax.set_title('3D Scatter Plot of PCA-reduced Data')

# Show the plot
plt.show()