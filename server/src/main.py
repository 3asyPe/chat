from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from app.db import init_db
from connection_manager import ConnectionManager


app = FastAPI()

manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(
                websocket=websocket,
                message={
                    "client_id": client_id,
                    "message": data,
                },
            )
            await manager.broadcast(
                websocket=websocket,
                message={
                    "client_id": client_id,
                    "message": data
                }
            )
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")