
import pymongo
from time import sleep
from tkinter import *
import threading
from binance.client import Client
from pushbullet import Pushbullet
client = Client("ncjfbm0ZJwzIg5riOIqjqiBw6LCm28h8481iorY6SvlxKOQxvAMulp852YNWJtTL","vqemkyWSUnQJAR4AcZu6mdtrqzgJ8ew7lcOJzsskZpfeNfKmZc2l0hnrPqBsa34i")


#quantity= '0.001'

time_res = client.get_server_time()
recvWindow=6000000


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#
main= Tk()
main.title("Output")
main.geometry("300x300")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#pushBullet

pb = Pushbullet("o.3vitfRuBRah6d3CfcA9I2j6nQGmZYuRy")

print (pb.devices)

device = pb.devices[0]


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

myclient_percentage = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds119014.mlab.com:19014/percentage_change_data")

mydb_percentage = myclient_percentage ["percentage_change_data"]

mycol_percentage = mydb_percentage ["data"]     # collection is mongo is same as a Table 


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



# shoterning techniques

percentage = 2


## mda ##

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


def MDABTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "MDABTC"   # LET ALL COINS HAVE COIN = CAPITAL SPELLING
    coin_mlabs = "mongodb://poya:Muhammad00.@ds135592.mlab.com:35592/data_db"
    row1 = 0
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient["data_db"]  #  MUST MAKE ANOTHER DATA BASE NAME = COIN 
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit 3%")
            print(mydict2)
            order = True
            sleep(100)
            
        if  percentage <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < percentage:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=MDABTC)
thread_a.daemon = True 
thread_a.start()

#_________________________________________________________________________________
#_________________________________________________________________________________
#_________________________________________________________________________________


def GVTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "gvtbtc"
    coin_mlabs = "mongodb://poya1:Muhammad00.@ds243254.mlab.com:43254/gvtbtc"
    row1 = 1 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=GVTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


def EOSBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "eosbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds243254.mlab.com:43254/eosbtc"
    row1 = 2 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=EOSBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def ADABTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "adabtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds243254.mlab.com:43254/adabtc"
    row1 = 3 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=ADABTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def DCRBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "dcrbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/dcrbtc"
    row1 = 4 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=DCRBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def BQXBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "bqxbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/bqxbtc"
    row1 = 5 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=BQXBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


def DASHBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "dashbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/dashbtc"
    row1 = 6 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=DASHBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def ICXBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "icxbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/icxbtc"
    row1 = 7 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=ICXBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________

def IOTABTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "iotabtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/iotabtc"
    row1 = 8 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=IOTABTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def KMDBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "kmdbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/kmdbtc"
    row1 = 9 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=KMDBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def MANABTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "manabtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/manabtc"
    row1 = 10 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=MANABTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________




def MTLBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "mtlbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/mtlbtc"
    row1 = 11 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=MTLBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def ONTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "ontbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/ontbtc"
    row1 = 12 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=ONTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def QKCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "qkcbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/qkcbtc"
    row1 = 13 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=QKCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def RVNBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "rvnbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/rvnbtc"
    row1 = 14 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=RVNBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________






def THETABTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "thetabtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/thetabtc"
    row1 = 15 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=THETABTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def XMRBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "xmrbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/xmrbtc"
    row1 = 16 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=XMRBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


def ZECBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "zecbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/zecbtc"
    row1 = 17 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=ZECBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


def ZRXBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "zrxbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/zrxbtc"
    row1 = 18 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0:
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=ZRXBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________

####     2222222222222222   stage srtage stage stage stage stage  22222222222222222222222222222222222



def BATBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "batbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds119161.mlab.com:19161/batbtc"
    row1 = 19 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=BATBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


def HOTBTC():
 #   threading.Timer(1.0, changes).start()
  #   output.delete(1.0, END)
#    order = False 
    coin = "hotbtc"
    coin_mlabs = "mongodb://poya1:Muhammad00.@ds119161.mlab.com:19161/hotbtc"
    row1 = 20 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=HOTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def NANOBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "nanobtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds119161.mlab.com:19161/nanobtc"
    row1 = 21 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=NANOBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def LINKBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "linkbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/linkbtc"
    row1 = 22 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=LINKBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def VIBBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "vibbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/vibbtc"
    row1 = 23 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=VIBBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def WANBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "wanbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/wanbtc"
    row1 = 24 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=WANBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def AIONBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "aionbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds239128.mlab.com:39128/aionbtc"
    row1 = 25 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=AIONBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def MITHBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "mithbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/mithbtc"
    row1 = 26 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=MITHBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def XEMBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "xembtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/xembtc"
    row1 = 27 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=XEMBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def QTUMBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "qtumbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/qtumbtc"
    row1 = 28 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=QTUMBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def REPBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "repbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds239128.mlab.com:39128/repbtc"
    row1 = 29 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=REPBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def XVGBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "xvgbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/xvgbtc"
    row1 = 30 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=XVGBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def IOSTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "iostbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/iostbtc"
    row1 = 0 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=IOSTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def QKCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "qkcbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/qkcbtc"
    row1 = 1 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=QKCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def SNMBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "snmbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/snmbtc"
    row1 = 2 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=SNMBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def WTCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "wtcbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/wtcbtc"
    row1 = 3 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=WTCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def OMGBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "omgbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds127589.mlab.com:27589/omgbtc"
    row1 = 4 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=OMGBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def ARNBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "arnbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds037185.mlab.com:37185/arnbtc"
    row1 = 5 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=ARNBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def DGDBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "dgdbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds233571.mlab.com:33571/dgdbtc"
    row1 = 6 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=DGDBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def DATABTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "databtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds225253.mlab.com:25253/databtc"
    row1 = 7 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=DATABTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def PIVXBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "pivxbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds225253.mlab.com:25253/pivxbtc"
    row1 = 8 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=PIVXBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def MFTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "mftbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds163672.mlab.com:63672/mftbtc"
    row1 = 9 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=MFTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def LSKBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "lskbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds225253.mlab.com:25253/lskbtc"
    row1 = 10 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=LSKBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def CMTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "cmtbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds233571.mlab.com:33571/cmtbtc"
    row1 = 11 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=CMTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def INSBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "insbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds233571.mlab.com:33571/insbtc"
    row1 = 12 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=INSBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def QLCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "qlcbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds233571.mlab.com:33571/qlcbtc"
    row1 = 13 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=QLCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def ENJBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "enjbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds233571.mlab.com:33571/enjbtc"
    row1 = 14 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=ENJBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def POLYBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "polybtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds017193.mlab.com:17193/polybtc"
    row1 = 15 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=POLYBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def VIBEBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "vibebtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds051524.mlab.com:51524/vibebtc"
    row1 = 16 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=VIBEBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def GOBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "gobtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds029831.mlab.com:29831/gobtc"
    row1 = 17 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=GOBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________

def NEBLBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "neblbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds125871.mlab.com:25871/neblbtc"
    row1 = 18 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=NEBLBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def GNTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "gntbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds153659.mlab.com:53659/gntbtc"
    row1 = 19 # add 1 to each new coin
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=2, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  file
    mycol = mydb["data"]  # collection - table 




    order = False
    while order == False:
        a.delete(1.0, END)
        a.config({"background": "white"})


        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
            c = x['k']['c']
            o = x['k']['o']
            eventTime = x['E']
            change = round(((float(c)-float(o)) / float(o)*100),2)
    
        
        mydict2 = {'time':eventTime, 'b':change}

            
   
        if change >= percentage:
            a.insert(END, change)
            a.config({"background": "Pink"})
            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
            mycol_percentage.insert_one(mydict2)
            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
            print(mydict2)
            order = True
            sleep(100)
            
        if  0 <= change < percentage :
            a.insert(END, change)
            a.config({"background": "light green"})
            
            
        if change < 0 :
            a.insert(END, change)
            a.config({"background": "red"})



            
    #    print ("Open: "+o+" -- Close:  "+c)
    #    print(change)
        order = False
        sleep(1)

            

thread_a = threading.Thread(target=GNTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


main.mainloop()  
