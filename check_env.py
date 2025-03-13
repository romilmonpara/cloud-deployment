# python -m venv myenv
# myenv\Scripts\activate 

import os

# check if virtual environment is runningoip
def is_virtualenv():
    return 'VIRTUAL_ENV' in os.environ

if is_virtualenv():
    print("Running inside a virtual environment.")
else:
    print("Not running inside a virtual environment.")
    