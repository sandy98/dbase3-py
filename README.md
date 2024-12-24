# DBase III Python Library

This project provides a Python library to manipulate DBase III database files. It allows reading, writing, adding, and updating records in the database.

Even though this file format for databases is largely no longer in use, the present work is a minitool useful to retrieve legacy data, as much as a tribute to a beautiful part of computer history.

## Features

- Read DBase III database files
- Write to DBase III database files
- Add new records
- Update existing records
- Filter and search records

## Installation

To install the library, clone this repository and navigate to the project directory:

```bash
git clone https://github.com/sandy98/dbase3-py.git
cd dbase3-py
```

## Usage

```python
from dbase3 import DBaseFile, FieldType
test = DbaseFile.create('db/test.dbf',
                    [('name', FieldType.CHARACTER.value, 50, 0),
                        ('age', FieldType.NUMERIC.value, 3, 0)])
test.add_record('John Doe', 30)
test.add_record('Jane Doe', 25)

print(test)
print(len(test))
print(test[:])
print(test.filter('name', 'ja', comp_func=self.istartswith))

```

The module itself, DBaseFile class and all its methods are thoroughly documented, so it should be easy to follow up.
