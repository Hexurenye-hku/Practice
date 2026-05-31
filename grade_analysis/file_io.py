import csv

# 实现 read_data。要求：
# 读取 CSV 文件
# 表头单独处理（不放进 data 里，或者放进去但后面能区分）
# 数据行的分数转成 int，不要留成字符串
# 用 try/except 处理 FileNotFoundError
def read_data(csvname, data):
    try:
        with open(csvname, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)

            for row in reader:
                for i in range(2,5):
                    row[i] = int(row[i])
                data.append(row)
        
        return data
    except FileNotFoundError as e:
        print(e)


# 把结果写进新csv:
# data1 是 {'平均分情况': {...}, '最高分情况': {...}, '最低分情况': {...}}
# data2 是 {'第1名': '...', '第2名': '...', '第3名': '...'}
# data3 是 [['李娜', '数学', 55], ...]
def write_data(newcsv,  ahl_res, rank_res, fail_res):

    ahl_names = ['科目', '平均分', '最高分', '最低分']
    rank_names = ['排名', '姓名', '总分']
    fail_names = ['不及格学生','科目','分数']
    subjects = ['语文', '数学', '英语']

    with open(newcsv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(ahl_names)

        for subject in subjects:
            writer.writerow([subject, f'{ahl_res['平均分情况'][subject]:.2f}', ahl_res['最高分情况'][subject], ahl_res['最低分情况'][subject]])     
                
    with open(newcsv, 'a', newline='', encoding='utf-8') as f1:
        writer1 = csv.writer(f1)
        writer1.writerow(rank_names)
        for i,v  in rank_res.items():
            
            writer1.writerow([i, v[0], v[1]])

    with open(newcsv, 'a', newline='', encoding='utf-8') as f2:
        writer2 = csv.writer(f2)
        writer2.writerow(fail_names)
        for line in fail_res:
            writer2.writerow(line)
    
    print(f"\n学生情况已保存到：{newcsv}。")
