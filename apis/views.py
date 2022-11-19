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
            return Response({"message":1, "userType":result["userType"]})
        return Response({"message":0})
        
    except Exception  as e:
        print(e)
        return Response({"message":0})


@api_view(['POST'])
def register(request):
    try:
        print(request.body)
        if request.POST.get('name'):

            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email=request.POST.get('email')
            password=request.POST.get('password')
            userType=request.POST.get('userType')
        else:
            name = request.body('name')
            mobile = request.body('mobile')
            email=request.body('email')
            password=request.body('password')
            userType=request.body('userType')
        print(email,password)
        mycursor.execute("select * from user where email='{0}'".format(email))
        result = mycursor.fetchall()
        if len(result)==1:
            return Response({"message":2})
        mycursor.execute("insert into user(name, mobile, email, password, userType) values('{}','{}', '{}', '{}', '{}')".format(name, mobile, email, password, userType))
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


@api_view(['POST'])
def addDish(request):
    try:
        dish=request.POST.get('dish')
        type=request.POST.get('type')
        email = request.POST.get('email')
        mycursor.execute("insert into orderDish(orderOf, orderType, dish) values('{}', '{}', '{}')".format(email, type, dish))
        
        x=mycursor.rowcount

        mydb.commit()
        if x==1:
            return Response({"message":1})
        return Response({"message":0})
    except:
        return Response({"message":0})


@api_view(['POST'])
def viewDish(request):
    try:
        type=request.POST.get('type')
        email = request.POST.get('email')
        mycursor.execute("select * from orderDish where orderOf='{}' and orderType='{}'".format(email, type))
        x=mycursor.fetchall()
        return Response(x)
    except :
        return Response({"message":0})

@api_view(['POST'])
def removeDish(request):
    try:
        id = request.POST.get("id")
        mycursor.execute("delete from orderDish where id={}".format(id))
        x=mycursor.rowcount

        mydb.commit()
        if x==1:
            return Response({"message":1})
        return Response({"message":0})
    except Exception as e:
        print(e)
        return Response({"message":0})



@api_view(['POST'])
def order(request):
    try:
        orderBy = request.POST.get('email')
        orderType = request.POST.get('type')

        mycursor.execute("insert into foodOrder(orderBy, orderType) values('{}', '{}')".format(orderBy, orderType))
        x=mycursor.rowcount

        mydb.commit()
        if x==1:
            return Response({"message":1})
        return Response({"message":0})
    except Exception as e:
        print(e)
        return Response({"message":0})


@api_view(['POST'])
def setOrder(request):
    try:
        orderBy = request.POST.get('email')
        orderType = request.POST.get('type')

        mycursor.execute("insert into setOrder(orderBy, orderType) values('{}', '{}')".format(orderBy, orderType))
        x=mycursor.rowcount

        mydb.commit()
        if x==1:
            return Response({"message":1})
        return Response({"message":0})
    except Exception as e:
        print(e)
        return Response({"message":0})


