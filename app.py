import os
from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/trending', methods=['GET'])
def get_trending_topics():
    # Initialize pytrends and set the region for trends
    pytrends = TrendReq(hl='en-US', tz=360)
    trending_searches_df = pytrends.trending_searches(pn='united_states')
    trending_topics = trending_searches_df[0].tolist()
    
    return jsonify(trending_topics=trending_topics)

if __name__ == '__main__':
    # Confirm the app is running and using the specified port
    print("Starting the app on the specified port.")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
