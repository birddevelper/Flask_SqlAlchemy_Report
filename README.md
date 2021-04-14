### This is easy to use tool for generating html table from sql query.

the package contains only one function named "generateFromSql" with 8 arguments :

* session : SQLAlchemy session
* title : the title of the report that will be shown on top of table
* sqltext : the sql query
* footerCols : a list of columns name that you want to have Sum of values on footer . Example : ['amount','price']
* direction (default = "ltr") : indicates direction of the report page.  "ltr"- Left to Right , "rtl" -  Right to Left
* font (default = "Tahoma") : font of title and table contents
* totalText (default = "Total") : title of footer row that will be the put below the first column.
* rowIndex (default = False) : indicates whether the table should have index column or not.
* headerRowColor (default = '#eeeeee') :  the header (title) row background color.
* evenRowColor (default = '#ffffff') :  the even rows background color.
* oddRowColor (default = '#ffffff') :  the odd rows background color.




## Installation
To install flask_sqlalchemy using pip type:

```shell
pip install flask-sqlalchemy-report
```

## Usage :

```bash
pip install flask-sqlalchemy-report
```


```python
from flask_sqlalchemy_report import Reporter 

@app.route('/listOfPersons', methods=['GET'])
def listOfPersons():
  
  return Reporter.generateFromSql(db.session, "Employee List","SELECT FirstName as 'First Name', LastName as 'Last Name', phone as 'Phone Number', salary as 'Salary' FROM persons", ['Salary'], "rtl", "Arial", "Total Salary", True,'#ffeeee','#ffeeff','#ffffff')
   
 ```
