import json


def write_json(path: str, value):
    """将 value 转成 json 字符串并写入 path 对应的 json 文件"""
    with open(path, 'w+', encoding='utf-8') as fw2:
        json.dump(value, fw2, indent=2, sort_keys=True, ensure_ascii=False)