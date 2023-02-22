import numpy as np

#------------------------------------------------------------------------------
#　持ち替え


def s_back(input_cube):#奥に持ち替え
    input_cube = np.rot90(input_cube, 1,axes=(0, 1))
    d1 = input_cube[0]
    d2 = input_cube[1]
    d3 = input_cube[2]
    d4 = input_cube[3]
    input_cube = np.array([d1,d2,d3,d4])
    return input_cube


def s_flont(input_cube):#手前に持ち替え
    input_cube = np.rot90(input_cube, -1,axes=(0, 1))
    d1 = input_cube[0]
    d2 = input_cube[1]
    d3 = input_cube[2]
    d4 = input_cube[3]
    input_cube = np.array([d1,d2,d3,d4])
    return input_cube
    

def s_right(input_cube):#右に持ち替え
    input_cube = np.rot90(input_cube, 1,axes=(0, 2))
    d1 = input_cube[0]
    d2 = input_cube[1]
    d3 = input_cube[2]
    d4 = input_cube[3]
    input_cube = np.array([d1,d2,d3,d4])
    return input_cube


def s_left(input_cube):#左に持ち替え
    input_cube = np.rot90(input_cube, -1,axes=(0, 2))
    d1 = input_cube[0]
    d2 = input_cube[1]
    d3 = input_cube[2]
    d4 = input_cube[3]
    input_cube = np.array([d1,d2,d3,d4])
    return input_cube

#------------------------------------------------------------------------------
#　回転

def r_u_right(input_cube):#上部右回転
    d1 = np.rot90(input_cube[0], -1)
    d2 = np.rot90(input_cube[1], -1)
    d3 = input_cube[2]
    d4 = input_cube[3]
    input_cube = np.array([d1,d2,d3,d4])
    return input_cube


def r_u_left(input_cube):#上部左回転
    d1 = np.rot90(input_cube[0], 1)
    d2 = np.rot90(input_cube[1], 1)
    d3 = input_cube[2]
    d4 = input_cube[3]
    input_cube = np.array([d1,d2,d3,d4])
    return input_cube


def r_l_right(input_cube):#部右回転
    d1 = input_cube[0]
    d2 = input_cube[1]
    d3 = np.rot90(input_cube[2], -1)
    d4 = np.rot90(input_cube[3], -1)
    input_cube = np.array([d1,d2,d3,d4])
    return input_cube


def r_l_left(input_cube):#下部左回転
    d1 = input_cube[0]
    d2 = input_cube[1]
    d3 = np.rot90(input_cube[2], 1)
    d4 = np.rot90(input_cube[3], 1)
    input_cube = np.array([d1,d2,d3,d4])
    return input_cube


def r_b_right(input_cube):#右部奥回転
    input_cube = s_right(input_cube)
    input_cube = r_u_right(input_cube)
    input_cube = s_left(input_cube)
    return input_cube


def r_f_right(input_cube):#右部手前回転
    input_cube = s_right(input_cube)
    input_cube = r_u_left(input_cube)
    input_cube = s_left(input_cube)
    return input_cube


def r_b_left(input_cube):#左部奥回転
    input_cube = s_left(input_cube)
    input_cube = r_u_left(input_cube)
    input_cube = s_right(input_cube)
    return input_cube


def r_f_left(input_cube):#左部手前回転
    input_cube = s_left(input_cube)
    input_cube = r_u_right(input_cube)
    input_cube = s_right(input_cube)
    return input_cube


def r_r_flont(input_cube):#手前右回転
    input_cube = s_back(input_cube)
    input_cube = r_u_right(input_cube)
    input_cube = s_flont(input_cube)
    return input_cube


def r_l_flont(input_cube):#手前左回転
    input_cube = s_back(input_cube)
    input_cube = r_u_left(input_cube)
    input_cube = s_flont(input_cube)
    return input_cube


def r_r_back(input_cube):#右回転
    input_cube = s_flont(input_cube)
    input_cube = r_u_left(input_cube)
    input_cube = s_back(input_cube)
    return input_cube


def r_l_back(input_cube):#奥左回転
    input_cube = s_flont(input_cube)
    input_cube = r_u_right(input_cube)
    input_cube = s_back(input_cube)
    return input_cube




#------------------------------------------------------------------------------
#　コマンド設定

def rotate(input_key,input_cube):

    if input_key == "w":#奥に持ち替え
        input_cube = s_back(input_cube)
        
    elif input_key == "s":#手前に持ち替え
        input_cube = s_flont(input_cube)
    
    elif input_key == "d":#右に持ち替え
        input_cube = s_right(input_cube)
        
    elif input_key == "a":#左に持ち替え
        input_cube = s_left(input_cube)
        
    elif input_key == "u":#上部右回転
        input_cube = r_u_right(input_cube)
        
    elif input_key == "y":#上部左回転
        input_cube = r_u_left(input_cube)
        
    elif input_key == "j":#下部右回転
        input_cube = r_l_right(input_cube)
        
    elif input_key == "h":#下部左回転
        input_cube = r_l_left(input_cube)
    
    elif input_key == "i":#右側奥回転
        input_cube = r_b_right(input_cube)
        
    elif input_key == "k":#右側手前回転
        input_cube = r_f_right(input_cube)
        
    elif input_key == "t":#左側奥回転
        input_cube = r_b_left(input_cube)
        
    elif input_key == "g":#左側手前回転
        input_cube = r_f_left(input_cube)
               
    elif input_key == "n":#手前右回転
        input_cube = r_r_flont(input_cube)
        
    elif input_key == "b":#手前左回転
        input_cube = r_l_flont(input_cube)
        
    elif input_key == "8":#奥右回転
        input_cube = r_r_back(input_cube)
        
    elif input_key == "7":#奥左回転
        input_cube = r_l_back(input_cube)
        
    return input_cube


#------------------------------------------------------------------------------
#　色表示設定

import re
color_dic = {'r':'\033[41m', 'g':'\033[42m', 'o':'\033[43m', 'b':'\033[44m', 'p':'\033[45m', 'w':'\033[47m', 'end':'\033[0m'}

def print_hl(text):
    list = ["r","g","o","b","p","w"]
    for color in list:
        for kw in color:
            bef = kw
            aft = color_dic[color] + kw + color_dic["end"]
            text = re.sub(bef, aft, text)
    return(text)