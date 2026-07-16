#Day 76. Introduction to Flask. Coding challenge

from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    page = f"""
    <html>
        <body>
            <p><a href="/portfolio">My Portfolio Page</a></p>
            <p><a href="/linktree">My Profiles Page</a></p>
        </body>
    </html>
    """
    return page


@app.route('/portfolio')
def portfolio():
    page = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="./static/stylesheets/portfolio.css" type="text/css" />
        <title>100DaysOfCode-Day73</title>
    </head>
    <body>
        <h1>Danny's Portfolio</h1>
        <h2>Day 56 Solution</h2>
        <p>
        So, day 56 was all about using csv reading and the file and folder
        manipulation to make 100 files in dozens of folders. This was tricky
        because the names of the folders and files were based on the top 100 most
        streamed songs and weren't simple to encode.
        </p>
        <img src="./static/images/imageDay56.png" width="900" height="500" />
    </body>
    </html>
    """
    return page


@app.route('/linktree')
def linktree():
    today = datetime.date.today()
    page = f"""
    <!-- Creating a link tree website -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="./static/stylesheets/linktree.css" />
        <title>Danny@Replit</title>
    </head>
    <body>
        <p>
        <h2>{today}</h2>
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