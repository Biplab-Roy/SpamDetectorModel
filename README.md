# SpamDetectorModel
### [link](https://spamdetectormodel.herokuapp.com/)
# What is Spam Message Classifier ?
As per cisco, Spam email is unsolicited and unwanted junk email sent out in bulk to an indiscriminate recipient list. Typically, spam is sent for commercial purposes. It can be sent in massive volume by botnets, networks of infected computers. spam email is sent for commercial purposes. While some people view it as unethical, many businesses still use spam. The cost per email is incredibly low, and businesses can send out mass quantities consistently. Spam email can also be a malicious attempt to gain access to your computer. The model has the ability to classify these spam messages/mails is known as Spam Message Classifier. 

# Techniques to bulild Spam Message Classifier.
- **Dataset Collection**:
Many Spam and ham datasets are out there. for this project one popular [dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset) has been choosen from kaggle.
- **Preprocessing**:
In case of message classifier data is in pure text. So before training some techniques need to be used to convert it into numerical data and for cleaning the unnessary data. 
- **Traning**:
There are various algorithms out there to deal with classification problems. Out of them most widely used algorithm is Naive Bayes.
- **Testing**:
Performance of Classification problems can be evaluated by some metrices like Number Of Misclassification, Confusion Matrix.

## Preprocessing
&emsp;&emsp;&emsp;Spam Message Classifier has text data as input parameter.Every messages always contains some words which don't provide any meaningfull context in order to get prediction. Example: 'is', 'was', 'being', etc. These word can be simply discarded since these affects model performance badly. Again there are some words which are very important for detecting spam messages like 'free', 'lottery', 'cash', etc. The words which don't gives any meaning for content that can be discarded using **nltk.corpus.stopwords**. All spacial symbols are removed using python **regex**. The words that are important for the model that can be present in the sentence in many forms, maybe in different tenses. The same meaning words with diffrent forms can be made same using **PorterStemmer**. <br>
  &emsp;&emsp;&emsp;After performing all these steps now messages contains only necessary stemmed words. To convert the text data in numerical technoques like TfIDf, Bag of Words. In this model **TfIDf** is used to make the dataset suitable for training. Following function is the example for doing preprocessing on the list of messages `X`;
  
  ```
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
stemmer = PorterStemmer()
def process(X):
    for i in range(len(X)):
      review = X[i]
      review = re.sub('[^a-zA-Z]'," ",review)
      words = review.lower().split()
      words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
      review = ' '.join(words)
      X[i] = review
  ```
## Naive Bayes
  Naive Bayes is well known algorithm which works on Bayes Theorem of Probability. It is a popular algorihm for text classification problems. The only assumption Naive Bayes has is that Input features are dependent on each other. <br>
  &emsp;&emsp;&emsp; Bayes Theorem says that <br>
    <img src="https://latex.codecogs.com/svg.image?P(\frac{A}{B})&space;=&space;\frac{P(A&space;\bigcap&space;B)}{P(B)}" title="P(\frac{A}{B}) = \frac{P(A \bigcap B)}{P(B)}"/>
    <br>
    To know more about [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier).
    
## Performance
  After performing validation in test dataset accuracy is found to be 96.42%. 
  
## Improvements
  - Random forest classifier with Naive Bayes can be used for more better performance.
  - Some better threshold can be choosen from ROC curve to reduce false negatives. It would be better to have some spam mails in inbox than having legit mails in spam box. 


## Connect with me
---
[LinkedIn](https://www.linkedin.com/in/biplab-roy-4b63b316a/) <br>
[Facebook](https://www.facebook.com/profile.php?id=100008888882996)
    
