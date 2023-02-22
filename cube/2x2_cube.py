import numpy as np
import rotate
import random

#------------------------------------------------------------------------------
#　初期設定


# キューブ：計算用
cube = np.array([\
               [[" "," "," "," "],\
               [" ","bb","bb"," "],\
               [" ","bb","bb"," "],\
               [" "," "," "," "]],\
                   \
               [[" ","oo","oo"," "],\
               ["rr"," "," ","pp"],\
               ["rr"," "," ","pp"],\
               [" ","gg","gg"," "]],\
                   \
               [[" ","oo","oo"," "],\
               ["rr"," "," ","pp"],\
               ["rr"," "," ","pp"],\
               [" ","gg","gg"," "]],\
                   \
               [[" "," "," "," "],\
               [" ","ww","ww"," "],\
               [" ","ww","ww"," "],\
               [" "," "," "," "]]],dtype=str)


# キューブ：表示用　（色をつけるため）
cube_display = str(cube)
cube_display =rotate.print_hl(cube_display)


# 混ぜる用のコマンドリスト
command_list = ["a","w","s","d","7","8","t","y","u","i","g","h","j","k","b","n"]


#------------------------------------------------------------------------------
#　メイン動作

while True:

    # キューブ表示
    print(cube_display)

    # コマンド入力
    print("==== コマンド一覧 ========================")
    print("持替え -----> 奥：w 手前：s 左：a 右：d")
    print("上面 ------> 右：u 左：y")
    print("下面 ------> 右：j 左：h")
    print("右側面 ----> 奥：i 手前：k")
    print("左側面 ----> 奥：t 手前：g")
    print("奥面 ------> 右：8 左：7")
    print("手前面 ----> 右：n 左：b")
    print("その他 -----> 混ぜる：mix 終了:end")
    print("========================================")
    revolution = input("コマンドを入力してください ---> ")
    
    # コマンド処理
    if revolution == "mix":# 混ぜる
        n = int(input("混ぜる回数を入力して下さい。 ---> "))
        i = 0
        
        for i in range(n):# 実際に混ぜるプログラム
            input_key = random.choice(command_list)
            cube = rotate.rotate(input_key,cube)
            
    if revolution == "end":# 終了
        break
    
    else:# 回転
        cube = rotate.rotate(revolution,cube)
    
    #　キューブ表示用に色付け
    cube_display = str(cube)
    cube_display = rotate.print_hl(cube_display)
