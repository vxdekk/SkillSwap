from flask import Flask, render_template, request, redirect
import json
#sigma
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def nalozi_skills():
    try:
        with open('skills.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def shrani_skills(skills):
    with open('skills.json', 'w') as f:
        json.dump(skills, f, indent=4)

@app.route('/register', methods=['GET', 'POST'])
def registracija():
    skills = nalozi_skills()

    if request.method == 'POST':
        znam = request.form['znam_po_meri'] if request.form['znam_po_meri'] else request.form['znam_izbira']
        zelim_se_nauciti = request.form['zelim_po_meri'] if request.form['zelim_po_meri'] else request.form['zelim_izbira']

        
        for nova_vescina in [znam, zelim_se_nauciti]:
            if nova_vescina and nova_vescina not in skills:
                skills.append(nova_vescina)
        shrani_skills(skills)

        uporabnik = {
            "ime": request.form['name'],
            "znam": znam,
            "zelim_se_nauciti": zelim_se_nauciti,
            "discord": request.form['discord']
        }

        try:
            with open('users.json', 'r') as f:
                uporabniki = json.load(f)
        except FileNotFoundError:
            uporabniki = []

        uporabniki.append(uporabnik)

        with open('users.json', 'w') as f:
            json.dump(uporabniki, f, indent=4)

        return redirect('/')
    return render_template('register.html', skills=skills)

@app.route('/search', methods=['GET', 'POST'])
def iskanje():
    skills = nalozi_skills()

    if request.method == 'POST':
        skill = request.form['skill']

        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        
        matching_users = [user for user in users if user.get('znam') == skill]

        return render_template('search.html', users=matching_users, skills=skills)

    return render_template('search.html', users=None, skills=skills)

@app.route('/prijava', methods=['GET', 'POST'])
def prijava():
    if request.method == 'POST':
        vneseno_ime = request.form['ime']
        vnesen_discord = request.form['discord']

        



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
