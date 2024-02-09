import json


def open_json(path):
    """打开 path 对应的 json 文件"""
    with open(path, 'r', encoding='utf-8') as f:
        tmp = json.load(f)
    return tmp