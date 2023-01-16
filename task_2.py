"""Задание 2"""
from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def result():
    posl = request.form.get('posl')
    sum = 0
    if posl != None:
        posl = posl.split()
        for symbol in posl:
            if int(symbol) > 0:
                sum += int(symbol)
    return render_template("taslk_2.html", sum = sum)

if __name__ == '__main__':
    app.run()