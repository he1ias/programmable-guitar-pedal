import network
import time
from machine import Pin, ADC
from array import array

try:
    import asyncio
except ImportError:
    import uasyncio as asyncio

SSID = "****"
PASSWORD = "********"

MAX_SAMPLES = 2000

signal = ADC(Pin(27))
buffer = array("H")

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    for _ in range(20):
        if wlan.isconnected():
            break
        print("Connecting to Wi-Fi...")
        time.sleep(1)
    if not wlan.isconnected():
        raise RuntimeError("Wi-Fi connection failed")
    print("Connected! Open http://%s/" % wlan.ifconfig()[0])

async def background():
    while True:
        if len(buffer) < MAX_SAMPLES:
            buffer.append(signal.read_u16())
        await asyncio.sleep(0.001)

with open("voltmeter.html", "rb") as f:
    home = f.read()

async def handle(reader, writer):
    global buffer

    try:
        request = await reader.readline()
        while True:
            line = await reader.readline()
            if not line or line == b"\r\n":
                break

        parts = request.decode().split()
        path = parts[1] if len(parts) > 1 else "/"
        path = path.split("?")[0]

        if path == "/read":
            body = bytes(buffer)
            buffer = array("H")
            ctype = "application/octet-stream"
        else:
            body = home
            ctype = "text/html"

        header = (
            "HTTP/1.0 200 OK\r\n"
            "Content-Type: %s\r\n"
            "Content-Length: %d\r\n\r\n" % (ctype, len(body))
        )
        writer.write(header.encode())
        writer.write(body)
        await writer.drain()
    except Exception as error:
        print("Client error:", error)
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    connect()
    asyncio.create_task(background())
    await asyncio.start_server(handle, "0.0.0.0", 80)
    while True:
        await asyncio.sleep(3600)

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()

