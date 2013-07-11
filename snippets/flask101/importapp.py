from flask101 import app

@app.route('/special')
def special_feature():
    return 'This only exists if the module ran is importapp.py'

if __name__ == '__main__':
    app.run()
