# 时间函数举例4:一个猜数游戏，判断一个人反应快慢

import time
import random

if __name__ == '__main__':
    play_it = input("Do you want to play it.('y' or 'n')")
    while play_it == 'y':
        i = random.randint(0, 2 ** 32) % 100
        print('please input number you guess:\n')
        start = time.process_time()
        guess = int(input('input your guess:\n'))
        while guess != i:
            if guess > i:
                print('please input a little smaller')
                guess = int(input('input your guess:\n'))
            else:
                print('please input a little bigger')
                guess = int(input('input your guess:\n'))
        end = time.process_time()
        var = (end - start) / 18.2
        print(var)
        if var < 15:
            print('you are very clever!')
        elif var < 25:
            print('you are normal!')
        else:
            print('you are stupid!')
        print('Congradulations')
        print('The number you guess is %d' % i)
        play_it = input("Do you want to play it.('y' or 'n')")