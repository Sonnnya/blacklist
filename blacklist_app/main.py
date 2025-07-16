from fastapi import FastAPI
from api.customers import router as customers_router

app = FastAPI()

app.include_router(customers_router)
