from flask import Flask ,render_template

app=Flask(__name__)

@app.route("/",methods={"GET","POST"})
def user():
    try:
        return render_template("index.html")
    except Exception as e:
        return e 


@app.route("/test")
def test():
    try:
        return "helloo "
    except Exception as e:
        return "error caught: "+e

if __name__=="__main__":
    app.run(debug=True)
