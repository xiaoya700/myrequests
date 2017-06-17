### 说明

requests是一个相当相当棒的库, 让写爬虫变得如此简单, 但为了保持通用性?, 某些地方它让我们自己发挥, 如每次请求的headers, 我们就要自己添加; 爬取过程中出现的一些异常情况, 我们需要自己写try-except处理等.
但根据我实际写爬虫的经验来看, 这一部分的代码很多都是重复的, 每次都写一遍, 就很不pythonic, 所以我封装了这个库, 能够简化代码，节省时间.

因为只是改写requests的Session类的request方法，api与requests完全一致，所以可以很方便的改回requests.


### 增加功能

- 打印每次请求的url
- 不传入headers参数，则每次请求会随机选择一个user-agent组成headers
- 默认请求的等待时间缩短为2s，请求无响应会等待1s重新尝试，至多4次
- 返回状态码非200也会等待1s后重新尝试，至多4次，可以应对抓取过快，服务器返回错误状态码情况
- 4次失败后，不抛出异常，会打印错误信息，返回None，并在当前目录下生成错误信息文件


### Useage

```python
import myrequests as requests # 推荐这么写


url = 'https://www.baidu.com'
r = requests.get(url)
if r:
    print(r.text)
```