import os
import re

files = ["index.html", "presentation.html", "infographic.html", "illustrations.html", "banners.html", "identity.html"]
base_dir = r"c:\Users\anew3\Desktop\project"

titles = {
    "index.html": "الرئيسية | 3M Academic Design",
    "presentation.html": "تصميم العروض التقديمية | 3M Academic Design",
    "infographic.html": "الإنفوجرافيك التعليمي | 3M Academic Design",
    "illustrations.html": "الصور التوضيحية العلمية | 3M Academic Design",
    "banners.html": "تصميم البنرات والبوسترات | 3M Academic Design",
    "identity.html": "هوية المعلم (كروت شخصية) | 3M Academic Design"
}

footer_socials = """<div class="flex gap-4 md:gap-6">
                    <a href="https://www.facebook.com/3mnal" target="_blank" rel="noopener noreferrer"
                        class="w-11 h-11 md:w-10 md:h-10 rounded-full bg-gray-50 flex items-center justify-center text-gray-500 hover:bg-primary hover:text-white transition-standard">
                        <i class="fab fa-facebook-f"></i>
                    </a>
                    <a href="https://www.linkedin.com/in/eng3mno3man/" target="_blank" rel="noopener noreferrer"
                        class="w-11 h-11 md:w-10 md:h-10 rounded-full bg-gray-50 flex items-center justify-center text-gray-500 hover:bg-primary hover:text-white transition-standard">
                        <i class="fab fa-linkedin-in"></i>
                    </a>
                    <a href="https://wa.me/+201110119993" target="_blank" rel="noopener noreferrer"
                        class="w-11 h-11 md:w-10 md:h-10 rounded-full bg-gray-50 flex items-center justify-center text-gray-500 hover:bg-primary hover:text-white transition-standard">
                        <i class="fab fa-whatsapp"></i>
                    </a>
                </div>"""

for filename in files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Title
    content = re.sub(r'<title>.*?</title>', f"<title>{titles[filename]}</title>", content, flags=re.IGNORECASE|re.DOTALL)

    # 2. OG tags
    content = re.sub(r'<meta\s+property="og:image"\s+content="[^"]*">', f'<meta property="og:image" content="https://mohamed-3m-nouman.github.io/3M-academic-design-services/logo.png">', content)
    content = re.sub(r'<meta\s+property="og:url"\s+content="[^"]*">', f'<meta property="og:url" content="https://mohamed-3m-nouman.github.io/3M-academic-design-services/">', content)

    # 3. Handle <style> blocks
    content = re.sub(r'\s*<style>[\s\S]*?</style>', '', content)

    # 4. Remove dir="ltr"
    content = content.replace('dir="ltr" class="slider-container group"', 'class="slider-container group"')

    # 5. Script replacement
    content = re.sub(r'<script>\s*// Set current year[\s\S]*?</script>', '<script src="./main.js"></script>', content)

    # 6. Footer Socials
    content = re.sub(r'<div class="flex gap-4 md:gap-6">[\s\S]*?</div>(?=\s*</div>\s*<div class="text-center)', footer_socials, content)

    # 7. Copyright
    content = re.sub(r'&copy;\s*<span id="current-year"></span>.*?</p>', r'&copy; <span id="current-year"></span> 3M Academic Design - بيت التصميم الأكاديمي. جميع الحقوق محفوظة.\n                </p>', content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

with open(os.path.join(base_dir, "style.css"), "a", encoding="utf-8") as f:
    f.write('''\n
/* Custom image slider styles (RTL Native) */
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
    clip-path: inset(0 0 0 50%);
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
    right: 50%;
    width: 4px;
    background: #fff;
    z-index: 5;
    transform: translateX(50%);
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

.label-after { right: 20px; }
.label-before { left: 20px; }
''')

print("All fixes applied successfully.")
