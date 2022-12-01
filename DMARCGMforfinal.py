import matplotlib.pyplot as plt
import numpy as np 
import math


def LinearCGDMAR(A, b, x0, tol=1e-5):
    xk = x0
    rk = np.dot(A, xk) - b

    #pk is the step size
    pk = -rk
    rk_norm = np.linalg.norm(rk)
    
    
    iter = 0
    while rk_norm > tol:
        apk = np.dot(A, pk)
        rkrk = np.dot(rk, rk)
        gkminusone = rk
        alpha = rkrk / np.dot(pk, apk)
        xk = xk + alpha * pk
        rk = rk + alpha * apk
        gk = rk
        
        
        normgk = np.linalg.norm(gk)
        normgksquare = normgk**2

        LHS = normgksquare
        RHS =(normgk/np.linalg.norm(gk-gkminusone)**2) *abs((np.dot(gkminusone,gk)))
        
        #calculating the DMAR search direction
        if(LHS >= RHS):
            beta = (LHS - RHS)/(np.linalg.norm(gkminusone)**2)
        else:
            beta = 0
    

        pk = -rk + beta * pk
        
        
        
        rk_norm = np.linalg.norm(rk)
        iter = iter+1
        
    return xk


