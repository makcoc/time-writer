import datetime
a = 1
t = datetime.datetime(1,1,1,0,0,0)
with open("output.txt", "a") as f:
        while a < 250:
                print(t.strftime("%M:%S"), end= ', ', file=f)
                a +=1
                t = t + datetime.timedelta(0,1)

