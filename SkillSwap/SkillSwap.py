from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def load_skills():
    try:
        with open('skills.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_skills(skills):
    with open('skills.json', 'w') as f:
        json.dump(skills, f, indent=4)

@app.route('/register', methods=['GET', 'POST'])
def register():
    skills = load_skills()

    if request.method == 'POST':
        can_do = request.form['can_do_custom'] if request.form['can_do_custom'] else request.form['can_do_select']
        want_to_learn = request.form['want_to_learn_custom'] if request.form['want_to_learn_custom'] else request.form['want_to_learn_select']

        # Avtomatsko dodaj novi skill, če še ni v seznamu
        for new_skill in [can_do, want_to_learn]:
            if new_skill and new_skill not in skills:
                skills.append(new_skill)
        save_skills(skills)

        user = {
            "name": request.form['name'],
            "can_do": can_do,
            "want_to_learn": want_to_learn,
            "discord": request.form['discord']
        }

        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        users.append(user)

        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)

        return redirect('/')
    return render_template('register.html', skills=skills)



if __name__ == '__main__':
    app.run(debug=True)
