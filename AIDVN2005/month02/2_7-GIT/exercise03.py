"""
    文件括号验证匹配
        用户可以根据 input() 选择一个文本文件
        (存在大量的括号(),[],{},《》，但是这些括号可能存在匹配不正确的情况)，
        判断文件中扣号匹配是否正确，
        如果正确则回复完全正确的信息，
        如果不正确，需要告知提示不正确，并且指出括号不正确的位置。
"""


class MyList:
    """
        充当容器，存储左括号
    """

    def __init__(self):
        self._elem = []

    def push(self, val):
        """
            尾部增加一项
        """
        self._elem.append(val)

    def pop(self):
        """
            删除尾部一项
        """
        return self._elem.pop()

    def empty(self):
        """
            判断列表是否为空
        """
        return self._elem == []


class Ver:
    """
        用来验证括号思路
    """

    def __init__(self):
        self.parents = "{}[]()"
        self.left_parent = "{[("
        self.opposite = {'}': '{', ')': '(', ']': '['}
        self.vessel = MyList()

    def parent(self, text):
        """
            生成器： 遍历字符串, 提供括号字符及其位置
        """
        i, len_text = 0, len(text)
        # 循环遍历字符串
        while True:
            while i < len_text and text[i] not in self.parents:
                i += 1
            if i >= len_text:
                return
            else:
                yield text[i], i
                i += 1

    def ver(self, text):
        """
            文件是否匹配的验证工作
        """
        for pr, i in self.parent(text):
            if pr in self.left_parent:
                self.vessel.push((pr, i))
            elif self.vessel.empty() or self.vessel.pop()[0] != self.opposite[pr]:
                print("UnMatching is found at %d for %s" % (i, pr))
                break
        else:
            if self.vessel.empty():
                print("All parentheses are matched")
            else:
                p = self.vessel.pop()
                print("UnMatching is found at %d for %s" % (p[1], p[0]))


if __name__ == '__main__':
    file = input(">>>")
    v = Ver()
    with open(file) as f:
        v.ver(f.read())
