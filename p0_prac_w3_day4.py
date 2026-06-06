'''
任务一：词频统计

写一个程序，输入一段英文文本（字符串），输出出现频率最高的 10 个词和它们的次数。

要求：
- 不区分大小写（The 和 the 算同一个词）
- 去掉标点符号（至少处理 . , ! ? " ' ( ) 这几个）
- 输出格式：the: 15，按频率从高到低排列
- 不准用 Counter

'''
def words_frequency(s):
    
    s = s.lower()
    
    for i in s:
        if i in ['.', ',', '!', '?', '"', '\'','(', ')','-']:
           s = s.replace(i, ' ')
    
    s_list = s.split()

    s_dict = {}

    for i in s_list:
        if i not in s_dict:
            s_dict[i] = 1
        else: 
            s_dict[i] = s_dict[i] + 1
    
    sorted_s = dict(sorted(s_dict.items(), key = lambda x:x[1], reverse=True)[:10])

    return sorted_s

# s1 = """Sundar Pichai, CEO of Alphabet and Google, said: “2026 is off to a terrific start. Our AI investments and full stack approach are lighting up every part of the business. Search had a strong quarter with AI experiences driving usage, queries at an all time high, and 19% revenue growth. Google Cloud revenues grew 63% with backlog nearly doubling quarter on quarter to over $460 billion. This was our strongest quarter ever for our consumer AI plans, driven by the Gemini App. Overall the number of paid subscriptions has now reached 350 million, with YouTube and Google One being the key drivers. Gemini Enterprise has great momentum with 40% quarter on quarter growth in paid monthly active users. And, finally, I’m pleased to see Waymo surpass 500,000 fully autonomous rides a week. These outstanding results are built on our differentiated, full stack approach. Our first-party models, like Gemini, are now processing more than 16 billion tokens per minute via direct API use by our customers, up 60% from last quarter. It’s really exciting to see how our AI investments are delivering value for our users, customers and business.”"""
# print(words_frequency(s1))


'''
任务二：简单通讯录

写一个命令行通讯录程序，支持以下操作：
- 添加联系人（姓名 + 电话）
- 查找联系人（输入姓名，返回电话）
- 删除联系人
- 显示所有联系人
- 退出程序

要求：
- 用字典存储数据
- 用 while True + input() 实现交互循环
- 输入非法指令时提示"无效操作"，不崩溃

'''

def add_contact(dict, name, phonenumber):
    dict[name] = phonenumber
    print(f"已添加: {name.capitalize()} --> {phonenumber}")

def find_contact(dict, name):
    if name in dict:
        number = dict[name]
        print(f"{name.capitalize()}'s phonenumber is {number}.")
    else:
        print(f"{name.capitalize()} is not in the contact address.")

def delete_contact(dict, name):
    if name in dict:
        dict.pop(name)
        print(f'{name.capitalize()} 已删除')
    else:
        print(f"联系人 {name.capitalize()} 不存在")

def view_all_contact(dict):
    for name,number in dict.items():
        print(f'{name.capitalize()}: {number}')

def main():
    contact_dict = {}

    while True:
        print("""
本程序支持：
- 添加联系人（姓名 + 电话）>>> add(name, number)
- 查找联系人（输入姓名，返回电话）>>> find(name)
- 删除联系人 >>> delete(name)
- 显示所有联系人 >>> view all
         """)
        
        user_input = input("请输入内容（输入q退出）：")

        # exit condition
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("程序已退出")
            break

        # bussiness logic
        
        #add
        if user_input.lower().startswith('add(') and user_input.endswith(")"):
            content = user_input[4:-1]

            try:
                name, number = content.split(',')
                name = name.strip().lower()
                number = number.strip()

                add_contact(contact_dict, name, number)  

            except:
                print("格式错误，应为: add(name, number)")     

        #find
        if user_input.lower().startswith("find(") and user_input.endswith(")"):
            name = user_input[5:-1]

            try:
                name = name.strip().lower()

                find_contact(contact_dict, name)
            
            except:
                print("格式错误，应为: find(name)")

        #delete
        if user_input.lower().startswith('delete(') and user_input.endswith(")"):
            content = user_input[7:-1]

            try:
                content = content.strip().lower()

                delete_contact(contact_dict, content)
            
            except:
                print("格式错误，应为: delete(name)")
       
        #view
        if user_input.lower() == 'view all':
            try:
                view_all_contact(contact_dict)
            except:
                print("格式错误，应为:view all")

if __name__ == "__main__":
    main()