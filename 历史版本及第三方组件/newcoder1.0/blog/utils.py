import hashlib

# 加密函数sha256,生成一个64位的字符串
def encryption(data):
    hash = hashlib.sha256()
    hash.update(data.encode('utf8'))
    return hash.hexdigest()