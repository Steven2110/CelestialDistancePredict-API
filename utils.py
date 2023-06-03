import pickle
import pandas as pd
import os
import sklearn

from constants import c, H

def DTRPredict(ug: float, gr: float, ri: float, iz: float) -> float:
    cwd = os.getcwd()
    path = 'model/DTRmodel.pkl'
    print(cwd)
    print(os.path.join(cwd, path), flush=True)
    data = {
        'ug': [ug],
        'gr': [gr],
        'ri': [ri],
        'iz': [iz]
    }
    X = pd.DataFrame(data)
    print(X)

    pickled_model = pickle.load(open(os.path.join(cwd, path), 'rb'))
    
    y = pickled_model.predict(X)
    return y[0]

def get_distance_from_redshift(redshift: float) -> float:
    '''
    Return distance of an object in Megaparsec from redshift value (z) using velocity formula.
    v = c * z = H * d
    * v = velocity (km/s)
    * c = speed of light (km/s)
    * z = redshift 
    * H = Hubble parameter (km/s)
    * d = distance (Mpc)(Megaparsec)
    '''
    print(c)
    print(c * redshift)
    return c * redshift / H
