import io, csv

# 1. 把一个字符串列表写入文件，每行一个 —— write_lines(filename, lines) :

def write_lines(filenames, lines):
    with open(filenames, 'w', encoding = 'utf-8', errors = 'ignore') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    
        return None

quotes = [
    "Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that distant afternoon when his father took him to discover ice. At that time Macondo was a village of twenty adobe houses, built on the bank of a river of clear water that ran along a bed of polished stones, which were white and enormous, like prehistoric eggs. The world was so recent that many things lacked names, and in order to indicate them it was necessary to point.\n多年以后，面对行刑队，奥雷里亚诺·布恩迪亚上校将会回想起父亲带他去见识冰块的那个遥远的下午。那时的马孔多是一个二十户人家的村落，泥巴和芦苇盖成的屋子沿河岸排开，湍急的河水清澈见底，河床里卵石洁白光滑宛如史前巨蛋。世界新生伊始，许多事物还没有名字，提到的时候尚需用手指指点点。",
    "\"Things have a life of their own,\" the gypsy proclaimed with a harsh accent. \"It's simply a matter of waking up their souls.\"\n“万物皆有灵，”吉普赛人用嘶哑的嗓音宣告，“只需唤起它们的灵性。”",
    "\"We have still not had a death,\" he said. \"A person does not belong to a place until there is someone dead under the ground.\"\nÚrsula replied with a soft firmness:\n\"If I have to die for the rest of you to stay here, I will die.\"\n“我们还没有死过人，”他说，“一个人只要没有个死去的亲人埋在地下，那他就还不属于这个地方。”\n乌苏拉温柔而坚决地反驳：\n“为了你们能留在这里，如果需要我死，那我就去死。”",
    "The secret of a good old age is simply an honorable pact with solitude.\n一个幸福晚年的秘诀不是别的，而是与孤寂签订一个体面的协定。",
    "The past was a lie, that memory has no return, that every spring gone by could never be recovered, and that the wildest and most tenacious love was an ephemeral truth in the end.\n过去都是假的，回忆是一条没有归途的路，以往的一切春天都无法复原，即使最狂乱且坚韧的爱情，归根结底也不过是一种瞬息即逝的现实。",
    "Before reaching the final line, however, he had already understood that he would never leave that room, for it was foreseen that the city of mirrors (or mirages) would be wiped out by the wind and exiled from the memory of men at the precise moment when Aureliano Babilonia would finish deciphering the parchments, and that everything written on them was unrepeatable since time immemorial and forever more, because races condemned to one hundred years of solitude did not have a second opportunity on earth.\n不过，在到达终行之前，他已经明白自己再也走不出这间屋子，因为根据预言，就在奥雷里亚诺·巴比伦破译完羊皮卷的瞬间，这座镜子之城（或蜃景之城）将会被飓风抹去，从世人的记忆中根除，羊皮卷上所载的一切将永远不会重现，自永远至永远，因为注定经受百年孤独的家族不会有第二次机会在大地上出现。",
    "\"There were more than three thousand of them,\" was all that José Arcadio Segundo said. \"I'm sure now that everybody who was on the station was killed.\"\n\"There haven't been any dead in Macondo,\" he said. \"Since the time of Colonel Aureliano Buendía there hasn't been anything or anybody in this town that deserves to be worried about.\"\n“应该有三千多人，”他只说了这么一句话，“现在我确信车站上所有的人都死了。”\n“马孔多没有发生过任何事，现在没有将来也没有。这是一个幸福的村庄。”"
]

# write_lines('iotest.txt', quotes)

# 2. 读取文件，返回一个字符串列表（每行一个元素，去掉换行符）—— read_lines(filename)  
def read_lines(filename):
    str_lines = []
    with open(filename, 'r', encoding = 'utf-8', errors = 'ignore') as f:
        for line in f.readlines():
           line = line.strip()
           str_lines.append(line)
        
        return str_lines


lines = read_lines('iotest.txt')
# print(type(lines))   # 应该输出 <class 'list'>
# print(lines[0])      # 应该输出第一行，没有 \n

# 3. 读取一个CSV文件，打印每一行的内容（每行是一个列表）—— read_csv(filename)
def read_csv(fliename):
    with open(fliename, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)

# read_csv('iotest.csv')

# 4. # 把一个二维列表写入CSV文件 —— write_csv(filename, rows)
# 例如：rows = [["姓名","分数"], ["张三", 90], ["李四", 85]] 
def write_csv(filename, rows):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

data = [
    ["ID", "姓名",  "年龄", "分数", "是否合格"],
    [1,    "张三",  22,     85.5,   True],
    [2,    "李四",  20,     92.0,   True],
    [3,    "王五",  23,     78.3,   False],
    [4,    "赵六",  21,     88.7,   True],
    [5,    "孙七",  19,     95.2,   True],
    [6,    "周八",  22,     67.5,   False]
]

write_csv('datatest2.csv', data)

read_csv('datatest2.csv')