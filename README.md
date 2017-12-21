# 下厨房 API

下厨房官方并没有放出 API，本着自己动手丰衣足食的理念，配合 [Toapi](https://github.com/gaojiuli/toapi) 快速实现了一个 API.

目前实现的接口有`搜索`、`分页`、`列表`和`详细内容` 4 个部分。

## Overview

本项目是基于新生的开源项目 [Toapi](https://githu
b.com/gaojiuli/toapi) 快速实现的产物，由于该项目处于刚起步状态，很多特性都处于非稳定状态，随时会发生变更（如路由 `route` 匹配规则就在本项目诞生的时候发生了变更），所以不建议在生产环境中使用。

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
toapi run
```

## Example

搜索

> GET `/search/<keyword>`

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

> GET `/recipe/<no>/`

```json
{
    "Content": [
        {
            "cover": "http://s2.cdn.xiachufang.com/59f01d9a877011e6b87c0242ac110003_2622w_2064h.jpg?imageView2/2/w/660/interlace/1/q/90",
            "grade": "8.5",
            "materials": [
                {
                    "name": "鸡蛋",
                    "unit": "2个"
                },
                {
                    "name": "温水",
                    "unit": "200克"
                },
                {
                    "name": "盐",
                    "unit": "1/4勺"
                },
                {
                    "name": "香葱",
                    "unit": "少许"
                },
                {
                    "name": "香油",
                    "unit": "少许"
                },
                {
                    "name": "生抽",
                    "unit": "少许"
                }
            ],
            "name": "蒸鸡蛋",
            "steps": [
                {
                    "desc": "鸡蛋打入碗入打散，注入温水搅匀，加入盐调味，将混合好的蛋液过筛两至三遍",
                    "img": "",
                    "step": 1
                },
                {
                    "desc": "盖上保鲜膜，放入蒸锅，大火加热，当蒸锅中的水沸腾后转为小火蒸10分钟，关火，焖几分钟。",
                    "img": "",
                    "step": 2
                },
                {
                    "desc": "取出，撒上香葱，淋上香油、生抽，开吃",
                    "img": "",
                    "step": 3
                }
            ],
            "tip": "几点体会，1、鸡蛋与水的比例是1:1，如果想嫩些可1:1.5；2、加温水（大约40度）搅匀；3、至少过筛两遍；4、蒸前盖上保鲜膜；5、大火加热沸腾后转小火；6、大约蒸10分钟焖几分钟。另外，如果要添加虾仁，可在小火蒸到七八分钟蛋液凝固到一定的程度时，把保鲜膜打开将虾仁放在蛋羹上，继续盖上保鲜膜，蒸2至3分钟关火，再焖几分钟。"
        }
    ]
}
```

