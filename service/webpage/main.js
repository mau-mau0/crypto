var ws = new WebSocket("wss://ws-api.kucoin.com/endpoint?token=2neAiuYvAU61ZDXANAGAsiL4-iAExhsBXZxftpOeh_55i3Ysy2q2LEsEWU64mdzUOPusi34M_wGoSf7iNyEWJwjDpKR3zLnc_qURhouO340p6s6oMZBeddiYB9J6i9GjsxUuhPw3BlrzazF6ghq4L0SqSvVGXBYse3OKoHhJp0I=.epP4twHtbbyzniXlloGupg==");

// Connection opened
ws.addEventListener('open', function (event) {
    console.log('Hello Server!');
    setInterval(function () {
        sendMsg(event = event,
            input = {
                "id": "1545910590801",
                "type": "ping"
            }
        )
    }, 4999)
});

ws.onmessage = function (event) {
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