# walkDirectory

Small Python 3 scripts that walk the current working directory and append plain-text reports. They use only the standard library.

## What they do

- `walk.py` appends every matched path to `allfiles.txt`. It then counts names — the text after the last `\` — and appends those counts to `counter.txt`, lowest count first.
- `walkSpecial.py` prints each `*.txt` path and appends those paths to `allfiles.txt`.
- `size.py` appends each path and its size in bytes to `sizes.txt`, smallest first. A path that cannot be sized is recorded as `0`.

Output files are opened in append mode, so running a script again adds to the existing file.

## Run

From the directory you want to scan:

```bash
python3 walk.py
python3 walkSpecial.py
python3 size.py
```
