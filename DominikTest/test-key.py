import keyboard

key_entered = ''
print('start')
while key_entered != 'q':
    key_entered = keyboard.read_key()
    print(key_entered)