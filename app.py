from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    global kinoko_count, takenoko_count
    if request.form.get('item') == 'kinoko':
        kinoko_count += 1
    elif request.form.get('item') == 'takenoko':
        takenoko_count += 1
    
    kinoko_percent = kinoko_count / (kinoko_count + takenoko_count) * 100
    takenoko_persent = takenoko_count / (kinoko_count + takenoko_count) * 100
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
