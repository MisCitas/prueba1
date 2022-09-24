from django.shortcuts import render
from django.db import connection
from getmac import get_mac_address 

# Create your views here.
def iniciar(request):
    resp=""
    return render(request,'Registro.html',{ 'res':resp})  

def registrar(request):
    resp=""
    print(request.method)
    if request.method=='GET':
        mac=get_mac_address()
        cursor  = connection.cursor()
        sSql="select * from citas_macs where &direccionMac&='"+mac+"'"
        cursor.execute(sSql.replace('&','"'))
        rs=cursor.fetchone()
        if rs:
            resp="mac ya registrada!!!"
        else:
            sSql="insert into citas_macs(&direccionMac&,&estado&) values('"+mac+"','A')"
            cursor.execute(sSql.replace('&','"'))
            connection.commit()
            resp="mac registrada con exito!!!"
    return render(request,'Registro.html',{ 'res':resp})  