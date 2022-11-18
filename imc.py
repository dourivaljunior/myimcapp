from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def imc():
    imc=0
    if request.method=='POST' and 'peso' in request.form and 'altura' in request.form:
        peso=float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
        imc=round(peso/((altura/100)**2),1)
    return render_template("imc.html",imc=imc)
if __name__ == "__main__":
    app.run(debug=True)


