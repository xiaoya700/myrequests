# myrequests

在用requests过程中，只要一个url请求错误，或者出现未响应，
那么整个程序就中断了，每次都写异常捕获未免很麻烦；
每次要传入user-agent也很麻烦，干脆封装成一个库

只是改写requests的Session类的request方法，
api与requests完全一致，
所以可以很方便的改回requests


**增加了以下功能：**

- 打印每次请求的url
- 不传入headers参数，则每次请求会随机选择一个user-agent组成headers
- 默认请求的等待时间缩短为3s，请求无响应会等待0.5s重新尝试，至多4次
- 返回状态码非200也会等待0.5s后重新尝试，至多4次，可以应对抓取过快，服务器返回错误状态码情况
- 4次失败后，不会抛出异常，会打印错误信息，返回None，并在当前目录下生成错误信息文件


### Usage

```python
import myrequests as requests # 推荐这么写


url = 'https://www.baidu.com'
r = requests.get(url)
if r:
    print(r.text)
```