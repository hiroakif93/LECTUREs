import random
import csv

class car:
    
    def __init__(self, course):   
        self.course = course
        self.speed = 0
        self.condition = 0
        self.direction = [1, 0]
        self.x = 0
        self.y = 0
        
        self.cartype =  "🚗"
        self.turn = 0
    
    def accele(self, pow=1):
        self.speed += 1
        self.move()
        
    def brake(self, pow=1):
        self.speed -= 1 
        self.move()
        
    def hundle(self, action):
        self.condition = action
        
        if self.condition == 1:
            self.turn += 1
            self.turn_dir()
            self.move()
            self.condition = 0
        elif self.condition == -1:
            self.turn -= 1
            self.turn_dir()
            self.move()
            self.condition = 0
        else:
            self.turn = 0
            self.condition = 0
    
    def turn_dir(self):
        
        if self.turn >3:
            self.turn=0
        if self.turn < 0:
            self.turn=3
            
        if self.turn==0:
            self.direction = (1, 0)
            self.cartype =  "🚗"
        elif self.turn == 1:
            self.direction = (0, 1)
            self.cartype =  "🚘"
        elif self.turn == 2:
            self.direction = (-1, 0)
            self.cartype =  "🚗"
        else:
            self.direction = (0, -1) 
            self.cartype =  "🚘"
    
    def show_place(self):
        _course = self.course.copy()
        _course[self.x][self.y] = self.cartype
        for i in _course:
            print("".join(i))    
    def show_position(self):
        print("=== 現在のコース ===")
        for y in range(len(self.course)):
            row_str = ""
            for x in range(len(self.course[0])):
                if x == self.x and y == self.y:
                    row_str += self.cartype
                else:
                    row_str += self.course[y][x]+"  "
            print(row_str)
        print()    
        
    def move(self):
        dx, dy = self.direction
        self.x += dx*self.speed
        self.y += dy*self.speed
        self.show_position()
        
        if self.course[self.y][self.x] == "x":
            self.condition = "Corse Out!!"
            print(self.condition)

class truck(car):
    def __init__(self, course):
        super().__init__(course)      # 親クラスの初期化を呼び出す
        self.cartype = "🚚"
        
    def brake(self, pow=1):
        self.speed -= 5 * pow

class sports(car):
    def __init__(self, course):
        super().__init__(course)      # 親クラスの初期化を呼び出す
        self.cartype = "🏎️"
        
    def accele(self, pow=1):
        self.speed += 20 * pow  # 通常より2倍加速
       


if __name__ == "__main__":
    
    with open("race.csv", newline='', encoding="utf-8-sig") as f:
        reader = csv.reader(f, delimiter=',')  # タブ区切り対応
        course = [row for row in reader]
    
    mycar = car(course)    
    mycar = sports(course)    
          
    while mycar.course[mycar.y][mycar.x] != "G":
                
        myaction = int(input("行動を選んでください\n1:加速\n2:左折\n3:右折\n4:ブレーキ\n5:そのまま\n"))
        
        if myaction == 1:
            mycar.accele()
        elif myaction == 2:
            mycar.hundle(1)
        elif myaction == 3:
            mycar.hundle(-1)
        elif myaction == 4:
            mycar.brake(-1)
        else:
            mycar.move()        
        
        
        
        
                    