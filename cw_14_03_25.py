from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def form():
    if request.methods=='POST':
        data={
        "Name":request.form.get("name"),
        "Email":request.form.get("mail"),
        "Password":request.form.get("pwd"),
        "Gender":request.form.get("gender"),
        "Interests":request.form.get("Interests"),
        "Country":request.form.get("country"),
        "Comments":request.form.get("comments"),
        "file":request.files.get("file").filename if request.files.get("file") else "No file uploaded"     
        }
        return render_template("result.html",data=data)
    return render_template("form1.html")
if __name__=="__main__"
    app.run(debug=True)
    