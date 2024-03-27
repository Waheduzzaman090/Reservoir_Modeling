# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 00:54:18 2019

@author: Md. Waheduzzman Nouman
"""
import ThermoProperty as TP
from scipy.optimize import brentq
import numpy as np


def Pinch(Ph0,Th0,m_h,fluid_h,Pc0,Tc0,m_c,fluid_c,PPT,N = 500):
    
    def f(Tb): #pinch at regenerator
        Th = np.zeros(N+1)
        Tc = np.zeros(N+1)
        dT = np.zeros(N+1)
        h_h = np.zeros(N+1)
        h_c = np.zeros(N+1)
        
        h5 = TP.H_TP(Tc0,Pc0,fluid_c)
        
        h_b = TP.H_TP(Tb,Pc0,fluid_c)
        Q = m_c*(h_b - h5)
        q = Q/(N)
        
        
        
        Th[0] = Th0
        Tc[0] = Tb
        dT[0] = Th[0] - Tc[0]
        
        h_h[0] = TP.H_TP(Th[0],Ph0,fluid_h)
        h_c[0] = TP.H_TP(Tc[0],Pc0,fluid_c)
        
        for n in range(1,N+1):
            h_h[n] = h_h[n-1] - q/m_h
            h_c[n] = h_c[n-1] - q/m_c
            
            Th[n] = TP.T_PH(Ph0,h_h[n],fluid_h)
            Tc[n] = TP.T_PH(Pc0,h_c[n],fluid_c)
            
            dT[n] = Th[n] - Tc[n]
            
        return min(dT) - PPT
        
    
    Tb = brentq(f,Tc0,Th0)
    return Tb

def Pinch_check(Ph0,Th0,m_h,fluid_h,Pc0,Tc0,m_c,fluid_c,Tb,PPT,N = 500):
    #(inlet conditions of HEX(Ph0,Th0,m_h,Pc0,Tc0,m_c),Tb cold fluid outlet temperature )
        
        
    Th = np.zeros(N+1)
    Tc = np.zeros(N+1)
    dT = np.zeros(N+1)
    h_h = np.zeros(N+1)
    h_c = np.zeros(N+1)
    
    h5 = TP.H_TP(Tc0,Pc0,fluid_c)
    
    h_b = TP.H_TP(Tb,Pc0,fluid_c)
    Q = m_c*(h_b - h5)
    q = Q/(N)
    
    
    
    Th[0] = Th0
    Tc[0] = Tb
    dT[0] = Th[0] - Tc[0]
    
    h_h[0] = TP.H_TP(Th[0],Ph0,fluid_h)
    h_c[0] = TP.H_TP(Tc[0],Pc0,fluid_c)
    
    for n in range(1,N+1):
        h_h[n] = h_h[n-1] - q/m_h
        h_c[n] = h_c[n-1] - q/m_c
        
        Th[n] = TP.T_PH(Ph0,h_h[n],fluid_h)
        Tc[n] = TP.T_PH(Pc0,h_c[n],fluid_c)
        
        dT[n] = Th[n] - Tc[n]
    # plt.plot(range(0,N+1),dT)
    # plt.plot(range(0,N+1),Th-273.15)
    # plt.plot(range(0,N+1),Tc-273.15)
    # plt.show()
   
    if min(dT) < PPT:
        print("pinch occure ",min(dT))
        
        return 0
    else:
        return min(dT)
        