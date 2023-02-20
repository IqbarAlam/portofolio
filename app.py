from flask import Flask,render_template,jsonify,request
app = Flask(__name__,static_url_path='',static_folder='./static',template_folder='./templates')

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run('0.0.0.0',5000,debug=True)