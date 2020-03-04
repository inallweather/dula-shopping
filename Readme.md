# 嘟啦购物商城
## 系统环境搭建
> 1. 使用官网推荐的包管理工具 Pipenv,具体配置可以查看github上的pipenv
>    安装使用 python3 -m pip install pipenv
> 2. 系统使用 python3.6 + flask 1.1 + mysql 5.2,具体python3.6的
>    的安装，flask及mysql安装请参照相关官方安装方法。

## 使用方法
> 1. git https://github.com/inallweather/dula-shopping.git
>    存放在本地的一个文件夹下面，然后通过终端进入这个项目的根目录下，执行
>    pipenv install，这个命令会自动创建虚拟环境及安装相应程序所需要的
>    包，用pycharm打开后，把刚才创建的虚拟环境配置给解析器
> 2. 通过终端登录到mysql数据库，然后执行命令：
>```
>    create database dulashopping default charset utf8;
>  ```  
> 3. 在pycharm里面找到shopping这个应用，在这个目录下有一个config.py
>    修改数据库的登录用户名及密码及地址
>
> 4. 在项目根目录下，执行数据库的迁移：
>```
>    python3 shopping.py db init
>    python3 shopping.py db migrate
>    python3 shopping.py db upgrade
>    这时可以去数据库当查看是否有表，或着在执行这些命令时是否报错
> ```
>然后在终端执行
>```
> python3 shopping.py runserver
>```
>运行项目
>
>查看是否已经改了

