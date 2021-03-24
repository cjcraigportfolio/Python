##############
Dataset
##############
1. Our dataset deals with HomeDepot products. HomeDepot is the largest home improvement retailer in the United States, supplying tools, construction products, and services. 
The dataset we will be using under the home-depot-product-search-relevance zipfile. 

Within the zipfile, is the train.csv and product_descriptions.csv file. 

The dataset has the following dimensions:

product_descriptions.csv		
		-124429 Observations
		-2 features
			-product_uid --> Unique identifier for each product
			-product_description --> Describes the product with the information about type, make, dimensions etc.

train.csv
		-74068 Observations
		-5 features
			-id --> Unique identifer for determining each search entry
			-product_uid --> Unique identifier for each product
			-product_title --> Short description about the product
			-search_term --> User entered search term
			-relevance --> If the results were relevant. Contains numbers from 1 to 3 with 3 being the most relevant result.

EDA is performed on all of these features to display the frequencies of the terms.
Preprocessing is performed on the dataset to remove all the punctuations and stopwords.
The link to the original data is: https://www.kaggle.com/c/home-depot-product-search-relevance/data


**Dataset Note**
It is important to note, that we ended using a subset of our dataset by selecting the first 10k rows from the product_description.csv file. The reason for this, is that we did not have the computing power process such a large dataset with the original amount of information.

##############
IPYNB
##############
1. CSC_575_Home_Depot - This notebook goes over the intial EDA, preprocessing, methods that we performed on the dataset. 

The EDA involves the below:
		
		- Number of unqiue terms.
		- Word cloud based on the frequencies of the search terms.
		
The preprocessing involves the below.

		- Remove all the stop words and punctuations.
		- Convert the descriptions into lower case.

Implementing Data for Inverted Index and Search Retrieval involves the below	
		
		- Calculate the total frequency, document frequency and idf for each term
		- Create an inverted index for each term
		- Calculate the document length for each product_uid

Search and retrieval process involves the below.
		
		- Accept input and calculate the cosine similarity by finding the dot product for each input term against the product_uid.
		- Normalizing the measure and displaying results in descending order of similarity measure.

Evaluation involves the below.
		
		- Evaluate the precision and recall for sample records by retrieving the product_uid for each search term.		
		- Visualize the precision and recall with graphs.
		
UI involves the below.

		- Accept user input and retrieve the results with product_uid and product_descriptions.
		- Include the functionality of clearing the screen and exiting the application.


##############
References
##############
Below are our references:

Dataset ---> https://www.kaggle.com/c/home-depot-product-search-relevance/data

Bamshad Mobasher Homework and Lectures


