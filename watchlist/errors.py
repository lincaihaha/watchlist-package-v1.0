
from flask import render_template
from watchlist import app

# 错误处理函数
@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    
    print("==============================")
    return render_template('errors/404.html'), 404  # 返回模板和状态码