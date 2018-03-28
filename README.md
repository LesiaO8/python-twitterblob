# TwitterBlob
## Description
Sentiment analysis with TextBlob on tweets searched by keyword, graphed with matplotlib and optionally saved to csv files

## Usage
First, add your Twitter API keys over the _YOUR_KEY_HERE_ placeholders. This are obtained from the Twitter Application Management page. Replace _my_keyword_ with your search query and optionally specify a file to save to and a tweet count (defaults to 1000).

```
python TwitterBlob.py my_keyword --file saved_data.csv --count 1000
```
## Examples
Below are a few results:
```
python TwitterBlob.py love --count 10000
```
![alt text](https://github.com/paubric/TwitterBlob/blob/master/Figure_1.png)
```
python TwitterBlob.py hate --count 10000
```
![alt text](https://github.com/paubric/TwitterBlob/blob/master/Figure_2.png)

## Disclaimer
I am not responsible for malicious usage.
