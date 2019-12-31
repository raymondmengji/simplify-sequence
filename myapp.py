from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hello", methods=["POST"])
def hello():
    sequence = request.form['sequence']
    first_index = request.form['FirstIndex']
    second_index = request.form['SecondIndex']

    def remove_stuff(x):
        answer = ""

        for letter in x:
            if letter.isalpha():
                answer += letter
        return answer

    new_sequence = remove_stuff(sequence)
    return new_sequence[int(first_index)-1:int(second_index)]

if __name__ == '__main__':
    app.run(debug=True)