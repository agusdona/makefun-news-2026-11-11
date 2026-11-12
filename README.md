# make.fun bounty entry — "Write the best summary of 11 November's world news"

Bounty: https://make.fun/bounty/news-summary-01 ($200, ends Thu 12 Nov 2026 18:30 UTC / Fri 13 Nov 01:30 WIB)

## The summary

`entry.txt` holds the final summary, in English, condensed from the draft in
`../summary.md` (~3,079 words). It covers the day's most important and most
checkable stories: the US shutdown reaching day 42, the Abu Dhabi
Ukraine–Russia talks and prisoner exchange, Trump's statement on Iran, the
Hormuz tanker mine strike, Gaza strikes and floods, COP31 opening in Antalya,
the CoreWeave-led market rebound, China's $1.04 trillion trade surplus, and
the Bessent/Hegseth developments in Washington.

## Exact size (verified)

- Characters: **1849** (requirement: 1–2,000)
- UTF-8 bytes: **1859**
- Words: **294**
- SHA-256 of `entry.txt`: `0132ecb0becef4ecb962fe59c2254af1c1acb113ad93ed3f1dad6aa09971c36d`
- No trailing newline; the file is exactly the text the program writes.

## Files

- `entry.txt` — the summary itself.
- `main.py` — Python 3.13, standard library only, no network. Writes the
  summary to `/output/entry.txt`, creating `/output` if needed. Deterministic:
  two runs produce byte-identical output.
- `README.md` — this file.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.txt`. Verify with:

```sh
python3 main.py && sha256sum /output/entry.txt
python3 main.py && sha256sum /output/entry.txt   # same hash both times
wc -m /output/entry.txt   # 1849 characters
```

Status: built and verified locally only. NOT submitted; no account or
repository was created for this entry.
