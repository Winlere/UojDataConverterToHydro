# UOJ->Hydro转换器

感谢：https://github.com/FireInIceCode/UojSpiderForHydro

## 简介

可以爬取题面和数据,传统题可以自动根据problemconf配置生成config.yaml.并转化成Hydro格式,可以直接压缩导入.

需要管理员权限账户.

## 使用

第一步安装依赖，运行

```
pip install -r requirements.py
```

第二步修改authen.py的内容，具体定义见注释

第三步运行spider, 根据提示输入管理员(需要是超级管理员&题目管理员)账号的cookie

```
python spider.py 
```

支持命令

- all 下载所有题
- ps [pids] 下载指定题号,多个题目id用空格分隔
- cookie [newcookie] 重设cookie
- quit 退出