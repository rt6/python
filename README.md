# Python and PyCharm Demo

## ALEMBIC

Use Alembic to automate DB migrations (add/create tables and fields) between production and development.

The alembic directory contains all the automatic generated migration scripts.
It sits under your applications source code tree. 
Your application may have more than 1 alembic sub directory.
These alembic directories are also called **migration environment.**
```sh
/app
    /alembic1
    /alembic2
```

### Install Alembic
```bash
conda install alembic
```

### Initialize migration environment
This will create a directory that contains all your alembic DB migration source code.

```bash
cd app
alembic init migration
```

Open `alembic.ini` in the /myapp directory, and add the db engine details:
```python
# change
sqlalchemy.url = driver://user:pass@localhost/dbname
# to
sqlalchemy.url = mysql+pymysql://root@localhost/demo
```

Open `env.py` in the `migrations/` directory and import the Base object:
This links Alembic with SqlAlchemy.
Alembic uses this to autogenerate migration code.

```python
parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(parent_dir)
from myapp.models import Base
target_metadata = Base.metadata
```

Now you can autogenerate the migration scripts 
```bash
alembic revision --autogenerate -m "first revision"
alembic upgrade heads
alembic current
alembic heads
```


## VIRTUALENV
Package dependency and package version management.

On windows, open command prompt:
```sh
# create a new virtual environment
virutalenv ENV
```
For more details: https://virtualenv.pypa.io/en/stable/userguide/#activate-script

To use virtualenv
```sh
# activate the virtual environment
source bin/activate

# list packages 
pip freeze --local 
pip list --local

# deactivate the virtual environment
deactivate
```
