# UOJ->Hydro转换器

感谢：https://github.com/FireInIceCode/UojSpiderForHydro

## 简介

可以爬取题面和数据,传统题可以自动根据problemconf配置生成config.yaml.并转化成Hydro格式,可以直接压缩导入.

需要管理员权限账户.

## 使用

运行

```
pip install -r requirements.py
```

修改authen.py的内容，具体定义见注释


然后运行spider.py,输入cookie和.支持命令
```
python spider.py 
```

- all 下载所有题
- ps [pids] 下载指定题号,多个题目id用空格分隔
- cookie [newcookie] 重设cookie
- quit 退出