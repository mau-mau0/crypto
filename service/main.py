from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

html_file = open("/crypto/service/webpage/index.html", "r")
# html_file = open("F:\Documents\Programming\pricelistener\crypto\service\webpage", "r")
app = FastAPI()
app.mount()
html = html_file.read()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
