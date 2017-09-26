# mfp-weight-log
A simple selenium-based scraper to collect a 1 year weight log from myfitnesspal.

# Requires:
- json
- selenium
- argparse
- [PhantomJS](http://phantomjs.org/download.html)

# How to run:
To run mfp_weight_log.py, simply install the dependencies and call:
```
python mfp_weight_log.py -un username -pw password
```
If you want to save the scraped data to a csv rather than printing it, add the argument -s filename:
```
python mfp_weight_log.py -un username -pw password -s weight_log.csv
```
