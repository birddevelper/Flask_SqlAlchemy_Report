from flask import render_template_string 
from sqlalchemy import  text


def generateFromSql(session, title, sqltext, footerCols, direction="ltr", font="Tahoma", totalText = "Total", rowIndex = False, headerRowColor ='#eeeeee' ,evenRowColor = '#ffffff', oddRowColor="#ffffff") :
   sumCols=[]
   try :
         if(len(sqltext) < 8 or ("select" not in sqltext.lower())) :
               return ('Not Valid SQL') 

         sql_query = text(sqltext)
         sumCols=footerCols
         # execute sql query and retrieve data from db
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
               for attr, value in dict(d).items() :
                  if(attr in sumCols):
                     sumOfColumn[attr]=sumOfColumn[attr]+float(str(value).replace(",", ""))
         
         totalColumnSet = False
         if(sumCols != None) :
            for col, val in sumOfColumn.items() :
               if(val!="-") :
                  sumOfColumn[col] = format(float(str(val)),",")
               elif (totalColumnSet == False) :
                  sumOfColumn[col] = totalText
                  totalColumnSet = True
         
         # report jinja template to generate data from data retrieved from data base
         template= "<table dir=\"{{direction}}\"  border=\"1\" class=\"table table-striped\" style=\"width:93%;font-family:'{{font}}'\"> <thead> <tr> <th colspan='{{(columns|length)+1}}' style=\"font-family:'{{font}}';font-weight: bold;\"  > {{title}} </th> </tr> <tr style='background-color:{{headerRowColor}}'>{% if(rowIndex==True)  %} <td align=\"center\"> </td> {% endif %} {% for c in columns %} <th>{{ c }}</th> {% endfor %} </tr> </thead> <tbody> {% for d in data %} <tr style='background-color:{% if(loop.index % 2 == 0 )  %} {{evenRowColor}} {% else %} {{oddRowColor}} {% endif %} '  > {% if(rowIndex==True)  %}  <td align=\"center\">{{ loop.index }}</td> {% endif %}  {% for attr, value in dict(d).items() %} <td align=\"center\">{{ value }}</td> {% endfor %} </tr> {% endfor %} {% if(sumOfColumn != None )  %} <tr  style='background-color:#eee;font-weight: bold;'> <td></td> {% for a,v in sumOfColumn.items() %} <td align=\"center\">{{ v }}</td> {% endfor %} </tr> {% endif %}</tbody> </table>"

         return render_template_string(template,title=title,data=data,columns=columns,sumOfColumn=sumOfColumn,direction=direction,font=font,totalText=totalText, rowIndex = rowIndex, headerRowColor =headerRowColor ,evenRowColor = evenRowColor, oddRowColor= oddRowColor )
   except BaseException as e :
          return ("Error :" + str(e))   
