import os

path = r"c:\Users\anew3\Desktop\project\style.css"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

horizontal_slider_css = """
/* Custom image slider styles */
.slider-container {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    background: #e2e8f0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

.slider-container img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    pointer-events: none;
}

.img-after {
    z-index: 2;
    clip-path: inset(0 50% 0 0);
}

.img-before {
    z-index: 1;
}

.slider-input {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    cursor: ew-resize;
    z-index: 10;
}

.slider-button {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 4px;
    background: #fff;
    z-index: 5;
    transform: translateX(-50%);
    pointer-events: none;
}

.slider-button::after {
    content: '\\2194';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 44px;
    height: 44px;
    background: #FFC107;
    color: #212529;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    border: 3px solid #fff;
}

.slider-label {
    position: absolute;
    top: 20px;
    background: rgba(0,0,0,0.6);
    color: white;
    padding: 8px 20px;
    border-radius: 30px;
    font-size: 14px;
    font-family: 'Cairo', sans-serif;
    font-weight: 700;
    backdrop-filter: blur(4px);
    z-index: 4;
    letter-spacing: 0.5px;
}

.label-after { left: 20px; }
.label-before { right: 20px; }
"""

# Keep only lines 0 to 69 from the old CSS.
new_lines = lines[:69]
new_css = "".join(new_lines) + horizontal_slider_css

with open(path, "w", encoding="utf-8") as f:
    f.write(new_css)

print("CSS Fixed completely")
