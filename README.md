# Technical-test-data-scientist
Predicting sex using machine learning

Steps to setup and run the test

Choose the directory where the test will be run (I recommend desktop). I use the package management system conda to run Python projects. Check documentation in < https://docs.conda.io/en/latest/>.

1-	Open the terminal.app;
2-	Choose the directory with the command **cd Desktop**;
3-	Create a folder to host files and the environment with the command **mkdir test**. This will create a folder named “test” on your desktop;
4-	Save the files ‘end-to-end-technical-test-data-scientist.ipynb’, ‘sex_predictor.pk’, ‘sex_predictor.py’, ‘requirements.txt’, and the input data named as ‘newsample.csv’ inside the folder ‘test’;
5-	Use the command **cd test** to change the directory to the folder 'test';
6-	Create a virtual environment for your project. Use the venv module that comes with Python to create a virtual environment. For example, to create a virtual environment called env in the root directory of your project, run the following command: **python3 -m venv env**;
7-	Activate the virtual environment running the following command for macOS or linux run: **source env/bin/activate**. If you’re using Winddowns run **env\Scripts\activate.bat**;
8-	Use pip to install the packages from the requirements.txt file. Run the following command: **pip install -r requirements.txt**;
9-	 This will install all the required packages and their dependencies in the virtual environment.
Note: Make sure that you are using the correct version of pip and Python for your project. It's a good practice to create and use a virtual environment for each Python project to isolate its dependencies and avoid conflicts with other packages;
10-	 Use the command **python3 sex_predictor.py** to run the model. It will generate a file named ‘newsample_PREDICTIONS_Igor_Barbosa_Lima.csv’ containing a column named ‘Sex’ with the predictions made by the Logistic Regression model inside the folder 'test'.
11- To see the whole project in Jupiter notebook use the comand **jupyter noteboo** and open the file ‘end-to-end-technical-test-data-scientist.ipynb’ in your browser.

*Obs: Make sure that your input file has no missing values.

