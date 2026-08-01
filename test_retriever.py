from app.vectorstore.chroma_store import chroma_store

query = "What is a Kubernetes Pod?"

results = chroma_store.similarity_search(query)

print(f"Found {len(results)} result(s)\n")

for i, doc in enumerate(results, start=1):
    print("=" * 60)
    print(f"Result {i}")
    print("=" * 60)
    print(doc.page_content)
    print()
    