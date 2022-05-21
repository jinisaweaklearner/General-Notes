## generate new env
python3 -m venv ./env_name

## activate env
source ./bin/activate

## decatevate env
deactivate

## import from other folder
```
# - folder_a
#    - common.py
#   - folder_b
#     - file.py
from .common import execute_query

# use __init__.py
https://stackoverflow.com/questions/448271/what-is-init-py-for
```

## add arguments
```
import argparse

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument("--print_string", help="Prints the supplied argument.", default=”A random string.”)

args = parser.parse_args()

print(args.print_string)
```

