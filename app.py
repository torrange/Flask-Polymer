#!/usr/bin/env python2

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def main():
	return render_template("index.html")

@app.route("/posts")
def posts():
	posts = open("./static/json/posts.json").read()
	return(posts)

if __name__ == '__main__':
	app.run(host="127.0.0.1", port=5000)