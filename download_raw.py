import requests

with open("./exe_raw.json", mode="w+b") as exe_raw:
    exe = requests.get("https://github.com/burningtnt/HMCL-Snapshot-Update/raw/v5/artifacts/v5/uploaders/local-storage.gh-repo/HMCL-dev/HMCL/main/gradle.yml.exe.json")
    print(exe)
    print(exe.text)
    exe_raw.write(exe.content)

with open("./jar_raw.json", mode="w+b") as jar_raw:
    jar = requests.get("https://github.com/burningtnt/HMCL-Snapshot-Update/raw/v5/artifacts/v5/uploaders/local-storage.gh-repo/HMCL-dev/HMCL/main/gradle.yml.jar.json")
    print(jar)
    print(jar.text)
    jar_raw.write(jar.content)
