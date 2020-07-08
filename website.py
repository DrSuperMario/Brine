from flask import Flask, request, render_template
from models.data_reader import *



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

        
@app.route('/result', methods=['POST','GET'])
def result():


    if request.method == 'POST':

        if request.form['submit_button'] == 'Get All Data':
        
            pressed = get_all_data()
            return render_template('result.html', pressed=pressed)

        elif request.form['submit_button'] == 'Get Group Data':

            pressed = get_group_data()
            return render_template('result.html', pressed=pressed)

        elif request.form['submit_button'] == 'Get Data by Id' and request.form['market'] == 'stock':

            pressed = find_data_by_group(1)
            return render_template('result.html', pressed=pressed)

        elif request.form['submit_button'] == 'Get Data by Id' and request.form['market'] == 'crypto':

            pressed = find_data_by_group(2)
            return render_template('result.html', pressed=pressed)
        
        elif request.form['submit_button'] == 'Get Data by Id' and request.form['market'] == 'forex':

            pressed = find_data_by_group(3)
            return render_template('result.html', pressed=pressed)
        
        elif request.form['submit_button'] == 'Search ticker':

            pressed = find_data_by_ticker(str(request.form.get('search_field')).upper())
            return render_template('result.html', pressed=pressed)

                
    



if __name__=="__main__":
    app.run(port=5050)
   
