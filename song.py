# coding: utf-8
# auther: Loveice
# 代码唱歌


import winsound
X = 1
Y = 0.5 
_s = 392 * X 
_L = 440 * X 
D = 524 * X 
R = 578 * X 
M = 660 * X 
F = 698 * X 
S = 784 * X 
L = 880 * X 
T = 500 
winsound.Beep (_L,T)
winsound.Beep (_L,T / 2) 
winsound.Beep (_s,T / 2) 
winsound.Beep (_L,T)
winsound.Beep (_L,T / 2) 
winsound.Beep (_L,T / 2)
winsound.Beep (D,T )
winsound.Beep (R,T / 2)
winsound.Beep (D,T / 2) 
winsound.Beep (_L,T * 2)
time.sleep(Y) 
