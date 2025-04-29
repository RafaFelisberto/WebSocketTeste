connected_users = {}  # { username: [websocket_connections] }

async def handler(websocket, path):
    username = None
    try:
        # Usuário envia seu nome ao conectar
        username = await websocket.recv()
        if username in connected_users:
            connected_users[username].append(websocket)
        else:
            connected_users[username] = [websocket]
        #Seleciona a mensagem e envia ao cliente desejado
        async for message in websocket:
            if message.startswith("/msg "):
                parts = message.split(" ", 2)
                target_user = parts[1]
                msg_content = parts[2]

                if target_user in connected_users:
                    for conn in connected_users[target_user]:
                        await conn.send(f"[Privado] {username}: {msg_content}")
            else:
                # Mensagem pública
                for user_conns in connected_users.values():
                    for conn in user_conns:
                        if conn != websocket:
                            await conn.send(f"[{username}] {message}")
    finally:
        # Remove esta conexão da lista
        if username and websocket in connected_users.get(username, []):
            connected_users[username].remove(websocket)
            #Encerra a conexão.
            if not connected_users[username]: 
                del connected_users[username]