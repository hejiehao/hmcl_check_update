import json
import os
from requests_toolbelt import MultipartEncoder
import requests
from utils.open_json import *
from utils.write_json import *

base_url = "https://www.kookapp.cn"

headers = {
    "Authorization": f"Bot {os.environ['KOOK_BOT_TOKEN']}",
    "Content-type": "application/json"
}

exe_raw, jar_raw = open_json("./exe_raw.json"), open_json("./jar_raw.json")

exe_file = MultipartEncoder(
    fields={'file': (exe_raw['jar'][112:], requests.get(exe_raw['jar']).content)}
)

jar_file = MultipartEncoder(
    fields={'file': (jar_raw['jar'][112:], requests.get(jar_raw['jar']).content)}
)

# 上传文件
exe_upload = requests.post(f"{base_url}/api/v3/asset/create", data=exe_file, headers={
    "Authorization": f"Bot {os.environ['KOOK_BOT_TOKEN']}",
    "Content-type": exe_file.content_type
})
print(exe_upload.text)
exe_kook = exe_raw
exe_kook['jar'] = exe_upload.json()['data']['url']
write_json("./exe_kook.json", exe_kook)

jar_upload = requests.post(f"{base_url}/api/v3/asset/create", data=jar_file, headers={
    "Authorization": f"Bot {os.environ['KOOK_BOT_TOKEN']}",
    "Content-type": jar_file.content_type
})
print(jar_upload.text)
jar_kook = jar_raw
jar_kook['jar'] = jar_upload.json()['data']['url']
write_json("./jar_kook.json", jar_kook)

card = json.dumps([
    {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
            {
                "type": "header",
                "text": {
                    "type": "plain-text",
                    "content": "HMCL 快照版更新啦！"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "kmarkdown",
                    "content": "(met)all(met)"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "header",
                "text": {
                    "type": "plain-text",
                    "content": "exe 版本："
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "kmarkdown",
                    "content": f"""最新的 exe 版本为：{exe_raw['version']}
exe SHA-1：{exe_raw['jarsha1']}"""
                }
            },
            {
                "type": "file",
                "title": exe_raw['jar'][112:],
                "src": exe_kook['jar'],
                "size": 0
            },
            {
                "type": "divider"
            },
            {
                "type": "header",
                "text": {
                    "type": "plain-text",
                    "content": "jar 版本"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "kmarkdown",
                    "content": f"""最新的 jar 版本为：{jar_raw['version']}
jar SHA-1：{jar_raw['jarsha1']}"""
                }
            },
            {
                "type": "file",
                "title": jar_raw['jar'][112:],
                "src": jar_kook['jar'],
                "size": 0
            },
            {
                "type": "divider"
            },
            {
                "type": "action-group",
                "elements": [
                    {
                        "type": "button",
                        "theme": "primary",
                        "value": f"https://github.com/HMCL-dev/HMCL/commit/{exe_raw['version'][8:]}",
                        "click": "link",
                        "text": {
                            "type": "plain-text",
                            "content": "GitHub Commit"
                        }
                    }
                ]
            }
        ]
    }
])

# 发送消息
send = requests.post(f"{base_url}/api/v3/message/create", data=json.dumps({
    "content": card,
    "type": 10,
    "target_id": "3378477242796997"
}), headers=headers)
print(send.text)
