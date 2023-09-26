# flask + pyecharts + pyinstaller 示例程序
- 离线环境可运行

## 参考
- [脱离http server离线使用本地echart资源](https://zhuanlan.zhihu.com/p/586325992)
- [pycharts打包文档](https://pyecharts.org/#/zh-cn/pyinstaller_pack)
- [解决flask找不到templates静态问题](https://github.com/ciscomonkey/flask-pyinstaller/tree/master)

## 对应html使用`url_for`连接到本地pychart
- 在`__init__.py`中进行了如下设置
  ```python
    if getattr(sys, 'frozen', False):
        template_folder = os.path.join(sys._MEIPASS, 'templates')
        static_folder = os.path.join(sys._MEIPASS, 'static')
        print(template_folder,static_folder)
        test_app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    else:
        test_app = Flask(__name__)
  ```
  - 这样设置只要`url_for`中有`static`便会找到该文件夹的本地**绝对**地址
- 添加`build.py`在打包时候将静态文件打包
  - `'--add-data', './app/static/js/*;static/js',`添加js静态文件
- 在`.html`中进行如下设置
  - `<script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>`以便请求请求静态文件
- `resources` *不知道是不是有用*
  - 在`Lib\site-packages`中找到pyechart然后将`datasets`与`templates`复制进去

## 目录结构
├─.venv
│  ├─Include
│  ├─Lib
│  │  └─site-packages 各类包
│  │      
│  └─Scripts
├─app
│  ├─static
│  │  ├─js
│  │  └─pycharts-dep 作用不明
│  │      
│  ├─templates
│  └─__pycache__
├─build pyinstaller
├─dist
├─resources
│  ├─datasets
│  │  └─__pycache__
│  └─templates
└─__pycache__