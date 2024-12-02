from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

users = {}
accounts = {}

global user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/auth', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        return check_auth(email, password)
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']


        users[email] = {'firstName': firstName,
                        'lastName': lastName,
                        'email': email,
                        'password': password,
                        'accounts': []}
        return redirect(url_for('index'))

    else:
        return render_template('register.html')


def check_auth(email, password):
    if email in users.keys():
        if users[email]['password'] == password:
            return redirect(url_for('access_painel', token=email))

    return redirect(url_for('login'))


@app.route('/painel/<token>')
def access_painel(token):
    user = users[token]
    print(user)
    return render_template('painel.html', user=user)


@app.route("/bank_account/<id_bank>")
def get_bank_account(id_bank):
    return


@app.route('/bank_account/new', methods=['GET', 'POST'])
def new_bank_account():
    if request.method == 'POST':

        accountName = request.form['accountName']
        accountType = request.form['accountType']
        creditLimit = request.form['creditLimit']
        creditDate = request.form['creditDate']

        accounts[len(accounts) + 1] = {'accountName': accountName,
                                       'accountType': accountType,
                                       'creditLimit': creditLimit,
                                       'creditDate': creditDate}
        return redirect(url_for('access_painel'), user)
    else:
        return render_template('new_account.html')


@app.route('/bank_account/update/<id_bank>')
def update_bank_account(id_bank):
    return


@app.route('/bank_account/delete/<id_bank>')
def delete_bank_account(id_bank):
    return


if "__main__" == __name__:
    app.run(debug=True)
