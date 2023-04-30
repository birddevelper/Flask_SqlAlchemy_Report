[![Downloads](https://static.pepy.tech/personalized-badge/flask-sqlalchemy-report?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads)](https://pepy.tech/project/flask-sqlalchemy-report)

### Flask_SqlAlchemy_Report is an easy to use tool for generating html table from sql query.

The package contains single function named "generateFromSql" which accepts 11 arguments :

* session : SQLAlchemy session
* title : The title of the report that will be shown on top of table
* sqltext : The sql select query to retrieve data
* footerCols : A list of columns name that you want to have Sum of values on footer . Example : ['amount','price']
* direction (default = "ltr") : Indicates direction of the report page.  "ltr"- Left to Right , "rtl" -  Right to Left
* font (default = "Tahoma") : Font of title and table contents
* totalText (default = "Total") : Title of footer row that will be the put below the first column.
* rowIndex (default = False) : Indicates whether the table should have index column or not.
* headerRowColor (default = '#eeeeee') :  The header (title) row background color.
* evenRowColor (default = '#ffffff') :  The even rows background color.
* oddRowColor (default = '#ffffff') :  The odd rows background color.



## Installation
To install flask_sqlalchemy using pip :

```shell
pip install flask-sqlalchemy-report
```

## Usage :


```python
from flask_sqlalchemy_report import Reporter 

@app.route('/listOfPersons', methods=['GET'])
def listOfPersons():
  reportTitle = "Employee List"
  sqlQuery = "SELECT FirstName as 'First Name', LastName as 'Last Name', phone as 'Phone Number', salary as 'Salary' FROM persons"
  columnsToBeSummarized = ['Salary']
  fontName = "Arial"
  headerRowBackgroundColor = '#ffeeee'
  evenRowsBackgroundColor = '#ffeeff'
  oddRowsBackgroundColor = '#ffffff'
  rowIndexVisibility = True
  return Reporter.generateFromSql(db.session, reportTitle, sqlQuery, columnsToBeSummarized, 
                                  "ltr", fontName, "Total Salary", rowIndexVisibility,
                                  headerRowBackgroundColor, evenRowsBackgroundColor, oddRowsBackgroundColor
                                  )
   
 ```

## See More 
[Read More ](https://m-shaeri.ir/blog/generate-html-table-from-sql-query-in-flask/)
