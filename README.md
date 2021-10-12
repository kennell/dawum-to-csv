# dawum-to-csv

This script parses german election survey result data data from [dawum.de](https://dawum.de) JSON format to a flat CSV file for easier processing.

### Requirements

* Python 3.6+

### Dependencies

* requests
* python-slugify[unidecode]

### Usage

1. Clone this repository

`git clone https://github.com/kennell/dawum-to-csv`

2. Install the dependencies

`pip install requests python-slugify[unidecode]` 

3. Run script 

`python3 dawum-to-csv.py > output.csv`

### Legal

This script only parses the data provided by dawum.de Please make sure you understand the [licensing requirements](https://dawum.de/API/) for the actual data.
