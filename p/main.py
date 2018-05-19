from flask import Flask, render_template, redirect, url_for, request
from opcua import Client
from dbop2y import stationdb
from forms import StationSetUpForm

app = Flask(__name__)
currentStation = ''
app.config['SECRET_KEY']='b32ed2c46bcdc53f1b330dee8f7c8cf2'

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/stationInformations")
def stationInformations():
    print(currentStation)
    return render_template('station_info.html')


def opendefaultbrowser(url):
    import webbrowser
    webbrowser.open(url)


@app.route("/stationCreate")
def Return_stationCreate():
    temp = []
    newdb = stationdb(tableName='station', path='staiondb.db')
    newdb.dbCommit()
    temp = newdb.getStaitonlist()
    newdb.dbClose()
    return render_template("form1.html", name=temp[0], ip=temp[1])

@app.route("/stationCreate", methods=["POST"])
def stationCreate():
    global currentStation
    cked=False
    temp = []
    newdb = getTempDbObject()

    req_from=request.form

    print(request.form.to_dict())

    if 'stationDummy_Added' in req_from:
        Dummy=DummyDataCtreat()
        for i in range(len(Dummy)):
            # for k,v in Dummy[i].items():
            #     # newdb.createRows(k,v)
            #     print(k,v)
            print(Dummy[i].values())
        # newdb.dbCommit()
        # temp = newdb.getStaitonlist()
        # newdb.dbClose()
        # return render_template("form1.html", name=temp[0], ip=temp[1])

    if 'stationAdded' in req_from:
        tableName = request.form["stationName"]
        ipaddress = request.form["IP_1"] + '.' +request.form["IP_2"] + '.' +request.form["IP_3"] + '.' +request.form[
            "IP_4"]
        print('station is added..')
        newdb.createRows(tableName, ipaddress)
        newdb.dbCommit()
        temp = newdb.getStaitonlist()
        newdb.dbClose()
        currentStation = tableName
        return render_template("form1.html", name=temp[0], ip=temp[1])

    if 'stationDelete' in req_from:
        stationDel=request.form['stationDelete']
        newdb.dbRowDelect(stationDel)
        temp = newdb.getStaitonlist()
        newdb.dbCommit()
        newdb.dbClose()

        return render_template("form1.html", name=temp[0], ip=temp[1])

    return "no found"


@app.route("/formtest", methods=['GET','POST'])
def formtest():
    form=StationSetUpForm()
    if form.validate_on_submit():
        print('data is submitted')
        return redirect(url_for('formtest'))
    return render_template("formtest.html",form=form)


def DummyDataCtreat():
    dummy=[]
    for i in range(0,100):
        d = {}
        d['station']='station'+str(i)
        d['ip']='192.168.0.'+str(i)
        dummy.append(d)
    return  dummy

def getTempDbObject():
    return  stationdb(tableName='station', path='staiondb.db')

if __name__ == '__main__':
    opendefaultbrowser('http://127.0.0.1:5000/')
    app.run(debug=True)
