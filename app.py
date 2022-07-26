from flask import Flask 

app=Flask(__name__)

@app.route("/",methods={"GET","POST"})
def user():
    try:
        return "<h1> Hello </h1>"
    except Exception as e:
        return e 
if __name__=="__main__":
    app.run(debug=True)
