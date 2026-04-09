from fastapi import FastAPI
from app.api.devices import router as device_router

app = FastAPI(title="Perun API")

app.include_router(device_router, prefix="/devices", tags=["Devices"])

@app.get("/")
def root():
    return {"message": "Perun API running"}
