from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

#emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'])

#This prints the email at index 5
#print(emails.data[5])

#This prints ['rec.sport.baseball', 'rec.sport.hockey']
#print(emails.target_names)

#This prints the target of the email at index 5
#It is 1, so it is hockey related
#print(emails.target[5])

#Split data into training and test sets
#random_state will ensure that your dataset is split in the same way everytime you run the code
train_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset='train', shuffle=True, random_state=108)

test_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset='test', shuffle=True, random_state=108)

counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)

#List of counts of words in the training set
train_counts = counter.transform(train_emails.data)

#List of counts of words in the testing set
test_counts = counter.transform(test_emails.data)

classifier = MultinomialNB()
classifier.fit(train_counts, train_emails.target)
print(classifier.score(test_counts, test_emails.target))