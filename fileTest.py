# -*- coding: utf-8 -*-

if __name__ == '__main__':
    file = open("move.txt", "r")
    # print file.read()
    move = str(file.read()).split()
    file.close()
    print move[0]
    print move[1]
    print move[2]
    file.close()
