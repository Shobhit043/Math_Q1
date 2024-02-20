from flask import Flask, request, jsonify

app = Flask(__name__)

def read_input(filename):
    test_cases = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            nums = list(map(int, line.strip().split()))
            test_cases.append(nums)
    return test_cases

@app.route('/', methods=['GET','POST'])
def process_input():

    if 'output' not in request.files:
        return jsonify({'error': 'No input file provided'}), 400
    
    output = request.files['output']

    if output.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    test_cases = read_input('output.txt')

    for case in test_cases:

        if len(case) == 2:
            n, y = case
            if(y==-1):
                if((n%2)==0):
                    return jsonify({'result':'wrong answer'})
            else:
                return jsonify({'result':'wrong answer'})
    
        elif len(case) == 3:
            n, x, y = case
            if((n<=0) or (x<=0) or (y<=0)):
                return jsonify({'result':'wrong answer'})
            
            if((x**y)*y + (y**x)*x != n):
                return jsonify({'result':'wrong answer'})
            
        else:
            return jsonify({'result':"wrong format"})

    return jsonify({'result':'Passed'})

if __name__ == '__main__':
    app.run(debug=True)
