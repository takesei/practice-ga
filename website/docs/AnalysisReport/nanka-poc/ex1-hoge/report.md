import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Analysis Report: test[test]
- date: 2021/5/26
- author: takesei

## Overview
Test converting ipynb to markdown

## Data Location
- DUMMY URL
  - These files must be located in `./data`

---
```python
!pip install -r requirements.txt
```

<Tabs
defaultValue='stdout_batch'
values={[
{label: "STDOUT", value: 'stdout_batch'},
]}>

<TabItem value='stdout_batch'>

:::info STDOUT
```text
Requirement already satisfied: numpy==1.20.3 in /opt/conda/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (1.20.3)

```
:::
</TabItem>
</Tabs>


---
```python
import os
from typing import NamedTuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import mylib as lib
```



---
```python
class ScriptConfig(NamedTuple):
    # Write the Constant Value here...
    input_dir: str = './data'
    output_dir: str = './output'

conf = ScriptConfig()
os.makedirs(conf.output_dir, exist_ok=True)
```



---
```python
data = np.arange(100).reshape(10, -10).T
lib.multiplot(data)
```

<Tabs
defaultValue='image_png'
values={[
{label: "Image", value: 'image_png'},
{label: "[Out]", value: 'text_plain_batch'},
]}>

<TabItem value='image_png'>

:::note Image
![fig/4-0.png](fig/4-0.png)
:::
</TabItem>
<TabItem value='text_plain_batch'>

:::note Out
```text
<Figure size 576x324 with 10 Axes>
```
:::
</TabItem>
</Tabs>


---