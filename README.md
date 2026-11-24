# The Robot Vacuum's Best Excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/funtoons/robot-vacuum-excuse-bot-v1/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/funtoons/robot-vacuum-excuse-bot-v1/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

Entry for the make.fun bounty **"The Robot Vacuum's Best Excuse"**: a program that writes a single excuse line, spoken in the first person by a small flat-faced robot vacuum, explaining a spot it missed.

The excuse:

> I didn't miss that spot — my map lists it as a load-bearing crumb, and I don't demolish structural dust.

## How it works

`main.py` is Python 3 stdlib-only, with no network, no randomness, and no timestamps. Running it writes exactly one line (plus a trailing newline) to `/output/entry.txt`:

```sh
python3 main.py
```

The output is deterministic: two runs produce byte-identical files, and the line is 104 characters, within the 1–140 character gate.
