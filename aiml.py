from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python backend developer",
    "FastAPI developer",
    "Java frontend developer"
]

embeddings = model.encode(sentences)

for sentence, embedding in zip(sentences, embeddings):
    print(sentence)
    print(embedding)