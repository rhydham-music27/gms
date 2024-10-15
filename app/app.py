from flask import Flask,render_template,request

app = Flask(__name__)
unplist = []
@app.route('/login',methods=['GET','POST'])
def login():
    global unplist
    if request.method =='POST':
        unplist.append(request.form['user-name'])
        unplist.append(request.form['password'])
        print(unplist)
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)
