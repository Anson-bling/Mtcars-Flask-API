#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv("scripts/mtcars.csv")

predictor = data[['cyl', 'disp', 'hp', 'drat', 'wt', 'qsec']]
target = data['mpg']

lm = LinearRegression().fit(predictor, target)


def predict(dict_values, col_imp=predictor.columns, model=lm):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1, -1)
    y_pred = model.predict(x)[0]
    return y_pred




