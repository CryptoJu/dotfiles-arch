
with open('/home/ju/.config/hypr/hyprland.conf', 'r') as f:
    data = f.readlines()

key_to_check = input('Press a key')
print(key_to_check)

for line in data:
    line = line.strip('\n')
