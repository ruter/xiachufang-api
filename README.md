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

> GET `/recipe/<no>/`

```json
{
    "Content": [
        {
            "cover": "http://s2.cdn.xiachufang.com/9dc3e8a0873711e6b87c0242ac110003_680w_453h.jpg?imageView2/2/w/660/interlace/1/q/90",
            "grade": "8.1",
            "materials": [
                {
                    "name": "排骨",
                    "unit": ""
                },
                {
                    "name": "葱",
                    "unit": ""
                },
                {
                    "name": "姜",
                    "unit": ""
                },
                {
                    "name": "蒜",
                    "unit": ""
                },
                {
                    "name": "盐",
                    "unit": ""
                },
                {
                    "name": "生抽",
                    "unit": ""
                },
                {
                    "name": "老抽",
                    "unit": ""
                },
                {
                    "name": "料酒",
                    "unit": ""
                },
                {
                    "name": "白糖",
                    "unit": ""
                },
                {
                    "name": "鸡精",
                    "unit": ""
                }
            ],
            "name": "红烧排骨",
            "steps": [
                {
                    "desc": "排骨斩小块，冲洗干净；\n*前排的肉质会更嫩",
                    "img": "http://s2.cdn.xiachufang.com/50e67c7e8cc711e6a9a10242ac110002_214w_129h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 1
                },
                {
                    "desc": "先放锅里氽一遍水，为了去除血水；\n\n*焯水，就是将初步加工的原料放在开水锅中加热至半熟或全熟，取出以备进一步烹调或调味。它是烹调中特别是冷拌菜不可缺少的一道工序。对菜肴的色、香、味，特别是色起着关键作用。 焯水的应用范围较广，大部分蔬菜和带有腥膻气味的肉类原料都需要焯水。焯水，又称出水、飞水、淖水。\n\n1、 切好的肉（排骨、大块肉、鸡肉等）在开水中焯一下，可以去除肉原料中的血沫。\n2、 肉类原料经过开水焯过后变色即可，捞出沥干水分后可以进行下一步的烹调。",
                    "img": "http://s2.cdn.xiachufang.com/5106e5548cc711e6a9a10242ac110002_215w_143h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 2
                },
                {
                    "desc": "煮开后，用清水冲去浮沫，捞起来沥干水份；",
                    "img": "http://s2.cdn.xiachufang.com/51214f488cc711e6b87c0242ac110003_212w_142h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 3
                },
                {
                    "desc": "锅里热油，爆香葱姜蒜；",
                    "img": "http://s2.cdn.xiachufang.com/51490c9a8cc711e6b87c0242ac110003_216w_144h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 4
                },
                {
                    "desc": "倒入排骨，煸炒；",
                    "img": "http://s2.cdn.xiachufang.com/516554fe8cc711e6a9a10242ac110002_218w_147h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 5
                },
                {
                    "desc": "至排骨两面焦黄；",
                    "img": "http://s2.cdn.xiachufang.com/518c00d68cc711e6a9a10242ac110002_219w_148h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 6
                },
                {
                    "desc": "倒入生抽、老抽、料酒翻炒上色后，再倒入热开水，大概与排骨持平；\n\n* 炖肉要使用热水，不要加冷水。\n\n*生抽：老抽比例为2：1\n\n生抽老抽酱油:\n生抽、老抽都属于酱油，酱油是总称。\n生抽和老抽区别：\n生抽＝颜色较浅，酱味较浅，咸味较重，较鲜，多用于调味；\n老抽＝颜色较深，酱味浓郁，鲜味较低，故有加入草菇以提高其鲜味的草菇老抽等产品，一般用于给菜肴上色",
                    "img": "http://s2.cdn.xiachufang.com/51acc42e8cc711e6b87c0242ac110003_218w_148h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 7
                },
                {
                    "desc": "加锅盖，大火烧开水后转中小火继续烧；\n\n*肉质的软烂程度跟烧的时间也有很大关系。在烧煮过程，盐要迟放，水要一次加足，如果发现水太少，应加开水。\n\n*可以的话用连汤带肉转砂锅或者陶瓷锅之类的烧口感会更好~",
                    "img": "http://s2.cdn.xiachufang.com/51cb07b88cc711e6b87c0242ac110003_218w_147h.jpg?imageView2/2/w/300/interlace/1/q/90",
                    "step": 8
                },
                {
                    "desc": "最后至汤汁剩1/4多点，调入一点盐和白糖，鸡精，转大火收汁，即可。\n\n*收汁是烹调的一个手法，指的是把汤汁熬浓，菜肴在煸炒中的汤汁经过加热，由多到少，由稀到稠，可增加菜的浓度和香味、光泽。例如烹制红烧肉、红烧鱼等菜肴，通常最后一道工序就是大！火！把汤熬浓至黏稠，然后盛出肉或者鱼装盘，最后把锅底的浓汁倒在肉或者鱼的上面。",
                    "img": "http://s1.cdn.xiachufang.com/51e0073a8cc711e6a9a10242ac110002_218w_136h.jpg@2o_50sh_1pr_1l_300w_90q_1wh",
                    "step": 9
                }
            ],
            "tip": "红烧菜的制作要点如下：1、肉要煸透，鱼要煎香　　所谓煸透，就是指将锅内所有的肉块煸炒变色，肥肉冒油，见有亮光。一般市场上买的肉，最好先用水焯一下，再煸炒。焯的意义在于去除肉中的残血和腥味，煸炒时不要放太多油，煸炒完后要出些炒出的猪油，才能做到肥而不腻。如果做红烧鱼，一定要新鲜鱼，等煎至两面金黄，表面有一层薄薄的硬皮时方可出锅待烧。2、先上色，后加水，一步到位　　当原料煸炒或煎好后，倒入绍酒、老抽等作料。等酱油的颜色附着在原料上后，再加鲜汤或水。如果不等原料上色就放水，调料被水稀释，成菜就会灰白无光。　　汤水一次放足，中途不要续水，一定记住还要盖上锅盖。烧肉最好淹过原料，烧鱼可以少一些。一般说下汤以原料的2倍左右为宜，当烧至占原料的1/4时起锅。收汁不要过紧，过紧汤汁浓稠，会失去红烧菜的特色，勾芡也不要过浓，勾少许水淀粉，使汁明芡亮，主料突出。　　而且，两头用旺火，中间用中小火，下主料用急火烧开，撇净浮沫，调好口味，中火慢慢焖煮，烧至原料酥烂，使味汁渗入原料内部，最后用急火收浓汤汁即成。3、调色调味　　红烧菜的初步上色，是与烹调加工同时达到的，红烧鱼过油时即炸成浅红色，在正式烹调时上色需借助糖色、酱油、料酒、葡萄酒等提色，但注意不要上色过重，以免影响色泽。红烧菜口味以咸鲜为主，略带甜味，主要是用酱油调味，糖的用量要适度，宜少不宜多。　　红烧汁一般的比例是生抽：老抽：白糖　=　2：1：适量4、文火肉，急火鱼　　肉类大火烧开后应调文火炖煮，当原料接近酥烂时，要立即转入大火收浓汤汁，而鱼类，则应该全程使用大火烧煮，水量要一次性加足，收干汤汁后即可调味出锅，煎鱼的时候，热油后放入姜片，用铲子压着姜片在锅内抹一圈，这样鱼皮就不容易粘锅了，最好用不粘锅。"
        }
    ]
}
```

