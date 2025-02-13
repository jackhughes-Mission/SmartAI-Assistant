import asyncio
from bleak import BleakScanner, BleakClient

TARGET_NAME_FRAGMENT = "MELK"

client = None

async def find_device():
    print("Scanning for the device...")
    devices = await BleakScanner.discover()
    
    for d in devices:
        if d.name and TARGET_NAME_FRAGMENT.upper() in d.name.upper():
            print(f"Found the device: {d}")
            return d
    
    print("No device found. Check if it's powered on or if someone else is connected?")
    return None

async def connect_device(device):
    if not device:
        return None
    
    print(f"Connecting to {device.address}...")
    try:
        client = BleakClient(device.address)
        await client.connect()
        if not client.is_connected:
            print("Failed to connect.")
            return None

        print("Connected!")
        return client

    except Exception as e:
        print(f"Error: {e}")
        return None

async def connect():
    global client
    device = await find_device()
    client = await connect_device(device)
    return client

async def execute(client, command):
    if not client:
        return
        
    try:
        control_char_uuid = "0000fff3-0000-1000-8000-00805f9b34fb"
        await client.write_gatt_char(control_char_uuid, command, response=False)
        
        value = await client.read_gatt_char(control_char_uuid)
        print("Current state:", value)

    except Exception as e:
        print(f"Error: {e}")

async def turn_on():
    global client
    try:
        turn_on_command = bytearray([0x7E, 0x04, 0x04, 0x01, 0xFF, 0x00, 0x00, 0xEF])
        await execute(client, turn_on_command)
    except Exception as e:
        print(f"Error during turn on: {e}")

async def turn_off():
    global client
    try:
        turn_off_command = bytearray([0x7E, 0x04, 0x04, 0x00, 0x00, 0x00, 0x00, 0xEF])
        await execute(client, turn_off_command)
    except Exception as e:
        print(f"Error during turn off: {e}")

def connect_sync():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(connect())

def asyncio_turnon():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(turn_on())

def asyncio_turnoff():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(turn_off())
