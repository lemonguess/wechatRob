import chardet

def zh_to_unicode(chinese_str):
    """
    中文转Unicode编码
    :param chinese_str:
    :return:
    """
    unicode_str = chinese_str.encode("unicode_escape").decode()
    return unicode_str


def unicode_to_zh(unicode_str):
    """
    Unicode编码转中文
    :param unicode_str:
    :return:
    """
    chinese_str = bytes(unicode_str, 'utf-8').decode('unicode_escape')
    return chinese_str

def get_encode():
    """
    获取文件编码格式
    :return:
    """
    import chardet

    with open('50_1.xml', 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']
    return encoding
if __name__ == '__main__':
    strings = "中文"
    print(zh_to_unicode(strings))
    unicode_str = "\\u4e2d\\u6587"
    print(unicode_to_zh(unicode_str))