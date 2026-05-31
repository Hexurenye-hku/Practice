
def avg(lst):
    return sum(lst) / len(lst) if lst else 0

# 实现 ahl_score，要求：
# 计算语文、数学、英语三科各自的平均分、最高分、最低分
# return {'平均分情况' : avg_res, '最高分情况' : max_res, '最低分情况' : min_res}
def ahl_score(data):
    
    headers = ['语文', '数学', '英语']

    score_lst = []
    avg_lst = []
    max_lst = []
    min_lst = []

    for i in range(2,5):
        score = []

        for line in data:
            score.append(line[i])

        score_lst.append(score)
        
    for subject in score_lst:
        avg_lst.append(avg(subject))
        max_lst.append(max(subject))
        min_lst.append(min(subject))

    avg_res = dict(zip(headers, avg_lst))
    max_res = dict(zip(headers, max_lst))
    min_res = dict(zip(headers, min_lst))

    print('平均分情况:') 
    print(avg_res)
    print('最高分情况：')
    print(max_res)
    print('最低分情况：' )
    print(min_res)

    return {'平均分情况' : avg_res, '最高分情况' : max_res, '最低分情况' : min_res}

# 实现 total_rank3，要求：
# 计算每个学生的总分
# 输出总分前3名的姓名和总分
# return total_res, total_res = {'第1名': "('孙丽', 278)", '第2名': "('周婷', 277)", '第3名': "('王芳', 274)"}
def total_rank3(data):
    stu_ts = {}
    total_res = {}

    for line in data:
        stu_ts[line[1]] = line[2] + line[3] + line[4]

    top_3 = sorted(stu_ts.items(), key=lambda x:x[1], reverse=True)[:3]
    
    print("总分前3名的学生:")
    for i in range(0,3):
        print(f'第{i+1}名: {top_3[i]}')
        total_res[f'第{i+1}名'] = top_3[i]

    return total_res

# 实现 failed_list，要求：
# 找出任何一科不及格（<60分）的学生
# 输出姓名和具体哪科不及格、分数是多少
#  return total_failed, total_failed = [['李娜', '数学', 55], ['刘洋', '语文', 45], ['赵磊', '语文', 55], ['赵磊', '数学', 48], ['赵磊', '英语', 51], ['吴军', '英语', 58], ['朱强', '语文', 50], ['朱强', '数学', 44], ['胡斌', '语文', 43], ['胡斌', '数学', 38], ['胡斌', '英语', 55]]
def failed_list(data):

    total_failed = []

    header = ['语文', '数学', '英语']

    for line in data:

        for i in range(2,5):
            if line[i] < 60:
                total_failed.append([line[1], header[i-2], line[i]])
            
    print('不及格情况如下：')
    print(total_failed)

    return total_failed
