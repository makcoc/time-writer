import datetime
a = 1
t = datetime.datetime(1,1,1,0,0,0)
while a < 250:
       print(t.strftime("%M:%S"), end= ', ')
       a +=1
       t = t + datetime.timedelta(0,1)

