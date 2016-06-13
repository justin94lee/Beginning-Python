#!/usr/bin/python
# -*- coding: utf-8 -*-

# try: / except: / finally: 处理机制

#try:
#    print 'try...'
#    r = 10 / 5
#    print 'rusult:', r
#except ZeroDivisionError,e:
#    print 'except：', e
#finally:
#    print 'finally...'
#print 'END'
    
'''
# except捕捉多个错误
except (ZeroDivisionError, TypeError, NameError):

# 捕捉对象
except (ZeroDivisionError, TypeError), e:

# finally 子句
不管异常是否发生都会执行

# 异常之禅
try/except 还是 if/else

'''

#try:
#    x = input('input1>>>')
#    y = input('input2>>>')
#    
#    print x / y
#except (ZeroDivisionError, TypeError), e:
#    print e

###############################################################################

#while True:
#    try:
#        x = input('Enter the 1st number: ')
#        y = input('Enter the 2nd number: ')
#        
#        value = x / y
#        print 'x/y is ', value
#    except:
#        print 'Invaild input. Plz try again'
#    else:
#        break
        
# 只有在没有引发异常才能退出次循环

###############################################################################

'''
# 调试
断言 assert
增加一个条件，为真就什么都不做

Import logging
loggong.basicConfig(level=logging.INFO)
打印错误记录,level有debug，info，warning，error等几个级别

pbd调试工具
pdb.set_trace()
'''

n = input('>>>')
def foo(n):
    assert n != 0, 'Zero Error'
    return n / 1
foo(n)

###############################################################################

