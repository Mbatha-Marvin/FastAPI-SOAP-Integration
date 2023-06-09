# Prerequisite

1. Python 3.11



## Installation instructions

1. Unzip the project and cd into the project

2. Create a python virtual environment and activate it

3. Run the following command to install required python libraries 
   
   ```python
   pip install -r requirements.txt
   ```

4. To run the app execute the following command
   
   ```python
   uvicorn main:app --host=0.0.0.0 --port=8000 --reload
   ```

5. Once running head over to http://127.0.0.1:8000/v1/docs to access the swagger documentation.
   
   
