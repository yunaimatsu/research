import torch
from transformers import BertTokenizer, BertModel

def get_bert_model(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state
    cls_embeddings = embeddings[:, 0, :]
    return cls_embeddings

def calculate_cosine_similarity(vec1, vec2):
    cos_sim = torch.nn.functional.cosine_similarity(vec1, vec2)
    return cos_sim.item()

model_name = "bert-base-multilingual-cased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

word1 = input("比較したい単語の１つめを入力してください: ")
word2 = input("比較したい単語を２つめ入力してください: ")

embeddings1 = get_bert_model(word1, model, tokenizer)
embeddings2 = get_bert_model(word2, model, tokenizer)

calculate_cosine_similarity(embeddings1, embeddings2)
cosine_similarity = calculate_cosine_similarity(embeddings1, embeddings2)

print(f'{word1} と {word2} の距離は{cosine_similarity}です。')
