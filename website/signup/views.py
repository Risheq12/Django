from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
from platformdirs import user_cache_dir
fn=''
ln=''
em=''
pwd=''

# Create your views here.
def signupaction(request):
    global fn,ln,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", passwd="m.risheq12", database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="password":
                pwd=value
            if key=="email":
                em=value
           
                
        c="insert into users Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
        cursor.execute(c)
        m.commit()
    
    return render(request,'signup_page.html')