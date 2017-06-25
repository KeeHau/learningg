from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/<name>')
def index():
    return render_template('index.html')

@app.route('/submitForm', methods=['post'])
def submitForm():
    
    password=request.form['password']
    users={'maysam':'123','arash':'345','keehau':'ooo'}
    orginalPassword=users.get(name,False)
    if orginalPassword==password: 
        return render_template('index.html',name=name)
    else:
        return 'goto hell'
        


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)