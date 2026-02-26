import json
import os

png_signature = b'\x89PNG\r\n\x1a\n'

if __name__ == "__main__":
    ans = dict()
    os.mkdir("real_pngs")
    os.mkdir("fake_pngs")
    for root, dirs, files in os.walk("./images/"):  
        for filename in files:
            with open(f"images/{filename}", "rb") as f:
                file = f.read()
            if file[:8] == png_signature:
                ans[filename] = "Real PNG"
                os.rename(f"images/{filename}", f"real_pngs/{filename}")
            else:
                ans[filename] = "Fake PNG"
                os.rename(f"images/{filename}", f"fake_pngs/{filename}")
    with open('ans.json', 'w') as f:
        json.dump(ans, f)