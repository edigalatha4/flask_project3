from flask import Flask,render_template

AI=Flask(__name__)



@AI.route('/hai')
def hai():
    return render_template('hai.html')

@AI.route('/hello')
def hello():
    return render_template('hello.html')


if __name__=='__main__':
    AI.run(debug=True)
