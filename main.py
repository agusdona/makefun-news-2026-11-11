"""news-summary-01: the best summary of the world's news of Wednesday 11 November 2026.

Writes the summary to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader's container). Standard library only; deterministic:
the same bytes on every run, no network, no randomness.
"""

import os

SUMMARY = (
    "World news, Wednesday 11 November 2026: Russia and Ukraine held a second day "
    "of US-mediated talks in Abu Dhabi, their first such meeting in nine months, with "
    "American envoys Jared Kushner and Steve Witkoff pressing both sides toward a deal; "
    "Secretary of State Marco Rubio called the first day 'very productive', and the "
    "delegations, led by Rustem Umerov for Kyiv and Vladimir Medinsky for Moscow, "
    "discussed prisoner swaps and the return of Ukrainian children (AP)."
    "\n\nAt the COP31 climate summit in Antalya, Turkey, world leaders opened formal "
    "talks on curbing global warming; UN Secretary-General Antonio Guterres told them, "
    "'We know the truth. Now we must act on it,' though the leaders of the United States, "
    "China and India stayed away (AP)."
    "\n\nIn Washington, the House voted 211-204 to send eight articles of impeachment "
    "against Defense Secretary Pete Hegseth to the Judiciary Committee, shelving the "
    "effort brought by Republican Thomas Massie over the Iran war and other military "
    "actions (NPR)."
    "\n\nUS prosecutors charged three men over an alleged Iran-backed campaign of nearly "
    "20 attacks in Europe and America, including a September plot against RAF Fairford, "
    "the British base that housed US B-1 bombers; one defendant allegedly directed it "
    "from a New York jail cell (Justice Department)."
    "\n\nCongo's Ebola outbreak passed 11,000 cases, with 11,042 infections and 5,387 "
    "deaths, the country's deadliest outbreak; the Bundibugyo virus behind it, which has "
    "spread to eight of 26 provinces, has no vaccine (AP)."
    "\n\nUS consumer prices rose 0.4% in October, above forecasts, sending the S&P 500 "
    "down 0.4% and the Nasdaq 0.7% and pushing the 10-year Treasury yield above 5%, "
    "with a December rate rise now seen as near-certain (BLS)."
    "\n\nElsewhere, El Salvador struck the 400 Mawozo gang, President Trump sued the BBC, "
    "nine people were seriously hurt in a bus crash in Seongnam, South Korea, counting "
    "continued in Mississippi's Senate race, and Australia marked Remembrance Day "
    "(BBC; Yonhap; CBS)."
)


REQUIRED_MARKERS = ("11 November 2026", "Abu Dhabi", "COP31")


def validate(text):
    """Check the summary against the gate before writing it out."""
    if not (1 <= len(text) <= 2000):
        raise ValueError("summary must be 1 to 2000 characters, got %d" % len(text))
    if not any(not c.isspace() for c in text):
        raise ValueError("summary must contain a non-whitespace character")
    for marker in REQUIRED_MARKERS:
        if marker not in text:
            raise ValueError("summary is missing required marker: %s" % marker)


def main():
    validate(SUMMARY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()

