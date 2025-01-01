#-*- coding: utf_8 -*-

import os
from dbase3_py import DbaseFile, FieldType

def testdb():
    global test, index, jdoe
    
    if os.path.exists('db/test.dbf'):
        test = DbaseFile('db/test.dbf')
    else:
        test = DbaseFile.create('db/test.dbf',
                            [('name', FieldType.CHARACTER.value, 50, 0),
                             ('age', FieldType.NUMERIC.value, 3, 0)])
        test.add_record('John Doe', 30)
        test.add_record('Jane Doe', 25)

    index, jdoe = test.search('name', 'John Doe')
    jdoe['age'] += 1
    test.update_record(index, jdoe)
    jdoe = test[index]
    print("\nHere, John Doe!\n", jdoe, "\n")
    print()

    input("Press Enter to continue...")


