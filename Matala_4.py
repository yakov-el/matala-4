import json
import requests
def  dis_matrix():
    counter=0
    handle= open('D:\dests.txt', 'r',  encoding='utf-8')
    dic = dict()
    far1=far2=far3=0
    for line in handle:
        url="https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=%D7%AA%D7%9C%25%D7%90%D7%91%D7%99%D7%91&"
        dest="destinations="+line
        key="&key=AIzaSyBUnnHqHTv2c070bDHdP3sfNvEOtd0OMLY" 
        response = requests.get(url+dest+key)
        res= response.content.decode('utf-8')
        a_list = json.dumps(res)
        x=a_list.find("value")
        dist_km=int(a_list[x+9:x+17])/1000
        x= a_list.find("text",x,)
        if counter==0:
            duration=a_list[x+11:x+26]
        else:
            duration=a_list[x+11:x+25]
        p1="https://maps.googleapis.com/maps/api/geocode/json?address="
        p2= line
        p3="&key=AIzaSyBUnnHqHTv2c070bDHdP3sfNvEOtd0OMLY"   
        response = requests.get(p1+p2+p3)
        response= response.content.decode('utf-8')
        locstart=response.find('location')
        lat=response[locstart+37:locstart+47]
        lng=response[locstart+72:locstart+85]
        counter=counter+1
        dic[line]={'distance': dist_km,'duration': duration.rstrip(),'latitude': lat,'longitude':lng.rstrip()}  
        if dist_km>far1:
            far3=far2
            far2=far1
            far1= dist_km
        elif dist_km>far2:
            far3=far2
            far2=dist_km
        elif dist_km>far3:
            far3=dist_km            
    for line in dic:
        print(line, dic[line])
        print("    "
               "    " )
        print('*************************')
    print('far1:',far1,'far2:',far2,'far3:',far3)