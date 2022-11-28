from fastapi import FastAPI, Path
from .data import Payload, Resource


def create_app(name:str="SERVER"):
    app = FastAPI(
        title=f'{name.upper()} API',
        description="Central server for core server",
    )

    @app.get("/")
    async def root():
        return {"message": f'Welcome to {name} server!'}
    
    @app.get("/get-item/{item_id}")
    async def get_item(item_id:int=Path(None, description="ID of target.")):
        return 0

    @app.post("/add-data")
    async def add_data(payload:Payload=None):
        return payload

    return app