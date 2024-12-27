# DBase III Python Library

Python library meant to manipulate DBase III database files. It allows reading, writing, adding, and updating records in the database.

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

or

```bash 
pip install dbase3-py
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

### Dunder and 'private' Methods

- `__init__(self, filename: str)`: Initializes an instance of DBase3File from an existing dbf file.
- `__del__(self)`: Closes the database file when the instance is destroyed.
- `__len__(self)`: Returns the number of records in the database, including records marked to be deleted. Allows writing: `len(dbasefileobj)`
- `__getitem__(self, key)`: Returns a single record or a list of records (if slice notation is used) from the database. Allows: `dbasefileobj[3]` or `dbasefileobj[3:7]`  
- `__iter__(self)`: Returns an iterator over the records in the database. Allows `for record in dbasefileobj: ...`
- `__str__(self)`: Returns a string representation of the database.
- `_init(self)`: Initializes the database structure by reading the header and fields. Meant for private use by DBaseFile instances.
- `def _test_key(self, key)`: Tests if the key is within the valid range of record indexes. Raises an IndexError if the key is out of range. Meant for internal use only.
    
### Class Methods

- `create(cls, filename: str, fields: List[Tuple[str, FieldType, int, int]])`: Creates a new DBase III database file with the specified fields. Returns a DbaseFile object pointing to newly created dbase file.

### Data Manipulation methods

- `add_record(self, record_data: dict)`: Adds a new record to the database.
- `update_record(self, index: int, record_data: dict)`: Updates an existing record in the database.
- `save_record(self, key, record)`: Writes a record (dictionary with field names and field values) to the database at the specified index. Params: key is the index (0 based position in dbf file). record is a dictionary corresponding to an item in the database (i.e: {'id': 1, 'name': "Jane Doe"}) Used internally by `update_record` 
- `del_record(self, key, value = True)`: Marks for deletion the record identified by the index 'key', or unmarks it if `value == False`. To efectively erase the record from disk the deletion must be confirmed by using `dbasefileobj.write()`

### Data searching/filtering methods

-  `search(self, fieldname, value, start=0, funcname="", comp_func=None)`: Searches for a record with the specified value in the specified field, starting from the specified index, for which the specified comparison function returns True. Returns a tuple with index:int and record:dict
-  `find(self, fieldname, value, start=0, comp_func=None)`: Wrapper for search() with funcname="find". Returns the first record (dictionary) found, or None if no record meeting given criteria is found.
-  `index(self, fieldname, value, start=0, comp_func=None)`:  Wrapper for search() with funcname="index". Returns index of the first record found, or -1 if no record meeting given criteria is found.
-  `filter(self, fieldname, value, comp_func=None)`: Returns a list of records (dictionaries) that meet the specified criteria.

### Data listing methods

-  `list(self, start=0, stop=None, fieldsep="|", recordsep='\n', records:list=None)`: Returns a list of records from the database, starting at 'start', ending at 'stop' or EOF, having fields separated by 'fieldsep' and records separated by '\n'. If 'records' is not None, the provided list is used instead of retrieving values from the database.
-  `csv(self, start=0, stop=None, records:list = None)`: Wrapper for 'list', using ',' as fieldsep.
-  `table(self, start=0, stop=None, records:list = None)`: Retrieves selected records using ad-hoc format, same as provided by sqlite3 CLI in .table mode.

### Static Methods (Auxiliary functions for searching/filtering)

- `istartswith(f: str, v: str) -> bool`: Checks if the string `f` starts with the string `v`, ignoring case.
- `iendswith(f: str, v: str) -> bool`: Checks if the string `f` ends with the string `v`, ignoring case.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact [Domingo E. Savoretti](mailto:esavoretti@gmail.com).

```

```
