<<<<<<< HEAD
'''
    if x <= 11 and 5<=y<=11
    wincase1    x = x , y giam
    wincase2    x tang , y giam
    wincase3    x tang , y =y
    wincase4    x tang , y tang
    wincase5    x = x , y tang
'''
from time import perf_counter as clock
moves =[
[9,3],
[8,3],
[8,4],
[7,6],
[7,5],
[6,5],
[6,6],
[5,7],
[10,2]]

black = moves[::2]
white = moves[1::2]
def find_win(move,player_moves):
    x,y = move[0],move[1]
    lines = [([[x,y+i] for i in range(5)],[x,y-1],[x,y+5]),
            ([[x+i,y+i] for i in range(5)],[x-1,y-1],[x+5,y+5]),
            ([[x+i,y] for i in range(5)],[x-1,y],[x+5,y]),
            ([[x+i,y-i] for i in range(5)],[x-1,y+1],[x+5,y-5]),
            ([[x,y-i] for i in range(5)],[x,y+1],[x,y-5])]
    for line,first,last in lines:
        lst = []
        for i in range(len(line)):
            if line[i] in player_moves:
                lst.append(line[i])
            else:
                break 
        if len(lst)==5:
            if first in player_moves or last in player_moves:
                continue
            return lst
        
def helo(player_moves):
    a = clock()
    for move in player_moves:
        WIN = find_win(move,player_moves)
        if WIN != None:
            b = clock()
            return WIN, b-a
        
print(helo(black))
print(helo(white))
=======
'''
    if x <= 11 and 5<=y<=11
    wincase1    x = x , y giam
    wincase2    x tang , y giam
    wincase3    x tang , y =y
    wincase4    x tang , y tang
    wincase5    x = x , y tang
'''
from time import perf_counter as clock
moves =[[6,6],  
        [7,6],  
        [7,7],  
        [8,6],  
        [9,5],  
        [9,7],  
        [8,8],  
        [6,4],  
        [5,5],  
        [11,9], 
        [10,7],
        [7,5], 
        [8,4], 
        [10,8],[9,9]
                ]

black = moves[::2]
white = moves[1::2]
def check_wincases(cord):
    x,y = cord[0],cord[1]
    wincase5 = [[x,y+i] for i in range(5)]
    wincase4 = [[x+i,y+i] for i in range(5)]
    wincase3 = [[x+i,y] for i in range(5)]
    wincase2 = [[x+i,y-i] for i in range(5)]
    wincase1 = [[x,y-i] for i in range(5)]
    if x <= 10 and 4 <= y <= 10:
        return [wincase1,wincase2,wincase3,wincase4,wincase5]
    elif x <= 10 and y <= 4:
        return [wincase3,wincase4,wincase5]
    elif x <= 10 and y >= 11:
        return [wincase1,wincase2,wincase3]
    elif x >= 10:
        if y <= 3:
            return [wincase5]
        elif y >=11:
            return [wincase1]
        else:
            return [wincase1,wincase5]
def find_win(move,player_moves):
    x,y = move[0],move[1]
    lines = [[[x,y+i] for i in range(5)],
            [[x+i,y+i] for i in range(5)],
            [[x+i,y] for i in range(5)],
            [[x+i,y-i] for i in range(5)],
            [[x,y-i] for i in range(5)]]
    for line in lines:
        lst = []
        for i in range(len(line)):
            if line[i] in player_moves:
                lst.append(line[i])
            else:
                break 
        if len(lst)==5:
            rx = line[1][0] - line[0][0]
            ry = line[1][1] - line[0][1]
            if [line[0][0]-rx,line[0][1]-ry] in player_moves or [line[-1][0]+rx,line[-1][1]+ry]  in player_moves:
                continue
            return lst
        
def helo(player_moves):
    a = clock()
    move_pos = 0
    while move_pos< len(player_moves):
        WIN = find_win(player_moves[move_pos],player_moves)
        if WIN != None:
            b = clock()
            return WIN, b-a
        move_pos+= 1
print(helo(black))
print(helo(white))
>>>>>>> dae349fe6b721f6f82bbea89e5e577c9d6f5189f
