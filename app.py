from flask import Flask, render_template
from datetime import date, datetime

app = Flask(__name__)

@app.route('/')
def index():
    wedding_date = date(2003, 5, 10)
    today = date.today()
    
    # Calculate total time
    years = today.year - wedding_date.year - ((today.month, today.day) < (wedding_date.month, wedding_date.day))
    
    # Calculate next anniversary
    next_anniversary_year = today.year if (today.month, today.day) < (wedding_date.month, wedding_date.day) else today.year + 1
    next_anniversary = date(next_anniversary_year, wedding_date.month, wedding_date.day)
    days_until = (next_anniversary - today).days

    return render_template('index.html', 
                           years=years, 
                           days_until=days_until, 
                           wedding_date=wedding_date.strftime("%B %d, %Y"))

if __name__ == '__main__':
    app.run(debug=True)
