from django.template import Library  # 导入模板中的库模块
import datetime, pytz
import math

# 创建一个库对象
register = Library()

# 处理时间展示
@register.filter(name="mytime")
def handletime(value):
    # 当前的时间(把没有时区的时间对象，转化成上海时区的对象)
    ctime = datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai"))

    # 过去的时间
    otime = value

    # 计算差值(datetime.timedelta对象)
    dtime = ctime - otime
    days = dtime.days
    seconds = dtime.seconds
    if days <= 0:
        if seconds // 60 < 60:
            return "{}分钟前".format(math.floor(seconds / 60)+1)
        elif seconds // 3600 < 24:
            return "{}小时前".format(seconds // 3600)
    elif days < 7:
        return "{}天前".format(days)
    else:
        return value