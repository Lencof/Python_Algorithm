# __Author__ __Lencof__
# spiral_sort.py

def spiralize(lop):
    
    def on_board(x, y):
        return 0 <= x < lop and 0 <= y < lop
        
    def is_one(x, y):
        return on_board(x, y) and spiral[y][x] == 1
        
    def can_move():
        return on_board(x+dx, y+dy) and not (is_one(x+2*dx, y+2*dy) or is_one(x+dx-dy, y+dy+dx) or is_one(x+dx+dy, y+dy-dx))
    
    spiral = [[0 for x in range(lop) for y in range(lop)]]
    x, y = -1, 0
    dx, dy = 1, 0
    turns = 0

    while (turns < 2):
        if can_move():
            x += dx
            y += dy
            spiral[y][x] = 1
            turns = 0
        else:
            dx, dy = -dy, dx
            turns += 1

    return spiral
