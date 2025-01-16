import asyncio
from bleak import BleakScanner, BleakClient

TARGET_NAME_FRAGMENT = "MELK"

async def find_device():
    print("Scanning for the device...")
    devices = await BleakScanner.discover()
    
    for d in devices:
        if d.name and TARGET_NAME_FRAGMENT.upper() in d.name.upper():
            print(f"Found the device: {d}")
            return d
    
    print("No device found. Check if it's powered on or if someone else is connected?")
    return None

async def connect_and_execute(device, command):
    if not device:
        return
    
    print(f"Connecting to {device.address}...")
    try:
        async with BleakClient(device.address) as client:
            if not client.is_connected:
                print("Failed to connect.")
                return

            print("Connected!")
            control_char_uuid = "0000fff3-0000-1000-8000-00805f9b34fb"
            
            await client.write_gatt_char(control_char_uuid, command, response=False)
            
            value = await client.read_gatt_char(control_char_uuid)
            print("Current state:", value)

    except Exception as e:
        print(f"Error: {e}")

async def turn_on():
    device = await find_device()
    turn_on_command = bytearray([0x7E, 0x04, 0x04, 0x01, 0xFF, 0x00, 0x00, 0xEF])
    await connect_and_execute(device, turn_on_command)

async def turn_off():
    device = await find_device()
    turn_off_command = bytearray([0x7E, 0x04, 0x04, 0x00, 0x00, 0x00, 0x00, 0xEF])
    await connect_and_execute(device, turn_off_command)

def asyncio_turnon():
    asyncio.run(turn_on())

def asyncio_turnoff():
    asyncio.run(turn_off())
