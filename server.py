import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path

app = Flask(__name__)

# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
features = np.array(features)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']

        # Simpan Query
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)

        # Batas Nilai
        per = np.linalg.norm(1.0)
        
        # Pencarian
        query = fe.extract(img)
        dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features
        ids = np.argsort(dists)[:20]  # Top 20 
        scores = [(dists[id], img_paths[id]) for id in ids]
        idf = np.argsort(dists)[:1] # Top 1
        
        if dists[idf] < per: # Bandingkan Top 1 ke Batas Nilai
            ket = "Benar"
            return render_template('index.html',
                               query_path=uploaded_img_path,
                               scores=scores,
                               ket=ket)


        else:
            ket = "Bukan"
            return render_template('index.html',
                               query_path=uploaded_img_path,
                               ket=ket)
            
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run("127.0.0.1")
