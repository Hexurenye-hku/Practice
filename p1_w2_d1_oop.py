# 题 1：定义一个 Student 类，初始化时接收 name（姓名）和 score（分数），写一个方法 get_grade()，根据分数返回等级：90分及以上返回 'A'，75-89 返回 'B'，60-74 返回 'C'，60分以下返回 'F'。
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 75: # elif 链的标准写法：每个条件只写下界，上界交给前面的条件处理。
            return 'B'
        elif self.score >= 60:
            return 'C'
        else:
            return 'F'
        
# 题 2：定义一个 Rectangle 类，初始化时接收 width 和 height，写两个方法：area() 返回面积，perimeter() 返回周长。
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.height + self.width) * 2