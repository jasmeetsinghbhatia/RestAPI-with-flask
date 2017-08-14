from flask import Flask, render_template

from routes import init_api_routes
from routes import init_website_routes


# create the Flask application
app = Flask(__name__)

# app.config['SECRET_KEY'] = 'Hello from the secret world of Flask! ;)'

init_api_routes(app)
init_website_routes(app)

#
# Template filters
#
@app.template_filter('senior_candidate')
def senior_candidate(candidates):
    result = []
    for candidate in candidates:
        for experience in candidate['experience']:
            if experience['years'] >= 5:
                result.append({
                    'first_name':candidate['first_name'],
                    'last_name':candidate['last_name'],
                    'years':experience['years'],
                    'domain':experience['domain']
                })
                break

    return result

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
