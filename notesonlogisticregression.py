Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

 RESTART: /Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py 
Variables: cBDict, cBData, cBTitles, cBWords, normDict, normData, normTitles, normWords
Already ran:
newDict = defaultdict(int)
for w in cBWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
for w in normWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
allWords = []
allWords = [[newDict[w],w] for w in newDict.keys()]
allWords.sort()
allWords.reverse()
words = [w[1] for w in allWords[:1500]]
wordId = dict(zip(words, range(1500)))
titleList = cBTitles + normTitles
X = [feature(d, wordId) for d in titleList]
>>> import sklearn
>>> y = [1] * len(cBTitles) + [0] * len(normTitles)
>>> from sklearn import LinearRegression

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    from sklearn import LinearRegression
ImportError: cannot import name LinearRegression
>>> from sklearn import LinearRegression()
SyntaxError: invalid syntax
>>> from sklearn import Linear_Regression

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    from sklearn import Linear_Regression
ImportError: cannot import name Linear_Regression
>>> from sklearn import LinearModel

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    from sklearn import LinearModel
ImportError: cannot import name LinearModel
>>> history

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    history
NameError: name 'history' is not defined
>>> 
 RESTART: /Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py 
Variables: cBDict, cBData, cBTitles, cBWords, normDict, normData, normTitles, normWords
Already ran:
newDict = defaultdict(int)
for w in cBWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
for w in normWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
allWords = []
allWords = [[newDict[w],w] for w in newDict.keys()]
allWords.sort()
allWords.reverse()
words = [w[1] for w in allWords[:1500]]
wordId = dict(zip(words, range(1500)))
titleList = cBTitles + normTitles
X = [feature(d, wordId) for d in titleList]
>>> countPunct("The. Man. Ran, over(the dog!!!")
7
>>> countPunct(titleList[34])
0
>>> titleList[34]
u'THE SADDEST MAN ON YOUTUBE FINDS LOVE'
>>> 
 RESTART: /Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py 
Variables: cBDict, cBData, cBTitles, cBWords, normDict, normData, normTitles, normWords
Already ran:
newDict = defaultdict(int)
for w in cBWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
for w in normWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
allWords = []
allWords = [[newDict[w],w] for w in newDict.keys()]
allWords.sort()
allWords.reverse()
words = [w[1] for w in allWords[:1500]]
wordId = dict(zip(words, range(1500)))
titleList = cBTitles + normTitles
X = [feature(d, wordId) for d in titleList]
y = [1] * len(cBTitles) + [0] * len(normTitles)
>>> cBList[24]

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    cBList[24]
NameError: name 'cBList' is not defined
>>> cBTitles[24]
u'HOW TO TAKE SHOWERS WITH YOUTUBERS'
>>> countCaps(cBTitles[24])
1.0
>>> test = "AbAbAb"
>>> countCaps(test)
0.5
>>> test = "AbAbAb "
>>> countCaps(test)
0.5714285714285714
>>> 
 RESTART: /Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py 
Variables: cBDict, cBData, cBTitles, cBWords, normDict, normData, normTitles, normWords
Already ran:
newDict = defaultdict(int)
for w in cBWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
for w in normWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
allWords = []
allWords = [[newDict[w],w] for w in newDict.keys()]
allWords.sort()
allWords.reverse()
words = [w[1] for w in allWords[:1500]]
wordId = dict(zip(words, range(1500)))
titleList = cBTitles + normTitles
X = [feature(d, wordId) for d in titleList]
y = [1] * len(cBTitles) + [0] * len(normTitles)
>>> test = "AbAbAb "
>>> countCaps(test)
0.5
>>> countPunct(test)
0
>>> titleList[34]
u'THE SADDEST MAN ON YOUTUBE FINDS LOVE'
>>> titleList[100]
u'6 MORE OF THE MOST ANNOYING PEOPLE IN CS:GO'
>>> titleList[500]
u'Little Shop Of Horrors - Feed Me (Git It)'
>>> countCaps(titleList[500])
0.3333333333333333
>>> 
 RESTART: /Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py 
Variables: cBDict, cBData, cBTitles, cBWords, normDict, normData, normTitles, normWords
Already ran:
newDict = defaultdict(int)
for w in cBWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
for w in normWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
allWords = []
allWords = [[newDict[w],w] for w in newDict.keys()]
allWords.sort()
allWords.reverse()
words = [w[1] for w in allWords[:1500]]
wordId = dict(zip(words, range(1500)))
titleList = cBTitles + normTitles
X = [feature(d, wordId) for d in titleList]
y = [1] * len(cBTitles) + [0] * len(normTitles)
>>> y[-2:]
[1, 3]
>>> y[-5:]
[0, 0, 0, 1, 3]
>>> len(x)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    len(x)
NameError: name 'x' is not defined
>>> len(X)
972
>>> len(y)
974
>>> 3 + 2
5
>>> test = feature(titleList[3], wordId)
>>> len(test)
703
>>> 
 RESTART: /Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py 
Variables: cBDict, cBData, cBTitles, cBWords, normDict, normData, normTitles, normWords
Already ran:
newDict = defaultdict(int)
for w in cBWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
for w in normWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
allWords = []
allWords = [[newDict[w],w] for w in newDict.keys()]
allWords.sort()
allWords.reverse()
words = [w[1] for w in allWords[:1500]]
wordId = dict(zip(words, range(1500)))
titleList = cBTitles + normTitles
X = [feature(d, wordId) for d in titleList]
y = [1] * len(cBTitles) + [0] * len(normTitles)
>>> len(X)
971
>>> len(y)
971
>>> import sklearn
>>> from sklearn.linear_model import LogisticRegression
>>> logistic = LogisticRegression()
>>> lr = linear_model.logistic

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    lr = linear_model.logistic
NameError: name 'linear_model' is not defined
>>> lr = linear_model.LogisticRegression

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    lr = linear_model.LogisticRegression
NameError: name 'linear_model' is not defined
>>> import sklearn
>>> from sklearn.linear_model import LogisticRegression
>>> logistic = LogisticRegression()
>>> lr = logistic.fit(X, y)
>>> yhat =lr.predict(X)
>>> from sklearn.metrics import accuracy_score
>>> accuracy_score(y, yhat)
0.97528321318228628
>>> 
 RESTART: /Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py 

Traceback (most recent call last):
  File "/Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py", line 257, in <module>
    X = [feature2(d, wordId) for d in titleList]
  File "/Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py", line 226, in feature2
    feat.append(countCaps(datum))
NameError: global name 'feat' is not defined
>>> 
 RESTART: /Users/Ryan/github/spis16-project-planning-datamining-Jose-Ryan/youtubetitles.py 
Variables: cBDict, cBData, cBTitles, cBWords, normDict, normData, normTitles, normWords
Already ran:
newDict = defaultdict(int)
for w in cBWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
for w in normWords:
newDict[w[1].lower()] = newDict[w[1].lower()] + w[0]
allWords = []
allWords = [[newDict[w],w] for w in newDict.keys()]
allWords.sort()
allWords.reverse()
words = [w[1] for w in allWords[:1500]]
wordId = dict(zip(words, range(1500)))
titleList = cBTitles + normTitles
X = [feature(d, wordId) for d in titleList]
y = [1] * len(cBTitles) + [0] * len(normTitles)
>>> import sklearn
>>> from sklearn.linear_model import LogisticRegression
>>> logistic = LogisticRegression()
>>> lr = logistic.fit(X, y)
>>> yhat =lr.predict(X)
>>> yhat
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
       1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 1, 0, 0, 0])
>>> from sklearn.metrics import accuracy_score
>>> accuracy_score(y, yhat)
0.95056642636457256
>>> lr.predict([cBTitles[2]])

Warning (from warnings module):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/utils/validation.py", line 386
    DeprecationWarning)
DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and willraise ValueError in 0.19. Reshape your data either using X.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    lr.predict([cBTitles[2]])
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/linear_model/base.py", line 268, in predict
    scores = self.decision_function(X)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/linear_model/base.py", line 249, in decision_function
    % (X.shape[1], n_features))
ValueError: X has 1 features per sample; expecting 2
>>> type(yhat)
<type 'numpy.ndarray'>
>>> yhat =lr.predict(titleList[24])

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    yhat =lr.predict(titleList[24])
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/linear_model/base.py", line 268, in predict
    scores = self.decision_function(X)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/linear_model/base.py", line 249, in decision_function
    % (X.shape[1], n_features))
ValueError: X has 1 features per sample; expecting 2
>>> yhat =lr.predict(X)
>>> accuracy_score([titleList[24]], yhat)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    accuracy_score([titleList[24]], yhat)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/metrics/classification.py", line 172, in accuracy_score
    y_type, y_true, y_pred = _check_targets(y_true, y_pred)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/metrics/classification.py", line 72, in _check_targets
    check_consistent_length(y_true, y_pred)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/utils/validation.py", line 176, in check_consistent_length
    "%s" % str(uniques))
ValueError: Found arrays with inconsistent numbers of samples: [  1 971]
>>> yhat =lr.predict([titleList[24]])

Warning (from warnings module):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/utils/validation.py", line 386
    DeprecationWarning)
DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and willraise ValueError in 0.19. Reshape your data either using X.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    yhat =lr.predict([titleList[24]])
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/linear_model/base.py", line 268, in predict
    scores = self.decision_function(X)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/linear_model/base.py", line 249, in decision_function
    % (X.shape[1], n_features))
ValueError: X has 1 features per sample; expecting 2
>>> title = titleList[24]
>>> titleFeat = feature(title, wordId)
>>> lr.predict([titleFeat])

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    lr.predict([titleFeat])
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/linear_model/base.py", line 268, in predict
    scores = self.decision_function(X)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sklearn/linear_model/base.py", line 249, in decision_function
    % (X.shape[1], n_features))
ValueError: X has 703 features per sample; expecting 2
>>> predict([titleFeat])

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    predict([titleFeat])
NameError: name 'predict' is not defined
>>> titleFeat = feature2(title, wordId)
>>> lr.predict([titleFeat])
array([1])
>>> 
