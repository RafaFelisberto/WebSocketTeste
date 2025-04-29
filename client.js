const ws = new WebSocket("ws://seu-servidor-websocket");

ws.onopen = () => {
    //Login com o nome
    ws.send("Joao"); 
};

ws.onmessage = (event) => {
    console.log("Nova mensagem:", event.data);
};

//Mensagem Pública
ws.send("Olá a todos!");

//Mensagem Privada
ws.send("/msg Maria Tudo bem?");