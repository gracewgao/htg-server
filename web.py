from flask.ext.api import FlaskAPI
from flask import request, current_app, abort
from functools import wraps

app = FlaskAPI(__name__)
app.config.from_object('settings')


def token_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-API-TOKEN', None) != current_app.config['API_TOKEN']:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


# machine learning endpoints

@app.route('/predict', methods=['POST'])
@token_auth
def predict():
    from engines import content_engine
    item = request.data.get('item')
    num_predictions = request.data.get('num', 10)
    if not item:
        return []
    return content_engine.predict(str(item), num_predictions)


@app.route('/train')
@token_auth
def train():
    from engines import content_engine
    data_url = request.data.get('data-url', None)
    content_engine.train(data_url)
    return {"message": "Success!", "success": 1}


# POST method to create a new return
@app.route('/returns/new', methods=['POST'])
@token_auth
def new():
    return_json = request.get_json(force=True)

    # saves item details
    order_id = return_json['order_id']
    item_id = data.get_item(order_id)

    from engines import content_engine
    matches = content_engine.find_users('sample-user-date.csv', order_id, 10)

    return matches


if __name__ == '__main__':
    app.debug = True
    app.run()
