import random

class Box():
    def __init__(self,num):
        self.num = num
        self.goal = False
        self.status = False

class BoxList():
    def __init__(self):
        self.goal,self.empty = random.sample(range(100),2)
        self.box_list = []
        for i in range(100):
            box = Box(i)
            if i == self.goal:
                box.goal = True
            self.box_list.append(box)
        self.target = self.box_list[random.randint(0,99)]

    def run(self):
        if self.target.goal:
            # for i in self.box_list:
            #     if i != self.goal or i != self.empty:
            #         i.status = True
            self.final_box = [self.target,self.box_list[self.empty]]
        else:
            # for i in self.box_list:
            #     if i != self.goal or i != self.target.num:
            #         i.status = True
            self.final_box = [self.target,self.box_list[self.goal]]
        self.switch()
        return bool(self.target.goal)

    def switch(self):
        self.target = self.final_box[1]


if __name__ == '__main__' :
    w = 0
    times = 100000
    for i in range(times):
        k = BoxList()
        if k.run():
            w += 1
    print(w/times)

















