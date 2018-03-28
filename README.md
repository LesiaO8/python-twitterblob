# TwitterBlob
## Description
Sentiment analysis performed using TextBlob (by _bag of words_ method on default corpora) on tweets searched by keyword, graphed with matplotlib in terms of polarity and subjectivity, and optionally saved to csv files. It can be used to derive insights regarding the public opinion on a certain subject.

## Usage
First, add your Twitter API keys by replacing the _YOUR_KEY_HERE_ placeholders. Those are obtained from the Twitter Application Management page. Replace _my_keyword_ with your search query and optionally specify a file to save to, and a tweet count (defaults to 1000).

```
python TwitterBlob.py my_keyword --file saved_data.csv --count 1000
```
## Examples
Below are a few results:
```
python TwitterBlob.py love --count 10000
```
![alt text](https://github.com/paubric/TwitterBlob/blob/master/Figure_1.png)
We can observe that the majority of data points have a positive polarity. The yellow square indicates the average sentiment point on both axes. The red line represents the regression of the data points.
```
python TwitterBlob.py hate --count 10000
```
![alt text](https://github.com/paubric/TwitterBlob/blob/master/Figure_2.png)
In this example, the vast majority of data points have a negative polarity, therefore the general sentiment regarding the keyword might be bad.

## Disclaimer
I am not responsible for malicious usage.
