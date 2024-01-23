#   News influence in the stock price of AlphabetInc (Google)

##  Overview
The dataset contains information on 178 news articles from The New York Times 
related to Google. The class indicates the impact on the stock price of Alphabet, 
Inc. (whose main subsidiary is Google) the day the news article was published.

Class 0 indicates that the stock price decreased, by at least 2%. Class 1 indicates 
that the stock price remained within ±2%, and Class 2 indicates that the stock price 
increased, by at least 2%.

The information obtained from each news article consists of a wordbag of relevant 
words. I obtained these by making a GET request to different news articles, as this 
bypasses the protection against reading by non-subscribers. (Someone in the NYTimes
should be fired)

To obtain the links to the news articles, I emulated a Chrome browser using Selenium,
and to get the stock prices of Alphabet, Inc., I used Alpha Vantage's API.

I have not found a clear correlation between the collected wordbags and the assigned 
classes, but nevertheless, I consider that creating the dataset was an interesting 
exercise.

The dataset can be found in the /out folder.

##  Installation and Setup

To create your own dataset, follow these steps:

1. Clone the Repository:
    ```
    git clone https://github.com/Matx1n3/NYTimes-Influence-AlphabetInc.git
    ```
2. Navigate to Project Directory:
    ```
    cd NYTimes-Influence-AlphabetInc
    ```
3. Install Dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Set Up Configuration:

   Open the config.py file and configure the following parameters:

   * min_amount: The minimum number of news links to obtain.
   * dataset_filename: The name of the CSV file to store the dataset.
   * download_stock_data: Set to True if you want to download stock price data.
   
5. API Key configuration:
    
   This step is necessary only if you set download_stock_data to True. However, as more news are published, stock prices informations must be updated.
   Because of that, setting download_stock_data to True is recommended and therefore, also following these steps.

    To use Alpha Vantage's API for obtaining stock prices, you need to create a file named api_key.py in the src folder. Follow these steps:

    1. **Create api_key.py file:** 
        In the src folder, create a file named api_key.py.

    2. **Add API Key:**
        Open api_key.py and add the following line:

    ```
    api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
    ```
    Replace "YOUR_ALPHA_VANTAGE_API_KEY" with your actual Alpha Vantage API key.

    Note: If you don't have an Alpha Vantage API key, you can obtain one by signing up on their [website](https://www.alphavantage.co/support/#api-key).

    3. **Save the File:**
        Save the api_key.py file.

7. Run the Main Script:
    ```
    python3 src/main.py
    ```
   
This will start the process of obtaining news links, analyzing content, and collecting stock price data. The resulting dataset will be stored in the /out folder.
