import json
import os
from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
import msal

# Load config
with open("config.json") as config_file:
    config = json.load(config_file)

app = Flask(__name__)
app.secret_key = "super-secret-key"

# Session config
app.config["SESSION_TYPE"] = config["SESSION_TYPE"]
Session(app)

AUTHORITY = config["AUTHORITY"]
CLIENT_ID = config["CLIENT_ID"]
CLIENT_SECRET = config["CLIENT_SECRET"]
REDIRECT_PATH = config["REDIRECT_PATH"]
SCOPE = config["SCOPE"]

# Build MSAL app
def build_msal_app():
    return msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Login
@app.route("/login")
def login():

    auth_url = build_msal_app().get_authorization_request_url(
        SCOPE,
        redirect_uri=url_for("authorized", _external=True),
        prompt="select_account"
    )

    print("AUTH URL:", auth_url)

    return redirect(auth_url)

# Callback
@app.route(REDIRECT_PATH)
def authorized():

    if "code" not in request.args:
        return render_template(
            "error.html",
            result="Authorization failed."
        )

    result = build_msal_app().acquire_token_by_authorization_code(
        request.args["code"],
        scopes=SCOPE,
        redirect_uri=url_for("authorized", _external=True)
    )

    if "error" in result:
        return render_template("error.html", result=result)

    session["user"] = result.get("id_token_claims")

    return redirect(url_for("dashboard"))

# Dashboard
@app.route("/dashboard")
def dashboard():

    if not session.get("user"):
        return redirect(url_for("index"))

    user = session["user"]

    return render_template("dashboard.html", user=user)

# Home Page
@app.route("/home")
def home():

    if not session.get("user"):
        return redirect(url_for("index"))

    user = session["user"]

    return render_template("home.html", user=user)

# Reports Page
@app.route("/reports")
def reports():

    if not session.get("user"):
        return redirect(url_for("index"))

    user = session["user"]

    return render_template("reports.html", user=user)

# Settings Page
@app.route("/settings")
def settings():

    if not session.get("user"):
        return redirect(url_for("index"))

    user = session["user"]

    return render_template("settings.html", user=user)

# Logout
@app.route("/logout")
def logout():

    session.clear()

    logout_url = (
        "https://login.microsoftonline.com/common/oauth2/v2.0/logout"
        f"?post_logout_redirect_uri={url_for('index', _external=True)}"
    )

    return redirect(logout_url)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
