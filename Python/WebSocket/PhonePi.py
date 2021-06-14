
import asyncio
import websockets
import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


hostname = socket.gethostname()
IPAddr = get_ip()
print("El nombre del dispositivo es: " + hostname)
print("La IP del dispositivo es: " + IPAddr)

async def echo(websocket, path):
    async for message in websocket:
        if path == '//accelerometer':
            data = await websocket.recv()
            print(data)
            f = open("accelerometer.txt", "a")
            f.write(data+"\n")

        if path == '//gyroscope':
            data = await websocket.recv()
            print(data)
            f = open("gyroscope.txt", "a")
            f.write(data+"\n")

        if path == '//orientation':
            data = await websocket.recv()
            print(data)
            f = open("orientation.txt", "a")
            f.write(data+"\n")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '0.0.0.0', 5000))
asyncio.get_event_loop().run_forever()
