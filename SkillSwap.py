from flask import Flask, render_template, request, redirect, session
import json
import requests
from werkzeug.security import generate_password_hash, check_password_hash
#sigma
app = Flask(__name__)
app.secret_key = 'nekaj-zelo-tajnega'
YOUTUBE_API_KLJUC = 'AIzaSyAwAnuV__LH3lneUlREB-MdlcCOfw9CSNY'


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
            "password": generate_password_hash(request.form['geslo']),
            "znam": znam,
            "zelim_se_nauciti": zelim_se_nauciti,
            "discord": request.form['discord'],
            

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

@app.route('/login', methods=['GET', 'POST'])
def prijava():

    if request.method == 'POST':
        vneseno_ime = request.form['ime']
        vneseno_geslo = request.form['geslo']

        try:
            with open('users.json', 'r') as f:
                uporabniki = json.load(f)
        except FileNotFoundError:
            uporabniki = []

        for u in uporabniki:
            if u['ime'] == vneseno_ime and check_password_hash(u['password'], vneseno_geslo):

                session['uporabnik'] = vneseno_ime
                return redirect('/profil/' + vneseno_ime)

        return "Uporabnik ni najden ali napačni podatki", 401


    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('uporabnik', None)
    return redirect('/')

@app.route('/profil/<ime>')
def profil(ime):

    try:
        with open('users.json', 'r') as f:
            uporabniki = json.load(f)
    except FileNotFoundError:
        uporabniki = []

    for u in uporabniki:
        if u['ime'] == ime:
            tema = u.get('zelim_se_nauciti', '')
            videi = pridobi_youtube_videe(tema, YOUTUBE_API_KLJUC)
            return render_template('profile.html', uporabnik=u, videi=videi)
            

    return "Uporabnik ni najden", 404


def pridobi_youtube_videe(tema, api_key):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=3&q=how+to+learn+{tema}&key={api_key}"
    r = requests.get(url)
    if r.status_code != 200:
        return []
    data = r.json()
    return [
        {
            "naslov": v['snippet']['title'],
            "video_url": f"https://www.youtube.com/watch?v={v['id']['videoId']}"

        }
        for v in data['items']
    ]


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
