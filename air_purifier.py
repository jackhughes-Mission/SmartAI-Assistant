from pyvesync import VeSync
import keyring

manager = VeSync('', '')
autologgedin = False

actions = {
    'Turn on': lambda: manager.fans[0].turn_on(),
    'Turn off': lambda: manager.fans[0].turn_off(),
    'High': lambda: manager.fans[0].change_fan_speed(3),
    'Medium': lambda: manager.fans[0].change_fan_speed(2),
    'Low': lambda: manager.fans[0].change_fan_speed(1),
    'Sleep': lambda: manager.fans[0].sleep_mode(),
    'Username': lambda: manager.username,
    'Password': lambda: manager.password,
    'Light 0': lambda: manager.fans[0].set_night_light('off'),
    'Light 1': lambda: manager.fans[0].set_night_light('dim'),
    'Light 2': lambda: manager.fans[0].set_night_light('on')
}

def save_credentials(username, password):
    keyring.set_password('VeSync', 'username', username)
    keyring.set_password('VeSync', username, password)

def get_credentials():
    username = keyring.get_password('VeSync', 'username')
    password = keyring.get_password('VeSync', username)
    return username, password

def turn_on():
    print("Turning purifier on")
    actions['Turn on']()

def turn_off():
    print("Turning purifier off")
    actions['Turn off']()

def high_purifier():
    print("Increasing purifier")
    actions['High']()

def low_purifier():
    print("Decreasing purifier")
    actions['Sleep']()

def loginauto():
    global manager
    global autologgedin

    username, password = get_credentials()

    if username and password:
        manager = VeSync(username, password)
        manager.login()
        manager.update()
        autologgedin = True
        print("Logged in success")
    else:
        username_input = input("Username: ")
        password_input = input("Password: ")
        save_credentials(username_input, password_input)
        manager = VeSync(username_input, password_input)
        manager.login()
        manager.update()
        autologgedin = True
        print("Logged in success")


def main_purifier():
    print("Called purifer python script")
    loginauto()