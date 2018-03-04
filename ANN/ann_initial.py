#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:59:06 2018

@author: Das
"""
from ann_common import ANNCommon
from util import Util
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

class ANN:
    def fit(self, X, Y, epoch=100000):
        ann = ANNCommon()
        w1, b1, w2, b2 = ann.initialize_weights(X, Y, hidden_nodes=5)
        self.w1, self.b1, self.w2, self.b2, self.J = ann.backpropogation(X, w1, b1, w2, b2, epoch)
        
    def predict(self, X):
        ann = ANNCommon()
        S, P = ann.feedforward(X, self.w1, self.b1, self.w2, self.b2)
        self.P = P
        return P
    
    def score(self, Y, P):
        ann = ANNCommon()
        return ann.accuracy(Y, P)
    
    def plot_cost(self):
        plt.plot(self.J, label='Training cost')
        plt.show()
        

X, Y = Util().get_tabular_data('ecommerce_data.csv')
X = Util().normalize(X)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=28, shuffle=True)

model = ANN()
model.fit(X_train, y_train)
P = model.predict(X_train)
Yhat = np.argmax(P, axis=1)
accuracy = model.score(y_train, P) 

P_test = model.predict(X_test)
Y_test = np.argmax(P_test, axis=1)
accuracy_test = model.score(y_test, P_test)

model.plot_cost()
