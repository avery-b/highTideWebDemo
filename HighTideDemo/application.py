from flask import Flask, render_template
app = Flask(__name__)

#blob_mapped_dir = "/HighTideDemo/input"

@app.route('/')
def home():
    return render_template('map.html')
if __name__ == '__main__':
    app.run(debug=True)