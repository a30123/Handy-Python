# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:00:26 2015

@author: A30123
"""
X=np.asarray([173,155,175,171,166,167,163,155,159,168,166,169,159,154,160,66,49,72,68,63,64,61,52,55,65,61,73,57,49,60])
X=np.transpose(np.reshape(X,(2,15)))
X_prime_prime2=(X-np.mean(X,axis=0))/np.std(X,axis=0)