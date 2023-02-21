from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		input_value = int(request.form['input-value'])
		max_value = int(request.form['max-value'])
		if input_value > max_value:
			error = 'Input value cannot be greater than maximum value.'
			progress = 0
		else:
			error = None
			progress = input_value * 100 / max_value
	else:
		error = None
		progress = 0

	return render_template('index.html', progress=progress, error=error)



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)