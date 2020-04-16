from flask import Flask, request
from song_manager import SongManager
from song import Song
import json
import random
from datetime import datetime
from urllib.parse import unquote
import urllib

app = Flask(__name__)

song_mgr = SongManager('song_db.sqlite')


@app.route('/song', methods=['POST'])
def add_song():
    """ Add a song to the database """
    content = request.json

    try:
        song = Song(title=content['title'],
                    artist=content['artist'],
                    file_location=content['file_location'],
                    runtime=content['runtime'],
                    album=content['album'],
                    genre=content['genre'])
        song_mgr.add_song(song)

        response = app.response_class(
                status=200
        )
    except ValueError as e:
        response = app.response_class(
                response=str(e),
                status=400
        )
    return response


# @app.route('/student/<string:student_id>', methods=['GET'])
# def get_student(student_id):
#     """ Get a student from the database """
#     try:
#         student = student_mgr.get_student(student_id)
#         if student is None:
#             raise ValueError(f"Student {student_id} does not exist")
#
#         response = app.response_class(
#                 status=200,
#                 response=json.dumps(student.to_dict()),
#                 mimetype='application/json'
#         )
#         return response
#     except ValueError as e:
#         response = app.response_class(
#                 response=str(e),
#                 status=404
#         )
#         return response
#
#
# @app.route('/student/random', methods=['GET'])
# def random_student():
#     """ Return a random student from the database """
#     try:
#         names = student_mgr.get_all_students()
#
#         if len(names) > 0:
#             idx = random.randint(0, len(names) - 1)
#             random_student = names[idx]
#         else:
#             raise ValueError("No Students in DB")
#
#         response = app.response_class(
#                 status=200,
#                 response=json.dumps(random_student.to_dict()),
#                 mimetype='application/json'
#         )
#         return response
#     except ValueError as e:
#         response = app.response_class(
#                 response=str(e),
#                 status=404
#         )
#         return response
#
#
@app.route('/song/<string:file_location>', methods=['DELETE'])
def delete_song(file_location):
    """ Delete a student from the DB   """
    try:
        song_mgr.delete_song(file_location)

        response = app.response_class(
                status=200
        )
    except ValueError as e:
        response = app.response_class(
                response=str(e),
                status=404
        )
    return response


@app.route('/song/all', methods=['GET'])
def get_all_songs():
    """ Return a list of all student names    """
    songs = song_mgr.get_all_songs()

    response = app.response_class(
            status=200,
            response=json.dumps([s.meta_data() for s in songs]),
            mimetype='application/json'
    )

    return response


@app.route('/song/<string:file_location>', methods=['PUT'])
def update_song(file_location):
    """ Update the student information  """
    content = request.json

    try:
        song = song_mgr.get_song(file_location)
        song.album = content["album"]
        song.genre = content["genre"]
        song.rating = content["rating"]
        song_mgr.update_song(song)
        response = app.response_class(
                status=200
        )
    except ValueError as e:
        response = app.response_class(
                response=str(e),
                status=400
        )

    return response

# @app.route('/student/all', methods=['DELETE'])
# def delete_all_students():
#     """ Delete a student from the DB """
#     try:
#      student_mgr.delete_all_students()
#      response = app.response_class(
#      status=200
#     )
#     except ValueError as e:
#         response = app.response_class(response=str(e), status=404)
# 
#     return response

if __name__ == "__main__":
    app.run(debug=True)
