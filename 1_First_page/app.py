from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # 返回的内容会显示在浏览器中
    # return 'Welcome to My Watchlist!, hello'
    # 浏览器会以 HTML 的形式渲染返回值
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

# 通过访问 http://localhost:12345/home 来访问该页面
# 修改了路由，需要在后面加上 /home
@app.route('/home')
def home():
    return 'Welcome to My Watchlist!, home'

# 通过访问 http://localhost:12345/user/xxx 来访问该页面
# xxx 为任意字符串
# 通过 <> 来定义路由中的变量，变量名需要与函数中的参数名一致
@app.route('/user/<name>')
def user_page(name):
    # 通过传入的 name 参数来返回不同的内容
    return 'User page: %s' % name
    # return 'User page'




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6009, debug=True)