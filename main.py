from flask import Flask, render_template, jsonify
from wordcloud import WordCloud
from os import path
import os
from PIL import Image
import numpy as np
import xmljson
from xml.etree.ElementTree import fromstring

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


def word_cloud2data_set(word_cloud):
    data = xmljson.BadgerFish().data(fromstring(word_cloud.to_svg()))
    width = data['{http://www.w3.org/2000/svg}svg']['@width']
    height = data['{http://www.w3.org/2000/svg}svg']['@height']
    data = data['{http://www.w3.org/2000/svg}svg']['{http://www.w3.org/2000/svg}text']
    data = map(lambda d: {
        'text': d['$'],
        'font_size': d['@font-size'],
        'style': d['@style'],
        'transform': d['@transform'],
    }, data)
    return {
        'width': width,
        'height': height,
        'words': list(data)
    }


@app.route('/api/wordcloud')
def api_word_cloud():
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    text = open(path.join(d, 'sample.txt')).read()
    alice_mask = np.array(Image.open(path.join(d, 'alice_mask.png')))
    word_cloud = WordCloud(background_color='white', max_words=2000, mask=alice_mask, contour_width=3,
                          contour_color='steelblue').generate(text)
    return jsonify(word_cloud2data_set(word_cloud))


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
