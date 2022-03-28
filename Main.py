from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import datetime
import mysql.connector



from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')

@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')

@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')

@app.route("/Post")
def Post():
    return render_template('Post.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

           conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
           # cursor = conn.cursor()
           cur = conn.cursor()
           cur.execute("SELECT * FROM register ")
           data = cur.fetchall()
           return render_template('AdminHome.html' , data=data)

       else:
        return render_template('index.html', error=error)


@app.route("/AdminHome", methods=['GET', 'POST'])
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)



@app.route("/CommentInfo", methods=['GET', 'POST'])
def CommentInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb ")
    data = cur.fetchall()
    return render_template('CommentInfo.html', data=data)


@app.route("/UploadInfo", methods=['GET', 'POST'])
def UploadInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT distinct UserName, ImageInfo,Image	 FROM sharetb ")
    data = cur.fetchall()
    return render_template('UploadInfo.html', data=data)

@app.route("/WordTraining", methods=['GET', 'POST'])
def WordTraining():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM negtb ")
    data = cur.fetchall()
    return render_template('WordTraining.html', data=data)





@app.route("/newuser", methods = ['GET', 'POST'])
def newuser():
    error = None
    if request.method == 'POST':
        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        address = request.form['address']
        email = request.form['email']
        pnumber = request.form['phone']


        uname = request.form['uname']
        password = request.form['psw']
        file = request.files['file']
        file.save("static/upload/" + file.filename)



        mydb = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        cursor = mydb.cursor()
        mycursor = mydb.cursor()

        mycursor.execute("select max(id) from register")

        myresult = mycursor.fetchall()

        for x in myresult:
            y = x[0]
            break
        if y == None:
            print("No such charater available in string")
            x1=1
        else:
            y1 = y
            x1 =int(y1)+1
            print(x1)
        cursor.execute(
            "INSERT INTO register VALUES ('"+str(x1)+"','" + name1 + "','"+ gender1 +"','"+ Age +"','" + address + "','" + email + "','" + pnumber + "','" + uname + "','" + password + "','"+file.filename+"')")

        mycursor1 = mydb.cursor()
        mycursor1.execute("select * from register where id!='"+str(x1)+"'")
        myresult1 = mycursor1.fetchall()
        for z in myresult1:
            frid=z[0]
            fname=z[1]
            mycursor2 = mydb.cursor()
            mycursor2.execute("insert into frlist(id,uname,frname,status)values('','"+name1+"','"+str(fname)+"','0')")
            mycursor2 = mydb.cursor()
            mycursor2.execute("insert into frlist(id,uname,frname,status)values('','" + str(fname) + "','" + name1 + "','0')")
          
        mydb.commit()
        mydb.close()

        return render_template('UserLogin.html',data=myresult1,data1=myresult)


@app.route("/neword", methods=['GET', 'POST'])
def neword():
    error = None
    if request.method == 'POST':

        nword = request.form['nword']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        mycursor = conn.cursor()
        mycursor.execute(
            "insert into negtb values('','" + nword + "')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * 	 FROM negtb ")
        data = cur.fetchall()

        return render_template('WordTraining.html', data=data)



@app.route("/delete",methods = ['GET'])
def delete():


        id = request.args.get('id')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        cursor = conn.cursor()
        cursor.execute("delete from  negtb  where id='"+ id+"'  ")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * 	 FROM negtb ")
        data = cur.fetchall()

        return render_template('WordTraining.html', data=data)




@app.route("/login",methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['uname']
        session['uname'] = request.form['uname']
        password = request.form['password']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()

        if data is None:
            return 'Username or Password is wrong'
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM register where uname='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data)

@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register  where uname='" + uname +"'  ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/Friend")
def Friend():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM frlist  where uname='" + uname + "' and status='0' ")
    data1 = cur.fetchall()


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM frlist  where frname='" + uname + "' and Status='waiting' ")
    data2 = cur.fetchall()


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()

    cur.execute("SELECT * FROM frlist  where uname='" + uname + "'   and Status='Accept'  ")
    data3 = cur.fetchall()



    return render_template('Friend.html', data1=data1,data2=data2,data3=data3 )




def Friend1():

    rdata=''
    adata=''
    fdata=''
    data24=''

    n = session['uname']
    my_list = []

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    cursor = conn.cursor()
    cursor.execute("SELECT * from register where uname='" + n + "'")
    data = cursor.fetchall()
    for x in data:
        uid = x[0]
        print(uid)
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="1Socialnetpy")
    mycursor = mydb.cursor()

    mycursor.execute("select * from frlist where id='" + str(uid) + "' && status='0'")
    data1 = mycursor.fetchall()
    for x1 in data1:
        frid = str(x1[3])
        print(frid)
        mycursor1 = mydb.cursor()

        mycursor1.execute("select * from register where id='" + str(frid) + "'")
        data2 = mycursor1.fetchall()

        for f in data2:
            print(f[9])
            fs = str(f[9])

            my_list.append(f[9])
            print(my_list)


    mycursor.execute("select * from frlist where frid='" + str(uid) + "' && status='1'")
    data12 = mycursor.fetchone()
    if data12 is None:
        print('no accept')
        #return render_template('accept.html')
        data22=''
    else:
        aList = []
        mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="1Socialnetpy")
        mycursor1 = mydb1.cursor()

        mycursor1.execute("select * from frlist where frid='" + str(uid) + "' && status='1'")
        data21 = mycursor1.fetchall()
        for x1 in data21:
            frid = str(x1[0])
            print(frid)
            mycursor11 = mydb1.cursor()

            mycursor11.execute(
                "SELECT register.id, register.name, register.image FROM register INNER JOIN frlist ON register.id=frlist.id WHERE (frlist.frid ='" + str(
                    uid) + "' && frlist.status='1')  && register.id!='" + str(uid) + "'")
            data22 = mycursor11.fetchall()
            for v in data22:
                print(v[1])
                aList.append(v[1])

        print("Updated List : ", aList)
        d = aList
        print(d)







    mycursor1.execute("select * from frlist where name='" + str(n) + "' && status='2'")
    data23 = mycursor1.fetchone()
    if data23 is None:
        print('no frlist')
        data25=''
        #return render_template('frlist.html')
    else:
        aList = []

        mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="1Socialnetpy")
        mycursor1 = mydb1.cursor()

        mycursor1.execute("select * from frlist where name='" + str(n) + "' && status='2'")
        data24 = mycursor1.fetchall()
        for x1 in data24:
            frid = str(x1[0])
            print(frid)
            mycursor11 = mydb1.cursor()

            mycursor11.execute("select * from register where id='" + frid + "'")
            data25 = mycursor11.fetchall()
            for v in data25:
                print(v[9])
                aList.append(v[1])

        print("Updated List : ", aList)
        d = aList
        print(d)



    return render_template('Friend.html', data=data1,data1=data22,data2=data24 )




@app.route("/list1",methods = ['GET'])
def list1():


        id = request.args.get('id')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        cursor = conn.cursor()
        cursor.execute("update frlist set Status='waiting' where id='"+ id+"'  ")
        conn.commit()
        conn.close()

        return Friend()


@app.route("/accept1",methods = ['GET'])
def accept1():

        n = request.args.get('act')
        id=request.args.get('id')
        fname = request.args.get('name')
        uname = session['uname']

        print(fname)
        print(uname)



        if n=="snt":

            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="1Socialnetpy")
            mycursor = mydb.cursor()

            mycursor.execute(
                "update frlist set status='Accept' where id='" + str(id) + "'  ")
            mydb.commit()
            mydb.close()


            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="1Socialnetpy")
            mycursor = mydb.cursor()

            mycursor.execute("update frlist set status='Accept' where uname='" + str(uname)+ "' and frname='" + fname + "'")
            mydb.commit()
            mydb.close()



            mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="1Socialnetpy")
            mycursor1 = mydb1.cursor()

            mycursor1.execute("update frlist set status='Accept' where uname='" + str(fname) + "' and frname='" + uname + "'")
            mydb1.commit()
            mydb1.close()


            return Friend()
        if n=="rejt":

            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="1Socialnetpy")
            mycursor = mydb.cursor()

            mycursor.execute(
                "update frlist set status='Reject' where id='" + str(id) + "'  ")
            mydb.commit()
            mydb.close()

            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="1Socialnetpy")
            mycursor = mydb.cursor()
            mycursor.execute(
                "update frlist set status='Reject' where uname='" + str(uname) + "' and frname='" + fname + "'")
            mydb.commit()
            mydb.close()


            mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="1Socialnetpy")
            mycursor1 = mydb1.cursor()
            mycursor1.execute(
                "update frlist set status='Reject' where uname='" + str(fname) + "' and frname='" + uname + "'")
            mydb1.commit()
            mydb1.close()

            return Friend()

@app.route("/Home")
def Home():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sharetb  where frname='" + uname + "' ")
    data = cur.fetchall()

    return render_template('Home.html',data=data)


@app.route("/post1",methods = ['GET', 'POST'])
def post1():
    if request.method == 'POST':

        place=request.form['caption']
        f = request.files['file']
        f.save("static/upload/" +(f.filename))
        uname=session['uname']

        #g = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        mycursor = conn.cursor()
        mycursor.execute("insert into sharetb values('','" + uname + "','" + place + "','" + f.filename + "','"+uname+"')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        cursor = conn.cursor()
        cursor.execute("select * from frlist where uname='" + uname + "' and status='Accept'")
        data = cursor.fetchall()
        for x1 in data:
            fname = str(x1[2])

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
            mycursor = conn.cursor()
            mycursor.execute(
                "insert into sharetb values('','" + uname + "','" + place + "','" + f.filename + "','" + fname + "')")
            conn.commit()
            conn.close()





        return  Home()



@app.route("/cmt",methods = ['GET'])
def cmt():
    id = request.args.get('id')
    session['id'] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sharetb  where id='" + id + "'     ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb  where shareid='" + id + "'  and Ccount='0'    ")
    data1 = cur.fetchall()

    return render_template('Comment.html', data=data, data1=data1)







@app.route("/share",methods = ['GET'])
def share():

        id=request.args.get('id')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        cursor = conn.cursor()
        cursor.execute("SELECT *   FROM sharetb WHERE id  ='" + id + "'   ")
        data2 = cursor.fetchone()
        if data2:
            imginfo = data2[2]
            img = data2[3]

            print(imginfo)



        else:
            print('no data')



        uname=session['uname']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        cursor = conn.cursor()
        cursor.execute("select * from frlist where uname='" + uname + "' and status='Accept'")
        data = cursor.fetchall()
        for x1 in data:
            fname = str(x1[2])

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
            mycursor = conn.cursor()
            mycursor.execute(
                "insert into sharetb values('','" + uname + "','" + imginfo + "','" + img + "','" + fname + "')")
            conn.commit()
            conn.close()





        return  Home()






@app.route("/Notification")
def Notification():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb  where uname='" + uname + "'   and Ccount='1'  ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb  where uname='" + uname + "'   and Ccount='0'  ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb  where uname='" + uname + "'   and Ccount='2'  ")
    data2 = cur.fetchall()



    return render_template('Notification.html',data=data ,data1=data1,data2=data2)



@app.route("/CAccept",methods = ['GET'])
def CAccept():

        id=request.args.get('id')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
        mycursor = conn.cursor()
        mycursor.execute(
            "update   comtb set Ccount='0' where id='"+id+"' ")
        conn.commit()
        conn.close()

        return  Notification()


@app.route("/CReject", methods=['GET'])
def CReject():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    mycursor = conn.cursor()
    mycursor.execute(
        "update   comtb set Ccount='2' where id='" + id + "' ")
    conn.commit()
    conn.close()

    return Notification()



def sendmsg(targetno,message):
    import requests
    requests.post("http://smsserver9.creativepoint.in/api.php?username=fantasy&password=596692&to=" + targetno + "&from=FSSMSS&message=Dear user  your msg is " + message + " Sent By FSMSG FSSMSS&PEID=1501563800000030506&templateid=1507162882948811640")






if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)