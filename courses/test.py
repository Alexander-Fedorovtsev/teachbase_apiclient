import datetime
if __name__=="__main__":
    string = "2020-06-18T18:56:30.702+03:00"
    print(datetime.datetime.strptime(string[:19], "%Y-%m-%dT%H:%M:%S").date())
    #