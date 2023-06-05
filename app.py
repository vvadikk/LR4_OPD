from flask import Flask, render_template, request
import computation
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/', methods=['post', 'get'])
def form():
    k = True
    if request.method == 'POST':
        f = str(request.form.get('f'))
        x = str(request.form.get('x'))
        e = str(request.form.get("e"))
        degOrRad = str(request.form.get('degOrRad'))
    try:
        float(x)
        l = True
    except ValueError:
        l = False
    if not(l):
        result = "Argument must be a number"
    else:
        x = float(x)
        if degOrRad == "deg":
            deg = True
        elif degOrRad == "rad":
            deg = False
        else:
            result = "Choose: deg or rad"
            k = False
        if k:
            if e.isdigit():
                e = int(e)
                m = True
            else:
                result = "Precision must be a number"
                m = False
            if m:
                if f == "sin":
                    result = computation.sine(x, e, deg)
                elif f == "cos":
                    result = computation.cosine(x, e, deg)
                elif f == "tan":
                    result = computation.tangent(x, e, deg)
                elif f == "cot":
                    result = computation.cotangent(x, e, deg)
                elif f == "sec":
                    result = computation.secant(x, e, deg)
                elif f == "csc":
                    result = computation.cosecant(x, e , deg)
                else:
                    result = "No such function"
    return render_template('index.html', ans=result)
if __name__ == '__main__':
    app.run()
