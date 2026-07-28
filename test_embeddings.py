from app.services.embedding_service import embedding_service

embeddings = embedding_service.get_embeddings()

vector = embeddings.embed_query("What is Kubernetes?")

print(f"Vector dimension: {len(vector)}")
print(vector[:10])  # First 10 values
