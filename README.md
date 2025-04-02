# my-WebCrawler  

This repository contains a simple **web crawler** built using `BeautifulSoup` and `requests`.  
The crawler explores **internal links** within a website **up to a specified recursion level** and prints them.  

## Features  
-  Crawls a website and extracts internal links  
-  Supports recursion up to a user-defined depth  
-  Uses `BeautifulSoup` for HTML parsing  
-  Runs in the terminal with `requests` for fetching pages
-  Saves the urls in a `PDF file` (if the user wishes so)

##  Project Details  
This project was built for **Winter in Data Science (WiDS'23)**, organized by the **Analytics Club of IIT Bombay** :P .

##  Installation & Usage  
### **Install Dependencies**  
Run the following command in your terminal to install required libraries:  
```bash
pip install requests beautifulsoup4
```  

### **Run the Crawler**  
```bash
python crawler.py <website_url> <recursion_depth>
```  
Example:  
```bash
python crawler.py (https://web-scraping.dev/) 3
```  
#### Alternatively, if you prefer a Jupyter Notebook, run the ipynb file!
