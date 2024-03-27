# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:52:56 2024

@author: Md. Waheduzzaman Noumans
"""
from pymoo.core.problem import Problem,ElementwiseProblem
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.algorithms.soo.nonconvex.de import DE
from pymoo.problems import get_problem
from pymoo.operators.sampling.lhs import LHS
from pymoo.optimize import minimize
import numpy as np
from binary import binary
import matplotlib.pyplot as plt



#problem = get_problem("ackley", n_var=10)

def optimize(data):



    class MyProblem(ElementwiseProblem):
    
        def __init__(self):
            super().__init__(n_var=2,
                             n_obj=1,
                             n_ieq_constr=0,
                             xl=np.array([100,10e5]),
                             xu=np.array([200,30e5]))
    
        def _evaluate(self, x, out, *args, **kwargs):
            data['Turbine_inlet_temp'] = x[0]
            data['Turbine_inlet_pressure'] = x[1]
            result,_,_ = binary(data)
            f1 =  (-result['Thermal efficiency(%)'])       
            out["F"] = [f1]
    
    
    problem = MyProblem()
    
    
    algorithm = DE(
        pop_size=10
    )
    

    res = minimize(problem,
                   algorithm,
                   seed=10,
                   verbose=False)
    res.F = -1*res.F
    return res

