import paramiko
import os
from dotenv import load_dotenv
import asyncio

def connect_to_rasp_pi():
    load_dotenv()

    HOST = os.getenv("HOST")
    USERNAME = os.getenv("USERNAME")
    PORT = os.getenv("PORT")
    PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH")

    if not all([HOST, USERNAME, PORT, PRIVATE_KEY_PATH]):
        print("Error: Missing environment variables")
        return "Error: Missing environment variables for Raspberry Pi connection"

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        expanded_key_path = os.path.expanduser(PRIVATE_KEY_PATH)
        
        print(f"Attempting to connect to {HOST}:{PORT} as {USERNAME}")
        
        ssh_client.connect(
            hostname=HOST,
            username=USERNAME,
            port=int(PORT),
            key_filename=expanded_key_path
        )

        stdin, stdout, stderr = ssh_client.exec_command("sudo fail2ban-client status sshd")
        
        output = stdout.read().decode()
        errors = stderr.read().decode()
        print(output)
        
        stdin.close()
        stdout.close()
        stderr.close()
        
        if errors:
            return f"Error: {errors}"
        return output

    except Exception as e:
        return f"Connection failed: {str(e)}"
    finally:
        if 'ssh_client' in locals():
            ssh_client.close()


async def connect_to_rasp_pi_async():
    await asyncio.to_thread(connect_to_rasp_pi)