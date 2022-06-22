from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
from platformdirs import user_cache_dir
em=''
pwd=''

# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", passwd="m.risheq12", database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="password":
                pwd=value
            if key=="email":
                em=value
           
                
                
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall()) 
        if t==():
            return render(request, "error.html")
        else:
            return render(request, "home.html")   
        
    return render(request,'login_page.html')