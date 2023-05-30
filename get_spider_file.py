from crawls.zhihu import zhihu_xiaoshuo
import os
def get_file_path(msg):

    # 知乎专栏小说爬虫
    if msg.startswith("https://www.zhihu.com/market/paid_column/"):
        file_name = zhihu_xiaoshuo.zhxs_main(msg)
        file_path = os.getcwd() + os.sep + file_name.replace('/', '\\')
        return file_path
    else:
        return ''