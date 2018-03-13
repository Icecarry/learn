--01 mysql 数据库的操作

    -- 链接数据库
	mysql -uroot -p密码


    
	-- 不显示密码
	  mysql -uroot -p
    密码:mysql
    -- 退出数据库
    --quit/exit/ctrl + d
    exit
    quit/exit /ctrl+d
    

    -- sql语句最后需要有分号;结尾
    -- 显示数据库版本 version
    select version();

    -- 显示时间 now
	select now();
    
	-- 查看当前使用的数据库
    select database();

    -- 查看所有数据库
	show databases;

    -- 创建数据库
    -- create database 数据库名 charset=utf8;
	create database python77 charset = utf8;

    -- 查看创建数据库的语句
    -- show create database 数据库名
   show create database python77;
     

    -- 使用数据库
    -- use 数据库的名字
    use database python77;

    -- 删除数据库
    -- drop database 数据库名;
   drop database python77;


--02 数据表的操作

    -- 查看当前数据库中所有表
   show tables;
    
varchar
    -- 创建表
	-- int unsigned 无符号整形
    -- auto_increment 表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值
    -- create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);
    create table class(
        classname (255),
        address int
        );

	

    -- 查看表结构
    -- desc 数据表的名字;
	desc class;
   
    -- 创建 classes 表(id、na        classname (255),
me)
    create table classes (
        id int unsigned primary key 
        auto_increment,
        name varchar(30) not null
        );
	
	
    -- 创建 students 表(id、name、age、high (decimal)、
    --gender (enum)、cls_id)
   create table students ( id int unsigned primary key auto_increment,
    name varchar(30),age int unsigned, high decimal(5,2),
    gender enum("男",'女','妖','保密') default '保密',cls_id int unsigned );
  
	

    -- 查看表的创建语句
    -- show create table 表名字;
    show create table classes;

    -- 修改表-添加字段 mascot (吉祥物)
    -- alter table 表名 add 列名 类型;
    alter table classes add mascot varchar(50);


    -- 修改表-修改字段：不重命名版
    -- alter table 表名 modify 列名 类型及约束;
   alter table classes modify mascot  varchar(20);
	


    -- 修改表-修改字段：重命名版
    -- alter table 表名 change 原名 新名 类型及约束;
	alter table classes change mascot jxw int unsigned;


    -- 修改表-删除字段
    -- alter table 表名 drop 列名;
    alter table classes drop jxw;
	


    -- 删除表
    -- drop table 表名;
    -- drop database 数据库;
    drop table classes;
    drop database python7;
   
   

    
--03 增删改查(curd)

    -- 增加
+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(20)      | NO   |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+
        -- 全列插入
        -- insert [into] 表名 values(...)
        -- 主键字段 可以用 0  null   default 来占位
        -- 向classes表中插入 一个班级
		--insert into 表名 (字段,name) values(值...)
        insert into classes (id ,name ) values(1 ,"python7");
            insert into classes (name ) values("python7");
                insert into classes values(102,"python7");


        -- 向students表插入 一个学生信息
+--------+-------------------------------------+------+-----+---------+----------------+
| Field  | Type                                | Null | Key | Default | Extra          |
+--------+-------------------------------------+------+-----+---------+----------------+
| id     | int(10) unsigned                    | NO   | PRI | NULL    | auto_increment |
| name   | varchar(20)                         | NO   |     | NULL    |                |
| age    | int(10) unsigned                    | YES  |     | NULL    |                |
| high   | decimal(5,2)                        | YES  |     | NULL    |                |
| gender | enum('男','女','中性','保密')       | YES  |     | 保密    |                |
| cls_id | int(11)                             | YES  |     | NULL    |                |
+--------+-------------------------------------+------+-----+---------+----------------+
		-- 全部插入
        insert into students (name,age,high,gender,cls_id) values("zhang",19,1.90,'男',1);
        -- 部分插入
        -- insert into 表名(列1,...) values(值1,...)
       

        -- 多行插入
        insert into students (name,age,high,gender,cls_id) values("zhang",19,1.90,'男',1),("main",19,1.90,4,1);
		


    -- 修改
    -- update 表名 set 列1=值1,列2=值2... where 条件;
        -- 全部修改
        update students set gender = 4;
		
		-- 按条件修改

        update students set gender = 3 where id = 3;
		
		-- 按条件修改多个值
		-- update students set gender ="",name = "xxx" where ;

		update students set gender = 3,high = 1.80 where id = 3;
		
    -- 查询基本使用
        -- 查询所有列
        -- select * from 表名;
        select * from students;

        ---定条件查询    
        
        select * from students where id = 4;


        -- 查询指定列
        -- select 列1,列2,... from 表名;
        select name,age from students;
        


        -- 可以使用as为列或表指定别名
        -- select 字段[as 别名] , 字段[as 别名] from 数据表;
        select name as 姓名 from students;


        -- 字段的顺序
        select age,name from students;
    

    -- 删除
        -- 物理删除
        -- delete from 表名 where 条件
      delete from students where id = 4;

        -- 逻辑删除
        -- 用一个字段来表示 这条信息是否已经不能再使用了
        -- 给students表添加一个 is_delete 字段 bit 类型
		--alter table 表名 add 字段 类型 default 默认值;
        alter table students add is_delete bit default 0;
        
		
	-- 数据库备份与恢复(了解)
		-- mysqldump –uroot –p 数据库名 > python.sql;
		-- mysql -uroot –p 新数据库名 < python.sql; # 注意导入的时候需要先要创建数据库
        mysqldump -uroot -p python7 > python7.sql

        mysql -uroot -p python7 < python7.sql


