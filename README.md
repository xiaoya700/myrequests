### 说明

加强requests的信息提示和健壮性.

API与requests完全一致, 所以可以很方便的改回requests.


### 增加功能

- 打印每次请求的url, 如: '[2018-05-18 18:00:19,745] [INFO] get: xxx.xxx.com', 可以关闭
- 默认请求的等待时间缩短为5s, 请求无响应会等待3s重新尝试, 至多4次
- 返回状态码非200或3XX, 会等待3s后重新尝试, 至多4次
- 出现 ConnectionError, ChunkedEncodingError 错误, 也会等待3s后重新尝试, 至多4次
- 4次失败后, 不抛出异常, 会打印错误信息, 返回None, 并在当前目录下生成错误信息文件MyRequestsError.log


### Useage

```python
import myrequests as requests # 推荐这么写

url = 'https://www.baidu.com'
r = requests.get(url)
if r:
    print(r.text)

# 不打印请求信息
from myrequests import logger
logger.close_print_info()
r = requests.get(url)
if r:
    print(r.text)
```


下载地址: 

github: [https://github.com/zzzzer91/myrequests](https://github.com/zzzzer91/myrequests)

另外附赠一个基于此的小爬虫, 呃, 就是抓取一些妹子图片啦, hh:

github: [https://github.com/zzzzer91/mzitu_spider](https://github.com/zzzzer91/mzitu_spider)
