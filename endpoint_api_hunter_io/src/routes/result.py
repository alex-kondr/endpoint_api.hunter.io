from fastapi import APIRouter, Depends

try:
    from src.db import db
    from src.schemas.db import DBModel, DBModelUpdate
except ModuleNotFoundError:
    from ...src.db import db
    from ...src.schemas.db import DBModel, DBModelUpdate


router = APIRouter(prefix="/result", tags=["result"])


@router.get("/", name="Return data", response_model=DBModel)
async def get_result():
    return db.result


@router.post("/", name="Data replacement", response_model=DBModel)
async def replace_data(data: DBModel = Depends()):
    db.result = data
    return db.result


@router.patch("/", name="Update status", response_model=DBModel)
async def update_data(data: DBModelUpdate = Depends()):
    db.result["data"]["status"] = data.status
    return db.result


@router.delete("/", name="Clear data", response_model=DBModel)
async def delete_result():
    db.result = {}
    return db.result
