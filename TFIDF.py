import DataReader as DR
from sklearn import svm
from nltk.tokenize import word_tokenize,RegexpTokenizer
from nltk.stem import *
import re
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.linear_model import LogisticRegression as LR
import matplotlib.pyplot as plt

#Read training data
Ang_Songs=DR.readData("Data-Set/Angry/Train/","angry")
Hap_Songs=DR.readData("Data-Set/Happy/Train/","happy")
Sad_Songs=DR.readData("Data-Set/Sad/Train/","sad")
Rel_Songs=DR.readData("Data-Set/Relaxed/Train/","relaxed")
SongsTrain=[Ang_Songs,Hap_Songs,Sad_Songs,Rel_Songs]

#ReadTestingData
AngT_Songs=DR.readData("Data-Set/Angry/Test/","angry")
HapT_Songs=DR.readData("Data-Set/Happy/Test/","happy")
SadT_Songs=DR.readData("Data-Set/Sad/Test/","sad")
RelT_Songs=DR.readData("Data-Set/Relaxed/Test/","relaxed")
SongsTTrain=[AngT_Songs,HapT_Songs,SadT_Songs,RelT_Songs]

SongsWordsTrain=[[],[]]
for i in range(4):
	for song in SongsTrain[i]:
		s=song[4]
		SongsWordsTrain[0].append(s)
		SongsWordsTrain[1].append(i)

SongsWordsTTrain=[[],[]]
for i in range(4):
	for song in SongsTTrain[i]:
		s=song[4]
		SongsWordsTTrain[0].append(s)
		SongsWordsTTrain[1].append(i)
     


#stemmer = PorterStemmer()
stemmer = SnowballStemmer("english")
tokenizer = RegexpTokenizer("[\w’]+", flags=re.UNICODE)



def tokenize(text):
    #tokens = word_tokenize(text)
    tokens = tokenizer.tokenize(text)
    stems = []
    for item in tokens:
        stems.append(stemmer.stem(item))
    return stems
    
#print(SongWordsTrain)
#print(SongsTrain[:][3])

vectorizer = TfidfVectorizer(tokenizer=tokenize,min_df=1, ngram_range = ( 1 ,3), sublinear_tf = True, stop_words = "english")

print ("Vectorizing training...")

train_x = vectorizer.fit_transform(SongsWordsTrain[0])
#print(train_x)
print ("Vectorizing test...")
#print(vectorizer.get_feature_names())

test_x = vectorizer.transform(SongsWordsTTrain[0])
#print(test_x)

print ("Training...")
print ("NB...")
modelA = MultinomialNB()
modelA.fit(train_x, SongsWordsTrain[1])
print(modelA.score(train_x, SongsWordsTrain[1]))
#print(modelA.predict(test_x))
print(modelA.score(test_x,SongsWordsTTrain[1]))


print ("SVM...")
modelB = svm.SVC(kernel='linear', C=1, gamma=1) 
modelB.fit( train_x, SongsWordsTrain[1])
print(modelB.score(train_x, SongsWordsTrain[1]))
#print(modelB.predict(test_x))
print(modelB.score(test_x,SongsWordsTTrain[1]))

print ("LR...")
modelC = LR()
modelC.fit( train_x, SongsWordsTrain[1])
print(modelC.score(train_x, SongsWordsTrain[1]))
#print(modelC.predict(test_x))
print(modelC.score(test_x,SongsWordsTTrain[1]))

