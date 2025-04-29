import asyncio
import websockets

#Conexão ao servidor.
async def connect_to_websocket(uri):
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")
        try:
            while True:
             message = await websocket.recv()
             #Processa a mensagem recebida.
             print(f"Received: {message}")
        except websockets.exceptions.ConnectionClosed:
              print("Connection closed by the server")

    if __name__ == "__main__":
        uri = "ws://websocket-fh6l.onrender.com/" 
        #Começa a rodar de maneira assíncrona.
        asyncio.run(connect_to_websocket(uri))
