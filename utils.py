class button:
    def __init__(self, x, y, lenght, width):
        self.x = x
        self.y = y
        self.l = lenght
        self.w = width
        self.msg = ''

    def isSelected(self,x,y):
        return self.x <= x <= self.x + self.l and self.y <= y <= self.y + self.l
    
    def setMsg(self, msg):
        self.msg = msg