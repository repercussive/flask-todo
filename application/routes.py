from application import app

@app.route('/')
def home():
  return "Todo app!"