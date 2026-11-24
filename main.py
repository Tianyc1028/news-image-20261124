"""Sum up 24 November 2026's world news in one image.

A deterministic program with no network access. It paints a newspaper
front page with Pillow from the story list baked into this file and
writes /output/entry.png: 1024x1024, under 1 MiB. The bundled DejaVu
fonts make the render identical on any machine, so two runs produce
the same bytes.

News verified 25 November 2026 (Beijing) against Reuters, AP, the
Wall Street Journal, Times Now and Anadolu Agency. Every fact below
was reported on 24 November 2026.
"""
import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = "/output/entry.png"
SIZE = 1024

PAPER = (248, 244, 235)
INK = (20, 20, 20)
RED = (176, 32, 26)
NAVY = (28, 52, 84)
SEA = (168, 200, 222)
SAND = (233, 221, 193)
MUTED = (96, 96, 96)
FLAME = (232, 122, 18)


def load_font(filename, size):
    return ImageFont.truetype(os.path.join(HERE, filename), size)


def serif(size):
    return load_font("DejaVuSerif-Bold.ttf", size)


def sans(size):
    return load_font("DejaVuSans.ttf", size)


def sans_bold(size):
    return load_font("DejaVuSans-Bold.ttf", size)


def wrap_text(draw, text, font, max_width):
    lines = []
    current = ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        elif current:
            lines.append(current)
            current = word
        else:
            lines.append(word)
            current = ""
    if current:
        lines.append(current)
    return lines


def block(draw, text, font, x, y, width, fill=INK, gap=None):
    gap = gap if gap is not None else int(font.size * 1.3)
    for line in wrap_text(draw, text, font, width):
        draw.text((x, y), line, font=font, fill=fill)
        y += gap
    return y


def hline(draw, x, y, x2, width=2, fill=INK):
    draw.line([(x, y), (x2, y)], fill=fill, width=width)


LEAD = (
    "Three oil tankers struck naval mines in the Strait of Hormuz and "
    "caught fire, Iran's Revolutionary Guards said, as the US-Iran war "
    "at sea spread to the world's busiest oil chokepoint. A fourth "
    "tanker was also reported hit. In Washington, Vice President JD "
    "Vance and Secretary of State Marco Rubio met Qatar's prime "
    "minister about reviving negotiations, while the US imposed fresh "
    "sanctions on Iran's shadow banking networks and investigated "
    "suspected Iranian cyberattacks on ships."
)

WORLD = [
    ("UKRAINE",
     "Ukraine sank a Russian warship in a Libyan port with sea drones, "
     "taking the war far beyond Europe. Russian strikes killed four "
     "near Kyiv and two in Zaporizhzhia, wounding 40."),
    ("GAZA",
     "Israeli strikes killed Hamas security chief Naeem Abu Nahel and "
     "six others in Gaza. A day earlier three were killed, including "
     "a worker for the UN agency UNRWA."),
    ("CHINA",
     "Shanghai party chief Chen Jining, a member of the ruling "
     "Politburo, is under investigation, state news agency Xinhua "
     "said — the fourth top leader probed since 2025."),
    ("ISRAEL",
     "Gadi Eisenkot clinched the first coalition deal since last "
     "month's election, signing with Avigdor Lieberman's party as he "
     "races to form a government by 6 December."),
    ("YEMEN",
     "Houthi fighters pushed to within 60 km of Aden, but the "
     "government army said the city will hold. A Riyadh finance "
     "district tower was hit in an attack blamed on the Houthis."),
    ("MARKETS",
     "Nvidia's relief rally over Jensen Huang's return faded fast: "
     "shares slid 6% and the Nasdaq fell 1.5% as tech stumbled and "
     "investors eyed US inflation and GDP data."),
]

NUMBERS = [
    ("3", "tankers hit mines and burned in Hormuz"),
    ("4th", "tanker reported hit, Iran said"),
    ("74", "lashes for an Iranian singer and her team"),
    ("175", "migrants missing after a boat from Senegal lost contact"),
    ("5.3", "magnitude of an earthquake in Nepal"),
    ("60 km", "how close Houthi fighters got to Aden"),
]


def draw_masthead(draw):
    draw.rectangle([0, 0, SIZE, 88], fill=INK)
    draw.text((SIZE // 2, 10), "THE WORLD IN ONE PICTURE",
              font=serif(40), fill=PAPER, anchor="ma")
    draw.text((SIZE // 2, 58), "ONE DAY  •  ONE IMAGE  •  EVERY STORY THAT MATTERED",
              font=sans_bold(14), fill=(222, 202, 162), anchor="ma")


def draw_lead(draw):
    m = 36
    x0, x1 = m, SIZE - m
    draw.text((x0, 98), "TUESDAY 24 NOVEMBER 2026",
              font=sans_bold(21), fill=INK)
    draw.text((x1, 98), "THE WORLD TODAY",
              font=sans_bold(21), fill=RED, anchor="ra")
    hline(draw, x0, 126, x1, 3)
    draw.text((SIZE // 2, 138), "MINES IN THE STRAIT",
              font=serif(58), fill=RED, anchor="ma")
    draw.text((SIZE // 2, 206),
              "Three tankers burning after hitting mines in Hormuz",
              font=serif(25), fill=INK, anchor="ma")
    y = block(draw, LEAD, sans(19), x0, 244, x1 - x0, gap=24)
    return y + 10


def draw_strait_map(draw, y):
    m = 36
    x0, x1 = m, SIZE - m
    w, h = x1 - x0, 120
    draw.rectangle([x0, y, x1, y + h], fill=SEA, outline=INK, width=2)
    # Iran along the top, Arabia along the bottom: a schematic, not a map.
    draw.polygon([(x0, y), (x1, y), (x1, y + 34), (x0 + 640, y + 48),
                  (x0 + 480, y + 34), (x0 + 300, y + 46), (x0 + 120, y + 36),
                  (x0, y + 32)], fill=SAND, outline=INK)
    draw.polygon([(x0, y + h), (x1, y + h), (x1, y + h - 30),
                  (x0 + 660, y + h - 44), (x0 + 420, y + h - 34),
                  (x0 + 180, y + h - 42), (x0, y + h - 32)],
                 fill=SAND, outline=INK)
    draw.text((x0 + 16, y + 6), "IRAN", font=sans_bold(16), fill=MUTED)
    draw.text((x0 + 16, y + h - 26), "ARABIA", font=sans_bold(16), fill=MUTED)
    draw.text((x0 + w - 190, y + 52), "STRAIT OF HORMUZ",
              font=sans_bold(14), fill=NAVY)
    # Mine markers with flames: three burning tankers in the channel.
    for tx in (300, 480, 650):
        draw.ellipse([x0 + tx, y + 56, x0 + tx + 16, y + 72],
                     fill=INK, outline=INK)
        draw.line([(x0 + tx + 8, y + 56), (x0 + tx + 8, y + 48)],
                  fill=INK, width=2)
        draw.rectangle([x0 + tx - 22, y + 74, x0 + tx + 38, y + 86],
                       fill=INK)
        draw.polygon([(x0 + tx - 12, y + 74), (x0 + tx - 4, y + 56),
                      (x0 + tx + 4, y + 74), (x0 + tx + 12, y + 60),
                      (x0 + tx + 20, y + 74)], fill=FLAME)
    draw.text((x0, y + h + 8),
              "SCHEMATIC MAP — NOT TO SCALE  •  QATAR TALKS: Vance and Rubio "
              "met the Qatari PM on Monday about negotiations",
              font=sans(13), fill=INK)
    return y + h + 24


def draw_world(draw, y):
    m = 36
    x0, x1 = m, SIZE - m
    draw.text((x0, y), "AROUND THE WORLD", font=serif(24), fill=INK)
    hline(draw, x0, y + 32, x1, 2)
    col_w = (x1 - x0 - 28) // 2
    row_h = 100
    top = y + 44
    for i, (kick, text) in enumerate(WORLD):
        cx = x0 + (i % 2) * (col_w + 28)
        cy = top + (i // 2) * row_h
        draw.text((cx, cy), kick, font=sans_bold(17), fill=RED)
        block(draw, text, sans(15), cx, cy + 22, col_w, gap=19)
    return top + 3 * row_h + 4


def draw_numbers(draw, y):
    m = 36
    x0, x1 = m, SIZE - m
    hline(draw, x0, y, x1, 2)
    draw.text((x0, y + 8), "THE DAY IN NUMBERS", font=sans_bold(16), fill=RED)
    col_w = (x1 - x0) // 3
    for i, (num, label) in enumerate(NUMBERS):
        cx = x0 + (i % 3) * col_w
        cy = y + 34 + (i // 3) * 34
        draw.text((cx, cy), num, font=serif(20), fill=INK)
        num_w = draw.textlength(num, font=serif(20))
        block(draw, label, sans(13), cx + num_w + 8, cy + 3,
              col_w - num_w - 12, gap=16)
    foot = y + 34 + 68 + 6
    hline(draw, x0, foot, x1, 2)
    draw.text((x0, foot + 6),
              "Sources: Reuters, AP, Wall Street Journal, Times Now, "
              "Anadolu Agency — 24 Nov 2026",
              font=sans(13), fill=MUTED)
    draw.text((x1, foot + 6), "24 NOV 2026", font=sans_bold(13),
              fill=MUTED, anchor="ra")


def main():
    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(img)
    draw_masthead(draw)
    y = draw_lead(draw)
    y = draw_strait_map(draw, y)
    y = draw_world(draw, y)
    draw_numbers(draw, y)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    img.save(OUT_PATH, format="PNG", optimize=True)
    with open(OUT_PATH, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()[:12]
    print("wrote", OUT_PATH, "sha256:", digest)


if __name__ == "__main__":
    main()
