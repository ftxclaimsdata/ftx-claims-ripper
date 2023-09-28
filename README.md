NOTE: If possible, use `all.csv` to avoid spamming the site

Rip source: https://restructuring.ra.kroll.com/FTX/Home-ClaimInfo

Rip method:
1. Chrome Developer Tools > Network > (Filter) Doc > Home-ClaimInfo > Copy > Copy as cURL
2. https://curlconverter.com/

## Usage

```sh
python ripper.py
python merge.py pages/*.csv -o all-dirty.csv
python clean.py all-dirty.csv -o all.csv
csvlens all.csv
```

https://github.com/YS-L/csvlens
