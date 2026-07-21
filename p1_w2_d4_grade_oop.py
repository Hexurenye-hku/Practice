import csv

class Student(object):
    def __init__(self, stu_id, name, chi_score, math_score, eng_score):
        self.stu_id = stu_id
        self.name = name
        self.chi_score = chi_score
        self.math_score = math_score
        self.eng_score = eng_score
    
    def total_score(self):
        return self.chi_score + self.math_score + self.eng_score

class ClassRoom(object):
    def __init__(self, stu_list):
        self.students = stu_list

    def get_failed(self):
        failed_stu = []

        for stu in self.students:
            if stu.chi_score < 60 or stu.math_score < 60 or stu.eng_score < 60:
                failed_stu.append(stu)
        
        return failed_stu
    
    def rank(self):
        ranking_stu = sorted(self.students, key = lambda x: x.total_score(), reverse=True)
        return ranking_stu

    def ahl_score(self):

        subject_stats = {}

        subjects = ['chi_score', 'math_score', 'eng_score']

        for subject in subjects:
            subject_stat = {}

            subject_scores = [getattr(stu, subject) for stu in self.students]

            subject_avg = sum(subject_scores) / len(subject_scores)
            subject_stat['avg'] = subject_avg
            
            subject_max = max(subject_scores)
            subject_stat['max'] = subject_max

            subject_min = min(subject_scores)
            subject_stat['min'] = subject_min

            subject_stats[subject] = subject_stat
    
        return subject_stats

def read_data(csv_in):
    with open(csv_in, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        stus_data = []

        for row in reader:
            stu = Student(int(row['学号']), row['姓名'], int(row['语文']), int(row['数学']), int(row['英语']))
            stus_data.append(stu)
        
    return stus_data

class_rm = ClassRoom(read_data('students.csv'))
ahl_score = class_rm.ahl_score()
rank = class_rm.rank()
failed = class_rm.get_failed()



def write_data(csv_out, ahl_score, rank, failed):


    ahl_names = ['科目', '平均分', '最高分', '最低分']
    rank_names = ['排名', '姓名', '总分']
    fail_names = ['不及格学生','科目','分数']
    subjects = {'语文':'chi_score', '数学':'math_score', '英语':'eng_score'}        

    with open(csv_out, 'w', newline='', encoding='utf-8') as f0:
        writer = csv.writer(f0)
        
        writer.writerow(["平均分情况如下:"])
        writer.writerow(ahl_names)
        for subject, code in subjects.items():
            writer.writerow([subject, f"{ahl_score[code]['avg']:.2f}", f"{ahl_score[code]['max']:.2f}",f"{ahl_score[code]['min']:.2f}"] )

    # 竞赛式排名来自分数比较:某人的名次 =(总分严格高于他的人数)+ 1
    scores = [x.total_score() for x in rank]
    
    with open(csv_out,'a', newline='', encoding='utf-8') as f1:
        writer1 = csv.writer(f1)

        writer1.writerow(["排名情况如下: "])
        writer1.writerow(rank_names)
        for stu in rank:

            count = 0
            for score in scores:
                if score > stu.total_score():
                    count += 1

            count += 1
            rank_no = count

            writer1.writerow([f'第{rank_no}名', stu.name, stu.total_score()])
    

    with open(csv_out,'a', newline='', encoding='utf-8') as f2:
        writer2 = csv.writer(f2)

        writer2.writerow(["不及格情况如下: "])
        writer2.writerow(fail_names)
        for stu in failed:
           for subject, attr in subjects.items():
               score = getattr(stu, attr)
               if score < 60:
                   writer2.writerow([stu.name, subject, score])

write_data('students_oop.csv', ahl_score, rank, failed)