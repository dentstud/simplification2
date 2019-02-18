
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

percentage = 3


## mda ##

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


def XLMBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "xlmbtc"   # LET ALL COINS HAVE COIN = CAPITAL SPELLING
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/xlmbtc"
    row1 = 0
    
    
    a= "output"+coin
    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
    a = Text(main, width=20, height=1, background= "light blue")
    a.grid(row= row1, column=0, sticky=W)
    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
    mydb = myclient[coin]  #  MUST MAKE ANOTHER DATA BASE NAME = COIN 
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

            

thread_a = threading.Thread(target=XLMBTC)
thread_a.daemon = True 
thread_a.start()

#_________________________________________________________________________________
#_________________________________________________________________________________
#_________________________________________________________________________________


def LTCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "ltcbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/ltcbtc"
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

            

thread_a = threading.Thread(target=LTCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


def TRXBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "trxbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/trxbtc"
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

            

thread_a = threading.Thread(target=TRXBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def BNBBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "bnbbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/bnbbtc"
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

            

thread_a = threading.Thread(target=BNBBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def ETCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "etcbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/etcbtc"
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

            

thread_a = threading.Thread(target=ETCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def NEOBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "neobtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/neobtc"
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

            

thread_a = threading.Thread(target=NEOBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


def WAVESBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "wavesbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/wavesbtc"
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

            

thread_a = threading.Thread(target=WAVESBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


#
#def USDCBTC():
# #   threading.Timer(1.0, changes).start()
# #   output.delete(1.0, END)
##    order = False 
#    coin = "usdcbtc"
#    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/usdcbtc"
#    row1 = 7 # add 1 to each new coin
#    
#    
#    a= "output"+coin
#    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
#    a = Text(main, width=20, height=1, background= "light blue")
#    a.grid(row= row1, column=0, sticky=W)
#    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
#    mydb = myclient[coin]  #  file
#    mycol = mydb["data"]  # collection - table 
#
#
#
#
#    order = False
#    while order == False:
#        a.delete(1.0, END)
#        a.config({"background": "white"})
#
#
#        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
#            c = x['k']['c']
#            o = x['k']['o']
#            eventTime = x['E']
#            change = round(((float(c)-float(o)) / float(o)*100),2)
#    
#        
#        mydict2 = {'time':eventTime, 'b':change}
#
#            
#   
#        if change >= percentage:
#            a.insert(END, change)
#            a.config({"background": "Pink"})
#            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
#            mycol_percentage.insert_one(mydict2)
#            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
#            print(mydict2)
#            order = True
#            sleep(100)
#            
#        if  0 <= change < percentage :
#            a.insert(END, change)
#            a.config({"background": "light green"})
#            
#            
#        if change < 0:
#            a.insert(END, change)
#            a.config({"background": "red"})
#
#
#
#            
#    #    print ("Open: "+o+" -- Close:  "+c)
#    #    print(change)
#        order = False
#        sleep(1)
#
#            
#
#thread_a = threading.Thread(target=USDCBTC)
#thread_a.daemon = True 
#thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________

def BTGBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "btgbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/btgbtc"
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

            

thread_a = threading.Thread(target=BTGBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def VETBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "vetbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/vetbtc"
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

            

thread_a = threading.Thread(target=VETBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def TUSDBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "tusdbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/tusdbtc"
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

            

thread_a = threading.Thread(target=TUSDBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________




def ZILBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "zilbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/zilbtc"
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

            

thread_a = threading.Thread(target=ZILBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



#def PAXBTC():
# #   threading.Timer(1.0, changes).start()
# #   output.delete(1.0, END)
##    order = False 
#    coin = "paxbtc"
#    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/paxbtc"
#    row1 = 12 # add 1 to each new coin
#    
#    
#    a= "output"+coin
#    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
#    a = Text(main, width=20, height=1, background= "light blue")
#    a.grid(row= row1, column=0, sticky=W)
#    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
#    mydb = myclient[coin]  #  file
#    mycol = mydb["data"]  # collection - table 
#
#
#
#
#    order = False
#    while order == False:
#        a.delete(1.0, END)
#        a.config({"background": "white"})
#
#
#        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
#            c = x['k']['c']
#            o = x['k']['o']
#            eventTime = x['E']
#            change = round(((float(c)-float(o)) / float(o)*100),2)
#    
#        
#        mydict2 = {'time':eventTime, 'b':change}
#
#            
#   
#        if change >= percentage:
#            a.insert(END, change)
#            a.config({"background": "Pink"})
#            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
#            mycol_percentage.insert_one(mydict2)
#            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
#            print(mydict2)
#            order = True
#            sleep(100)
#            
#        if  0 <= change < percentage :
#            a.insert(END, change)
#            a.config({"background": "light green"})
#            
#            
#        if change < 0:
#            a.insert(END, change)
#            a.config({"background": "red"})
#
#
#
#            
#    #    print ("Open: "+o+" -- Close:  "+c)
#    #    print(change)
#        order = False
#        sleep(1)
#
#            
#
#thread_a = threading.Thread(target=PAXBTC)
#thread_a.daemon = True 
#thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def BCDBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "bcdbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/bcdbtc"
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

            

thread_a = threading.Thread(target=BCDBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



#def BCNBTC():
# #   threading.Timer(1.0, changes).start()
# #   output.delete(1.0, END)
##    order = False 
#    coin = "bcnbtc"
#    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/bcnbtc"
#    row1 = 14 # add 1 to each new coin
#    
#    
#    a= "output"+coin
#    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
#    a = Text(main, width=20, height=1, background= "light blue")
#    a.grid(row= row1, column=0, sticky=W)
#    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
#    mydb = myclient[coin]  #  file
#    mycol = mydb["data"]  # collection - table 
#
#
#
#
#    order = False
#    while order == False:
#        a.delete(1.0, END)
#        a.config({"background": "white"})
#
#
#        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
#            c = x['k']['c']
#            o = x['k']['o']
#            eventTime = x['E']
#            change = round(((float(c)-float(o)) / float(o)*100),2)
#    
#        
#        mydict2 = {'time':eventTime, 'b':change}
#
#            
#   
#        if change >= percentage:
#            a.insert(END, change)
#            a.config({"background": "Pink"})
#            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
#            mycol_percentage.insert_one(mydict2)
#            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
#            print(mydict2)
#            order = True
#            sleep(100)
#            
#        if  0 <= change < percentage :
#            a.insert(END, change)
#            a.config({"background": "light green"})
#            
#            
#        if change < 0:
#            a.insert(END, change)
#            a.config({"background": "red"})
#
#
#
#            
#    #    print ("Open: "+o+" -- Close:  "+c)
#    #    print(change)
#        order = False
#        sleep(1)
#
#            
#
#thread_a = threading.Thread(target=BCNBTC)
#thread_a.daemon = True 
#thread_a.start()
#

#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________






def STRATBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "stratbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/stratbtc"
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

            

thread_a = threading.Thread(target=STRATBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________



def SCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "scbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/scbtc"
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

            

thread_a = threading.Thread(target=SCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


def BTSBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "btsbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/btsbtc"
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

            

thread_a = threading.Thread(target=BTSBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


#def HSRBTC():
# #   threading.Timer(1.0, changes).start()
# #   output.delete(1.0, END)
##    order = False 
#    coin = "hsrbtc"
#    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/hsrbtc"
#    row1 = 18 # add 1 to each new coin
#    
#    
#    a= "output"+coin
#    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
#    a = Text(main, width=20, height=1, background= "light blue")
#    a.grid(row= row1, column=0, sticky=W)
#    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
#    mydb = myclient[coin]  #  file
#    mycol = mydb["data"]  # collection - table 
#
#
#
#
#    order = False
#    while order == False:
#        a.delete(1.0, END)
#        a.config({"background": "white"})
#
#
#        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
#            c = x['k']['c']
#            o = x['k']['o']
#            eventTime = x['E']
#            change = round(((float(c)-float(o)) / float(o)*100),2)
#    
#        
#        mydict2 = {'time':eventTime, 'b':change}
#
#            
#   
#        if change >= percentage:
#            a.insert(END, change)
#            a.config({"background": "Pink"})
#            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
#            mycol_percentage.insert_one(mydict2)
#            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
#            print(mydict2)
#            order = True
#            sleep(100)
#            
#        if  0 <= change < percentage :
#            a.insert(END, change)
#            a.config({"background": "light green"})
#            
#            
#        if change < 0:
#            a.insert(END, change)
#            a.config({"background": "red"})
#
#
#
#            
#    #    print ("Open: "+o+" -- Close:  "+c)
#    #    print(change)
#        order = False
#        sleep(1)
#
#            
#
#thread_a = threading.Thread(target=HSRBTC)
#thread_a.daemon = True 
#thread_a.start()
#

#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________

####     2222222222222222   stage srtage stage stage stage stage  22222222222222222222222222222222222



def AEBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "aebtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/aebtc"
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

            

thread_a = threading.Thread(target=AEBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


def PPTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "pptbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/pptbtc"
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

            

thread_a = threading.Thread(target=PPTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def STEEMBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "steembtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/steembtc"
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

            

thread_a = threading.Thread(target=STEEMBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#def NPXSBTC():
# #   threading.Timer(1.0, changes).start()
# #   output.delete(1.0, END)
##    order = False 
#    coin = "npxsbtc"
#    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/npxsbtc"
#    row1 = 22 # add 1 to each new coin
#    
#    
#    a= "output"+coin
#    Label(main, text=coin).grid(row=row1, column=1, sticky=E)
#    a = Text(main, width=20, height=1, background= "light blue")
#    a.grid(row= row1, column=0, sticky=W)
#    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
#    mydb = myclient[coin]  #  file
#    mycol = mydb["data"]  # collection - table 
#
#
#
#
#    order = False
#    while order == False:
#        a.delete(1.0, END)
#        a.config({"background": "white"})
#
#
#        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
#            c = x['k']['c']
#            o = x['k']['o']
#            eventTime = x['E']
#            change = round(((float(c)-float(o)) / float(o)*100),2)
#    
#        
#        mydict2 = {'time':eventTime, 'b':change}
#
#            
#   
#        if change >= percentage:
#            a.insert(END, change)
#            a.config({"background": "Pink"})
#            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
#            mycol_percentage.insert_one(mydict2)
#            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
#            print(mydict2)
#            order = True
#            sleep(100)
#            
#        if  0 <= change < percentage :
#            a.insert(END, change)
#            a.config({"background": "light green"})
#            
#            
#        if change < 0 :
#            a.insert(END, change)
#            a.config({"background": "red"})
#
#
#
#            
#    #    print ("Open: "+o+" -- Close:  "+c)
#    #    print(change)
#        order = False
#        sleep(1)
#
#            
#
#thread_a = threading.Thread(target=NPXSBTC)
#thread_a.daemon = True 
#thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def SNTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "sntbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/sntbtc"
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

            

thread_a = threading.Thread(target=SNTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def ARDBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "ardbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/ardbtc"
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

            

thread_a = threading.Thread(target=ARDBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def ARKBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "arkbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/arkbtc"
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

            

thread_a = threading.Thread(target=ARKBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def BNTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "bntbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/bntbtc"
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

            

thread_a = threading.Thread(target=BNTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def MCOBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "mcobtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/mcobtc"
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

            

thread_a = threading.Thread(target=MCOBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def XZCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "xzcbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/xzcbtc"
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

            

thread_a = threading.Thread(target=XZCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def GXSBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "gxsbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/gxsbtc"
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

            

thread_a = threading.Thread(target=GXSBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def POWRBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "powrbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/powrbtc"
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

            

thread_a = threading.Thread(target=POWRBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def ELFBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "elfbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/elfbtc"
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

            

thread_a = threading.Thread(target=ELFBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def LRCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "lrcbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/lrcbtc"
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

            

thread_a = threading.Thread(target=LRCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def ZENBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "zenbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/zenbtc"
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

            

thread_a = threading.Thread(target=ZENBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def ENGBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "engbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/engbtc"
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

            

thread_a = threading.Thread(target=ENGBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def NASBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "nasbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/nasbtc"
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

            

thread_a = threading.Thread(target=NASBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def LOOMBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "loombtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/loombtc"
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

            

thread_a = threading.Thread(target=LOOMBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def SYSBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "sysbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/sysbtc"
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

            

thread_a = threading.Thread(target=SYSBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def FUNBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "funbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/funbtc"
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

            

thread_a = threading.Thread(target=FUNBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def EDOBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "edobtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/edobtc"
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

            

thread_a = threading.Thread(target=EDOBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def AGIBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "agibtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/agibtc"
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

            

thread_a = threading.Thread(target=AGIBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def GASBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "gasbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/gasbtc"
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

            

thread_a = threading.Thread(target=GASBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#def ICNBTC():
# #   threading.Timer(1.0, changes).start()
# #   output.delete(1.0, END)
##    order = False 
#    coin = "icnbtc"
#    coin_mlabs = "mongodb://poya:Muhammad00.@ds041671.mlab.com:41671/icnbtc"
#    row1 = 11 # add 1 to each new coin
#    
#    
#    a= "output"+coin
#    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
#    a = Text(main, width=20, height=1, background= "light blue")
#    a.grid(row= row1, column=2, sticky=W)
#    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
#    mydb = myclient[coin]  #  file
#    mycol = mydb["data"]  # collection - table 
#
#
#
#
#    order = False
#    while order == False:
#        a.delete(1.0, END)
#        a.config({"background": "white"})
#
#
#        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
#            c = x['k']['c']
#            o = x['k']['o']
#            eventTime = x['E']
#            change = round(((float(c)-float(o)) / float(o)*100),2)
#    
#        
#        mydict2 = {'time':eventTime, 'b':change}
#
#            
#   
#        if change >= percentage:
#            a.insert(END, change)
#            a.config({"background": "Pink"})
#            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
#            mycol_percentage.insert_one(mydict2)
#            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
#            print(mydict2)
#            order = True
#            sleep(100)
#            
#        if  0 <= change < percentage :
#            a.insert(END, change)
#            a.config({"background": "light green"})
#            
#            
#        if change < 0 :
#            a.insert(END, change)
#            a.config({"background": "red"})
#
#
#
#            
#    #    print ("Open: "+o+" -- Close:  "+c)
#    #    print(change)
#        order = False
#        sleep(1)
#
#            
#
#thread_a = threading.Thread(target=ICNBTC)
#thread_a.daemon = True 
#thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def SUBBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "subbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds041671.mlab.com:41671/subbtc"
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

            

thread_a = threading.Thread(target=SUBBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def NXSBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "nxsbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/nxsbtc"
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

            

thread_a = threading.Thread(target=NXSBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#def DENTBTC():
# #   threading.Timer(1.0, changes).start()
# #   output.delete(1.0, END)
##    order = False 
#    coin = "dentbtc"
#    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/dentbtc"
#    row1 = 14 # add 1 to each new coin
#    
#    
#    a= "output"+coin
#    Label(main, text=coin).grid(row=row1, column=3, sticky=E)
#    a = Text(main, width=20, height=1, background= "light blue")
#    a.grid(row= row1, column=2, sticky=W)
#    myclient = pymongo.MongoClient(coin_mlabs)   #mongodb://localhost:27017/
#    mydb = myclient[coin]  #  file
#    mycol = mydb["data"]  # collection - table 
#
#
#
#
#    order = False
#    while order == False:
#        a.delete(1.0, END)
#        a.config({"background": "white"})
#
#
#        for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
#            c = x['k']['c']
#            o = x['k']['o']
#            eventTime = x['E']
#            change = round(((float(c)-float(o)) / float(o)*100),2)
#    
#        
#        mydict2 = {'time':eventTime, 'b':change}
#
#            
#   
#        if change >= percentage:
#            a.insert(END, change)
#            a.config({"background": "Pink"})
#            #client.order_market_buy(symbol = 'MDABTC', quantity = '0')
#            mycol_percentage.insert_one(mydict2)
#            push = pb.push_note(coin, "hit"+str(percentage)+ " %")
#            print(mydict2)
#            order = True
#            sleep(100)
#            
#        if  0 <= change < percentage :
#            a.insert(END, change)
#            a.config({"background": "light green"})
#            
#            
#        if change < 0 :
#            a.insert(END, change)
#            a.config({"background": "red"})
#
#
#
#            
#    #    print ("Open: "+o+" -- Close:  "+c)
#    #    print(change)
#        order = False
#        sleep(1)
#
#            
#
#thread_a = threading.Thread(target=DENTBTC)
#thread_a.daemon = True 
#thread_a.start()
#

#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def SALTBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "saltbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/saltbtc"
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

            

thread_a = threading.Thread(target=SALTBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def STORJBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "storjbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/storjbtc"
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

            

thread_a = threading.Thread(target=STORJBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def NULSBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "nulsbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/nulsbtc"
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

            

thread_a = threading.Thread(target=NULSBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________

def CVCBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "cvcbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145574.mlab.com:45574/cvcbtc"
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

            

thread_a = threading.Thread(target=CVCBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
def BRDBTC():
 #   threading.Timer(1.0, changes).start()
 #   output.delete(1.0, END)
#    order = False 
    coin = "brdbtc"
    coin_mlabs = "mongodb://poya:Muhammad00.@ds145584.mlab.com:45584/brdbtc"
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

            

thread_a = threading.Thread(target=BRDBTC)
thread_a.daemon = True 
thread_a.start()


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________


main.mainloop()  
