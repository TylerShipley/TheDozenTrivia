from flask import Flask
from flask import render_template
import random

app = Flask(__name__)


# function to stash questions and answers lists
def read_and_split_data(filename):
    Questions = []
    Answers = []
    # Open and read the file line by line
    with open(filename, 'r') as file:
        for line in file:
            # If the line contains the delimiter
            if "::" in line:
                question, answer = line.split("::", 1)
                Questions.append(question)
                Answers.append(answer.strip())  # Using strip() to remove any trailing newlines or spaces
        
    return Questions, Answers

# function to pull a random question and answer and its index
def pickQuestion(list):
    index = random.randint(0, len(list)-1)
    return index


# populate lists
cfbquestions, cfbanswers = read_and_split_data("Q&A/collegefootball.txt")
cbbquestions, cbbanswers = read_and_split_data("Q&A/collegebasketball.txt")
geoquestions, geoanswers = read_and_split_data("Q&A/geography.txt")
historyquestions, historyanswers = read_and_split_data("Q&A/history.txt")
misquestions, misanswers = read_and_split_data("Q&A/MISCELLANEOUS.txt")
mlbquestions, mlbanswers = read_and_split_data("Q&A/mlb.txt")
nbaquestions, nbaanswers = read_and_split_data("Q&A/nba.txt")
moviequestions, movieanswers = read_and_split_data("Q&A/movies.txt")
nflquestions, nflanswers = read_and_split_data("Q&A/nfl.txt")
otherquestions, otheranswers = read_and_split_data("Q&A/othersports.txt")
restquestions, restmlbanswers = read_and_split_data("Q&A/restaurants.txt")
telquestions, telanswers = read_and_split_data("Q&A/television.txt")




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cfb.html')
def cfb():
    index = pickQuestion(cfbquestions)
    question = cfbquestions[index]
    answer = cfbanswers[index]
    cfbquestions.pop(index)
    cfbanswers.pop(index)
    return render_template('cfb.html', question=question, answer=answer)

@app.route('/cbb.html')
def cbb():
    index = pickQuestion(cbbquestions)
    question = cbbquestions[index]
    answer = cbbanswers[index]
    cbbquestions.pop(index)
    cbbanswers.pop(index)
    return render_template('cbb.html', question=question, answer=answer)

@app.route('/mlb.html')
def mlb():
    index = pickQuestion(mlbquestions)
    question = mlbquestions[index]
    answer = mlbanswers[index]
    mlbquestions.pop(index)
    mlbanswers.pop(index)
    return render_template('mlb.html', question=question, answer=answer)

@app.route('/nfl.html')
def nfl():
    index = pickQuestion(nflquestions)
    question = nflquestions[index]
    answer = nflanswers[index]
    nflquestions.pop(index)
    nflanswers.pop(index)
    return render_template('nfl.html', question=question, answer=answer)

@app.route('/NBA.html')
def nba():
    index = pickQuestion(nbaquestions)
    question = nbaquestions[index]
    answer = nbaanswers[index]
    nbaquestions.pop(index)
    nbaanswers.pop(index)
    return render_template('NBA.html', question=question, answer=answer)

@app.route('/othersports.html')
def othersports():
    index = pickQuestion(otherquestions)
    question = otherquestions[index]
    answer = otheranswers[index]
    otherquestions.pop(index)
    otheranswers.pop(index)
    return render_template('othersports.html', question=question, answer=answer)

@app.route('/food.html')
def food():
    index = pickQuestion(restquestions)
    question = restquestions[index]
    answer = restmlbanswers[index]
    restquestions.pop(index)
    restmlbanswers.pop(index)
    return render_template('food.html', question=question, answer=answer)

@app.route('/movies.html')
def movies():
    index = pickQuestion(moviequestions)
    question = moviequestions[index]
    answer = movieanswers[index]
    moviequestions.pop(index)
    movieanswers.pop(index)
    return render_template('movies.html', question=question, answer=answer)

@app.route('/television.html')
def television():
    index = pickQuestion(telquestions)
    question = telquestions[index]
    answer = telanswers[index]
    telquestions.pop(index)
    telanswers.pop(index)
    return render_template('television.html', question=question, answer=answer)

@app.route('/geography.html')
def geography():
    index = pickQuestion(geoquestions)
    question = geoquestions[index]
    answer = geoanswers[index]
    geoquestions.pop(index)
    geoanswers.pop(index)
    return render_template('geography.html', question=question, answer=answer)

@app.route('/history.html')
def history():
    index = pickQuestion(historyquestions)
    question = historyquestions[index]
    answer = historyanswers[index]
    historyquestions.pop(index)
    historyanswers.pop(index)
    return render_template('history.html', question=question, answer=answer)

@app.route('/Miscellaneous.html')
def miscellaneous():
    index = pickQuestion(misquestions)
    question = misquestions[index]
    answer = misanswers[index]
    misquestions.pop(index)
    misanswers.pop(index)
    return render_template('Miscellaneous.html', question=question, answer=answer)


if __name__ == "__main__":
    app.run(debug=True)