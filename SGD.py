'''
SVM model using SGD.

Implements regularized linear models (SVM, logistic regression) with
stochastic gradient descent (SGD) learning
'''

print('Importing things...')
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import SGDClassifier
import helper

# Load training and test datasets.
print('Loading training and test sets...')
X_train, y_train, X_test = helper.load_data('data/training_data.txt',
                                            'data/test_data.txt')

# ------------------------------------------------------------------------------
# PARAMETERS FOR SVM with SGD
loss = 'hinge'
penalty = 'l2'
alpha = 0.001 #optimal alpha
tol = 0.00001
max_iter = 1000
shuffle = True
learning_rate = 'optimal'


# PARAMETERS FOR CROSS-VALIDATION
k = 5
# ------------------------------------------------------------------------------

# Create SVM with SGD model.
clf = SGDClassifier(loss=loss, penalty=penalty, alpha=alpha, tol=tol,
max_iter=max_iter, shuffle=shuffle, learning_rate=learning_rate)

# Fit model and get training error.
print('Training model...')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_train)
print('Training accuracy: %g' % helper.accuracy(y_train, y_pred))

# Get cross-validation error.
print('Evaluating model...')
err_val = np.mean(cross_val_score(clf, X_train, y_train, cv=k))
print('Validation accuracy: %g' % err_val)

helper.process_output(clf.predict(X_test).astype(int), 'out/SGD_1.txt')
