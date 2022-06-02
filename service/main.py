from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Kucoin Websocket</title>
    </head>
    <body>
        <h1>Kucoin Websocket</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
            <li>Enter Channel Subscription Above</li>
        </ul>
        <script>
            var ws = new WebSocket("wss://ws-api.kucoin.com/endpoint?token=2neAiuYvAU61ZDXANAGAsiL4-iAExhsBXZxftpOeh_55i3Ysy2q2LEsEWU64mdzUOPusi34M_wGoSf7iNyEWJwjDpKR3zLnc_qURhouO340p6s6oMZBeddiYB9J6i9GjsxUuhPw3BlrzazF6ghq4L0SqSvVGXBYse3OKoHhJp0I=.epP4twHtbbyzniXlloGupg==");

            // Connection opened
            ws.addEventListener('open', function (event) {
                console.log('Hello Server!');
                setInterval(function(){
                    sendMsg(event=event,
                            input = {
                                        "id":"1545910590801",
                                        "type":"ping"
                                    }
                    )
                }, 4999)
            });

            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }

            function sendMsg(event, input) {
                var input = input
                ws.send(JSON.stringify(input))
                input.value = ''
                event.preventDefault()
                console.log(JSON.stringify(input))
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
