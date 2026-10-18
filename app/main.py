from fastapi import FastAPI, HTTPException
from routers.lugares import router as lugar_router
from routers.llm import router as llm_router

app = FastAPI()

app.include_router(lugares_router)
app.include_router(llm_router)

@app.get("/")
def root():
    return {
        "message": "Todo funcionando correctamente"
    }
app.include_router(lugar_router)


