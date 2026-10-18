from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Todo funcionando correctamente"
    }
app.include_router(router)



