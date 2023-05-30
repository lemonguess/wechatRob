from crawls.zhihu import zhihu_xiaoshuo
from utils.log_util import Logger
logger = Logger().get_logger()

def zhihu_xiaoshuo_spider(url):
    zhihu_xiaoshuo.zhxs_main(url)
    logger.info("完成")

if __name__ == '__main__':
    url = "https://www.zhihu.com/market/paid_column/1575901064246743040/section/1622203480050905088"
    zhihu_xiaoshuo_spider(url)