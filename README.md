# Case Scraper using Juriscraper API
Court Case data manipulation scripts using Juriscraper and several data sinks in the US court system to collect information about judges. Specifically this involves gathering case metadata based on docket numbers and district court identifiers for tens of thousands of cases in federal court. This case information is uniquely matched using the free API (https://free.law/idb-facts/#how-can-i-link-up-the-idb-with-pacer) to a longer docket number that contains the judge's initials inside the longer docket numbers. The end is a case to judge matching problem, using judge data freely accessible from a different API (https://free.law/judicial-database/). The end product should be a data file (e.g., .csv).

## Requirements
Python 2

## Usage
Given a csv file with Court Case data that includes docket numbers and district numbers run 

```python
merge_dfs.py
```

to merge the databases with padded docket numbers nad district names.

A dataset with judges has already been provided, but otherwise, the load_judges.py file can be modified to create a new dataset given a different data dump.