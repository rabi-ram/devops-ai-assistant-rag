from app.services.llm_service import llm_service

answer = llm_service.ask("What is Docker?")

print(answer)
