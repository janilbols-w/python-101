# Pandas usage
```python
import pandas as pd
```

## merge
```python
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                    'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
df2 = pd.DataFrame({'key': [ 'K3', 'K4', 'K5','K6', 'K7', 'K8'],
                    'B': ['B0', 'B1', 'B2', 'B3', 'B4', 'B5']})
pd.merge(df1, df2, on='key',how='outer')                    
```
```md
[out]:
id  key A B
0	K0	A0	NaN
1	K1	A1	NaN
2	K2	A2	NaN
3	K3	A3	B0
4	K4	A4	B1
5	K5	A5	B2
6	K6	NaN	B3
7	K7	NaN	B4
8	K8	NaN	B5
```
