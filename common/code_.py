
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

import random

from common import cache_


def send_code(phone):
    #生成code
    code_set = set()
    while len(code_set) < 4:
        code_set.add(str(random.randint(0.9)))
    code = ''.join(code_set)
    #保存code到缓存中，-redis
    cache_.save_code()
    #发送短信

    pass

def valid_code(phone, code):
    #从缓存中读取phone中的code（发送的code）
    #判断输入的code和缓存中的code是否相同
    code_cache = cache_.get_code(phone)
    return code_cache == code