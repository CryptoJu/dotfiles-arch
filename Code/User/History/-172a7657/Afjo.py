
import keyboard
with open('/home/ju/.config/hypr/hyprland.conf', 'r') as f:
    data = f.readlines()

while True:
    key_to_check = keyboard.read_key()
    print(key_to_check)

for line in data:
    line = line.strip('\n')
