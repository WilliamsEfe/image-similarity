import time, sys, requests, requests_cache, cv2, numpy, urllib.request as ur
from PIL import Image
from skimage import io
from flask import Flask, render_template, request, jsonify
from flask_httpauth import HTTPTokenAuth
import ssl

# for certificate verfication of https
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)
app.config['FLASK_ENV'] = 'dev'
auth = HTTPTokenAuth(scheme='Bearer')

# instantiating a set of tokens
tokens = {
    "secret-token-1": "leke",
    "secret-token-2": "muath"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)


@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def home():
    if request.method == 'POST':
        # first try to read as file(for local images)
        try:
            image1 = request.files.get('image1', '')
            image1.save('test_image1.png')
            img1 = cv2.imread('test_image1.png', 0)
        # if it fails try it as a web image
        except:
            try:
                img1 = io.imread(request.form['image1'], pilmode='1')
            except TimeoutError:
                return {"message": "Timeout! Connect to stronger network"}                
            except:
                return {"message": "Invalid image path selected"}
        # first try to read as file(for local images)
        try:
            image2 = request.files.get('image2', '')
            image2.save('test_image2.png')

            img2 = cv2.imread('test_image2.png', 0)
        # if it fails try it as a web image
        except:
            try:
                img2 = io.imread(request.form['image2'], pilmode='1')
            except TimeoutError:
                return {"message": "Timeout! Connect to stronger network"}    
            except:
                return {"message": "Invalid image path selected"}
        img1 = cv2.resize(img1, (220, 180))
        img2 = cv2.resize(img2, (220, 180))
        res = cv2.absdiff(img1, img2)
        #--- convert the result to integer type ---
        res = res.astype(numpy.uint8)
        #--- find percentage similarity based on number of pixels that are not zero ---
        percentage = (1 - (numpy.count_nonzero(res))/ res.size) * 100
        answer = str(round(percentage, 2))
        return {"similarity":answer + " %"}


if __name__ == '__main__':
    app.run(debug=True)
