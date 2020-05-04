I am looking for help with a basic data collection task. I have a data set (in .csv format) that contains docket numbers and district court identifiers for about 45,000 cases in federal court. This case information can be uniquely matched using a free API (https://free.law/idb-facts/#how-can-i-link-up-the-idb-with-pacer) to a longer docket number that contains the judge's initials. I want to add the longer docket numbers and the judges' initials to the data set. In addition, using the judges' initials, I want to match the cases to judge data freely accessible from a different API (https://free.law/judicial-database/). The end product should be a data file (e.g., .csv) that I can import and work with in Stata. I am willing to pay $250 for this work. It should be pretty easy for someone with a background in CS.

Yes, I was thinking that district + judge's name should be enough to match the judge initials with the judge data. But it would seem that the date of case filing and the dates of the judge's tenure (which I think is included in the judge data set) could also help narrow, if necessary. I can put some more thought into it, too if you run into troubles.

I've got the second half workflow figured out - querying the judges data, given the first and last initial (if we have the middle initial this will help also). Aside from the issue about possible disambiguation.


No, I spoke with the folks at the Free Law Project and they said PACER's API is free (but undocumented?). See here: https://free.law/idb-facts/#how-can-i-link-up-the-idb-with-pacer. I'm not looking to get documents, docket sheets, etc. (which cost $0.10 a piece), just the extended case number, which is free, and which happens to have the judge's initials. Free Law Project told me that's an easy way to get judge info and link to the IDB (that's the data that I sent you in .csv). They said they recommend using Juriscraper, which has an API specifically for this purpose: https://github.com/freelawproject/juriscraper/blob/master/juriscraper/pacer/hidden_api.py#L13.