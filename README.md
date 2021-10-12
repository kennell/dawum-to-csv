# dawum-to-csv

This script parses german election survey result data data from dawum.de JSON format to a flat CSV file

### Requirements

* Python 3.6+

### Dependencies

* Requests
* python-slugify[unidecode]

### Usage

1. Clone this repository

`git clone https://github.com/kennell/dawum-to-csv`

2. Install the dependencies

`pip install requests python-slugify[unidecode]` 

3. Run script 

`python3 dawum-to-csv.py > output.csv`
