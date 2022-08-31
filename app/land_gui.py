"""
[land_gui.py]
"""

#==============================================================================#

import sys
import json
import os
import imghdr
import time
from web3 import Web3
from hashlib import sha256
from flask import Flask, request, render_template, redirect, abort, send_file
from werkzeug.utils import secure_filename
from ethereum.utils import check_checksum
from setting import FILE_DIR, FILE_PATH, PORT_GUI

#==============================================================================#

app = Flask(__name__)

#==============================================================================#

def save_document(data_dict, document):
    filename = secure_filename(document.filename)

    my_hash = sha256(document.read()).hexdigest();
    document.seek(0, 0)

    land_hash_dir = os.path.join(FILE_PATH, my_hash)
    try:
        os.makedirs(land_hash_dir)
    except OSError as e:
        print(e)

    document.save(os.path.join(land_hash_dir, document.filename))

    data_dict["timestamp"] = int(time.time())
    data_dict["land_hash"] = my_hash
    data_dict["street_num"] = int(data_dict["street_num"])
    with open(os.path.join(land_hash_dir ,'land_info.json'), 'w') as f:
        json.dump(data_dict, f, indent=4)

    print(f"Saved {document.filename} successfully")
    print(f"Hash: {my_hash}")
    print(data_dict)

#==============================================================================#

@app.route('/')
def index():
    print(os.path.join('static', 'people_photo'))
    return render_template("public/index.html", user_image="display_photo.jpg")


@app.route("/about-us", methods=["GET"])
def about_us():
    return render_template("public/about-us.html")


@app.route("/register-land", methods=["GET", "POST"])
def register_land():
    if request.method == "POST":
        if request.files:
            document = request.files["document"]
            data_dict = request.form.to_dict()
            try:
                is_valid_owner_addr = check_checksum(data_dict["owner_addr"])
            except Exception as e:
                print(e)
                is_valid_owner_addr = False

            if not document.filename:
                print("No filename given.")
            elif not document.filename.endswith(".pdf"):
                print("Invalid file - must enter a PDF")
            elif is_valid_owner_addr:
                save_document(data_dict, document)

            return redirect(request.url)

    return render_template("public/register-land.html")


@app.route('/lands', defaults={'req_path': ''})
@app.route('/lands/<path:req_path>')
def lands(req_path="FILE_DIR"):

    abs_path = os.path.join(FILE_PATH, req_path)

    if not os.path.exists(abs_path):
        return abort(404)

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = sorted(os.listdir(abs_path))
    return render_template('public/lands.html', files=files)

#==============================================================================#

if __name__ == '__main__':
    if len(sys.argv) != 1:
        raise SystemExit(f"Usage: {sys.argv[0]}")

    try:
        os.makedirs(FILE_PATH)
    except OSError as e: # pragma: no cover
        print(e)

    app.run(debug=True, port=PORT_GUI)
