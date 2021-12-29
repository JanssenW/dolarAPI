from flask import Flask
from main import returnDollarValue

app = Flask("ValorDolar")

@app.route("/vd", methods=["GET"])
def valorDolar():
    dolar = returnDollarValue()
    return dolar

app.run()

