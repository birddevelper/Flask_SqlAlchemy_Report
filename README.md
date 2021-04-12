This is easy to use tool for generating html table from sql query.

the package contains only one function named "generateFromSql" with 8 arguments :

* session : SQLAlchemy session
* title : the title of the report that will be shown on top of table
* sqltext : the sql query
* footerCols : a list of columns name that you want to have Sum of values on footer . Example : ['amount','price']
* direction (default = "ltr") : indicates direction of the report page.  "ltr"- Left to Right , "rtl" -  Right to Left
* font (default = "Tahoma") : font of title and table contents
* totalText (default = "Total") : title of footer row that will be the put below the first column.
* rowIndex (default = False) : indicates whether the table should have index column or not.

<b>
usage :
</b>

<code style='font-tahoma;font-size:12px;color:blue'>
  
from flask_sqlalchemy_report import Reporter 

@app.route('/listOfPersons', methods=['GET'])

def listOfPersons():
  
  return Reporter.sqlPrinter(db.session, "Employee List","SELECT FirstName as 'First Name', LastName as 'Last Name', phone as 'Phone Number', salary as 'Salary' FROM persons", ['Salary'], "rtl", "Arial", "Total Salary", True)
  
 </code>
