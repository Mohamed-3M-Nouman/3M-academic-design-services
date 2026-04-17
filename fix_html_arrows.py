import os
import re

files = ["presentation.html", "infographic.html", "illustrations.html", "banners.html", "identity.html"]
base_dir = r"c:\Users\anew3\Desktop\project"

for filename in files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Revert accidental fa-arrows-alt-v back to fa-arrows-alt-h
    content = content.replace('fa-arrows-alt-v', 'fa-arrows-alt-h')

    # Ensure "dir='ltr'" is definitely present
    if '<div class="slider-container group">' in content:
        content = content.replace('<div class="slider-container group">', '<div dir="ltr" class="slider-container group">')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Icons and wrappers verified")
