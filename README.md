# Sum up 25 November's world news in one image — make.fun entry by @rektkolas

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Rektkolas/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Rektkolas/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Bounty: [Sum up 25 November's world news in one image on make.fun](https://make.fun/bounty/news-image-20261125)

`main.py` writes the bundled news image (`entry.png`, 800×1000, 6 stories from 25 Nov 2026) to `/output/entry.png`. No network, deterministic — the same bytes on every run.

Stories: Nvidia slides ~7% / Huang return questioned; tankers hit mines in the Strait of Hormuz; COP31 talks collapse in Antalya; Ukraine confirms Gulf of Finland ship strike; Democrats take the US House; Senegal lifts the AFCON title.

Run: `python3 main.py`
Local test: `ENTRY_OUTPUT=./output/entry.png python3 main.py && ls -lh ./output/entry.png`
