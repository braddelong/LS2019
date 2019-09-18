# delong_classes.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class solow:
    
    """ 
    Implements the Solow growth model calculation of the 
    capital-output ratio κ and other model variables
    using the update rule:
    
    κ_{t+1} = κ_t + ( 1 - α) ( s - (n+g+δ)κ_t )
    
    Built upon and modified from Stachurski-Sargeant 
    <https://quantecon.org> class **Solow** 
    <https://lectures.quantecon.org/py/python_oop.html>
    """
    
    def __init__(self, n=0.01,              # population growth rate
                       s=0.20,              # savings rate
                       δ=0.03,              # depreciation rate
                       α=1/3,               # share of capital
                       g=0.01,              # productivity
                       κ=0.2/(.01+.01+.03), # current capital-labor ratio
                       E=1.0,               # current efficiency of labor
                       L=1.0):              # current labor force  

        self.n, self.s, self.δ, self.α, self.g = n, s, δ, α, g
        self.κ, self.E, self.L = κ, E, L
        self.Y = self.κ**(self.α/(1-self.α))*self.E*self.L
        self.K = self.κ * self.Y
        self.y = self.Y/self.L
        self.α1 = 1-((1-np.exp((self.α-1)*(self.n+self.g+self.δ)))/(self.n+self.g+self.δ))
        self.initdata = vars(self).copy()
        
    def calc_next_period_kappa(self):
        "Calculate the next period capital-output ratio."
        # Unpack parameters (get rid of self to simplify notation)
        n, s, δ, α1, g, κ= self.n, self.s, self.δ, self.α1, self.g, self.κ
        # Apply the update rule
        return (κ + (1 - α1)*( s - (n+g+δ)*κ ))

    def calc_next_period_E(self):
        "Calculate the next period efficiency of labor."
        # Unpack parameters (get rid of self to simplify notation)
        E, g = self.E, self.g
        # Apply the update rule
        return (E * np.exp(g))

    def calc_next_period_L(self):
        "Calculate the next period labor force."



class malthusian:
    
    """
    Implements the Malthusian Model with:
    
    1. population growth 
        n =  β*(y/(ϕ ysub)-1)
        
    2. growth of efficiency-of-labor 
        g = h-n/γ
    """
    def __init__(self,
                 L = 1,               # initial labor force
                 E = 1/3,             # initial efficiency of labor
                 K = 3.0,             # initial capital stock
                 
                               # determinants of n (population growth):
                 β = 0.025,           # responsiveness of population growth to increased prosperity.
                 ϕ = 1,               # luxuries parameter
                 ysub = 1,            # subsistence level
                 
                               # determinants of g(efficiency-of-labor growth):
                 h = 0,               # rate at which useful ideas are generated
                 γ = 2.0,             # effect-of-resource scarcity parameter  
                 
                 s = 0.15,            # savings-investment rate
                 α = 0.5,             # orientation-of-growth-toward-capital parameter
                 δ = 0.05,            # deprecation rate on capital parameter
                ):
        self.L, self.E, self.K, self.h, self.γ, self.s, self.α, self.δ = L, E, K, h, γ, s, α, δ 
        self.β, self.ϕ, self.ysub = β, ϕ, ysub
        
        # production (or output)
        self.Y = self.K**self.α*(self.E*self.L)**(1-self.α) 
        self.y = self.Y/self.L
        
        # capital-output ratio 
        self.κ = self.K/self.Y    
        
        # population growth 
        self.n = self.β*((self.y/(self.ϕ*self.ysub)) - 1)
        
        # growth rate of efficiency-of-labor
        self.g = self.h-self.n/self.γ
        
        # store initial data
        self.initdata = vars(self).copy()
    
    def update(self):
        # unpack parameters
        K, s, Y, δ, L, n, E, g, α =self.K, self.s, self.Y, self.δ, self.L, self.n, self.E, self.g, self.α
        β, ϕ, ysub, h, γ = self.β, self.ϕ, self.ysub, self.h, self.γ
        
        #update variables        
        K = s*Y + (1-δ)*K
        L = L*np.exp(n)
        E = E*np.exp(g)
        Y = K**α*(E*L)**(1-α)
        y = Y/L
        κ = K/Y
        n = β*(y/(ϕ*ysub)-1)
        g = h-n/γ
                
        #store variables
        self.K, self.s, self.Y, self.δ, self.L, self.n, self.E, self.g, self.α = K, s, Y, δ, L, n, E, g, α
        self.κ, self.y = κ, y
        
    def gen_seq(self, t, var = 'κ', init = True, log = False):
        "Generate and return time series of selected variable. Variable is κ by default."
        
        path = []
        
        # initialize data 
        if init == True:
            for para in self.initdata:
                 setattr(self, para, self.initdata[para])

        for i in range(t):
            path.append(vars(self)[var])
            self.update()
        
        if log == False:
            return path
        else:
            return np.log(np.asarray(path))

    def steady_state(self, disp = True):
        "Calculate variable values in the steady state"
        #unpack parameters
        s, γ, h, δ, ϕ, ysub, β, α= self.s, self.γ, self.h, self.δ, self.ϕ, self.ysub, self.β, self.α
        
        self.mal_κ = s/(γ*h+δ)
        # malthusian rate of population growth
        self.mal_n = γ*h
        # malthusian standard of living
        self.mal_y = ϕ*(ysub+γ*h/β)
        self.mal_E = self.mal_y*((γ*h+δ)/s)**(α/(1-α))
        
        if display == True:
            return(f'steady-state capital-output ratio κ: {self.mal_κ:.2f}')
            return(f'Malthusian rate of population growth n: {self.mal_n: .2f}')
            return(f'Malthusian standard of living y: {self.mal_y:.2f}')
            return(f'steady-state efficiency-of-labor E: {self.mal_E:.2f}') 
        else: 
            return(self.mal_κ,self.mal_n,self.mal_y,self.mal_E)



class gini:
    """
    For a two-class distribution of income. Initialize 
    the class with a size-of-upper-class variable
    equal to 1/5 and a share-of-upper-class variable
    equal to 4/5
    """
    
    def __init__(self,
                 upper_class = 1/5,       # size of upper class
                 share = 4/5              # share of upper class
                ):
        self.upper_class = upper_class
        self.share = share
        self.gini_value = self.share - self.upper_class
        self.income_ratio = ((self.share/self.upper_class)/
            ((1-self.share)/(1-self.upper_class)))

