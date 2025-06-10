import tkinter as tk
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
        display = []
        for y in range(len(self.course)):
            row = ""
            for x in range(len(self.course[0])):
                if x == self.x and y == self.y:
                    row += self.cartype + "  "
                else:
                    row += self.course[y][x]+ "  "
            display.append(row)
        return "\n".join(display)
        
    def move(self):
        dx, dy = self.direction
        self.x += dx*self.speed
        self.y += dy*self.speed
        self.show_position()
        
        if self.course[self.y][self.x] == "x":
            self.condition = "Corse Out!!"
            print(self.condition)
            


class GameApp:
    def __init__(self, root, car):
        self.root = root
        self.car = car

        root.title("レースゲーム")

        # 左：コース表示
        self.course_label = tk.Label(root, text=self.car.show_position(), font=("TakaoGothic", 20), justify="center")
        self.course_label.pack(side="left", padx=20, pady=20)

        # 右：操作ボタン
        control_frame = tk.Frame(root)
        control_frame.pack(side="right", padx=20, pady=20)

        tk.Button(control_frame, text="加速", command=self.accelerate).pack(pady=5)
        tk.Button(control_frame, text="左折", command=self.turn_right).pack(pady=5)
        tk.Button(control_frame, text="右折", command=self.turn_left).pack(pady=5)
        tk.Button(control_frame, text="直進", command=self.move_straight).pack(pady=5)
        tk.Button(control_frame, text="ブレーキ", command=self.brake).pack(pady=5)

    def update_display(self):
        self.course_label.config(text=self.car.show_position())

    def accelerate(self):
        self.car.accele()
        self.update_display()

    def turn_left(self):
        self.car.hundle(1)
        self.update_display()

    def turn_right(self):
        self.car.hundle(-1)
        self.update_display()

    def move_straight(self):
        self.car.move()
        self.update_display()
    
    def brake(self):
        self.car.brake(-1)
        self.update_display()

# メイン処理
if __name__ == "__main__":
    with open("race.csv", newline='', encoding="utf-8-sig") as f:
        reader = csv.reader(f, delimiter=',')  # タブ区切り対応
        course = [row for row in reader]
    
    root = tk.Tk()
    car = car(course)
    app = GameApp(root, car)
    root.mainloop()