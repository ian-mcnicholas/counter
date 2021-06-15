from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'secret'

@app.route('/')
def counter():
    if 'counter' in session:
        session['counter'] = session['counter'] + 1 
    else:
        session['counter'] = 1 

    counter = session['counter']
    return render_template('index.html', counter = counter)



@app.route('/destroy_session')
def destroy():
    session['counter'] = 0 

    return redirect('/')


@app.route('/plus2', methods=['POST'])
def plus2():
    session['counter'] = session['counter']+1 
    # only + 1 because the redirect to home adds +1 also

    return redirect('/')
    

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0 
    

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)   