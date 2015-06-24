#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS course;

    CREATE TABLE IF NOT EXISTS course  (
        cou_sn   INTEGER,     --序号
        cou_no   TEXT,        --学号
        name     TEXT,        --姓名
        pice     TEXT,        --出生日期
        sex      TEXT,        --性别
        notes    TEXT,        --班级
        PRIMARY KEY(cou_sn)
    );
    -- CREATE UNIQUE INDEX idx_course_no ON course(cou_no);

    CREATE SEQUENCE seq_cou_sn 
        START 10000 INCREMENT 1 OWNED BY course.cou_sn;

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句
    
def init_data():
    sqlstr = """
    DELETE FROM course;

    INSERT INTO course (cou_sn, cou_no, name, pice, sex, notes)  VALUES 
        (101, '1310650403',  '李德辉', '1994-12-27', '男', '信息1304'), 
        (102, '1310650401',  '王浩然', '1994-08-16', '男', '信息1304'),
        (103, '1310650410',  '赵志鹏', '1994-10-26', '男', '信息1304');

    """
    with db_cursor() as cur :
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')

