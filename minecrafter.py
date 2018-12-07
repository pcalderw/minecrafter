from app import app


raise ValueError('Configuration not filled out')
app.config['registration_secret'] = #Me
app.config['SECRET_KEY'] = #Me

if __name__ == '__main__':
    app.run('0.0.0.0', 5433, debug=True)