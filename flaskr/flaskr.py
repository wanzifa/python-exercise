#这个地方coding:utf-8似乎没啥用？
# coding: utf-8

#把所有的import引入给写全
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


#配置信息
DATABASE = 'c://flaskr//flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# 写个实例
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True) # override!


#连接指定的数据库，这里应该是配置信息里的datebase
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


#初始化数据库
def init_db():
    “”“函数/类注释建议写在函数/类的内部”“”
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


#请求数据库连接（这地方说实话没懂那个after_request和那个teardown_request的特征和区别）
@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    """teardowm_request就是即使服务器出现异常，也会执行操作
       这里的操作就是关闭数据库连接"""
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


#show_entries应该就是传说中的一个视图函数。。。然后route（）函数用来告诉Flask
#用于显示函数的url
@app.route('/')
def show_entries():
    “”“这里是flask原生的操作数据库的方式,即直接通过cur执行sql语句”“”
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


#当url为···/add时 返回一个错误提示页面
#但是对这个里面的代码不是很理解，总感觉这个模块没什么意义（逃
#这里除了给出url，还给出了http请求方法post，post是允许提交的请求方法。
#这里有个小问题：post是不是也能执行get的功能？想一想只有get了才能显示才能提交咩~（逃
@app.route('/add', methods=['POST'])  # methods 默认是包含GET的:)
def add_entry():
    """写文章"""
    if not session.get('logged_in'):
        # 如果没有登录，引发401错误(无权限)
        abort(401)
    # 否则，执行sql语句向数据库中添加文章
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    # 将文章提交到数据库中
    g.db.commit()
    # 消息闪现
    flash('New entry was successfully posted')
    # 重定向
    return redirect(url_for('show_entries'))


#登入函数。这里和上面格式一样，没太懂这里为啥还专门强调了个get
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = '该用户名不存在'
        elif request.form['password'] != app.config['PASSWORD']:
            error = '密码无效'
        else:
            session['logged_in'] = True
            flash('登陆成功啊哈哈哈！')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


#登出函数
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('您已登出')
    return redirect(url_for('show_entries'))

#只有这个模块被直接调用时，app才能运行起来
if __name__ == '__main__':
    app.run()
