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
