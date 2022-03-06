from flask import Flask, render_template 
app = Flask(__name__)    

headings = ("First Name", "Last Name", "Full Name")

users = (
    ("Michael", "Choi", "Michael Choi"),
    ("John", "Supsupin", "John Supsupsin"),
    ("Mark", "Guillen", "Mark Guillen")
)
@app.route('/')
def table():
    return render_template("index.html", users = users, headings = headings)

if __name__=="__main__":
    app.run(debug=True)