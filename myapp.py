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
    new_sequence = remove_stuff(sequence).lower()
    sub_sequence_dict = {}

    prev_index = 0
    for i in range(len(sub_sequence)):
        if sub_sequence[i] == ',':
            sub_sequence_dict[remove_stuff(sub_sequence[prev_index:i]).lower()] = []
            prev_index = i+1
    #get the last sub_sequence
    sub_sequence_dict[remove_stuff(sub_sequence[prev_index:len(sub_sequence)]).lower()] = []

    def find_indexes(sub_sequence):
        indexes = []
        for i in range(len(new_sequence)):
            if new_sequence[i:i+len(sub_sequence)] == sub_sequence:
                indexes.append([i+1, i+len(sub_sequence)])
        return indexes

    for key in sub_sequence_dict:
        sub_sequence_dict[key] = find_indexes(key)

    #format string
    return_string = ""
    for key in sub_sequence_dict:
        if len(sub_sequence_dict[key]) == 0:
            return_string += key + ": No site<br />"
        else:
            return_string += key + " Number: " + str(len(sub_sequence_dict[key])) + " Indexes: " + str(sub_sequence_dict[key]) + "<br/>"
    
    return return_string.strip()


if __name__ == '__main__':
    app.run(debug=True)