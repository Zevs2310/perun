from fastapi import APIRouter, HTTPException
from app.services.device_service import get_all_devices, get_device_by_id

router = APIRouter()

@router.get("/")
def get_devices():
    return get_all_devices()

@router.get("/{device_id}")
def get_device(device_id: int):
    device = get_device_by_id(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device
