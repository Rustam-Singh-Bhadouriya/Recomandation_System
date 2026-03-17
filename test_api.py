from API.helper.formatter import Simplify_split_arr, Simplify_pred
import requests as rq
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

url = "http://127.0.0.1:5000/predict"

data = {
    "features": [10, 3, 4.6, "male", 500, 4.3, "PUMA", 0.82, 600, "Yes", "summer", "plains"]
}

res = rq.post(url, json=data)

print("Status:", res.status_code)
print(res.json())  