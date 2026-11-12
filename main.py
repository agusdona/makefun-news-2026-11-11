#!/usr/bin/env python3
"""Write the 11 November 2026 world-news summary to /output/entry.txt.

Stdlib only, no network, no randomness, no time or locale dependence.
Deterministic: every run writes the same bytes.
"""

from pathlib import Path

SUMMARY = "On Wednesday, November 11, 2026, the US federal shutdown entered its 42nd day — the longest in American history — as the House prepared to vote on a Senate funding deal, passed 60–40, that would reopen the government. The fight over health-care subsidies had furloughed hundreds of thousands of workers and disrupted airports nationwide. In Abu Dhabi, two days of US-mediated talks between Ukraine and Russia ended without a ceasefire but with agreement on what US envoy Jared Kushner called the war's largest prisoner exchange. Russian strikes left more than 850,000 Ukrainians without power, and NATO scrambled jets after drones strayed into Baltic airspace. President Donald Trump declared the war with Iran 'militarily effectively over,' even as a tanker struck a naval mine in the Strait of Hormuz, closed for more than 250 days. In Gaza, Israeli strikes killed at least 10 people over two days, and winter floods submerged 70,000 tents sheltering about 350,000 displaced people. At COP31 in Antalya, UN Secretary-General António Guterres warned that the climate crisis is 'outrunning us,' with the planet heading for more than 2.5°C of warming even if current pledges are met. Markets rebounded after a hot inflation reading: US consumer prices rose 0.4% in October, the 10-year Treasury yield hit 5.03%, and the S&P 500 rose 1.31% to 7,619.38 while the Nasdaq gained 1.60%, led by AI cloud firm CoreWeave, up 24.7% after reporting revenue of about $3.66 billion. China's goods trade surplus passed $1 trillion for a second consecutive year, reaching $1.04 trillion in the first ten months of 2026. In Washington, Treasury Secretary Scott Bessent was moved to a military base after intelligence said Iranian plotting against US officials had advanced, and House Republicans blocked an effort to impeach Defense Secretary Pete Hegseth, 211–204."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()
