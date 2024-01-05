import numpy as np

def Set_s(N:int):
    """This function populates the matrix of slip systems.
   
    The number of slip systems is a key input in Crystal Plasticity models.
    In our sample simulation, we have 12 slip systems.
    This function is currently only coded for this example (i.e. N=12), but
    it should be expanded in the future to handle other scenarios.
    `Here`_ is a link to our paper. 
   
   
    Args:
        N (int): The number of slip systems. (i.e. needs to be 12, currently)
   
    Returns:
        s: The specific matrix of slip systems. (a 12x3 - or Nx3 - numpy array)
   
    .. _Here:
        https://link.springer.com/article/10.1007/s00466-021-02073-7
   
    """
   
   
   
    # Assumption that N = 12
    
    s = np.zeros([N,3]) # 3 for [x,y,z] values
   
    s[0] =  [ 1, -1,  1] # the extra spaces are just for visual effect
    s[1] =  [-1, -1,  1]
    s[2] =  [ 1,  1,  1]
    s[3] =  [-1,  1,  1]
    s[4] =  [-1,  1,  1]
    s[5] =  [-1, -1,  1]
    s[6] =  [ 1,  1,  1]
    s[7] =  [ 1, -1,  1]
    s[8] =  [-1,  1,  1]
    s[9] =  [-1,  1, -1]
    s[10] = [ 1,  1,  1]
    s[11] = [ 1,  1, -1]
    
    b = 0.5 # normalization factor for this particular set of vectors
    s = np.multiply(s,b)
    
    return(s)


if __name__ == "__main__":
    A = Set_s(12)

    print(A)
