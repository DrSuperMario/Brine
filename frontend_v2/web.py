from flask import (
                    Flask, 
                    render_template, 
                    session, 
                    redirect, 
                    url_for, 
                    request, 
                    send_file
)


web = Flask(__name__)

@web.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')


if(__name__=='__main__'):
    web.run(port=5050, debug=True)