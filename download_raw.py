import requests

with open("./exe_raw.json", mode="w+b") as exe_raw:
    exe = requests.get("https://github.com/burningtnt/HMCL-Snapshot-Update/raw/v4/artifacts/v4/b8e16c58e93651e8bad5cd7322143f4386f59aa6/f9a373cbf92e9726381a470cab99843b35709f04.exe.json")
    print(exe)
    exe_raw.write(exe.content)

with open("./jar_raw.json", mode="w+b") as jar_raw:
    jar = requests.get("https://github.com/burningtnt/HMCL-Snapshot-Update/raw/v4/artifacts/v4/b8e16c58e93651e8bad5cd7322143f4386f59aa6/f9a373cbf92e9726381a470cab99843b35709f04.jar.json")
    print(jar)
    jar_raw.write(jar.content)
