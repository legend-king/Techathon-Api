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

mycursor = mydb.cursor(dictionary=True, buffered=True)
# mycursor = mydb.cursor(buffered=True)
@api_view(['POST'])
def login(request):
    try:
        if request.POST.get('email'):
            email=request.POST.get('email')
            password=request.POST.get('password')
        else:
            data = json.loads(request.body)
            email=data['email']
            password=data['password']
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
            data = json.loads(request.body)
            print(data)
            name = data['name']
            mobile = data['mobile']
            email=data['email']
            password=data['password']
            userType=data['userType']
        
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
    except Exception as e:
        print(e)
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
        wantedTime = request.POST.get('wantedTime')

        mycursor.execute("insert into setOrder(orderBy, orderType, wantedTime) values('{}', '{}', '{}')".format(orderBy, orderType, wantedTime))
        x=mycursor.rowcount

        mydb.commit()
        if x==1:
            return Response({"message":1})
        return Response({"message":0})
    except Exception as e:
        print(e)
        return Response({"message":0})



@api_view(['POST'])
def viewOrder(request):
    try:
        orderBY = request.POST.get('email')
        mycursor.execute("select distinct f.id,f.acceptedBy, f.status, u.mobile,f.orderType from foodOrder f, user u where status!='completed' and status!='cancelled'  and orderBy='{}' and userType=1".format(orderBY))
        # x=mycursor.rowcount
        data=mycursor.fetchall()
        # mydb.commit()
        print(data)
        return Response(data)
    except Exception as e:
        print(e)
        return Response({"message":0})

@api_view(['GET'])
def viewOrders(request):
    try:

        mycursor.execute("select * from foodOrder where status='ordered'")
        # x=mycursor.rowcount
        data=mycursor.fetchall()
        print(data)
        return Response(data)
    except Exception as e:
        print(e)
        return Response({"message":0})


@api_view(['POST'])
def cancelOrder(request):
    try:
        id = request.POST.get("id")
        mycursor.execute("update foodOrder set status='cancelled' where id={}".format(id))
        x=mycursor.rowcount

        mydb.commit()
        if x==1:
            return Response({"message":1})
        return Response({"message":0})
    except:
        return Response({"message":0})


@api_view(['POST'])
def acceptOrder(request):
    try:
        id = request.POST.get("id")
        email = request.POST.get("email")
        mycursor.execute("update foodOrder set status='accepted', acceptedBy='{}' where id={}".format(email,id))
        x=mycursor.rowcount

        mydb.commit()
        if x==1:
            return Response({"message":1})
        return Response({"message":0})
    except:
        return Response({"message":0})