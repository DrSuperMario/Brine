from flask import Flask, request, render_template
import models.data_reader as read




app = Flask(__name__)


@app.route('/')
def home():
    try:

        return render_template('home.html')

    except ConnectionError:
        return {'message','Connection not made'}, 400

        
@app.route('/result', methods=['POST','GET'])
def result():

    if request.method == 'POST':

        if request.form['submit_button'] == 'Get All Data':
        
            pressed = read.get_all_data()
            return render_template('result.html', pressed=pressed)

        elif request.form['submit_button'] == 'Get Group Data':

            pressed = read.get_group_data()
            return render_template('result.html', pressed=pressed)

        elif request.form['submit_button'] == 'Get Data by Id' and request.form['market'] == 'stock':

            pressed = read.find_data_by_group(1)
            return render_template('result.html', pressed=pressed)

        elif request.form['submit_button'] == 'Get Data by Id' and request.form['market'] == 'crypto':

            pressed = read.find_data_by_group(2)
            return render_template('result.html', pressed=pressed)
        
        elif request.form['submit_button'] == 'Get Data by Id' and request.form['market'] == 'forex':

            pressed = read.find_data_by_group(3)
            return render_template('result.html', pressed=pressed)

            
    



if __name__=="__main__":
    app.run(debug=True, port=5050)
