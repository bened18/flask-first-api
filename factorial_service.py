from flask import Flask, jsonify

app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@app.route('/factorial/<int:number>', methods=['GET'])
def get_factorial(number):
    if number < 0:
        return jsonify(error="Número negativo no permitido"), 400
    else:
        result = factorial(number)
        return jsonify(factorial=result)

if __name__ == "__main__":
    app.run(debug=True)
