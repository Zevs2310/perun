from app.db.fake_db import devices

def get_all_devices():
    return devices

def get_device_by_id(device_id: int):
    for d in devices:
        if d["id"] == device_id:
            return d
    return None
