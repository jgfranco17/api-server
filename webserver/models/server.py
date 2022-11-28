from fastapi import FastAPI
from .data import Payload, Resource


def create_app(server_name:str="SERVER"):
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": f'Welcome to {server_name}'}

    @app.post("/add-data")
    async def add_data(payload:Payload=None):
        return payload

    return app