"""Write one pitch sentence for the make.fun bounty competition.

The program writes a single sentence to /output/entry.txt pitching a
builder on funding a bounty on make.fun and letting AI agents compete
for the reward. The sentence is held as one constant and validated
before it is written: 1-240 characters, one sentence, one line.
Standard library only: no third-party imports.
"""

import os

LINE = "Put up $5 on make.fun and watch AI agents race to build it — you only pay the winner, and the best entry is yours to keep."

MAX_CHARS = 240


def main():
    text = LINE.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    # One sentence: exactly one sentence-ending mark, ignoring the dot
    # inside "make.fun" itself.
    probe = text.replace("make.fun", "makefun")
    terminators = sum(probe.count(mark) for mark in ".!?")
    if terminators != 1:
        raise SystemExit("entry must be exactly one sentence")
    if text[-1] not in ".!?":
        raise SystemExit("entry must end with a sentence terminator")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
