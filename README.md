These are some Juriscraper and other Court Case data manipulation scripts to help a friend with a data collection task across several data sinks in the US court system. Specifically this involves gathering case metadata based on docket numbers and district court identifiers for tens of thousands of cases in federal court. This case information is uniquely matched using a free API (https://free.law/idb-facts/#how-can-i-link-up-the-idb-with-pacer) to a longer docket number that contains the judge's initials inside the longer docket numbers. The end is a case to judge matching problem, using judge data freely accessible from a different API (https://free.law/judicial-database/). The end product should be a data file (e.g., .csv).
