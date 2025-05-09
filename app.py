from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the ER number and DOB from the form
        er_no = request.form['er_no']
        
        admit_card_url = f'https://bteup.ac.in/ESeva/Student/AdmitCard.aspx?EnrollNumber={er_no}'
        verification_card_url = f'https://bteup.ac.in/ESeva/Student/VerificationCard.aspx?EnrollNumber={er_no}'
        insta_url = "https://www.instagram.com/coderbaba7/"
        youtube = "https://www.youtube.com/@coderbaba7"
        return render_template('index.html', admit_card_url=admit_card_url, verification_card_url=verification_card_url, er_no=er_no,insta_url=insta_url, youtube=youtube)
        
        
    return render_template('index.html', admit_card_url=None, verification_card_url=None, error=None,insta_url=None, youtube=None)

if __name__ == '__main__':
    app.run(debug=True)