# Biblioteca Python para DBase III

Biblioteca de Python diseñada para manipular archivos de bases de datos DBase III. Permite leer, escribir, agregar y actualizar registros en la base de datos.

Aunque este formato de archivo para bases de datos ya no se utiliza en gran medida, el presente trabajo es una miniherramienta útil para recuperar datos antiguos, así como un homenaje a una hermosa parte de la historia de la informática.

## Características

- Leer archivos de bases de datos DBase III
- Escribir en archivos de bases de datos DBase III
- Agregar nuevos registros
- Actualizar registros existentes
- Filtrar y buscar registros

## Instalación

Para instalar la biblioteca, clone este repositorio y navegue hasta el directorio del proyecto:

```bash
git clone https://github.com/sandy98/dbase3-py.git
cd dbase3-py
```

o

```bash 
pip install dbase3-py
```

## Uso

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

El módulo en sí, la clase DBaseFile y todos sus métodos están completamente documentados, por lo que debería ser fácil seguirlo.

Básicamente, cada instancia de DBaseFile, ya sea instanciada a través de un archivo DBase III existente o creada a través del método de fábrica DBaseFile.create(filename), es un objeto tipo lista con capacidades de indexación, que también actúa como un iterador a través de los registros presentes en el archivo .dbf. También admite el método 'len', que informa la cantidad de registros presentes en la base de datos, incluso aquellos marcados para su eliminación.
Además de eso, hay un grupo de métodos destinados a la manipulación de datos (add_record para inserciones, update_record para actualizaciones y del_record para marcar/desmarcar eliminaciones).
También hay un grupo de métodos (búsqueda, índice, hallazgo, filtro) para ayudar a recuperar datos seleccionados.

En su etapa actual de desarrollo, no hay soporte para campos de memo o campos de índice, aunque esto está planeado para futuras versiones, en caso de que surja suficiente interés.
También está previsto un método `exec` para ejecutar instrucciones similares a SQL, pero no está operativo en este momento.

Para obtener más información, consulte la documentación a continuación.

## Documentación

### Clases

#### `DBaseFile`

Clase para manipular archivos de base de datos DBase III.

### Métodos 'Dunder' y 'privados' 

- `__init__(self, filename: str)`: Inicializa una instancia de DBase3File desde un archivo dbf existente.
- `__del__(self)`: Cierra el archivo de base de datos cuando se destruye la instancia.
- `__len__(self)`: Devuelve la cantidad de registros en la base de datos, incluidos los registros marcados para eliminarse. Permite escribir: `len(dbasefileobj)`
- `__getitem__(self, key)`: Devuelve un único registro o una lista de registros (si se utiliza la notación de 'slices') de la base de datos. Permite: `dbasefileobj[3]` o `dbasefileobj[3:7]`  
- `__iter__(self)`: Devuelve un iterador sobre los registros de la base de datos. Permite: `for record in dbasefileobj: ...`
- `__str__(self)`: Devuelve una representación de cadena de la base de datos.
- `_init(self)`: Inicializa la estructura de la base de datos leyendo el encabezado y los campos. Destinado para uso privado por parte de instancias de DBaseFile.
- `def _test_key(self, key)`: Comprueba si la clave está dentro del rango válido de índices de registros. Genera un error de índice si la clave está fuera del rango. Solo para uso interno.
    
### Class Methods

- `create(cls, filename: str, fields: List[Tuple[str, FieldType, int, int]])`: Crea un nuevo archivo de base de datos DBase III con los campos especificados. Devuelve un objeto DbaseFile que apunta al archivo dbase recién creado.
### Data Manipulation methods

- `add_record(self, record_data: dict)`: Agrega un nuevo registro a la base de datos.
- `update_record(self, index: int, record_data: dict)`: Actualiza un registro existente en la base de datos.
- `save_record(self, key, record)`: Escribe un registro (diccionario con nombres de campos y valores de campos) en la base de datos en el índice especificado. Parámetros: la clave es el índice (posición basada en 0 en el archivo dbf). El registro es un diccionario que corresponde a un elemento en la base de datos. (i.e: {'id': 1, 'name': "Jane Doe"}) Usado internamente por `update_record` 
- `del_record(self, key, value = True)`: Marca para su eliminación el registro identificado por el índice 'clave', o lo desmarca si `value == False`. Para borrar efectivamente el registro del disco, la eliminación debe confirmarse utilizando `dbasefileobj.write()`
- `write(self, filename=None)`: Escribe el archivo actual en el disco, omitiendo los registros marcados para su eliminación. Si se proporciona un nombre de archivo distinto del actual, se guarda el archivo de base de datos en el nuevo destino y se conserva el nombre de archivo anterior.

### Data searching/filtering methods

-  `search(self, fieldname, value, start=0, funcname="", comp_func=None)`: Escribe el archivo actual en el disco, omitiendo los registros marcados para su eliminación. Si se proporciona un nombre de archivo distinto del actual, se guarda el archivo de base de datos en el nuevo destino y se conserva el nombre de archivo anterior.
-  `find(self, fieldname, value, start=0, comp_func=None)`: Contenedor para search() con funcname="find". Devuelve el primer registro (diccionario) encontrado, o None si no se encuentra ningún registro que cumpla los criterios dados.
-  `index(self, fieldname, value, start=0, comp_func=None)`:  Contenedor para search() con funcname="index". Devuelve el índice del primer registro encontrado o -1 si no se encuentra ningún registro que cumpla los criterios dados.
-  `filter(self, fieldname, value, comp_func=None)`: Devuelve una lista de registros (diccionarios) que cumplen los criterios especificados.
- `exec(self, sql_cmd:str)`: Diseñado para recuperar datos de forma personalizada. Aún no está operativo. Al invocarlo, se genera un error NotImplemented.
### Data listing methods

-  `list(self, start=0, stop=None, fieldsep="|", recordsep='\n', records:list=None)`: Devuelve una lista de registros de la base de datos, comenzando en 'start', terminando en 'stop' o EOF, con campos separados por 'fieldsep' y registros separados por '\n'. Si 'records' no es None, se utiliza la lista proporcionada en lugar de recuperar valores de la base de datos.
-  `csv(self, start=0, stop=None, records:list = None)`: Contenedor para 'lista', que utiliza "," como separador de campos.
-  `table(self, start=0, stop=None, records:list = None)`: Recupera registros seleccionados utilizando el formato ad-hoc, el mismo que proporciona la CLI de sqlite3 en modo .table.
### Static Methods (Auxiliary functions for searching/filtering)

- `istartswith(f: str, v: str) -> bool`: Comprueba si la cadena `f` comienza con la cadena `v`, ignorando mayúsculas y minúsculas.
- `iendswith(f: str, v: str) -> bool`: Comprueba si la cadena `f` termina con la cadena `v`, ignorando mayúsculas y minúsculas.

## Contribuciones

¡Se aceptan contribuciones! Abra un issue o envíe una solicitud de incorporación de cambios.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulte el archivo LICENCIA para obtener más detalles.
## Contact

Para cualquier duda o sugerencia, por favor contacte con nosotros. [Domingo E. Savoretti](mailto:esavoretti@gmail.com).

