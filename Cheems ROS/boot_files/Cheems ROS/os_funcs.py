import random,time,os,threading
from playsound import playsound

def set_os_def():
    os.system('mode con cols=90 lines=50')
    os.system('title Cheems ROS')

def draw_cheems():
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓█▓▓▒▒▓▓▓▓▓▓█████▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓███▓▓▓▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓███▓▓▓▓▓▒▒▒▒░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░█████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓█▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░''')
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓████▓▒░░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▒░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.3))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████▓▓▓░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓█▓░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓████▓▓▓▓███▓░░░░░░░░░░░░░░░░░''')
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓███▓▓▓█████▓░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.3))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓███▓▓▓█████▓▓▒░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓███▓▓▓▓█████▓▓▒░░░░░░░░░░░░░░░░''')
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓███▓▓▓▓██▓▓███▒░░░░░░░░░░░░░░░░░''')
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓███████████▓▓▓▓▒░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓████████████▓░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▒▒▒▒▒▓▓▓██▓▓▓▓▓▓▒▓▓▓▓▓▓▓██████████▓▒░░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.3))
    print('''░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓█▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓████████▓░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒▓▒░░░░░░▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓█████▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█▓██▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▒▒▒░░▒░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    print('''░░░░░░░░░░░░░░░░░░░░░▒▓▓▒▒▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░▓▓▓▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    print('''░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.3))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▓▓▒▒░▒▓░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▒▒▒░░░░▒▒▒▒░░░▒▒▒░░░▒▒░░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░█▒░░░░▒█▒▓▓░▒▓▒▒▓░▒▓▒▓▒░█▒▒▓▒▒▓░▒▓▒▒░░░░░▒░░▒░▒▒░░░▒░▒░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█▒░░░░▒▓░░█░█▒▒▒▓░█▒▒▒▒░█░░█░░▓▒░▒▓▒░░░░░▓░▒░░▒▒░░░▒░░░▒▒░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▓▓▒▓░▒▓░░█░▒▓▒▒░░▒▓▒▒░░█░░▓░░▓▒▒▒▒▓░░░░░▒░░▒░░▒▒▒▒░░░▒▒▒░░░░░░░░░░░░░░░░░░''')
    time.sleep(random.uniform(0.1, 0.2))
    print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')

def setsound(sound):
    playsound('files/src/media/sounds/' + sound)

def play_sound(sound):
    sound_thread = threading.Thread(target = setsound,args = [sound])
    sound_thread.start()