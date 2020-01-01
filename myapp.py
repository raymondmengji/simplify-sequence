from flask import Flask, render_template, request
app = Flask(__name__)

def remove_stuff(x):
    answer = ""

    for letter in x:
        if letter.isalpha():
            answer += letter
    return answer

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hello", methods=["POST"])
def hello():
    sequence = request.form['sequence']
    first_index = request.form['FirstIndex']
    second_index = request.form['SecondIndex']

    new_sequence = remove_stuff(sequence)
    return new_sequence[int(first_index)-1:int(second_index)]

@app.route("/find", methods=["POST"])
def find():
    sequence = request.form['sequence']
    sub_sequence = request.form['sub_sequence']
    
    new_sequence = remove_stuff(sequence)
    new_sub_sequence = remove_stuff(sub_sequence)
    
    indexes = []
    for i in range(len(new_sequence)):
        if new_sequence[i:i+len(new_sub_sequence)] == new_sub_sequence:
            indexes.append([i+1, i+len(new_sub_sequence)])
    return str(indexes)


if __name__ == '__main__':
    app.run(debug=True)