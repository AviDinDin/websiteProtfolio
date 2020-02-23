from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

def write_to_scv_file(data):
    with open('database.csv',newline='', mode='a') as file:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])


def write_to_text_file(data):
    with open('database.txt', 'a') as file:
        file.write(data)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_scv_file(data)
        return hello_world()
    else:
        return 'submit faild'#render_template('login.html', error=error)




if __name__ == '__main__':
    app.run()