from flask import Flask, render_template, request
import requests

app = Flask(__name__)
# can add additional page after /

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "All OK"

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sent", methods=["POST"])
def sent():
    return render_template("sent.html")

@app.route("/contact", methods=["POST"])
def contact_form():
    form_data = request.form
    send_simple_message(form_data["email"], form_data["name"])
    receive_message(form_data["email"], form_data["name"], form_data["message"])
    return render_template("sent.html")

def send_simple_message(nosy_person, name):
    form_data = request.form
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0e4f6c1364cd4dd4b37fea67b9afc7c6.mailgun.org/messages",
        auth=("api", "c9b7fafb60c13e46ba3e46ea3a6d94dd-059e099e-c9e3fdee"),
        data={"from": "STUCK <mailgun@sandbox0e4f6c1364cd4dd4b37fea67b9afc7c6.mailgun.org>",
              "to": nosy_person,
              "subject": "We've recieved your message!",
              "html": render_template("autoresponse.html", names=name.title())})

def receive_message(email, name, message):
    form_data = request.form
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0e4f6c1364cd4dd4b37fea67b9afc7c6.mailgun.org/messages",
        auth=("api", "c9b7fafb60c13e46ba3e46ea3a6d94dd-059e099e-c9e3fdee"),
        data={"from": "STUCK Message <mailgun@sandbox0e4f6c1364cd4dd4b37fea67b9afc7c6.mailgun.org>",
              "to": "kakay.pang@hotmail.co.uk",
              "subject": "STUCK Message from {}".format(name.title()),
              "html": render_template("message.html", names=name.title(), emails=email.lower(), messages=message)})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
