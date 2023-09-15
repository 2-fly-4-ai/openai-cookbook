import openai
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Function to retrieve embeddings
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']

# 1. Load the CSV
csv_path = 'dummy_terms.csv'
data = pd.read_csv(csv_path)

# Assuming the terms are in a column named 'terms'
terms = data['terms'].tolist()

# 2. Initialize the OpenAI API
openai.api_key = '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'

# 3. Retrieve embeddings for each term
embeddings = [get_embedding(term) for term in terms]

# 4. Cluster terms based on their embeddings
# Using KMeans clustering, decide the optimal number of clusters (k) based on your data.
k = 5  # Example: clustering into 5 groups
kmeans = KMeans(n_clusters=k)
labels = kmeans.fit_predict(embeddings)

# 5. Group terms based on their clusters
grouped_terms = {i: [] for i in range(k)}

for term, label in zip(terms, labels):
    grouped_terms[label].append(term)

for label, grouped in grouped_terms.items():
    print(f"Cluster {label + 1}: {', '.join(grouped)}")

# 6. Save to a new CSV
output_data = {'Term': [], 'Cluster': []}

for label, grouped in grouped_terms.items():
    for term in grouped:
        output_data['Term'].append(term)
        output_data['Cluster'].append(label + 1)

output_df = pd.DataFrame(output_data)
output_df.to_csv('clustered_terms.csv', index=False)

print("Saved results to 'clustered_terms.csv'.")
