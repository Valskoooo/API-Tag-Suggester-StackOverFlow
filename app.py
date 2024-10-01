from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import myfunct

app = FastAPI(
    title="Stack Overflow Tags Predictions API",
)

@app.get("/", response_class=FileResponse)
async def get_homepage():
    return FileResponse("html/index.html")

@app.get("/tag/")
async def get_tag(n: int = Query(...), s: str = Query(...)):
    tag = myfunct.predict_tags(s, n)
    return {
        "Nombre de tags": n,
        "Sentence": s,
        "Tags": tag
    }
    #return {"Nombre de tags": n, "Sentence": s}