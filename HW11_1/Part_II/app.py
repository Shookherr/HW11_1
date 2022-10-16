# Домашнее задание урок 11. Шумихин Алексей 16.10.22
from flask import Flask, render_template
import utils

app = Flask(__name__)   # create an instance of the Flask class

data = utils.load_candidates_from_json('candidates.json')  # get data from file


@app.route('/')
def page_main():
    return render_template('list.html', candidates=data)


@app.route('/candidates/<int:candidate_id>')
def page_person(candidate_id):
    _, cand_data = utils.get_candidate(candidate_id, data)
    return render_template('single.html', candidate=cand_data)


@app.route('/search/<candidate_name>')
def page_search_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name, data)
    return render_template('search.html', number=len(candidates), candidates=candidates)



@app.route('/skill/<skill_name>')
def page_search_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name, data)
    return render_template('skill.html', skill=skill_name, number=len(candidates), candidates=candidates)


app.run()
