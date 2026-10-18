from fastapi import APIRouter
from pydantic import BaseModel
import httpx


router = APIRouter(prefix="/llm", tags=["llm"])

class Question(BaseModel):
    prompt: str

@router.post("/ask")
async def ask(question: Question):
    async with httpx.AsyncClient(timeout=530) as client:
        response = await client.post(
                "http://127.0.0.1:11434/v1",
                json={
                    "model": "qwen3:4b",
                    "messages": [{ "role": "user", "content": question.prompt}]
                    }

                )
        return { "answer": response.json()["choises"][0]["message"]["content"]}


