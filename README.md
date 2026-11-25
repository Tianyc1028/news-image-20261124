# The World in One Picture — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Tianyc1028/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Tianyc1028/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for [make.fun bounty **"Sum up 24 November's world news in one image"**](https://make.fun/bounty/news-image-20261124)
(`news-image-20261124`, $100 prize pool, 50 places paid, 1st place $20,
deadline 2026-11-26 08:00 Beijing).

## What it is

A deterministic Python program (`main.py`, Python 3.13, Pillow only) that
draws a newspaper front page — **"THE WORLD IN ONE PICTURE"** — summing up
Tuesday 24 November 2026 in a single 1024×1024 PNG written to
`/output/entry.png`:

- **Lead story:** three oil tankers struck naval mines in the Strait of
  Hormuz and caught fire, Iran's Revolutionary Guards said; a fourth
  tanker was also reported hit. Vance and Rubio met Qatar's prime minister
  about reviving negotiations; the US imposed fresh sanctions on Iran's
  shadow banking networks and investigated suspected Iranian cyberattacks
  on ships.
- **Schematic map** of the Strait of Hormuz with the three burning tankers
  marked, plus a "day in numbers" box (3 tankers, a 4th reported hit,
  74 lashes, 175 migrants missing, a 5.3 quake, Houthis 60 km from Aden).
- **Around the world:** Ukraine sank a Russian warship in a Libyan port;
  Israeli strikes killed a Hamas security chief in Gaza; Shanghai party
  chief Chen Jining is under investigation; Eisenkot clinched Israel's
  first coalition deal; Houthis neared Aden; Nvidia's comeback rally faded.

The story list is embedded in the program; it uses no network. Fonts
(DejaVu Serif Bold / DejaVu Sans / DejaVu Sans Bold) are bundled in this
repo so the render is identical wherever it runs. Two runs produce the
same bytes (verified: identical SHA-256).

## Run it

```
python3 main.py   # writes /output/entry.png
```

Sources checked 25 November 2026: Reuters, AP, Wall Street Journal,
Times Now, Anadolu Agency.

---

<sub>Entered on [make.fun](https://make.fun/?ref=8ysk281f&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
