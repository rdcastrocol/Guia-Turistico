from fastapi import APIRouter,HTTPExeption
import storage
from schemas import Lugar

router = APIRouter(
    prefix="/lugares",
    tags=["lugares"],
)    
    
    
@router.get("/")
def get_lugares(limit: int = 5):
#    return {"lugares": []}
    return list(storage.lugares.values())[:limit]
@router.get("/{lugar_id}")
def get_lugar(lugar_id: int):
##    return {"id": lugar_id}
 #   return lugares.get(lugar_id)
    lugar = storage.lugares.get(lugar_id)
     if not lugar:
        raise HTTPException(
              status_code=404,
              detail="Lugar no encontrado"
                )
        return lugar


@router.post("/s", status_code=201)
def create_lugar(lugar: Lugar):
   # global next_id

    lugar.id = storage.next_id
    storage.lugares[storage.next_id] = lugar
    storage.next_id += 1

    return lugar

@router.delete("/{lugar_id}")
def delete_lugar(lugar_id: int):
   # return lugares.pop(lugar_id, None)
    lugar = storage.lugares.pop(lugar_id, None)

    if not lugar:
        raise HTTPException(
              status_code=404,
              detail="Lugar no encontrado"

