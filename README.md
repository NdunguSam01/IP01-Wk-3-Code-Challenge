# IP01 Wk1 Code Challenge
## Description

The aim of this project is to create a restaurant-review domain. 

It creates three models (Customer, Restaurant and Reviews) and creates relationship(s) between the them and displays the required data using SQLAlchemy via the created relationships.

At the end of the project, the following relationships are created: 

1. A 'has-many' relationship between a Restaurant and Reviews
2. A 'has-many' relationship between a Customer and Reviews
3. A 'one-to-one' relationship between a Review and a Restaurant
3. A 'one-to-one' relationship between a Review and a Customer
4. A 'has-many' relationsip between a Restaurant and a Customer via the Review model 

## Project Pre-requisites

To successully run this project, the following software(s) need to be installed in your machine: 

1. **Python** - You can download it from their [official site](https://www.python.org/downloads/).
2. **Pipenv** - This is a Python virtual environment management tool that automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile. You can download it from their [official site](https://pypi.org/project/pipenv/).

## Project Set-Up Instructions

In order to successfully view the output of this project, create a new directory where you want to store the project files, navigate into it and follow the instructions below: 

1. **Cloning**- clone the repository by typing the following command into your terminal: 

    ```
    git clone https://github.com/NdunguSam01/IP01-Wk-3-Code-Challenge.git
    ```

    Optionally, you can download the zipped file by clicking the green Code button then selecting the "Download ZIP" option.

2. **Installing dependencies** - since this project needs various dependencies to run, type the following command in your terminal:

    ```
    pipenv install
    ```

    After this operation is completed, run the following command to enter into the virtual environment:

    ```
    pipenv shell
    ```


3. **Running the scripts** - to view the output, navigate into the lib folder and type the following command in your terminal

    ```
    python3 debug.py
    ```

    The debug.py is the script that contains all the methods used to complete the project's intended purpose.


## Expected Results

Once the project successfully runs, you should be able to see the results on the terminal

## Author
[Samuel Muigai](https://github.com/NdunguSam01)


## License 
MIT License

Copyright &copy; 2024 Samuel Muigai

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.