from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/",methods=["GET","POST"])


def main():
    if request.method=="POST":
        resp = request.form


        if resp.get('opt')== 'BullDog':
            result = "Price is: 25K "
            return render_template("input1.html", resp=result)

        elif resp.get('opt') == 'Poodle':
            result = "Price is: 20K "
            return render_template("input2.html", resp=result)


        elif resp.get('opt') == 'German Shepherd':
            result = "Price is: 35K "
            return render_template("result3.html", resp=result)

        elif resp.get('opt') == 'Chihuahua':
            result = "Price is: 30K "
            return render_template("result4.html", resp=result)


    else:

        return render_template("input.html")




if __name__ == '__main__':
    app.run(debug=True)