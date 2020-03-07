import os

for i in os.listdir(os.path.dirname(__file__)):
    if i.endswith(".html"):
        with open(os.path.join(os.path.dirname(__file__), i), encoding='utf8') as f:
            content = f.read()
        with open(os.path.join(os.path.dirname(__file__), i), mode='w', encoding='utf8')as f:
            f.write(content.replace("../i.creativecommons.org/l/by/3.0/80x15.png", "images/80x15.png"))
