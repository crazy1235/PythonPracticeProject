# -*- coding: utf-8 -*-
import math
import logging
from logging import log as logger
import os

# 导入模块

print '------------ 导入模块 ------------'

print math.pow(2, 0.5)
print math.pow(3, 2)
print math.pow(3, 3)
print math.pi

print 'from math import pow, sin, log  这种写法直接饮用pow，sin，log这三个函数，math包下的其他函数没有导入进来'

print '如果遇到不同模块下函数名相同，则可以通过模块名引用函数名来调用，或者对函数起一个别名'

print math.log(10)

print logging.log(10, 'something')

print logger(10, 'something')

#
print os.path.isdir(r'C:\windows')
print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')

# 动态导入模块

print '------------ 动态导入模块 --------------'

print '有时候，两个不同的模块提供了相同的功能，比如StringIO和cStringIO都提供了StringIO这个功能 \n' \
      '因为Python是动态语言，解释执行，因此python代码运行速度慢。\n' \
      '如果要提高python代码的运行速度，最简单的办法就是把某些关键函数用c语言重写，这样就能大大提高运行速度。\n' \
      '同样的功能，StringIO是纯python代码编写的，而cStringIO部分函数是C写的，因此cStringIO运行速度更快。'

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

print '上述代码现场时从cStringIO导入，如果失败了（比如cStringIO没有被安装），再尝试从StringIO导入\n' \
      '这样，如果cStringIO模块存在，则可以获得更快的执行速度，如果cStringIO不存在，则代码运行速度变慢，但不影响正常执行！'

print  '--------------------------'

try:
    import json
except ImportError:
    from simplejson import json

print json.dumps({'python': 2.7})

# _future_
print 'Python的新版本会引入一些新的功能，但是实际上在上一个老版本就已经存在了。\n' \
      '要试用这些新特性，就可以导入_future_模块的某些功能来实现！'

print 'Python2.7的整数出发运算结果仍是整数；但是Python3.x已近改进了整数的出发运算，"/"除将得到浮点数，"//"除得到的是整数'

print 10 / 3

# from __future__ import division

print 10 / 3

# 安装第三方模块
print '两种模块管理工具\n' \
      '1. easy_install \n' \
      '2. pip 这是官方推荐的方式'


