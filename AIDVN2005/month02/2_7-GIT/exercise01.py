"""
    在文件中匹配地址
    利用所给文件完成：编写一个函数，传入端口名称，
    返回这个端口运行情况中所表述的 `address` 地址信息。
    提示：
        -   每段之间有空行
        -   每段单词是端口号
        -   端口名可能很复杂
"""

import re


def get_address(port):
    """
        根据端口号返回对应的 address
    :param port: 端口名称
    :return: 端口对应的地址
    """
    file = open('exc.txt')
    while True:
        data = ""
        for line in file:
            if line == "\n":
                break
            data += line
        if not data:
            return "没有找到该端口"
        # 匹配端口号
        obj = re.match(r'\S+', data)
        if port == obj.group():
            # pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
            pattern = r'(\d{1,3}\.){3}\d{1,3}/\d{2}|Unknown'
            res = re.search(pattern, data)
            if res:
                return res.group()

if __name__ == '__main__':
    port = input(">>>")
    print(get_address(port))
