from flask import Flask
import os
app = Flask(__name__)
@app.route(&#39;/&#39;)
def hello():
build_id = os.getenv(&#39;BUILD_ID&#39;, &#39;Local&#39;)
return f&quot;&lt;h1&gt;Hello from Flask!&lt;/h1&gt;&lt;p&gt;Deployed via Jenkins Webhook. Build
ID: {build_id}&lt;/p&gt;&quot;
if __name__ == &quot;__main__&quot;:
app.run(host=&#39;0.0.0.0&#39;, port=5000)