# 下厨房 API

下厨房官方并没有放出 API，本着自己动手丰衣足食的理念，配合 [Toapi](https://github.com/gaojiuli/toapi) 快速实现了一个 API.

目前实现的接口有`搜索`、`分页`、`列表`、`分类`和`详细内容` 5 个部分。

## Overview

本项目是基于新生的开源项目 [Toapi](https://github.com/gaojiuli/toapi) 快速实现的产物， ~由于该项目处于刚起步状态，很多特性都处于非稳定状态，随时会发生变更（如路由 `route` 匹配规则就在本项目诞生的时候发生了变更），所以不建议在生产环境中使用。~ 项目已经发布正式版，可以放心使用。

## Usage

克隆项目或直接下载项目源码到本地

```bash
git clone https://github.com/ruter/xiachufang-api.git
```

安装依赖

```bash
cd xiachufang-api/
pip install -r requirements.txt
```

运行项目

```bash
python wsgi.py
```

访问 `http://your_server_ip:5000`

## Cache

`Toapi` 本身提供了 3 种缓存机制：

- `MemoryCache` - 服务重启后已缓存的数据都会销毁
- `RedisCache` - 需安装并启动 `Redis`
- `MemcachedCache` - 需安装并启动 `Memcached`

默认使用的是 `MemoryCache`，可以自己手动更改配置使用其他另外两种缓存方式。

为了方便使用，本项目已经在 `settings.py` 中默认配置了 `MemoryCache` 和 `RedisCache`，并且默认使用 `MemoryCache`.

若要使用 `RedisCache` 缓存，需要先修改 `app.py` 中的配置，并确保在运行该项目之前 `Redis` 的服务已经启动，以下是参考步骤

*app.py*

```python
# 全局替换 MemCacheSettings 为 RedisCacheSettings
# 共有两处需要修改，修改后如下

from settings import RedisCacheSettings

api = Api(URL, settings=RedisCacheSettings)
```

*settings.py*

```python
# 找到 class RedisCacheSettings(Settings)
# 检查 'cache_config' 里的配置和当前环境使用的 Redis 配置是否一致
# 这里使用的是默认配置

'cache_config': {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0
}
```

## Example

可请求的 `URI` 有 4 个：

- `/search/<keyword>`
- `/category/`
- `/category/<no>/` 和 `/category/<no>/?page=<page>`
- `/recipe/<no>/`

搜索菜谱

> GET `/search/鸡蛋`

```json
{
    "Page": [
        {
            "next": "/category/394/?page=2"
        }
    ],
    "Recipe": [
        {
            "cover": "http://s2.cdn.xiachufang.com/84c059f68aa211e6b87c0242ac110003_1536w_2048h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "虎皮蛋（爱吃卤鸡蛋的不容不过～）",
            "url": "/recipe/101772749/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/59f01d9a877011e6b87c0242ac110003_2622w_2064h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "蒸鸡蛋",
            "url": "/recipe/1052846/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/49fdcc782dc611e7947d0242ac110002_1488w_1984h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "卤鸡蛋",
            "url": "/recipe/102275135/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/c35432e086f711e6b87c0242ac110003_480w_640h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "葱花鸡蛋饼",
            "url": "/recipe/45007/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/a79c5420896c11e6a9a10242ac110002_1280w_1280h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "鸡蛋饼",
            "url": "/recipe/100553539/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/e0edf7e4876c11e6a9a10242ac110002_2448w_3264h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "鸡蛋汤面",
            "url": "/recipe/1050858/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/07145394876511e6a9a10242ac110002_500w_667h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "尖椒鸡蛋",
            "url": "/recipe/1047057/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/45bd2aa6882f11e6b87c0242ac110003_640w_638h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "正宗糖醋鸡蛋",
            "url": "/recipe/100133845/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/8d9f4042898911e6a9a10242ac110002_1280w_1280h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "鸡蛋米饭饼",
            "url": "/recipe/100564118/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/5a8ace493fda4d658883ffbc92f3e911_2304w_1536h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "鸡蛋小饼干",
            "url": "/recipe/102216617/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/289c5b70882c11e6a9a10242ac110002_650w_650h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "鸡蛋葱油饼",
            "url": "/recipe/100128338/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/a319b8bc8ac411e6a9a10242ac110002_1880w_1879h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "简单易学牛奶鸡蛋布丁",
            "url": "/recipe/101791580/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/fc88b1be86f011e6b87c0242ac110003_500w_633h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "鸡蛋土豆饼",
            "url": "/recipe/15758/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/e98ea8f05edd11e7bc9d0242ac110002_3024w_4032h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "虎皮鸡蛋",
            "url": "/recipe/102329470/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/fb63737a88f611e6b87c0242ac110003_750w_728h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "快手啤酒卤鸡蛋",
            "url": "/recipe/100475480/"
        },
        {
            "cover": "http://s1.cdn.xiachufang.com/c3f53dc8878011e6a9a10242ac110002_3088w_2056h.jpg@2o_50sh_1pr_1l_215w_136h_1c_1e_90q_1wh",
            "name": "剁椒鸡蛋",
            "url": "/recipe/1067968/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/99e123f888e811e6a9a10242ac110002_638w_638h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "鸡蛋芝士烤吐司",
            "url": "/recipe/100462057/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/9622c1568b8911e6a9a10242ac110002_1920w_1080h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "土豆丝鸡蛋饼",
            "url": "/recipe/101877531/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/2eb6a4ba899f11e6a9a10242ac110002_640w_640h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "西红柿鸡蛋",
            "url": "/recipe/100573951/"
        },
        {
            "cover": "http://s2.cdn.xiachufang.com/6bcc1b0288da11e6b87c0242ac110003_650w_650h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90",
            "name": "火腿肠葱花鸡蛋饼",
            "url": "/recipe/100448277/"
        }
    ]
}
```

获取详细菜谱

> GET `/recipe/101829462/`

```json
{
    "Content": [
        {
            "cover": "http://s2.cdn.xiachufang.com/d0cb97448b8c11e6a9a10242ac110002_1614w_1080h.jpg?imageView2/2/w/660/interlace/1/q/90",
            "grade": "8.5",
            "materials": [
                {
                    "name": "猪前蹄",
                    "unit": "一只"
                },
                {
                    "name": "冰糖",
                    "unit": "一块"
                },
                {
                    "name": "桂皮",
                    "unit": "二片"
                },
                {
                    "name": "八角",
                    "unit": "二个"
                },
                {
                    "name": "香叶",
                    "unit": "二片"
                },
                {
                    "name": "姜",
                    "unit": "一小块"
                },
                {
                    "name": "油",
                    "unit": "适量"
                },
                {
                    "name": "盐",
                    "unit": "适量"
                },
                {
                    "name": "生抽",
                    "unit": "适量"
                },
                {
                    "name": "白胡椒粉",
                    "unit": "适量"
                },
                {
                    "name": "豆腐乳",
                    "unit": "一块"
                },
                {
                    "name": "陈醋",
                    "unit": "一小勺"
                },
                {
                    "name": "啤酒.料酒或白酒",
                    "unit": "适量"
                },
                {
                    "name": "鸡精（可不放）",
                    "unit": "适量"
                }
            ],
            "name": "红烧猪蹄",
            "steps": [
                {
                    "desc": "猪蹄.让卖的师傅给处理干净.剁好..\n自己家是没办法剁的...\n\n猪蹄放入冷水锅中煮..\n煮开后.继续煮5分钟以上..\n然后捞出来..清洗干净备用！",
                    "img": "http://s1.cdn.xiachufang.com/d9c834a28dfc11e6a9a10242ac110002_1080w_1616h.jpg@2o_50sh_1pr_1l_300w_90q_1wh",
                    "step": 1
                },
                {
                    "desc": "锅里放油..冰糖放入.\n\n如果是整块的.\n小火加热一会儿.锅铲拍一下.\n冰糖会全部碎.",
                    "img": "http://s2.cdn.xiachufang.com/0aabdbe08b8d11e6a9a10242ac110002_1616w_1080h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 2
                },
                {
                    "desc": "小火.锅铲搅动.\n出现图片里的泡后.\n糖色就是炒好了..\n\n早了颜色不好看.\n晚了...会糊！！\n\n就好比女人..\n太年轻的木有味道.\n太老了.....\n\n一切.要刚刚好..",
                    "img": "http://s1.cdn.xiachufang.com/edfe036a8b8c11e6a9a10242ac110002_1616w_1080h.jpg@2o_50sh_1pr_1l_300w_90q_1wh",
                    "step": 3
                },
                {
                    "desc": "放入猪蹄翻炒.翻炒上色..",
                    "img": "http://s2.cdn.xiachufang.com/d96c03d08dfc11e6b87c0242ac110003_2048w_1536h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 4
                },
                {
                    "desc": "放入八角.桂皮.香叶.姜片....继续翻炒！",
                    "img": "http://s1.cdn.xiachufang.com/d8ed4e468dfc11e6a9a10242ac110002_1536w_2048h.jpg@2o_50sh_1pr_1l_300w_90q_1wh",
                    "step": 5
                },
                {
                    "desc": "炒出香味...\n\n不要怀疑自己的嗅觉或我的菜谱.\n不要凑锅里去闻香味出来木有.\n有可能..伱家抽油烟机风力太大..",
                    "img": "http://s1.cdn.xiachufang.com/d85363308dfc11e6a9a10242ac110002_1536w_2048h.jpg@2o_50sh_1pr_1l_300w_90q_1wh",
                    "step": 6
                },
                {
                    "desc": "放白胡椒粉.生抽..陈醋.",
                    "img": "http://s2.cdn.xiachufang.com/d7d9cbba8dfc11e6a9a10242ac110002_1536w_2048h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 7
                },
                {
                    "desc": "半瓶啤酒或二勺料酒.或一勺白酒...",
                    "img": "http://s2.cdn.xiachufang.com/d74b14748dfc11e6a9a10242ac110002_2048w_1536h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 8
                },
                {
                    "desc": "然后再加开水..倒入高压锅.\n上汽之后.\n改中小火压5分钟.\n愛吃特别烂的.可以多几分钟.\n\n反正....我又不吃！",
                    "img": "http://s2.cdn.xiachufang.com/d6d12aec8dfc11e6b87c0242ac110003_1536w_2048h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 9
                },
                {
                    "desc": "倒回锅里.加一块豆腐乳.捣碎..\n中小火焖煮！\n\n啥？没看见豆腐乳？\n喔..我家木有了.\n没放...=_=..",
                    "img": "http://s1.cdn.xiachufang.com/d55c85628dfc11e6a9a10242ac110002_1536w_2048h.jpg@2o_50sh_1pr_1l_300w_90q_1wh",
                    "step": 10
                },
                {
                    "desc": "汤汁收至剩一半时.\n放盐..大火收汁.\n\n成品颜色好看不好看.\n就看这一步了！",
                    "img": "http://s1.cdn.xiachufang.com/d4d5d13e8dfc11e6a9a10242ac110002_1536w_2048h.jpg@2o_50sh_1pr_1l_300w_90q_1wh",
                    "step": 11
                },
                {
                    "desc": "收干汁后...放一点鸡精.不放也行..",
                    "img": "http://s1.cdn.xiachufang.com/20a2d8868b8d11e6a9a10242ac110002_1614w_1080h.jpg@2o_50sh_1pr_1l_300w_90q_1wh",
                    "step": 12
                }
            ],
            "tip": "吃辣的话..后面丢几个小米椒.好好吃.不用高压锅或木有的.就在锅里直接加开水.尽量多加一些.烧开后.转小火慢炖.炖烂就行！但是后期一定要大火收汁！也可以放黄豆啥的.当然..催乳有良效.-_-#.."
        }
    ]
}
```

