from flask import Flask, render_template
from datetime import date, datetime
import pytz  # Import timezone library
from num2words import num2words # Converts to written words


app = Flask(__name__)

@app.route('/')
def index():
    # Define Philippines Timezone
    manila_tz = pytz.timezone('Asia/Manila')
    
    # Get today's date specifically in Manila
    today = datetime.now(manila_tz).date()
    
    wedding_date = date(2003, 5, 10)
    
    # Calculate years
    years = today.year - wedding_date.year - ((today.month, today.day) < (wedding_date.month, wedding_date.day))
    
	# Converts to written words
    numword = num2words(years, ordinal=True))
    
    # Calculate next anniversary
    # If today is the anniversary, the "next" one is next year
    if (today.month, today.day) == (wedding_date.month, wedding_date.day):
        next_anniversary_year = today.year + 1
    elif (today.month, today.day) < (wedding_date.month, wedding_date.day):
        next_anniversary_year = today.year
    else:
        next_anniversary_year = today.year + 1
        
    next_anniversary = date(next_anniversary_year, wedding_date.month, wedding_date.day)
    days_until = (next_anniversary - today).days

    return render_template('index.html', 
                           years=years, 
                           numword=numword,
                           days_until=days_until, 
                           wedding_date=wedding_date.strftime("%B %d, %Y"),
                           today_is_anniversary=(today == date(today.year, 5, 10)))

if __name__ == '__main__':
    app.run(debug=True)
