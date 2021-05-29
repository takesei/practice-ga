# Import your packages here
# Ex. import numpy as np


# Define your functions here
# Ex.
# def double(arg: int):
#   return arg * 2

import matplotlib.pyplot as plt
import pandas as pd
from typing import Iterable

def multiplot(data: Iterable[Iterable[float]]):
    temp = pd.DataFrame(data)
    temp.plot(figsize=(8, 4.5), sharey=True, subplots=True, layout=(2, len(temp)//2))