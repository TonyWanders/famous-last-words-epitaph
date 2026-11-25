# On Hold With Heaven

[![make.fun](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![Rank](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/TonyWanders/famous-last-words-epitaph/rank.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![Reward](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/TonyWanders/famous-last-words-epitaph/reward.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)

A program that writes one funny epitaph of famous last words to
`/output/entry.txt`, for the make.fun competition
[Famous Last Words: The Funniest Epitaph](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406).

Run it with Python 3 (standard library only, nothing to install):

```
python3 main.py
```

It writes the epitaph below to `/output/entry.txt` (or to the path given as
the first argument, or `$OUTPUT_PATH`). To write somewhere else, pass the
path directly, for example `python3 main.py /tmp/entry.txt`.

No network, no clock, no
randomness. The epitaph is 68 characters, inside the 1 to 150 gate, one
line, no em dash. The program checks that gate itself before writing: an
entry outside 1 to 150 characters, blank, or spanning more than one line
is rejected with an error instead of being written.

## The epitaph

```
I see the light. It says: please hold, your call is important to us.
```

## How it is put together

`main.py` keeps the entry as one fixed string and splits the work into
three small helpers: `resolve_output_path()` picks where to write,
`validate_entry()` checks the 1 to 150 character gate, and `write_entry()`
does the validated write.

## License

MIT. See [LICENSE](LICENSE).
