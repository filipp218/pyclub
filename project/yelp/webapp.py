from flask import Flask
from flask import request

from .main import load_feedback, save_feedback, add_comment

app = Flask(__name__)

HOME_PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <title>Made with love by Python Club</title>
  </head>
  <body>
    <div class="container-fluid">
    <h1>No comment - no food!</h1>

    <form>
      <div class="form-group">
        <input class="form-control" type="text" name="author" placeholder="Your name please">
        <label for="comment">Your fascinating comment</label>
        <textarea name="comment" class="form-control" id="comment" rows="3"></textarea>
      </div>
      <center>
          <button type="submit" name="like" class="btn btn-outline-success">Like!</button>
          <button type="submit" name="hate" class="btn btn-outline-danger">Hate!</button>
      </center>
    </form>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
"""


def save_new_comment(author, comment):
    feedback = load_feedback('feedback.json')
    add_comment(feedback, author, result)
    save_feedback(feedback, 'feedback_new.json')


@app.route("/")
def hello():
    hate = 'hate' in request.args
    like = 'like' in request.args
    if hate is False and like is False:
        return HOME_PAGE

    comment = request.args.get('comment', '')
    author = request.args.get('author', '')
    result = 'Hate! ' + comment if hate else 'Like! ' + comment
    save_new_comment(author, result)
    return 'Thank you for your piece of feedback! <3'
