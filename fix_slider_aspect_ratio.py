import os

path = r"c:\Users\anew3\Desktop\project\style.css"

with open(path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove the fixed aspect ratio
css = css.replace("aspect-ratio: 16 / 9;", "")

# Replace the absolute positioning rule for all images
old_img_rule = """.slider-container img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    pointer-events: none;
}"""

new_img_rule = """.slider-container img {
    width: 100%;
    object-fit: cover;
    pointer-events: none;
}"""
css = css.replace(old_img_rule, new_img_rule)

# Update img-before to control height naturally
old_img_before = """.img-before {
    z-index: 1;
}"""

new_img_before = """.img-before {
    display: block;
    height: auto;
    z-index: 1;
}"""
css = css.replace(old_img_before, new_img_before)

# Update img-after to be absolute
old_img_after = """.img-after {
    z-index: 2;
    clip-path: inset(0 50% 0 0);
}"""

new_img_after = """.img-after {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    z-index: 2;
    clip-path: inset(0 50% 0 0);
}"""
css = css.replace(old_img_after, new_img_after)

with open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("Aspect ratio fixed gracefully")
