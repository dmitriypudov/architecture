from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import secrets

app = FastAPI()

url_storage = {}

class URLItem(BaseModel):
    long_url: str

@app.post("/shorten")
def shorten_url(item: URLItem):
    short_code = secrets.token_urlsafe(5)[:6]
    url_storage[short_code] = item.long_url
    return {"short_url": f"http://127.0.0.1:8000/{short_code}"}

@app.get("/{short_code}")
def redirect(short_code: str):
    long_url = url_storage.get(short_code)
    if not long_url:
        raise HTTPException(status_code=404, detail="Not found")
    return RedirectResponse(long_url)