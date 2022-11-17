from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/input')
def form():
    return render_template('input.html')
 
@app.route('/output', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/input' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('output.html',form_data = form_data)
 
 
app.run(host='localhost', port=5000)
#'localhost' '0.0.0.0'
