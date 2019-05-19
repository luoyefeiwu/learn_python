#### 说明
1. 学习使用django
2. 命令总结
### Django常用命令如下:

|任务 | 命名|
|:---:|:---:|
| 创建新项目 | django-admin.py startproject project_name<br>(注意: windows系统下请用django-admin startproject xxx) 
| 创建新应用  | python manage.py startapp app_name<br>(注意: 你需要先cd进入创建的项目文件夹)|
|检测模型变化，生成新的数据库迁移文件   |   python manage.py makemigrations [app_label]<br>(注意: app名字可选。如果一个项目包含多个app，而你只更改了其中一个app的模型，建议后面加入具体的app名)|
|同步数据库与模型   |   python manage.py migrate|
|启动服务器 |   python manage.py runserver|
|创建超级用户   |   python manage.py createsuperuser|
|修改用户密码   |   python manage.py changepassword username|
|打开交互终端   |   python manage.py shell<br>python manage.py dbshell(数据库交互)|
|查看当前版本   |   python manage.py version|

### django-admin.py和manage.py其它命令

|命令|用途|
|:---:|:---:|
|python manage.py flush | 清空数据库内容，只留下空表|
|python manage.py test  |	开始测试|
|python manage.py collectstatic | 搜集静态文件|
|python manage.py createcachetable  | 创建缓存表|
|python manage.py check |   检测项目有没有问题|
|python manage.py inspectdb [table]	|   根据已有数据库反向生成django模型。你可以选择数据表名字|
|python manage.py makemessages	|   搜集所有的messages，可以生成指定文件格式如xml文件，供后期翻译|
|python manage.py sendemail [email]	|发送测试邮件|
|python manage.py showmigrations	|   显示所有数据库迁移文件|