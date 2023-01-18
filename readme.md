# py-SVG-converter

A easy way to convert a picture to SVG file.
<div style="display:flex; justify-content:center; align-items: center; width: 100%">
    <img src="./docs/input.png" alt="input.png" style="width:40%" />
    <span>👉</span>
    <img src="./docs/output.svg" alt="output.svg" style="width:40%;" />
</div>

## Installation

### Windows
 
 1. `git clone https://github.com/HaleyCH/py-SVG-converter.git`

 2. install `pypotrace` follow [this link](https://github.com/flupke/pypotrace#windows)

 3. `cd py-SVG-converter && pip install -r requirements.txt`

 ### Ubuntu

1. Install system dependencies:
```shell
$ sudo apt-get install build-essential python-dev libagg-dev libpotrace-dev pkg-config
```

2. Install pypotrace:
```shell
$ git clone https://github.com/flupke/pypotrace.git
$ cd pypotrace
$ pip install numpy
$ pip install .
```

3. Install py-SVG-converter:
```shell
$ git clone https://github.com/HaleyCH/py-SVG-converter.git
$ cd py-SVG-converter && pip install -r requirements.txt
```

### CentOS/RedHat

1. Install system dependencies:
```shell
$ sudo yum -y groupinstall "Development Tools"
$ sudo yum -y install agg-devel potrace-devel python-devel
```

2. Install pypotrace:
```shell
$ git clone https://github.com/flupke/pypotrace.git
$ cd pypotrace
$ pip install numpy
$ pip install .
```

3. Install py-SVG-converter:
```shell
$ git clone https://github.com/HaleyCH/py-SVG-converter.git
$ cd py-SVG-converter && pip install -r requirements.txt
```

## Usage:

```shell
$ cd py-SVG-converter
$ python convert.py -i path/to/input/img -o path/to/output/img -n total_color_num
```

or

```python
from convert.py import convert
import numpy as np
from PIL import Image

n_cluster = 5  # number of cluster centers
i = Image.open("path/to/input/img")
#
#  your process to img
#
arr_i = np.array(i)
convert(arr_i, n_cluster, "path/to/output/img")
```

# Related works

- [flupke/pypotrace](https://github.com/flupke/pypotrace)
