# News Summary — 11 November 2026 (make.fun news-summary-01)

A Python program that writes the best summary of the world's news of
Wednesday 11 November 2026 to `/output/entry.txt`.

## How it works

`main.py` holds the summary as a string, checks it against the gate
(1 to 2,000 characters, at least one non-whitespace character, and the
day's key markers present), then writes it out. Standard library only,
no network, no randomness: two runs write byte-identical output.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
wc -m out/entry.txt   # 1981 characters
```

## What the summary covers

Ordered by importance, a sentence or two a story, each with its source
named so a reader can verify it:

- Russia-Ukraine peace talks, second day in Abu Dhabi (AP)
- COP31 climate summit opens in Antalya (AP)
- US House shelves the Hegseth impeachment, 211-204 (NPR)
- US charges over the alleged Iran-backed RAF Fairford plot (Justice Department)
- Congo's Ebola outbreak passes 11,000 cases (AP)
- Hot US October CPI and the market fall (BLS)
- El Salvador, Trump v. the BBC, the Seongnam bus crash, the Mississippi
  Senate count, and Remembrance Day in Australia (BBC; Yonhap; CBS)

## Sources

Every event and figure in the summary comes from reporting published
for 11 November 2026: the Associated Press on the Abu Dhabi talks, the
COP31 opening and the Congo Ebola count; NPR on the House's 211-204
referral vote; the US Department of Justice's 10 November indictment
on the RAF Fairford plot; the Bureau of Labor Statistics' October CPI
release; and the BBC, Yonhap and CBS on the remaining items. Nothing
is invented: where a charge is only alleged, the summary says so.
