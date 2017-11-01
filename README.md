# PoliticalDonors
InsightData challenge

In this repository we take an input file whose columns are described in the link

http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml

We extract the main features of these txt files
    CMTE_ID
    ZIP_CODE 
    TRANSACTION_DT:
    TRANSACTION_AMT
    OTHER_ID
which are the inputs of the functions in Mychallenge.py to compute medianvals_by_zip.txt and medianvals_by_date.txt containing the current median, total dollar amount and total number of contributions by recipient and date.


The code process the informatoin line by line, updating median, total transaction amount and current number of transactions uniquely determined by Id and Zip code or Id and date.

As a final comment (due to time constraints) 
-The way to manage the data frame can be improved using a list to keep the transactions per (id and zip) or (id and date) in a single vector instead repeating information
