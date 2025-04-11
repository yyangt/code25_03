from flask import Flask, make_response
app = Flask(__name__)

@app.route('/data')
def get_data():
    # 创建一个响应对象，内容为JSON格式的字符串
    resp = make_response('{"key": "value"}')
    
    # 设置Cache-Control头，指定缓存时间为3600秒（1小时）
    resp.headers['Cache-Control'] = 'max-age=3600'
    
    # 返回响应对象
    return resp

if __name__ == '__main__':
    app.run()