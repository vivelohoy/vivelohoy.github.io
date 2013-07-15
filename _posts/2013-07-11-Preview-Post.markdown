---
layout: base
title: Theme Preview 
author: Wilberto Morales
author-link: http://www.facebook.com/wilbertotequie
---

##About Flask

Flask 'a microframework for Python' as the documentation says, is an amazing library to work with. Hoy and other news organizations like the Chicago Tribune have seen its ability and are starting to adapt it. Instead of being a complicated framework with complex setup and configurations, Flask can be ran with a mere 10 lines of code.

<code class="file">flask101.py</code>


{% highlight python %}
from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_home():
    return "Welcome to your website."

if __name__ == '__main__':
    app.run()

{% endhighlight %}

<code class="tc">python flask101.py</code>
<code class="note">This is a test</code>
