import numpy as np 
class Simplex(obj_fun):
    def __init__(self,obj_fun,max_mode=True):
        self.mat=np.array([[0],obj_fun])
        self.max_mode=max_mode
    def add_Constraint(self,a,b):
        self.mat=np.vstack