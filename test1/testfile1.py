import datetime
import pandas as pd

yhoo = DataReader("yhoo", "yahoo", datetime.datetime(2007, 1, 1),
    datetime.datetime(2012,1,1))
