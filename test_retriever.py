from app.services.retrieval_service import retrieval_service

results = retrieval_service.retrieve_with_score(
    "What is Terraform workspace?"
)

for document, score in results:
    print("=" * 60)
    print(f"Score: {score}")
    print(f"Source: {document.metadata}")
    print(document.page_content[:300])
    