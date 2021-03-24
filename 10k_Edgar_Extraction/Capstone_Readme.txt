##############
Dataset
##############
1. Our project deals with reading 10k reports from https://www.sec.gov/Archives/edgar/data
We have received a CSV file with all the ticker names and their URL's.

The dataset has the following dimensions:

tempURL.csv		
		-255 tickers
		-255 URL - Contains links to the 10k report

Output from this dataset is ---> rev_dict_test.csv
Then is manually cleaned. We have provided the fully cleaned version (further explained below). 

##############
IPYNB / PY
##############
1. 10k_compare_rev.py - This py reads the CSV file having ticker names, industry and revenues from 2015 - 2017

The csv used for this is ---> rev_dict_final.csv

The UI involves the below:
		- Option for the user to select the industry and two company tickers to compare
		- Table output to display the revenues for 2015 - 2017
		- Bar graph to compare the revenues of two companies
		- Stock price and volume for the two companies from 2014 - 2017.

Run instructions:
		- Save the py file to a particular directory
		- In windows using cmd, change directory to the path where file is stored
			- Execute the following command: streamlit run 10k_compare_rev.py 
		


