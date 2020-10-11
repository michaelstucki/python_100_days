import os
import time
import datetime
from playsound import playsound


def header():
    print('Pomodoro Timer: ')


def timer(minutes):
    d = datetime.date.today()
    t = datetime.time(0,minutes)
    timer = datetime.datetime.combine(d, t)
    dt = datetime.timedelta(seconds=1)
    
    for i in range(minutes * 60):
        os.system('clear')
        timer -= dt
        print(f'Timer: {timer.minute:02}:{timer.second:02}')
        time.sleep(1)

    print("Time's up! Time for break.")
    playsound('bell.mp3', False)
    time.sleep(5)
    exit()


def main():
    header()

    user_minutes = 0
    valid_input = False
    while not valid_input:
        try:
            user_minutes = int(input('Enter minutes for timer: '))
            if user_minutes <= 0:
                raise ValueError
            valid_input = True
        except ValueError:
            print('Minutes must be an integer greater than 0.')
    
    timer(user_minutes)


if __name__ == '__main__':
    main()
