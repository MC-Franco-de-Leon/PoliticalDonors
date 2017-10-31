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
which are the inputs of the functions in Mychallenge.py to compute medianvals_by_zip.txt and medianvals_by_date.txt: has the calculated median, total dollar amount and total number of contributions by recipient and date.

