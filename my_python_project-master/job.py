from flask import Flask, render_template

# 初始化app
app = Flask(__name__)
#11111
# 设置响应请求的目录
@app.route('/')
def index():
    return render_template("job.html")

if __name__ == '__main__':
    app.run() # 启动服务