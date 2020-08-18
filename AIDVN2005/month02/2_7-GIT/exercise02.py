"""
    一个文件，文件名："talk.txt"。
    在文件中保存着一些对话信息，格式如下：
    通过程序将该文件进行分离，每个人的说话内容，
    重新写入到一个新文件中，文件以这个人的名字命名。
    思路：
        1. 打开文件
        2. 遍历文件 --> 记录每个人说话内容 --> 字典存储{人：[x,x1,x2]}
        3. 写文件
"""

person = {}

file = open('talk.txt', 'r')
for line in file:
    if line[0:] != '\n':
        (role, line_spoken) = line.split(':', 1)
        if role not in person:
            person[role] = [line_spoken]
        else:
            person[role].append(line_spoken)

file.close()

for name in person:
    with open(name + '.txt', 'w') as fw:
        fw.writelines(person[name])
