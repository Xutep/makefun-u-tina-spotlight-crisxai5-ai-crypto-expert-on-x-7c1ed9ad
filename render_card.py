#!/usr/bin/env python3
"""Render the @crisxai5 spotlight card (1080x1350, 4:5) for the make.fun bounty.
Fresh code written in this session. Sharp vector-style text via PIL + Noto Sans.
Layout uses fixed coordinates so nothing overflows the canvas.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

W, H = 1080, 1350
random.seed(7)

BLACK = (10, 14, 24)
CYAN = (34, 211, 238)
VIOLET = (167, 139, 250)
GREEN = (52, 211, 153)
WHITE = (255, 255, 255)
MUTED = (176, 190, 214)
CARD = (22, 32, 58)
CARD_EDGE = (56, 78, 122)

def font(name, size):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/noto/{name}", size)

F_BLACK = lambda s: font("NotoSans-Black.ttf", s)
F_XBOLD = lambda s: font("NotoSans-ExtraBold.ttf", s)
F_BOLD = lambda s: font("NotoSans-Bold.ttf", s)
F_REG = lambda s: font("NotoSans-Regular.ttf", s)

img = Image.new("RGB", (W, H), BLACK)
d = ImageDraw.Draw(img, "RGBA")

for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(16 + (10 - 16) * t),
                                    int(26 + (14 - 26) * t),
                                    int(52 + (24 - 52) * t)))

for x in range(0, W, 54):
    d.line([(x, 0), (x, H)], fill=(255, 255, 255, 7), width=1)
for y in range(0, H, 54):
    d.line([(0, y), (W, y)], fill=(255, 255, 255, 7), width=1)

ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
od.ellipse([-220, -180, 420, 320], fill=(34, 211, 238, 55))
od.ellipse([760, 1050, 1320, 1520], fill=(167, 139, 250, 55))
od.ellipse([820, -120, 1180, 180], fill=(52, 211, 153, 32))
ov = ov.filter(ImageFilter.GaussianBlur(90))
img.paste(Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")

for _ in range(46):
    x = random.randint(30, W - 30)
    y = random.randint(30, H - 30)
    r = random.randint(2, 4)
    c = random.choice([CYAN, VIOLET, GREEN])
    d.ellipse([x - r, y - r, x + r, y + r], fill=c + (random.randint(60, 140),))

d.rectangle([0, 0, W, 10], fill=CYAN)
d.rectangle([0, 0, int(W * 0.55), 10], fill=VIOLET)

def centered(y, text, fnt, fill, tracking=0):
    if tracking == 0:
        w = d.textlength(text, font=fnt)
        d.text(((W - w) / 2, y), text, font=fnt, fill=fill)
        return
    total = sum(d.textlength(ch, font=fnt) + tracking for ch in text) - tracking
    x = (W - total) / 2
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += d.textlength(ch, font=fnt) + tracking

def wrap(text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

# --- fixed layout (y coordinates) ---
# badge 60..130 | SPOTLIGHT 200 | handle 268..410 | bar 424 | subhead 452
# tagline 528..624 | cards 652..1180 | CTA 1210..1310
y = 60
badge = "MUST-FOLLOW  ON  X"
bf = F_XBOLD(38)
bw = d.textlength(badge, font=bf) + 72
bx = (W - bw) / 2
d.rounded_rectangle([bx, y, bx + bw, y + 70], radius=35, outline=CYAN, width=3, fill=(34, 211, 238, 26))
d.text((bx + 36, y + 14), badge, font=bf, fill=CYAN)

centered(200, "SPOTLIGHT", F_BLACK(56), MUTED, tracking=14)
centered(268, "@crisxai5", F_BLACK(132), WHITE)
bar_w = 520
d.rounded_rectangle([(W - bar_w) / 2, 424, (W + bar_w) / 2, 434], radius=5, fill=CYAN)
d.rounded_rectangle([(W - bar_w) / 2, 424, (W - bar_w) / 2 + bar_w * 0.55, 434], radius=5, fill=VIOLET)
centered(452, "AI & CRYPTO EXPERT", F_XBOLD(56), CYAN, tracking=4)

ty = 528
for line in wrap("The sharp voice on AI agents, crypto alpha & Web3 innovation.", F_REG(36), 880):
    centered(ty, line, F_REG(36), MUTED)
    ty += 48

pillars = [
    ("AI AGENTS", "Practical agent workflows,", "built & explained in plain sight", CYAN),
    ("CRYPTO INSIGHTS", "Sharp reads on markets,", "narratives & on-chain moves", GREEN),
    ("WEB3 INNOVATION", "Tooling & automation for", "the next internet", VIOLET),
]
card_h, gap = 148, 20
x0, x1 = 72, W - 72
cy = 652
for title, l1, l2, accent in pillars:
    d.rounded_rectangle([x0, cy, x1, cy + card_h], radius=26, fill=CARD, outline=CARD_EDGE, width=2)
    d.rounded_rectangle([x0, cy, x0 + 14, cy + card_h], radius=7, fill=accent)
    d.text((x0 + 46, cy + 16), title, font=F_XBOLD(42), fill=WHITE)
    d.text((x0 + 46, cy + 70), l1, font=F_REG(32), fill=MUTED)
    d.text((x0 + 46, cy + 108), l2, font=F_REG(32), fill=MUTED)
    d.ellipse([x1 - 88, cy + 48, x1 - 28, cy + 108], outline=accent, width=4)
    d.text((x1 - 70, cy + 50), "›", font=F_BLACK(48), fill=accent)
    cy += card_h + gap

cta_y = 1210
d.rounded_rectangle([72, cta_y, W - 72, cta_y + 100], radius=50, fill=CYAN)
d.text((72 + 44, cta_y + 24), "x.com/crisxai5", font=F_XBOLD(50), fill=(8, 16, 30))
follow = "FOLLOW"
fw = d.textlength(follow, font=F_XBOLD(38))
fx = W - 72 - 44 - fw
d.text((fx, cta_y + 30), follow, font=F_XBOLD(38), fill=(8, 16, 30))
# chevron arrow drawn with lines (no glyph dependency)
ax = W - 72 - 44 + 18
ay = cta_y + 50
d.line([(ax, ay - 14), (ax + 16, ay), (ax, ay + 14)], fill=(8, 16, 30), width=6, joint="curve")

img.save("/home/hatch/workspace/makefun/entry-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/spotlight-crisxai5.png")
print("saved 1080x1350")
