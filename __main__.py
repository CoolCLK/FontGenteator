import os

# 此处可用于配置此脚本
# CONFIGURATION START
configuration_output_folder = './output/'
configuration_template_folder = './template/'
configuration_font_path = './font.ttc'
configuration_font_size = 30
configuration_font_color = (255, 0, 0)
def configuration_targets():
    # return list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()~`-=_+[]\\;\',./{}|:"<>?')
    l = []
    for c in range(256):
        l.append(chr(c))
    return l
def configuration_costume_format(font, char):
    return "文本//" + str(font.getname()[0]) + "//" + str(char)
# CONFIGURATION END

def configuration():
    if input("Install Pillow 9.5 library for setup the environment (Y/n) ").upper() == 'Y':
        os.system("python -m pip install Pillow==9.5")

configuration()

import random
from shutil import copy
import zipfile
from PIL import ImageFont, Image, ImageDraw
import json

def check_folder():
    if not os.path.exists(configuration_output_folder):
        os.mkdir(configuration_output_folder)
    if not os.path.exists(configuration_output_folder):
        os.mkdir(configuration_output_folder)

# 清空输出文件夹
def clear_output():
    del_list = os.listdir(configuration_output_folder)
    for f in del_list:
        file_path = os.path.join(configuration_output_folder, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

def copy_template():
    template_list = os.listdir(configuration_output_folder)
    for f in template_list:
        file_path = os.path.join(configuration_output_folder, f)
        if os.path.isfile(file_path):
            copy(file_path, './output')

def read_template():
    # 读取模板文件
    with open('./template/project.json', 'rb') as f:
        return json.load(f)

def save_assets():
    param = read_template()

    # 获取字体
    font = ImageFont.truetype(configuration_font_path, configuration_font_size)
    print('Using font ', font.getname(), ' sizes ', configuration_font_size)

    costume = {
        "isStage": False,
        "name": "Typer",
        "variables": {"Aqb[:,Kf5rsdNv@qw/WQ":["x",-10],"LwB!|[DK@6g+=c#Rr=R9":["y",160],"Z#}=veHk-!6=ohT5/l+U":["i",0]},
        "lists": {
        },
        "broadcasts": {
            "_b:9hNy/GS1IUj]X0qP.":"Remove all"
        },
        "blocks": {
            "B":{
                "opcode":"event_whenflagclicked",
                "next":"h",
                "parent":None,
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":True,
                "x":48,
                "y":64
            },
            "h":{
                "opcode":"control_forever",
                "next":None,
                "parent":"B",
                "inputs":{
                    "SUBSTACK":[
                        2,
                        "i"
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "j":{
                "opcode":"looks_hide",
                "next":"k",
                "parent":"i",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "k":{
                "opcode":"motion_gotoxy",
                "next":"l",
                "parent":"j",
                "inputs":{
                    "X":[
                        1,
                        [
                            4,
                            "-220"
                        ]
                    ],
                    "Y":[
                        1,
                        [
                            4,
                            "160"
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "l":{
                "opcode":"sensing_askandwait",
                "next":"C",
                "parent":"k",
                "inputs":{
                    "QUESTION":[
                        1,
                        [
                            10,
                            "Draw text..."
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "a":{
                "opcode":"control_repeat",
                "next":None,
                "parent":"m",
                "inputs":{
                    "TIMES":[
                        3,
                        "n",
                        [
                            6,
                            ""
                        ]
                    ],
                    "SUBSTACK":[
                        2,
                        "b"
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "n":{
                "opcode":"operator_length",
                "next":None,
                "parent":"a",
                "inputs":{
                    "STRING":[
                        3,
                        "D",
                        [
                            10,
                            ""
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "D":{
                "opcode":"sensing_answer",
                "next":None,
                "parent":"n",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "b":{
                "opcode":"looks_switchcostumeto",
                "next":"c",
                "parent":"a",
                "inputs":{
                    "COSTUME":[
                        3,
                        "o",
                        "E"
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "E":{
                "opcode":"looks_costume",
                "next":None,
                "parent":None,
                "inputs":{

                },
                "fields":{
                    "COSTUME":[
                        configuration_costume_format(font, "ÿ"),
                        None
                    ]
                },
                "shadow":True,
                "topLevel":True,
                "x":318,
                "y":589
            },
            "o":{
                "opcode":"operator_join",
                "next":None,
                "parent":"b",
                "inputs":{
                    "STRING1":[
                        1,
                        [
                            10,
                            configuration_costume_format(font, "")
                        ]
                    ],
                    "STRING2":[
                        3,
                        "p",
                        [
                            10,
                            ""
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "p":{
                "opcode":"operator_letter_of",
                "next":None,
                "parent":"o",
                "inputs":{
                    "STRING":[
                        3,
                        "F",
                        [
                            10,
                            ""
                        ]
                    ],
                    "LETTER":[
                        3,
                        [
                            12,
                            "i",
                            "Z#}=veHk-!6=ohT5/l+U"
                        ],
                        [
                            6,
                            ""
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "F":{
                "opcode":"sensing_answer",
                "next":None,
                "parent":"p",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "m":{
                "opcode":"data_setvariableto",
                "next":"a",
                "parent":"q",
                "inputs":{
                    "VALUE":[
                        1,
                        [
                            10,
                            "1"
                        ]
                    ]
                },
                "fields":{
                    "VARIABLE":[
                        "i",
                        "Z#}=veHk-!6=ohT5/l+U"
                    ]
                },
                "shadow":False,
                "topLevel":False
            },
            "r":{
                "opcode":"data_changevariableby",
                "next":"G",
                "parent":"d",
                "inputs":{
                    "VALUE":[
                        1,
                        [
                            4,
                            "1"
                        ]
                    ]
                },
                "fields":{
                    "VARIABLE":[
                        "i",
                        "Z#}=veHk-!6=ohT5/l+U"
                    ]
                },
                "shadow":False,
                "topLevel":False
            },
            "G":{
                "opcode":"motion_changexby",
                "next":None,
                "parent":"r",
                "inputs":{
                    "DX":[
                        1,
                        [
                            4,
                            "15"
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "s":{
                "opcode":"procedures_definition",
                "next":"q",
                "parent":None,
                "inputs":{
                    "custom_block":[
                        1,
                        "H"
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":True,
                "x":48,
                "y":504
            },
            "H":{
                "opcode":"procedures_prototype",
                "next":None,
                "parent":"s",
                "inputs":{

                },
                "fields":{

                },
                "shadow":True,
                "topLevel":False,
                "mutation":{
                    "tagName":"mutation",
                    "children":[

                    ],
                    "proccode":"Clone",
                    "argumentids":"[]",
                    "argumentnames":"[]",
                    "argumentdefaults":"[]",
                    "warp":"true"
                }
            },
            "C":{
                "opcode":"procedures_call",
                "next":None,
                "parent":"l",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False,
                "mutation":{
                    "tagName":"mutation",
                    "children":[

                    ],
                    "proccode":"Clone",
                    "argumentids":"[]",
                    "warp":"true"
                }
            },
            "i":{
                "opcode":"looks_cleargraphiceffects",
                "next":"j",
                "parent":"h",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "d":{
                "opcode":"control_create_clone_of",
                "next":"r",
                "parent":"e",
                "inputs":{
                    "CLONE_OPTION":[
                        1,
                        "I"
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "I":{
                "opcode":"control_create_clone_of_menu",
                "next":None,
                "parent":"d",
                "inputs":{

                },
                "fields":{
                    "CLONE_OPTION":[
                        "_myself_",
                        None
                    ]
                },
                "shadow":True,
                "topLevel":False
            },
            "q":{
                "opcode":"event_broadcast",
                "next":"m",
                "parent":"s",
                "inputs":{
                    "BROADCAST_INPUT":[
                        1,
                        [
                            11,
                            "Remove all",
                            "_b:9hNy/GS1IUj]X0qP."
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "J":{
                "opcode":"event_whenbroadcastreceived",
                "next":"K",
                "parent":None,
                "inputs":{

                },
                "fields":{
                    "BROADCAST_OPTION":[
                        "Remove all",
                        "_b:9hNy/GS1IUj]X0qP."
                    ]
                },
                "shadow":False,
                "topLevel":True,
                "x":48,
                "y":1136
            },
            "K":{
                "opcode":"control_delete_this_clone",
                "next":None,
                "parent":"J",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "L":{
                "opcode":"control_start_as_clone",
                "next":"t",
                "parent":None,
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":True,
                "x":48,
                "y":1304
            },
            "t":{
                "opcode":"looks_show",
                "next":"f",
                "parent":"L",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "u":{
                "opcode":"control_forever",
                "next":None,
                "parent":"f",
                "inputs":{
                    "SUBSTACK":[
                        2,
                        "v"
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "v":{
                "opcode":"looks_changeeffectby",
                "next":"w",
                "parent":"u",
                "inputs":{
                    "CHANGE":[
                        1,
                        [
                            4,
                            "3"
                        ]
                    ]
                },
                "fields":{
                    "EFFECT":[
                        "COLOR",
                        None
                    ]
                },
                "shadow":False,
                "topLevel":False
            },
            "f":{
                "opcode":"looks_seteffectto",
                "next":"u",
                "parent":"t",
                "inputs":{
                    "VALUE":[
                        3,
                        "M",
                        [
                            4,
                            "0"
                        ]
                    ]
                },
                "fields":{
                    "EFFECT":[
                        "COLOR",
                        None
                    ]
                },
                "shadow":False,
                "topLevel":False
            },
            "M":{
                "opcode":"motion_xposition",
                "next":None,
                "parent":"f",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "w":{
                "opcode":"motion_sety",
                "next":None,
                "parent":"v",
                "inputs":{
                    "Y":[
                        3,
                        "x",
                        [
                            4,
                            ""
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "c":{
                "opcode":"data_setvariableto",
                "next":"e",
                "parent":"b",
                "inputs":{
                    "VALUE":[
                        3,
                        "N",
                        [
                            10,
                            "0"
                        ]
                    ]
                },
                "fields":{
                    "VARIABLE":[
                        "x",
                        "Aqb[:,Kf5rsdNv@qw/WQ"
                    ]
                },
                "shadow":False,
                "topLevel":False
            },
            "e":{
                "opcode":"data_setvariableto",
                "next":"d",
                "parent":"c",
                "inputs":{
                    "VALUE":[
                        3,
                        "O",
                        [
                            10,
                            "0"
                        ]
                    ]
                },
                "fields":{
                    "VARIABLE":[
                        "y",
                        "LwB!|[DK@6g+=c#Rr=R9"
                    ]
                },
                "shadow":False,
                "topLevel":False
            },
            "N":{
                "opcode":"motion_xposition",
                "next":None,
                "parent":"c",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "O":{
                "opcode":"motion_yposition",
                "next":None,
                "parent":"e",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "x":{
                "opcode":"operator_add",
                "next":None,
                "parent":"w",
                "inputs":{
                    "NUM1":[
                        3,
                        [
                            12,
                            "y",
                            "LwB!|[DK@6g+=c#Rr=R9"
                        ],
                        [
                            4,
                            ""
                        ]
                    ],
                    "NUM2":[
                        3,
                        "y",
                        [
                            4,
                            ""
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "z":{
                "opcode":"operator_mathop",
                "next":None,
                "parent":"y",
                "inputs":{
                    "NUM":[
                        3,
                        "g",
                        [
                            4,
                            ""
                        ]
                    ]
                },
                "fields":{
                    "OPERATOR":[
                        "sin",
                        None
                    ]
                },
                "shadow":False,
                "topLevel":False
            },
            "P":{
                "opcode":"sensing_timer",
                "next":None,
                "parent":"A",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "y":{
                "opcode":"operator_multiply",
                "next":None,
                "parent":"x",
                "inputs":{
                    "NUM1":[
                        3,
                        "z",
                        [
                            4,
                            ""
                        ]
                    ],
                    "NUM2":[
                        1,
                        [
                            4,
                            "10"
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "A":{
                "opcode":"operator_multiply",
                "next":None,
                "parent":"g",
                "inputs":{
                    "NUM1":[
                        3,
                        "P",
                        [
                            4,
                            ""
                        ]
                    ],
                    "NUM2":[
                        1,
                        [
                            4,
                            "500"
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "Q":{
                "opcode":"motion_xposition",
                "next":None,
                "parent":"g",
                "inputs":{

                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            },
            "g":{
                "opcode":"operator_add",
                "next":None,
                "parent":"z",
                "inputs":{
                    "NUM1":[
                        3,
                        "A",
                        [
                            4,
                            ""
                        ]
                    ],
                    "NUM2":[
                        3,
                        "Q",
                        [
                            4,
                            ""
                        ]
                    ]
                },
                "fields":{

                },
                "shadow":False,
                "topLevel":False
            }
        },
        "comments": {
        },
        "currentCostume": 0,
        "costumes": [
        ],
        "sounds": [
        ],
        "volume": 100,
        "layerOrder": 1,
        "visible": True,
        "x": 0,
        "y": 0,
        "size": 100,
        "direction": 90,
        "draggable": False,
        "rotationStyle": "all around"
    }

    for t in configuration_targets():
        # 创建图片
        text_img = Image.new('RGBA', font.getsize(t))
        draw = ImageDraw.Draw(text_img)

        # 绘制
        w = configuration_font_size
        h = configuration_font_size
        x = 0
        y = 0
        draw.text((x, y), t, font=font, fill=configuration_font_color)
        text_img.crop((x, y, x + w, y + h))

        # 保存图片
        pic_name = ''
        while pic_name == '' or pic_name in os.listdir(configuration_output_folder):
            for ri in range(32):
                pic_name += random.choice('abcdefABCDEF0123456789')
        pic_e_name = pic_name + '.png'
        costume_name = configuration_costume_format(font, t)
        text_img.save(configuration_output_folder + pic_e_name)
        print('Save asset ', pic_e_name)
        # 修改project.json
        costume["costumes"].append({"name": costume_name,
                                    "bitmapResolution": 1,
                                    "dataFormat": "png",
                                    "assetId": pic_name,
                                    "md5ext": pic_e_name,
                                    "rotationCenterX": w / 2,
                                    "rotationCenterY": h / 2})
        print('Write asset ', costume_name, ' with ', pic_e_name)

    param["targets"].append(costume)
    print('Write costume ', costume["name"])

    # 保存project.json
    with open('./output/project.json', 'w') as r:
        json.dump(param, r)

def package_project():
    # 打包项目拷贝
    with zipfile.ZipFile('./output.sb3', mode='w', compression=zipfile.ZIP_STORED) as zf:
        for f in os.scandir(configuration_output_folder):
            try:
                name = f.name
                print('Package the file ' + str(name) + ' into output.sb3')
                zf.write(f, arcname=name)
            except Exception as e:
                print('Packaging the file ' + str(name) + ' error: ', e)
        print('Packaged the file output.sb3')

check_folder()
clear_output()
copy_template()
save_assets()
package_project()
