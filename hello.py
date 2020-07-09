from flask import Flask
from wordcloud import WordCloud
from os import path
import os
from PIL import Image
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'


@app.route('/wordcloud')
def wordcloud():
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    text = open(path.join(d, 'sample.txt')).read()

    alice_mask = np.array(Image.open(path.join(d, 'alice_mask.png')))

    wordcloud = WordCloud(background_color='white', max_words=2000, mask=alice_mask, contour_width=3,
                          contour_color='steelblue').generate(text)
    return wordcloud.to_svg()


if __name__ == '__main__':
    app.run(debug=False)
