import numpy as np
import random as rnd
import time as tm
import sys

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def solver( X, y, C, timeout, spacing ):
        (n, d) = X.shape
        t = 0
        totTime = 0

        # w is the normal vector and b is the bias
        # These are the variables that will get returned once timeout happens
        w = np.zeros( (d,) )
        b = 0
        tic = tm.perf_counter()
################################
#  Non Editable Region Ending  #
################################
        w = np.random.randn(d)
        b = rnd.random()

        # You may reinitialize w, b to your liking here
        # You may also define new variables here e.g. eta, B etc

################################
# Non Editable Region Starting #
################################
        X_new = np.ones((n,d+1))
        X_new[:,1:] = X
        W_new = np.append([0],w)
        print( w )
        print( W_new )
        while True:
                t = t + 1
                if t % spacing == 0:
                        print(totTime)
                        toc = tm.perf_counter()
                        totTime = totTime + (toc - tic)
                        if totTime > timeout:
                                print( w )
                                return (w, b, totTime)
                        else:
                                tic = tm.perf_counter()
################################
#  Non Editable Region Ending  #
################################
                #1 to be replaced by j
                for j in range(0,d+1):
                        Z = X_new.dot(W_new)
                        Z2 = y*Z
                        filter = (1-Z2)>=0
                        Z3 = np.sum(y*X_new[:,j]*filter)
                        Z4 = np.sum(X_new[:,j]*X_new[:,j]*filter)
                        Z5 = np.sum(Z*X_new[:,j]*filter)
                        '''X_new2 = X_new[filter,:]
                        y_new2 = y[filter]
                        Z3 = np.sum(y_new2*X_new2[:,j])
                        Z4 = np.sum(X_new2[:,j]*X_new2[:,j])
                        Z = Z[filter]
                        Z5 = np.sum(Z*X_new2[:,j])'''
                        W_new[j] = (2*C*Z3 - 2*C*Z5 + 2*C*W_new[j]*Z4)/(1+2*C*Z4)
                w = W_new[1:]
                b = W_new[0]




                # Write all code to perform your method updates here within the infinite while loop
                # The infinite loop will terminate once timeout is reached
                # Do not try to bypass the timer check e.g. by using continue
                # It is very easy for us to detect such bypasses - severe penalties await

                # Please note that once timeout is reached, the code will simply return w, b
                # Thus, if you wish to return the average model (as we did for GD), you need to
                # make sure that w, b store the averages at all times
                # One way to do so is to define two new "running" variables w_run and b_run
                # Make all GD updates to w_run and b_run e.g. w_run = w_run - step * delw
                # Then use a running average formula to update w and b
                # w = (w * (t-1) + w_run)/t
                # b = (b * (t-1) + b_run)/t
                # This way, w and b will always store the average and can be returned at any time
                # w, b play the role of the "cumulative" variable in the lecture notebook
                # w_run, b_run play the role of the "theta" variable in the lecture notebook
        print(w)
        return (w, b, totTime) # This return statement will never be reached
