#coding=utf8

import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.ensemble import RandomForestClassifier


def review_to_words(raw_review):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and
    # the output is a single string (a preprocessed movie review)
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(raw_review, "html.parser").get_text()
    #
    # 2. Remove non-letters
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))
    #
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]
    #
    # 6. Join the words back into one string separated by space,
    # and return the result.
    return( " ".join(meaningful_words))


def create_bag_of_words(clean_train_reviews):
    print "Creating the bag of words...\n"

    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.
    vectorizer = CountVectorizer(analyzer="word", \
                                 tokenizer=None, \
                                 preprocessor=None, \
                                 stop_words=None, \
                                 max_features=5000)

    # fit_transform() does two functions: First, it fits the model
    # and learns the vocabulary; second, it transforms our training data
    # into feature vectors. The input to fit_transform should be a list of
    # strings.
    train_data_features = vectorizer.fit_transform(clean_train_reviews)

    # Numpy arrays are easy to work with, so convert the result to an
    # array
    train_data_features = train_data_features.toarray()

    # Take a look at the words in the vocabulary
    vocab = vectorizer.get_feature_names()
    #print "The vocabulary: \n", vocab

    # Sum up the counts of each vocabulary word
    dist = np.sum(train_data_features, axis=0)
    #print "dist: ", dist

    # For each, print the vocabulary word and the number of times it
    # appears in the training set
    #for tag, count in zip(vocab, dist):
    #    print count, tag

    return vectorizer, train_data_features


def train_model(train_data_features):
    print "Training the random forest..."

    # Initialize a Random Forest classifier with 100 trees
    forest = RandomForestClassifier(n_estimators = 100)

    # Fit the forest to the training set, using the bag of words as
    # features and the sentiment labels as the response variable
    #
    # This may take a few minutes to run
    forest = forest.fit( train_data_features, train["sentiment"] )
    return forest


def create_submission_file(vectorizer, model):
    # Read the test data
    test = pd.read_csv("testData.tsv", header=0, delimiter="\t", \
                       quoting=3 )

    # Verify that there are 25,000 rows and 2 columns
    print test.shape

    # Create an empty list and append the clean reviews one by one
    num_reviews = len(test["review"])
    clean_test_reviews = []

    print "Cleaning and parsing the test set movie reviews...\n"
    for i in xrange(0,num_reviews):
        if( (i+1) % 1000 == 0 ):
            print "Review %d of %d\n" % (i+1, num_reviews)
        clean_review = review_to_words(test["review"][i])
        clean_test_reviews.append( clean_review )

    # Get a bag of words for the test set, and convert to a numpy array
    test_data_features = vectorizer.transform(clean_test_reviews)
    test_data_features = test_data_features.toarray()

    # Use the random forest to make sentiment label predictions
    result = model.predict(test_data_features)

    # Copy the results to a pandas dataframe with an "id" column and
    # a "sentiment" column
    output = pd.DataFrame( data={"id":test["id"], "sentiment":result} )

    # Use pandas to write the comma-separated output file
    output.to_csv("Bag_of_Words_model.csv", index=False, quoting=3)
    print "Submission file created!"


if __name__ == '__main__':
    # header=0 indicates the first line of the file contains column names,
    # delimiter indicates that the fields are separated by tabs,
    # quoting=3 tells Python to ignore doubled quotes
    train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter='\t', quoting=3)
    print "train.shape: ", train.shape
    print "train.columns.values: ", train.columns.values

    #clean_review = review_to_words(train["review"][0])
    #print clean_review

    # Get the number of reviews based on the dataframe column size
    num_reviews = train["review"].size

    # Initialize an empty list to hold the clean reviews
    clean_train_reviews = []

    # Loop over each review; create an index i that goes from 0 to the length
    # of the movie review list
    for i in xrange(0, num_reviews):
        # Call our function for each one, and add the result to the list of clean reviews
        if (i + 1) % 1000 == 0:
            print "Review %d of %d" % (i + 1, num_reviews)
        clean_train_reviews.append(review_to_words(train["review"][i]))

    #vectorizer, train_data_features = create_bag_of_words(clean_train_reviews)
    #model = train_model(train_data_features)
    #create_submission_file(vectorizer, model)
