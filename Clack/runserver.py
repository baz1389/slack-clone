from flask import Flask, render_template
app = Flask(__name__)

#Settings
app.config['DEBUG'] = True
app.config['PUSHER_CHAT_APP_ID'] = '217208'
app.config['PUSHER_CHAT_APP_KEY'] = '1700d3a26833a9d1a05d'
app.config['PUSHER_CHAT_APP_SECRET'] = '781d2f16c68822c44ef5'

import pusher

pusher_client = pusher.Pusher(
  app_id=app.config['PUSHER_CHAT_APP_ID'],
  key=app.config['PUSHER_CHAT_APP_KEY'],
  secret=app.config['PUSHER_CHAT_APP_SECRET'],
  ssl=True
)

# pusher_client.trigger('test_channel', 'my_event', {'message': 'hello world'})

@app.route("/")
def index():
    return render_template('index.html');

if __name__ == "__main__":
    app.run()
