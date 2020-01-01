import matplotlib.pyplot as plt
f=open('Dataset_1.txt',"r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(x.split()[0])
f.close()
result = list(map(int, result)) 
#print(result)
import numpy as np
import random
def coin_em(result, theta_A=None, theta_B=None, theta_C=None, maxiter=200):
    # Initial Guess
    theta_A = theta_A or random.random()
    theta_B = theta_B or random.random()
    theta_C = theta_C or random.random()
    thetas = [(theta_A, theta_B, theta_C)]
    # Iterate
    for c in range(maxiter):
        print("#%d:\t%0.f %0.2f %0.2f" % (c, theta_A, theta_B,theta_C))
        heads_A, tails_A, heads_B, tails_B, head_C, tails_C = e_step(result, theta_A, theta_B,theta_C)
        theta_A, theta_B, theta_C = m_step(heads_A, tails_A, heads_B, tails_B, head_C, tails_C)
        
    thetas.append((theta_A,theta_B,theta_C)) 
    return thetas, (theta_A,theta_B, theta_C)

def e_step(result, theta_A, theta_B, theta_C):    
    heads_A, tails_A = 0,0
    heads_B, tails_B = 0,0
    heads_C, tails_C = 0,0
    for i in range(len(result)):
        likelihood_A=coin_likelihood(result[i],theta_A)
        likelihood_B=coin_likelihood(result[i],theta_B)
        likelihood_C=coin_likelihood(result[i],theta_C)
        likelihood_E=likelihood_A+likelihood_B+likelihood_C
        p_A = likelihood_A / (likelihood_A + likelihood_B+likelihood_C)
        p_B = likelihood_B / (likelihood_A + likelihood_B+likelihood_C)
        p_C = likelihood_C / (likelihood_A + likelihood_B+likelihood_C)
        
        heads_A += p_A * result[i]
        tails_A += p_A * (20-result[i])
        heads_B += p_B * result[i]
        tails_B += p_B * (20-result[i])
        heads_C += p_C * result[i]
        tails_C += p_C * (20-result[i])
        plt.plot((i,likelihood_E))
   print(‘Pis are as follows’ )
   print(p_A/p_A+p_B+p_C)
   print(p_B/p_A+p_B+p_C)
   print(p_C/p_A+p_B+p_C)
   
   return heads_A, tails_A, heads_B, tails_B, heads_C, tails_C

def m_step(heads_A, tails_A, heads_B, tails_B, heads_C, tails_C):
    
    
    t_A = heads_A / (heads_A + tails_A)
    t_B = heads_B / (heads_B + tails_B)
    t_C = heads_C / (heads_C + tails_C)
    return t_A, t_B, t_C

def coin_likelihood(heads, bias):
    numHeads = heads
    x=pow(bias, numHeads) * pow(1-bias, 20-numHeads)
    return pow(bias, numHeads) * pow(1-bias, 20-numHeads)
plt.show()

thetas, _ = coin_em(result, 0.6, 0.5, 0.1, maxiter=200) 
