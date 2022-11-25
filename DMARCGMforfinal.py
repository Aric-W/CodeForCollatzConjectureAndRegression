import matplotlib.pyplot as plt
import numpy as np


def LinearCGDMAR(A, b, x0, tol=1e-5):
    xk = x0
    rk = np.dot(A, xk) - b
    pk = -rk
    rk_norm = np.linalg.norm(rk)
    
    num_iter = 0
    curve_x = [xk]
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
        RHS =(normgk/np.linalg.norm(gk-gkminusone)**2) *(np.dot(gkminusone,gk))
        
        if(LHS >= RHS):
            beta = (LHS - RHS)/(np.linalg.norm(gkminusone)**2)
        else:
            beta = 0
    # beta = np.dot(rk, rk) / rkrk

        pk = -rk + beta * pk
        
        num_iter += 1
        #curve_x.append(xk)
        rk_norm = np.linalg.norm(rk)
        #print('Iteration: {} \t x = {} \t residual = {:.4f}'.
        #      format(num_iter, xk, rk_norm))
    
    #print('\nSolution: \t x = {}'.format(xk))
        
    #return np.array(curve_x)
    return xk

#first array is the topmost row
A = [[5,0],[1,1]]
x0 = [0,0]
b = [1,1]

print(LinearCGDMAR(A, b, x0, tol=1e-7))