'''
    if x <= 11 and 5<=y<=11
    wincase1    x = x , y giam
    wincase2    x tang , y giam
    wincase3    x tang , y =y
    wincase4    x tang , y tang
    wincase5    x = x , y tang
'''
from time import perf_counter as clock
a = clock()
moves =    [[7,7],  
            [8,7],  
            [8,8],  
            [8,6],  
            [5,5],  
            [6,5],  
            [10,10],
            [7,9],  
            [9,9],  
            [11,11],
            [6,6]
            ]
for i in range(len(moves)):
    for j in range(2):
        moves[i][j]+=1

black = moves[::2]
white = moves[1::2]
def check_wincases(cord):
    x,y = cord[0],cord[1]
    area_mid = eval('x <= 11 and 5 <= y <= 11')
    area_top = eval('x <= 11 and y <= 4')
    area_bot = eval('x <= 11 and y >= 12')
    area_spe = eval('x >= 12')
    if area_mid:
        return [1,2,3,4,5]
    elif area_top:
        return [3,4,5]
    elif area_bot:
        return [1,2,3]
    elif area_spe:
        if y <= 4:
            return [5]
        elif y >=12:
            return [1]
        else:
            return [1,5]
def convert_wincase(wincase,move):
    x,y = move[0],move[1]
    wincase5 = [[x,y],[x,y+1],[x,y+2],[x,y+3],[x,y+4]]
    wincase4 = [[x,y],[x+1,y+1],[x+2,y+2],[x+3,y+3],[x+4,y+4]]
    wincase3 = [[x,y],[x+1,y],[x+2,y],[x+3,y],[x+4,y]]
    wincase2 = [[x,y],[x+1,y-1],[x+2,y-2],[x+3,y-3],[x+4,y-4]]
    wincase1 = [[x,y],[x,y-1],[x,y-2],[x,y-3],[x,y-4]]
    if wincase == [1,2,3,4,5]:
        return list((wincase1,wincase2,wincase3,wincase4,wincase5))
    if wincase == [3,4,5]:
        return list((wincase3,wincase4,wincase5))
    if wincase == [1,2,3]:
        return list((wincase1,wincase2,wincase3))
    if wincase == [5]:
        return wincase5
    if wincase == [1]:
        return wincase1
    if wincase == [1,5]:
        return list((wincase1,wincase5))
def find_win(win_lines,player):
    
    for line in win_lines:
        lst = []
        for i in range(len(line)):
            if line[i] in player:
                lst.append(line[i])
            else:
                break
        if len(lst)==5:
            return lst
        
def helo(moves):
    for move in moves:
        wincases = check_wincases(move)
        win_lines = convert_wincase(wincases,move)
        WIN = find_win(win_lines,moves)
        if WIN != None:
            return WIN 
print(helo(black))
print(helo(white))
b = clock()
print(b-a)











