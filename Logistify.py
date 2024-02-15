import pandas as pd #Establishing connections
import mysql.connector as sqlcon
import sqlalchemy as sq
import numpy as np
import matplotlib.pyplot as pl
cn=sqlcon.connect(host="localhost",user="root",password="1234",database="logistify")
cursor=cn.cursor()
if cn.is_connected()==False:
    print("Connection Error")#Welcome message
else:
    print("=="*25)
    print("=="*25)
    print("\t       Welcome to Logistify")
    print("\t                ---")
    print("\t    Your only logistic partner")
    print("=="*25)
    while True:
        print("=="*25)
        print("\t           Main Menu \n \n Choose your Genre \n \n 1. Customer \n 2. Seller \n 3. Administrator")
        print()
        log1=int(input("Please enter the appropriate number: "))
        print("=="*25)
        if log1 not in [1,2,3]:
            print("Invalid Entry")
            print("=="*25)
        elif log1==3: #For Administrators
            userid=input("Enter User ID: ")
            password=input("Enter Password: ")
            if userid=='admin' and password=='1234':
                print("=="*25)
                print("\t            Welcome")
                print("=="*25)
                comd=int(input("Type 1 for inserting CSV Files into MySQL: "))
                print()
                if comd!=1:
                     print("Invalid Entry")
                     print("=="*25)
                else:
                    filename.csv=input("Please enter the file name: ")
                    import pymysql
                    from sqlalchemy import create_engine
                    engine=create_engine('mysql+pymysql://root:1234@localhost/logistify')
                    conn=engine.connect()
                    tdf = pd.read_csv(filename)
                    tdf.to_sql(filename,conn,if_exists='replace',index=False)
                    print("Records imported successfully")
            else:
                print("=="*25)
                print("Invalid Login Credentials")
                print("=="*25)
                
            
        elif log1==1:#Customer Interface
            while True:
                print(" \n1. Register \n2. View your details \n3. Update your details \n4. View your order details \n5. Delete your account \n6. Search a Seller \n7. Back to the previous menu")
                print()
                cust1=int(input("Please enter the appropriate number: "))
                print("=="*25)
                if cust1 not in[1,2,3,4,5,6,7]:
                    print("Invalid Entry")
                    print("=="*25)
                cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                if cust1==1:
                    print("\t       Create Your Profile")
                    print()
                    consid=int(np.random.randint(10,100))
                    username=input("Create your Username: ")
                    df=pd.read_sql("select * from consumers",cn)
                    search=df[df.UserName==username]
                    if len(search)==0:
                        pswd=input("Create your Password: ")
                        name=input("Enter Your Name: ")
                        mobno=input("Enter Your Mobile Number: ")
                        age=input("Enter Your Age: ")
                        dob=input("Enter Your Date Of Birth: ")
                        addr=input("Enter Your Address: ")
                        city=input("Enter Your City: ")
                        state=input("Enter Your State: ")
                        pinc=input("Enter Your Pincode: ")
                            
                        sql="insert into consumers values({},'{}','{}','{}',{},{},'{}','{}','{}','{}',{})".format(consid,username,pswd,name,mobno,age,dob,addr,city,state,pinc)
                        cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                        cu=cn.cursor()
                        cu.execute(sql)
                        cn.commit()
                        print("Registered successfully")
                        print()
                        print("===="*20)
                        print()
                        print("Hi,",name,"!",[consid],"= This is your Consumer ID, we recommend you to note it down.")
                        print()
                        print("===="*20)
                        cu.close()
                        cn.close()
                        
                    else:
                        print()
                        print("Username already exists, create a different Username.")
                        print()
                        print("=="*25)
                
                elif cust1==2:
                    username=input("Enter your Username: ")
                    pswd=input("Enter your Password: ")
                    sql="select * from Consumers where UserName='{}' and Password='{}'".format(username,pswd)
                    df=pd.read_sql(sql,cn)
                    if len(df)==0:
                        print()
                        print("Invalid Credentials")
                        print("=="*25)
                    else:
                        print("=="*25)
                        print()
                        print(df)
                        print()
                        print("=="*25)
                        input("Hit ENTER to Continue")
                        while True:
                            cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                            print("=="*25)
                            print("\n Do you want to perform any operation?")
                            print()
                            print("1. View top 5 Customers")
                            print("2. View Bottom 5 Customers")
                            print("3. View Premium Customers with a graph")
                            print("4. View Ratings of Sellers with a graph")
                            print("5. Back to the previous menu")
                            print()
                            ch_s2=int(input("Please enter the appropriate number: "))
                            print("=="*25)
                            if ch_s2 not in [1,2,3,4,5]:
                                print("Invalid Entry")
                                print("=="*25)
                            elif ch_s2==1:
                                sql="select Name from consumers group by TotalOrders having TotalOrders>15".format(ch_s2)
                                df=pd.read_sql(sql,cn)
                                print(df)
                            elif ch_s2==2:
                                sql="select Name from consumers group by TotalOrders having TotalOrders<15".format(ch_s2)
                                df=pd.read_sql(sql,cn)
                                print(df)
                            elif ch_s2==3:
                                sql="select Name,TotalOrders from consumers".format(ch_s2)
                                df=pd.read_sql(sql,cn)
                                df.sort_values(by='TotalOrders')
                                df = df[df.TotalOrders>15]
                                print(df)
                                df.plot(kind='bar')
                                pl.xlabel("Customers")
                                pl.ylabel('Total Orders')
                                pl.title('Premium Customers')
                                pl.show()
                                print("=="*25)
                                input("Hit ENTER to Continue")
                                
                            elif ch_s2==4:
                                sql="select SellerName,Ratings from sellers".format(ch_s2)
                                df=pd.read_sql(sql,cn)
                                df.sort_values(by='Ratings')
                                print(df)
                                df.plot(kind='bar')
                                pl.xlabel('Sellers')
                                pl.ylabel('Ratings')
                                pl.title('Seller Ratings')
                                pl.show()
                                print("=="*25)
                                input("Hit ENTER to Continue")
                            elif ch_s2==5:
                                break
                        
                elif cust1==3:
                    username=input("Enter your Username: ")
                    pswd=input("Enter your Password: ")
                    sql="select * from Consumers where UserName='{}' and Password='{}'".format(username,pswd)
                    df=pd.read_sql(sql,cn)
                    if len(df)==0:
                        print()
                        print("Invalid Credentials")
                        print("=="*25)
                        
                        

                    else:
                        print("=="*25)
                        print("What do you want to update?")
                        print()
                        print("1.  Name")
                        print("2.  Mobile Number")
                        print("3.  Age")
                        print("4.  Date Of Birth")
                        print("5.  Address")
                        print("6.  City")
                        print("7.  State")
                        print("8.  Pincode")
                        print("9.  Username")
                        print("10. Password")
                        print()
                        cuid=int(input("Please enter the appropriate number: "))
                        print("=="*25)
                        if cuid not in [1,2,3,4,5,6,7,8,9,10]:
                            print("Invalid Entry")
                            print("=="*25)
                            break
                        elif cuid==1:
                            name=input("Enter new Name: ")
                            sql="Update Consumers Set Name = '{}' Where UserName = '{}' and Password = '{}'".format(name,username,pswd)
                        elif cuid==2:
                            mobno=input("Enter new Mobile Number: ")
                            sql="Update Consumers Set MobileNumber = '{}' Where UserName = '{}' and Password = '{}'".format(mobno,username,pswd)
                        elif cuid==3:
                            ag=input("Enter new Age: ")
                            sql="Update Consumers Set Age = '{}' Where UserName = '{}' and Password = '{}'".format(ag,username,pswd)
                        elif cuid==4:
                            dob=input("Enter new Date Of Birth: ")
                            sql="Update Consumers Set DateOfBirth = '{}' Where UserName = '{}' and Password = '{}'".format(dob,username,pswd)
                        elif cuid==5:
                            addr=input("Enter new Address: ")
                            sql="Update Consumers Set Address = '{}' Where UserName = '{}' and Password = '{}'".format(addr,username,pswd)
                        elif cuid==6:
                            city=input("Enter new City: ")
                            sql="Update Consumers Set City = '{}'Where UserName = '{}' and Password = '{}'".format(city,username,pswd)
                        elif cuid==7:
                            stat=input("Enter new State: ")
                            sql="Update Consumers Set State = '{}' Where UserName = '{}' and Password = '{}'".format(stat,username,pswd)
                        elif cuid==8:
                            pinc=input("Enter new PinCode: ")
                            sql="Update Consumers Set PinCode = '{}' Where UserName = '{}' and Password = '{}'".format(pinc,username,pswd)
                        elif cuid==9:
                            usenm=input("Enter new Username: ")
                            consid=input("Enter your Consumer ID: ")
                            sql="Update Consumers Set UserName = '{}' Where ConsumerID = '{}' and Password = '{}'".format(usenm,consid,pswd)
                        elif cuid==10:
                            usenm=input("Renter your Username: ")
                            pswd=input("Enter new Password: ")
                            sql="Update Consumers Set Password = '{}' Where UserName = '{}'".format(pswd,username)
                        else:
                            break
                        cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                        cu=cn.cursor()
                        cu.execute(sql)
                        cn.commit()
                        print("=="*25)
                        print()
                        print("Deatils Updated Successfully")
                        print()
                        print("=="*25)
                        cu.close()
                        cn.close()
                        
                elif cust1==4:
                    orid=int(input("Enter your Order ID: "))
                    sql="select * from Orders where OrderID='{}'".format(orid)
                    df=pd.read_sql(sql,cn)
                    if len(df)==0:
                        print("No order(s) found")
                        print("=="*25)
                    else:
                        print("=="*25)
                        print()
                        print(df)
                        print()
                        print("=="*25)
                        
                elif cust1==5:
                    username=input("Enter your Username: ")
                    pswd=input("Enter your Password: ")
                    sql="Delete from consumers Where UserName = '{}' and Password = '{}'".format(username,pswd)    
                    cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                    cu = cn.cursor()
                    cu.execute(sql)
                    cn.commit()
                    print()
                    a=(cu.rowcount)
                    if a!=0:
                        print("Account Deleted Successfully")
                    else:
                        print("Invalid Credentials")
                        print("=="*25)
                        break
                    print("=="*25)
                    cu.close()
                    cn.close()
                            
                elif cust1==6:
                    cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                    selid=input("Enter Seller ID: ")
                    sql="select SellerName,MobileNumber from Sellers where SellerID='{}'".format(selid)
                    df=pd.read_sql(sql,cn)
                    if len(df)==0:
                        print("=="*25)
                        print("Invalid Seller ID")
                        print("=="*25)
                    else:
                        print("=="*25)
                        print()
                        print(df)
                        print()
                        print("=="*25)
                        input("Hit ENTER to Continue")
                        print("=="*25)
    
                elif cust1==7:
                    break
        
        elif log1==2:#Seller Interface
            print(" \n1. Register \n2. View your details \n3. Update your details \n4. Manage your Orders \n5. Delete your account \n6. Search a Customer \n7. Back to the previous menu")
            print()
            selop=int(input("Please enter the appropriate number: "))
            print("=="*25)
            if selop not in[1,2,3,4,5,6,7]:
                print("Invalid Entry")
                print("=="*25)
            cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
            if selop==1:
                print("\t       Create Your Profile")
                print()
                selid=int(np.random.randint(10,100))
                username=input("Create your Username: ")
                df=pd.read_sql("select * from Sellers",cn)
                search=df[df.UserName==username]
                if len(search)==0:
                    pswd=input("Create your Password: ")
                    bname=input("Enter Your Business Name: ")
                    mobno=input("Enter Your Mobile Number: ")
                    adrs=input("Enter Your Address: ")
                
                    sql="insert into sellers values({},'{}','{}','{}',{},'{}')".format(selid,username,pswd,bname,mobno,adrs)
                    cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                    cu=cn.cursor()
                    cu.execute(sql)
                    cn.commit()
                    print("Seller registered successfully")
                    print()
                    print("===="*20)
                    print()
                    print("Hi,",bname,"!",[selid],"= This is your Seller ID, we recommended you to note it down.")
                    print()
                    print("===="*20)
                    cu.close()
                    cn.close()
                    
                    
                else:
                    print("=="*25)
                    print()
                    print("User already exists, create a different one.")
                    print()
                    print("=="*25)
                    
                        
            elif selop==2:
                print(" \n1. View Your Details \n2. View Total Sales of Last Year")
                print()
                detail=int(input("Please enter the appropriate number: "))
                print("=="*25)
                if detail not in [1,2]:
                    print("Invalid Entry")
                    print("=="*25)
                elif detail==1:
                    username=input("Enter your Username: ")
                    pswd=input("Enter your Password: ")
                    sql="select * from Sellers where UserName='{}' and Password='{}'".format(username,pswd)
                    df=pd.read_sql(sql,cn)
                    if len(df)==0:
                        print("=="*25)
                        print("Invalid Credentials")
                        print("=="*25)
                        
                    else:
                        print("=="*25)
                        print()
                        print(df)
                        print()
                        print("=="*25)
                        input("Hit ENTER to Continue")
                        while True:
                            cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                            print("=="*25)
                            print("\n Do you want to perform any operation?")
                            print()
                            print("1. View top 5 Sellers")
                            print("2. View Bottom 5 Sellers")
                            print("3. View Premium Customers with a graph")
                            print("4. View Ratings of Sellers with a graph")
                            print("5. Back to the Main Menu")
                            print()
                            ch_s2=int(input("Please enter the appropriate number: "))
                            print("=="*25)
                            if ch_s2 not in [1,2,3,4,5]:
                                print("Invalid Entry")
                                print("=="*25)
                            elif ch_s2==1:
                                sql="select SellerName from sellers group by Ratings having Ratings>4.0".format(ch_s2)
                                df=pd.read_sql(sql,cn)
                                print(df.head())
                            elif ch_s2==2:
                                sql="select SellerName from sellers group by Ratings having Ratings<4.0".format(ch_s2)
                                df=pd.read_sql(sql,cn)
                                print(df.head())
                            elif ch_s2==3:
                                sql="select Name,TotalOrders from consumers".format(ch_s2)
                                df=pd.read_sql(sql,cn)
                                df.sort_values(by='TotalOrders')
                                df = df[df.TotalOrders>15]
                                print(df)
                                df.plot(kind='bar')
                                pl.xlabel("Customers")
                                pl.ylabel('Total Orders')
                                pl.title('Premium Customers')
                                pl.show()
                                print("=="*25)
                                input("Hit ENTER to Continue")
                            elif ch_s2==4:
                                sql="select SellerName,Ratings from sellers".format(ch_s2)
                                df=pd.read_sql(sql,cn)
                                df.sort_values(by='Ratings')
                                print(df)
                                df.plot(kind='bar')
                                pl.xlabel('Sellers')
                                pl.ylabel('Ratings')
                                pl.title('Seller Ratings')
                                pl.show()
                                print("=="*25)
                                input("Hit ENTER to Continue")
                            elif ch_s2==5:
                                break
                            
                elif detail==2:
                    username=input("Enter your Username: ")
                    pswd=input("Enter your Password: ")
                    sql="select january,february,march,april,may,june,july,august,september,october,november,december from sales where UserName='{}' and Password='{}'".format(username,pswd)
                    df=pd.read_sql(sql,cn)
                    if len(df)==0:
                        print("=="*25)
                        print("Invalid Credentials")
                        print("=="*25)
                    else:
                        print("=="*25)
                        df.plot(kind='bar')
                        pl.xlabel('Months')
                        pl.xticks(df.index)
                        pl.ylabel('Sales')
                        pl.title('Sales of Last Year (2020)')
                        pl.show()
                    
            elif selop==3:
                username=input("Enter your Username: ")
                pswd=input("Enter your Password: ")
                sql="select * from Sellers where UserName='{}' and Password='{}'".format(username,pswd)
                df=pd.read_sql(sql,cn)
                if len(df)==0:
                    print("=="*25)
                    print("Invalid Credentials")
                    print("=="*25)
                                        
                else:
                    print("=="*25)
                    print("What do you want to update?")
                    print()
                    print("1. Business Name")
                    print("2. Mobile Number")
                    print("3. Address")
                    print("4. Username")
                    print("5. Password")
                    print()
                    seid=int(input("Please enter the appropriate number: "))
                    print("=="*25)
                    if seid not in [1,2,3,4,5]:
                        print("Invalid Entry")
                        print("=="*25)
                    
                    elif seid==1:
                        bname=input("Enter new Business Name: ")
                        sql="Update Sellers Set SellerName = '{}' Where UserName = '{}' and Password = '{}'".format(bname,username,pswd)
                    elif seid==2:
                        mobno=input("Enter new Mobile Number: ")
                        sql="Update Sellers Set MobileNumber = '{}' Where UserName = '{}' and Password = '{}'".format(mobno,username,pswd)
                    elif seid==3:
                        adrs=input("Enter new Address: ")
                        sql="Update Sellers Set Address = '{}' Where UserName = '{}' and Password = '{}'".format(adrs,username,pswd)
                    elif seid==4:
                        usenm=input("Enter new Username: ")
                        selid=input("Enter your Consumer ID: ")
                        sql="Update Sellers Set UserName = '{}' Where SellerID = '{}' and Password = '{}'".format(usenm,selid,pswd)
                    elif seid==5:
                        usenm=input("Renter your Username: ")
                        pswd=input("Enter new Password: ")
                        sql="Update Sellers Set Password = '{}' Where UserName = '{}'".format(pswd,username)
                    
                    else:
                        break
                    cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                    cu=cn.cursor()
                    cu.execute(sql)
                    cn.commit()
                    print("=="*25)
                    print()
                    print("Deatils Updated Successfully")
                    print()
                    print("=="*25)
                    cu.close()
                    cn.close()
                            
                
            elif selop==4:
                username=input("Enter your Username: ")
                pswd=input("Enter your Password: ")
                sql="select * from Sellers where UserName='{}' and Password='{}'".format(username,pswd)
                df=pd.read_sql(sql,cn)
                if len(df)==0:
                    print("=="*25)
                    print("Invalid Credentials")
                    print("=="*25)
                    
                else:
                    print("=="*25)
                    print("Manage all your orders in one go")
                    print("=="*25)
                    print("Choose the option as per your requirements")
                    print(" \n1. Modify Order Details \n2. Add New Order \n3. Delete Existing Order \n4. Search an Order")
                    print()
                    odel=int(input("Please enter the appropriate number: "))
                    print("=="*25)
                    if odel not in [1,2,3,4]:
                        print("Invalid Entry")
                        print("=="*25)
                        
                    if odel==1:
                        odid=int(input("Please enter the Order ID to continue: "))
                        sql="select * from Orders where OrderID={}".format(odid)
                        df=pd.read_sql(sql,cn)
                        print("=="*25)
                        print("What do you want to modify?")
                        print()
                        print("1.  Order Transit Location")
                        print("2.  Order Ordering Date")
                        print("3.  Order Delivery Date")
                        print("4.  Order Payment Type")
                        print("5.  Order Status")
                        print("6.  Order Type")
                        print("7.  Order Amount")
                        print("8.  Order Delivery Location")
                        print("9.  Order Quantity")
                        print("10. Ordered Product Name")
                        print("11. Order Transit Location Receiving Date")
                        print("12. Order Consumer ID")
                        print("13. Order Delivery Date previously entered in Transit Details")
                        print()
                        orid=int(input("Please enter the appropriate number: "))
                        print("=="*25)
                        if orid not in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
                            print("Invalid Entry")
                            print("=="*25)
                        elif orid==1:
                            otl=input("Enter new Order Transit Location: ")
                            sql="Update OrderTransit Set Location = '{}' Where OrderID = {}".format(otl,odid)
                        elif orid==2:
                            ored=input("Enter new Order Ordering Date: ")
                            sql="Update Orders Set OrderingDate = '{}' Where OrderID = {}".format(ored,odid)
                        elif orid==3:
                            oddt=input("Enter new Order Delivery Date: ")
                            sql="Update Orders Set DeliveryDate = '{}' Where OrderID = {}".format(oddt,odid)
                        elif orid==4:
                            opt=input("Enter new Order Payment Type: ")
                            sql="Update Orders Set PaymentType= '{}' Where OrderID = {}".format(otp,odid)
                        elif orid==5:
                            ost=input("Enter new Order Status: ")
                            sql="Update Orders Set Status = '{}' Where OrderID = {}".format(ost,odid)
                        elif orid==6:
                            ort=input("Enter new Order Type: ")
                            sql="Update Orders Set OrderType = '{}' Where OrderID = {}".format(ort,odid)
                        elif orid==7:
                            oram=input("Enter new Order Amount: ")
                            sql="Update Orders Set OrderAmount = '{}' Where OrderID = {}".format(oram,odid)
                        elif orid==8:
                            ordl=input("Enter new Order Delivery Location: ")
                            sql="Update Orders Set DeliveryLocation = '{}' Where OrderID = {}".format(ordl,odid)
                        elif orid==9:
                            orqt=input("Enter new Order Quantity: ")
                            sql="Update OrderDetails Set Amount = '{}' Where OrderID = {}".format(orqt,odid)
                        elif orid==10:
                            orpn=input("Enter new Ordered Product Name: ")
                            sql="Update OrderDetails Set ProductName = '{}' Where OrderID = {}".format(orpn,odid)
                        elif orid==11:
                            ortlrd=input("Enter new Order Transit Location Receiving Date: ")
                            sql="Update OrderTransit Set DateReceivedOn = '{}' Where OrderID = {}".format(ortlrd,odid)
                        elif orid==12:
                            oyyytp=input("Enter new Order Consumer ID: ")
                            sql="Update Orders Set ConsumerID = '{}' Where OrderID = {}".format(oyyytp,odid)
                        elif orid==13:
                            occctp=input("Enter new Order Delivery Date in Transit Details: ")
                            sql="Update OrderTransit Set DateDeliveredOn = '{}' Where OrderID = {}".format(occctp,odid)
                        else:
                            break
                        cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                        cu=cn.cursor()
                        cu.execute(sql)
                        cn.commit()
                        print("=="*25)
                        print()
                        print("Deatils Updated Successfully")
                        print()
                        print("=="*25)
                        cu.close()
                        cn.close()
                        
                    elif odel==2:
                        print("            Enter order details       ")
                        print()
                        orid=int(np.random.randint(10,100))
                        consid=input("Enter Consumer ID: ")
                        ordat=input("Enter Ordering Date: ")
                        ortyp=input("Enter Order Type: ")
                        oramt=input("Enter Order Amount: ")
                        patyp=input("Enter Payment Type: ")
                        orstat=input("Enter Order Status: ")
                        deldat=input("Enter Delivery Date: ")
                        ordl=input("Enter Order Delivery Location: ")
                    
                        sql="insert into orders values({},{},'{}','{}',{},'{}','{}','{}','{}')".format(orid,consid,ordat,ortyp,oramt,patyp,orstat,deldat,ordl)
                        cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                        cu=cn.cursor()
                        cu.execute(sql)
                        print("=="*25)
                        print()
                        print([orid],"= This is your Order ID, we recommend you to note it down.")
                        print()
                        print("=="*25)
                        cn.commit()
                        cu.close()
                        cn.close()
                        typecom=int(input("Type 1 to continue: "))
                        print("=="*25)
                        if typecom!=1:
                            print("Invalid Entry")
                            print("=="*25)
                        else:
                            oridd=input("Enter the Order ID given above: ")
                            prnm=input("Enter Product Name: ")
                            selid=input("Enter Your Seller ID: ")
                            prqty=input("Enter Product Quantity: ")
                            sql="insert into orderdetails values({},'{}',{},{})".format(oridd,prnm,selid,prqty)
                            cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                            cu=cn.cursor()
                            cu.execute(sql)
                            cn.commit()
                            cu.close()
                            cn.close()
                            print("=="*25)
                            print()
                            print("Order details added successfully")
                            print()
                            print("=="*25)
                            print(" \n1. Return to the Main Menu. \n2. Enter Order Transit Details.")
                            print()
                            typpco=int(input("Please enter the appropriate number: "))
                            if typpco not in [1,2]:
                                print("=="*25)
                                print("Invalid Entry")
                                print("=="*25)
                            elif typpco==1:
                                print("=="*25)
                            elif typpco==2:
                                print("=="*25)
                                oriddd=input("Enter Order ID: ")
                                ortrans=int(np.random.randint(10,100))
                                ortl=input("Enter Order Transit Location: ")
                                ordat=input("Enter the date on which the order was received at the transit location: ")
                                odrdat=input("Enter the date on which the order is supposed to be delivered: ")
                                sql="insert into ordertransit values({},{},'{}','{}','{}')".format(oriddd,ortrans,ortl,ordat,odrdat)
                                cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                                cu=cn.cursor()
                                cu.execute(sql)
                                print("=="*25)
                                print()
                                print([ortrans],"= This is your Transit ID, we recommend you to note it down.")
                                print()
                                print("=="*25)
                                cn.commit()
                                cu.close()
                                cn.close()
                                print()
                                print("Transit details added successfully")
                                print()
                                print("=="*25)
                            
                                
                    elif odel==3:
                        odid=input("Enter Order ID: ")
                        sql="delete from orders where OrderID = '{}'".format(odid)
                        cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                        cu = cn.cursor()
                        cu.execute(sql)
                        cn.commit()
                        a=(cu.rowcount)
                        cu.close()
                        cn.close()
                        if a!=0:
                            print("=="*25)
                            print()
                            print("Order(s) deleted successfully")
                            print()
                            print("=="*25)
                        else:
                            print()
                            print("Invalid Order ID")
                            print("=="*25)
                    elif odel==4:
                        odid=input("Enter Order ID: ")
                        sql="select * from Orders where OrderID='{}'".format(odid)
                        df=pd.read_sql(sql,cn)
                        if len(df)==0:
                            print("=="*25)
                            print("Invalid OrderID")
                            print("=="*25)
                        else:
                            print("=="*25)
                            print()
                            print(df)
                            print()
                            print("=="*25)
                            input("Hit ENTER to continue")
                            while True:
                                cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                                print("=="*25)
                                print("\n Do you want to perform any operation?")
                                print()
                                print("1. View top 5 Sellers")
                                print("2. View Bottom 5 Sellers")
                                print("3. View Premium Customers with a graph")
                                print("4. View Ratings of Sellers with a graph")
                                print("5. Back to the Main Menu")
                                print()
                                ch_s2=int(input("Please enter the appropriate number: "))
                                print("=="*25)
                                if ch_s2 not in [1,2,3,4,5]:
                                    print("Invalid Entry")
                                    print("=="*25)
                                elif ch_s2==1:
                                    sql="select SellerName from sellers group by Ratings having Ratings>4.0".format(ch_s2)
                                    df=pd.read_sql(sql,cn)
                                    print(df.head())
                                elif ch_s2==2:
                                    sql="select SellerName from sellers group by Ratings having Ratings<4.0".format(ch_s2)
                                    df=pd.read_sql(sql,cn)
                                    print(df.head())
                                elif ch_s2==3:
                                    sql="select Name,TotalOrders from consumers".format(ch_s2)
                                    df=pd.read_sql(sql,cn)
                                    df.sort_values(by='TotalOrders')
                                    df = df[df.TotalOrders>15]
                                    print(df)
                                    df.plot(kind='bar')
                                    pl.xlabel("Customers")
                                    pl.ylabel('Total Orders')
                                    pl.title('Premium Customers')
                                    pl.show()
                                    print("=="*25)
                                    input("Hit ENTER to Continue")
                                elif ch_s2==4:
                                    sql="select SellerName,Ratings from sellers".format(ch_s2)
                                    df=pd.read_sql(sql,cn)
                                    df.sort_values(by='Ratings')
                                    print(df)
                                    df.plot(kind='bar')
                                    pl.xlabel('Sellers')
                                    pl.ylabel('Ratings')
                                    pl.title('Seller Ratings')
                                    pl.show()
                                    print("=="*25)
                                    input("Hit ENTER to Continue")
                                elif ch_s2==5:
                                    break
                                
            elif selop==5:
                username=input("Enter your Username: ")
                pswd=input("Enter your Password: ")
                sql="delete from sellers where UserName='{}' and Password='{}'".format(username,pswd)
                cu = cn.cursor()
                cu.execute(sql)
                cn.commit()
                a=(cu.rowcount)
                cu.close()
                cn.close()
                if a!=0:
                    print("=="*25)
                    print()
                    print("Account Deleted Successfully")
                    print()
                    print("=="*25)    
                else:
                    print()
                    print("Invalid Credentials")
                    print("=="*25)
                
            elif selop==6:
                cn=sqlcon.connect(host='localhost',database='logistify',user='root',password='1234')
                custid=input("Enter Customer ID: ")
                sql="select Name,MobileNumber from consumers where ConsumerID='{}'".format(custid)
                df=pd.read_sql(sql,cn)
                if len(df)==0:
                    print("=="*25)
                    print("Invalid Consumer ID")
                    print("=="*25)
                else:
                    print("=="*25)
                    print()
                    print(df)
                    print()
                    print("=="*25)
                    
            elif selop==7:
                print()
                print("=="*25)
                
        input("Hit ENTER to Continue")
                    
                          
                    
                
            
