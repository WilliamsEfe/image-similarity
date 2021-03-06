# Image similarity calculator API.

This project is a single page flask app that reads local images or online images (URLs), receives authentication, calculates the similarity of a percentage scale (100% for the same image).

## Prerequisites
* flask
* opencv-python
* scikit-image
* numpy 


## Folder tree

- preview.gif --- A gif of results showing the image output.
- README.md --- A file that explains the project's walkaround
- requirements.txt --- Contains dependencies that are required by the project
- script.py --- contains the script that contains the api authentication, ssl handling and  similarity calculator 


## Getting Started

1. Clone the project from git(git clone https://github.com/Leke-Ariyo/image-similarity.git)
2. Go to 'image-similarity' directory.
3. Run `pip install -r requirements.txt` to download dependencies.
4. Run `python script.py` to start up


Open [http://localhost:5000]



## Contribution

1. Make your changes and them make a pull request

## Last updated

14-01-2020


