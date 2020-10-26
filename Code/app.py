from flask import Flask, request, render_template
import ensemble
import user_based 
import item_based
app = Flask(__name__, template_folder='.')


@app.route("/")
def landingpage():
    return render_template('landingPage.html')


@app.route('/recommend', methods=['POST'])
def recommend_movie():
    userid = request.form['userid']
    genre = request.form['genre']
    approach = request.form['approach']
    response = None
    if genre == 'N/A':
        genre = None
    if approach == 'item-based':
        response = item_based.get_rec_item(int(userid), genre)
    elif approach == 'user-based':
        response = user_based.get_rec_user(int(userid), genre)
    elif approach == 'ensemble':
        response = ensemble.ensemble(userid, genre)
    return render_template('response.html', data=response)


if __name__ == "__main__":
    app.run()
