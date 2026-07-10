#Introduction to Flask 
#Learning flask for the first time
from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    page = f"""
    <html>
        <body>
            <p><a href="/home">Go home</a></p>
        </body>
    </html>
    """
    return page

@app.route("/home")
def home():
    today = datetime.date.today()
    page = f"""
    <!-- Creating a link tree website -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="style.css" />
        <title>Danny@Replit</title>
    </head>
    <body>
        <h2>{today}</h2>
        <p>
        <img
            src="./static/images/myProfilePicture.jpeg"
            alt="Profile Picture"
            width="300"
            height="auto"
        />
        </p>
        <h1>Danny Flint Junior Yeboah</h1>
        <p class="aboutMe">A guy just trying to make it in the tech world</p>
        <br />
        <h3>Socials</h3>
        <br />
        <ul>
        <li>
            <a href="https://github.com/FlintDHawtblaster"
            >GitHub (djflint@github)</a
            >
        </li>
        <li>
            <a
            href="https://www.linkedin.com/in/danny-flint-junior-yeboah-593734290?utm_source=share_via&utm_content=profile&utm_medium=member_android"
            >LinkedIn (djflint@LinkedIn)</a
            >
        </li>
        <li><a href="https://x.com/djnr_flint">Twitter (djflint@x)</a></li>
        <li>
            <a
            href="https://www.instagram.com/djflint7?utm_source=qr&igsh=NWJnam5jemlhZW1t"
            >Instagram (djflint@instagram)</a
            >
        </li>
        <li>
            <a href="https://www.facebook.com/share/17qtW1exiJ/"
            >Facebook (djflint@facebook)</a
            >
        </li>
        <li>
            <a href="https://youtube.com/@flintjundy?si=Lt_F45iaRLaWA5yB"
            >YouTube (djflint@youtube)</a
            >
        </li>
        </ul>
    </body>
    </html>
    """
    return page

app.run(host='0.0.0.0', port=81)