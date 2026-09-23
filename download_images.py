"""
소재 썸네일을 img/ 폴더에 내려받는 스크립트.
Meta 이미지 URL은 서명이 붙은 임시 주소라 며칠 뒤(약 2026-09-27 전후) 만료됩니다.
만료 전에 한 번 실행해서 img/ 폴더째 깃허브에 올려 두면 계속 보입니다.

사용법:  python download_images.py
"""
import json, os, re, urllib.request

src = open(os.path.join(os.path.dirname(__file__), "data.js"), encoding="utf-8").read()
data = json.loads(re.search(r"window\.REPORT = (\{.*\});", src, re.S).group(1))
os.makedirs("img", exist_ok=True)
ok = fail = 0
for c in data["creatives"]:
    path = os.path.join("img", f"{c['creative_id']}.jpg")
    if os.path.exists(path):
        continue
    try:
        req = urllib.request.Request(c["thumb_remote"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r, open(path, "wb") as f:
            f.write(r.read())
        ok += 1
    except Exception as e:
        fail += 1
        print("실패:", c["name"], "-", e)
print(f"완료 {ok}개, 실패 {fail}개 (이미 있는 파일은 건너뜀)")
