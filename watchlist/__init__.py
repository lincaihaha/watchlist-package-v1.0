from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

#实例化
app=Flask(__name__)
# 初始化扩展，传入程序实例 app   config会增大开销
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'dev'  # 等同于 app.secret_key = 'dev'

db=SQLAlchemy(app) # 实例化数据库
login_manager = LoginManager(app)  # 实例化扩展类


#登陆管理器
@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    from watchlist.models import User
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    login_manager.login_view = 'login' # 配合登陆保护装饰器使用  未登录直接定位到login视图
    return user  # 返回用户对象

# 上下文处理函数  返回的数据所有模板都可以使用
@app.context_processor
def inject_user():  # 函数名可以随意修改
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)  # 需要返回字典，等同于 return {'user': user}



from watchlist import views, errors, commands