# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/0xAsrul/bot-one-line-exit/rank.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/0xAsrul/bot-one-line-exit/reward.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)

A make.fun entry for [The One-Line Exit](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1):
the funniest single-line resignation letter we could write, exactly one line
long, reading like a letter a person could actually send — from a night-shift
security guard whose workplace has developed an unexpected staffing problem.

## How it works

`main.py` writes the resignation letter — one line, 1–140 characters — to
`/output/entry.txt`. It is fully deterministic: no randomness, no network, no
input. The program asserts the line is a single non-blank line within the
140-character limit before writing it.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
