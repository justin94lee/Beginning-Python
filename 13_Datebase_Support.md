## Python DB  API

### 全局变量

任何支持DB API 2.0 版本的数据库模块都必须定义3个描述模块特性的全局变量

* apilevel ,是一个字符串常量，提供正在使用的API 版本号

* threadsafety ,是一个取值范围0~3的整数

* parastyle ,参数风格

### 异常

### 连接和游标

connect 函数

connect(dsn, user, passwd, host, datebase)

connect 函数的方法

    close()

    commit()

    rollback()

    cursor()

### 类型

### SQLite

    import sqlite3
    conn = sqlite3.connect('some.db')

    curs = conn.cursor()
    # 获得游标

    conn.commit()

    conn.close()
    
