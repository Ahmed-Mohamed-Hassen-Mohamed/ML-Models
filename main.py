from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List

app = FastAPI()
# gp api>uvicorn main:app
class Item(BaseModel):
    id: str
    embedding: List[List[float]]

@app.post("/get_embedding_face/")
async def get_embedding_face(body: list[str]):
    try:
        # images: List[UploadFile] = File(...)
        count = len(body)
        print("Number of images received:", count)
        
        return { "embedding": [[1,2,3,4],[4,3,2,1]] }
    except Exception as e:
        return {"error": str(e)}

@app.post("/get_embedding_fingerprint/")
async def get_embedding_fingerprint(body: list[str]):
    try:
        # Print the count of images received
        count = len(body)
        print("Number of images received:", count)

        return { "embedding": [[4,3,2,1],[1,2,3,4]] }
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/predict/")
async def predict(face: UploadFile = File(...), fingerprint: UploadFile = File(...)):
    try:
        
        return {"id": 2329}
    except Exception as e:
        return {"error": str(e)}

@app.post("/retrain/")
async def retrain(items: List[Item]):
    try:
        # Print the count of images received
        count = len(items)
        print("Number of images received:", count)

        return {"count": items[4].embedding}
    except Exception as e:
        return {"error": str(e)}