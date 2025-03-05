# 软件设计与分析课程作业

## 核心技术栈

| 技术              | 版本      | 用途         |
| ----------------- | --------- | ------------ |
| Python            | 3.10+     | 核心编程语言 |
| CustomTkinter     | 5.2.0+    | UI 框架      |
| Pillow            | 10.0.0+   | 图像处理     |
| Threading/Asyncio | 内置      | 异步任务处理 |
| SQLite/SQLAlchemy | 内置/2.0+ | 数据存储     |

## 模块设计

```
project/
├── main.py                 # 程序入口点
├── app/
│   ├── __init__.py
│   ├── controllers/        # 控制器模块
│   │   ├── __init__.py
│   │   └── app_controller.py
│   ├── models/             # 数据模型
│   │   ├── __init__.py
│   │   └── data_model.py
│   ├── views/              # 视图模块
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   └── widgets/
│   │       ├── __init__.py
│   │       └── custom_widgets.py
│   └── utils/              # 工具和辅助函数
│       ├── __init__.py
│       ├── config.py
│       └── helpers.py
├── resources/              # 资源文件
│   ├── images/
│   └── themes/
├── data/                   # 数据文件
├── tests/                  # 测试
└── requirements.txt        # 依赖列表
```

## License
This work is published under [GNU GPLv3][GPLv3] License.

[GPLv3]: LICENSE
