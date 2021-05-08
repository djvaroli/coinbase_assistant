from fastapi import FastAPI
import uvicorn

from krypt.app.routers import portfolio


app = FastAPI()
app.include_router(portfolio.router)


@app.get("/")
def home():
    return "Welcome to Krypto Assistant!"


if __name__ == "__main__":
    uvicorn.run(app, reload=True)



    




