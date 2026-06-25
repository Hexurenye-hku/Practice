'''
练习:写一个 Student(学生)类
属性需求:

name(姓名)
__score(分数,私有)
__id(学号,私有)

行为需求,你自己判断每条该用什么方式实现——这是这道题的重点,我不告诉你哪个该开 getter、哪个该开 setter、哪个都不开:

外部需要能查看学生的分数:getter
外部需要能修改学生的分数,但分数必须在 0 到 100 之间,超出范围不允许修改(这里要卡条件):setter
外部需要能查看学号:getter
学号一旦创建就不允许任何修改(想想现实:学号是注册时定的,之后不会变):都不开
'''
class Student(object):
    def __init__(self, name, id, score):
        self.name = name
        self.__id = id
        self.__score = score

    def get_score(self):
            return self.__score
    
    def set_score(self, score):
        if score >=0 and score <= 100:
            self.__score = score
            return True
        else:
            return False
        
    def get_id(self):
        return self.__id
    
bruce = Student('Bruce', '3036615370', 99) # 分数是要参与大小比较的,必须是数字。改成 99(整数)。

print(bruce.name)
print(bruce.get_score())
print(bruce.get_id())

bruce.set_score(85)
print(bruce.get_score())


bruce.set_score(999)
print(bruce.get_score())