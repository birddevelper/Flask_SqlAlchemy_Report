from flask import render_template,request,jsonify, session
from flask_login import login_required,current_user, login_user,logout_user
from flask import render_template_string , redirect, url_for
from flask import Blueprint  , flash 
from flask_wtf import FlaskForm 
import jdatetime, datetime
from markupsafe import escape
import jsons
from app import authorize
from sqlalchemy import or_, and_, text



def generateFromSql(session, title, sqltext, footerCols, direction="ltr", font="Tahoma", totalText = "Total", rowIndex = False) :
   sumCols=[]
   try :
         if(len(sqltext) < 8 or ("select" not in sqltext.lower())) :
               return ('Not Valid SQL') 

         sql_query = text(sqltext)
         sumCols=footerCols

         result=session.execute(sql_query)
         result_as_list = result.fetchall()
         columns =result.keys()
         data = result_as_list
         
         sumOfColumn = None
         if(sumCols != None) :
           sumOfColumn={}

         if(sumCols != None) :
            for c in columns :
               if(c in sumCols):
                  sumOfColumn[c]=0
               else:
                  sumOfColumn[c]="-"

         if(sumCols != None) :
            for d in data :
               for attr, value in d.items() :
                  if(attr in sumCols):
                     sumOfColumn[attr]=sumOfColumn[attr]+int(str(value).replace(",", ""))
         
         totalColumnSet = False
         if(sumCols != None) :
            for col, val in sumOfColumn.items() :
               if(val!="-") :
                  sumOfColumn[col] = format(int(str(val)),",")
               elif (totalColumnSet == False) :
                  sumOfColumn[col] = totalText
                  totalColumnSet = True
         
         template= "<html> <head> <meta charset=\"utf-8\"> <title> {{title}} </title> </head> <body > <center> <p dir=\"{{direction}}\" ><center><font  style=\"font-family:'{{font}}';font-weight: bold;\"  > {{title}} </font></center></p> <table dir=\"{{direction}}\"  border=\"1\" class=\"table table-striped\" style=\"width:93%;font-family:'{{font}}'\"> <thead> <tr style='background-color:#eee'> {% for c in columns %} <th>{{ c }}</th> {% endfor %} </tr> </thead> <tbody> {% for d in data %} <tr>  {% for attr, value in d.items() %} <td align=\"center\">{{ value }}</td> {% endfor %} </tr> {% endfor %} {% if(sumOfColumn != None )  %} <tr  style='background-color:#eee;font-weight: bold;'>  {% for a,v in sumOfColumn.items() %} <td align=\"center\">{{ v }}</td> {% endfor %} </tr>  {% endif %} </tbody> </table> </center> </body> </html>"
         if(rowIndex==True) :
            template= "<html> <head> <meta charset=\"utf-8\"> <title> {{title}} </title> </head> <body > <center> <p dir=\"{{direction}}\" ><center><font  style=\"font-family:'{{font}}';font-weight: bold;\"  > {{title}} </font></center></p> <table dir=\"{{direction}}\"  border=\"1\" class=\"table table-striped\" style=\"width:93%;font-family:'{{font}}'\"> <thead> <tr style='background-color:#eee'> <td align=\"center\"> </td> {% for c in columns %} <th>{{ c }}</th> {% endfor %} </tr> </thead> <tbody> {% for d in data %} <tr> <td align=\"center\">{{ loop.index }}</td> {% for attr, value in d.items() %} <td align=\"center\">{{ value }}</td> {% endfor %} </tr> {% endfor %} {% if(sumOfColumn != None )  %} <tr  style='background-color:#eee;font-weight: bold;'> <td></td> {% for a,v in sumOfColumn.items() %} <td align=\"center\">{{ v }}</td> {% endfor %} </tr> {% endif %}</tbody> </table> </center> </body> </html>"

         return render_template_string(template,title=title,data=data,columns=columns,sumOfColumn=sumOfColumn,direction=direction,font=font,totalText=totalText)
   except BaseException as e :
          return ("Error :" + str(e))   