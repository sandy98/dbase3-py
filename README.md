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
from dbase3_py.dbase3 import DBaseFile, FieldType
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

## Documentation

### Classes

#### `DBaseFile`

Class to manipulate DBase III database files.

- `__init__(self, filename: str)`: Initializes an instance of DBase3.
- `__del__(self)`: Closes the database file when the instance is destroyed.
- `init(self)`: Initializes the database structure by reading the header and fields.
- 

add_record(self, record_data: dict)

: Adds a new record to the database.

- `update_record(self, index: int, record_data: dict)`: Updates an existing record in the database.
- `istartswith(f: str, v: str) -> bool`: Checks if the string `f` starts with the string `v`, ignoring case.
- `iendswith(f: str, v: str) -> bool`: Checks if the string `f` ends with the string `v`, ignoring case.
- 

create(cls, filename: str, fields: List[Tuple[str, FieldType, int, int]])

: Creates a new DBase III database file with the specified fields.

### Methods

- `save_record(self, key, record)`: Writes a record (dictionary with field names and field values) to the database at the specified index. Params: key is the index (0 based position in dbf file). record is a dictionary corresponding to an item in the database (i.e: {'id': 1, 'name': "Jane Doe"})
- `__len__(self)`: Returns the number of records in the database, including records marked to be deleted.
- `__getitem__(self, key)`: Returns a single record or a list of records from the database.
- `__iter__(self)`: Returns an iterator over the records in the database.
- `__str__(self)`: Returns a string representation of the database.
 
## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact [Domingo E. Savoretti](mailto:esavoretti@gmail.com).

```

```
