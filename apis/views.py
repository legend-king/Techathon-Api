from rest_framework.decorators import api_view
from  rest_framework.response import Response

import mysql.connector
import json
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="must",
  database="techathon"
)

mycursor = mydb.cursor(dictionary=True)

@api_view(['POST'])
def login(request):
    try:
        email=request.POST.get('email')
        password=request.POST.get('password')
        mycursor.execute("select * from user where email='{}' and password='{}'".format(email, password))
        print(email, password)
        result = mycursor.fetchone()
        if result:
            return Response({"message":1})
        return Response({"message":0})
        
    except Exception  as e:
        print(e)
        return Response({"message":0})


@api_view(['POST'])
def register(request):
    try:
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email, password)
        mycursor.execute("select * from user where email='{0}'".format(email))
        result = mycursor.fetchall()
        if len(result)==1:
            return Response({"message":2})
        mycursor.execute("insert into user(name, mobile, email, password) values('{}','{}', '{}', '{}')".format(name, mobile, email, password))
        x=mycursor.rowcount

        mydb.commit()
        if x==1:
            return Response({"message":1})
        return Response({"message":0})
    except:
        return Response({"message":0})


@api_view(['POST'])
def forgotPass(request):
    try:
        email=request.POST.get('email')
        password=request.POST.get('password')
        mycursor.execute("select * from user where email='{0}'".format(email))
        result = mycursor.fetchall()
        if len(result)==0:
            return Response({"message":2})
        mycursor.execute("update user set password='{}' where email='{}'".format(password, email))
        x=mycursor.rowcount

        mydb.commit()
        if x==1:
            return Response({"message":1})
        return Response({"message":0})
    except:
        return Response({"message":0})
