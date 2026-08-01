from app.services.rag_service import rag_service

question = "What is a Kubernetes Pod?"

answer = rag_service.ask(question)

print(answer)
