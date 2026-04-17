import os

path = r"c:\Users\anew3\Desktop\project\style.css"

with open(path, "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("clip-path: inset(0 0 0 50%);", "clip-path: inset(0 50% 0 0);")
css = css.replace("right: 50%;\n    width: 4px;", "left: 50%;\n    width: 4px;")
css = css.replace("transform: translateX(50%);\n    pointer-events: none;", "transform: translateX(-50%);\n    pointer-events: none;")
css = css.replace(".label-after { right: 20px; }\n.label-before { left: 20px; }", ".label-after { left: 20px; }\n.label-before { right: 20px; }")

with open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS Reverted")
