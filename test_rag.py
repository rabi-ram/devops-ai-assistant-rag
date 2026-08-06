from app.services.rag_service import rag_service

question = "What is a Kubernetes Pod?"

response = rag_service.ask(question)

print("\nAnswer")
print("=" * 60)
print(response["answer"])

print("\nSources")
print("=" * 60)

for source in response["sources"]:
    print(
        f'{source["file"]} (Page {source["page"]})'
    )
    