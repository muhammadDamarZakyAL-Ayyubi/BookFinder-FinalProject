from flask import Flask, render_template, request, send_from_directory, redirect
import requests, os, re
from collections import Counter
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "bookfinder_secret"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "static", "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

GOOGLE_BOOKS_API = "https://www.googleapis.com/books/v1/volumes?q="

# NLTK FIX
nltk_data = ["punkt", "punkt_tab", "stopwords", "vader_lexicon"]
for d in nltk_data:
    try:
        nltk.data.find(d)
    except:
        nltk.download(d)

stop_eng = set(stopwords.words("english"))
stemmer = SnowballStemmer("english")
sia = SentimentIntensityAnalyzer()

def fetch_books(query, max_items=20):
    r = requests.get(GOOGLE_BOOKS_API + query + f"&maxResults={max_items}")
    data = r.json()
    books = []
    for item in data.get("items", []):
        info = item.get("volumeInfo", {})
        books.append({
            "title": info.get("title", "No title"),
            "authors": ", ".join(info.get("authors", ["Unknown"])),
            "desc": info.get("description", ""),
            "thumbnail": info.get("imageLinks", {}).get("thumbnail", ""),
            "rating": info.get("averageRating", "N/A"),
            "url": info.get("infoLink", "#")
        })
    return books

def crawl_wikipedia(topic, paragraphs=6):
    try:
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        r = requests.get(url)
        if r.status_code != 200:
            return ""
        soup = BeautifulSoup(r.text, "html.parser")
        paras = soup.select("#mw-content-text .mw-parser-output > p")
        result = []
        for p in paras:
            t = p.get_text().strip()
            if t:
                result.append(t)
            if len(result) >= paragraphs:
                break
        return "\n".join(result)
    except:
        return ""

def nlp_process(texts):
    full = " ".join(texts).lower()
    tokens = word_tokenize(re.sub(r"[^a-zA-Z\s]", " ", full))
    tokens = [t for t in tokens if len(t) >= 4 and t not in stop_eng]
    stems = [stemmer.stem(t) for t in tokens]
    freq = Counter(stems).most_common(7)

    s = {"pos":0, "neu":0, "neg":0}
    for t in texts:
        v = sia.polarity_scores(t)
        if v["compound"] >= 0.05: s["pos"]+=1
        elif v["compound"] <= -0.05: s["neg"]+=1
        else: s["neu"]+=1

    return freq, s, tokens

def generate_wordcloud(tokens, name):
    if not tokens:
        return None
    wc = WordCloud(width=800, height=400, background_color="white").generate(" ".join(tokens))
    file_path = os.path.join(OUT_DIR, name)
    wc.to_file(file_path)
    return f"outputs/{name}"

@app.route("/", methods=["GET","POST"])
def index():
    books = []
    crawl = ""
    q = ""
    if request.method == "POST":
        q = request.form.get("query")
        do_crawl = request.form.get("do_crawl") == "on"
        books = fetch_books(q)
        if do_crawl:
            crawl = crawl_wikipedia(q)
    return render_template("index.html", books=books, query=q, crawl_text=crawl)

@app.route("/dashboard")
def dashboard():
    books = fetch_books("popular books", 30)
    desc = [b["desc"] for b in books if b["desc"]]
    rate = [str(b["rating"]) for b in books]

    freq, s, tokens = nlp_process(desc)
    wc = generate_wordcloud(tokens, "wordcloud_dashboard.png")
    rdist = dict(Counter(rate))

    return render_template("dashboard.html", common_words=freq, sentiments=s,
                           rating_data=rdist, wordcloud=wc)

@app.route("/otomasi")
def otomasi():
    date = datetime.utcnow().strftime("%Y-%m-%d")
    api = "https://api.open-meteo.com/v1/forecast?latitude=-6.2088&longitude=106.8456&hourly=temperature_2m&timezone=UTC"
    r = requests.get(api).json()

    df = pd.DataFrame({
        "time": r["hourly"]["time"],
        "temp": r["hourly"]["temperature_2m"]
    })

    csv = f"otomasi_{date}.csv"
    png = f"otomasi_{date}.png"

    df.to_csv(os.path.join(OUT_DIR, csv), index=False)

    plt.figure(figsize=(10,4))
    plt.plot(pd.to_datetime(df["time"]), df["temp"])
    plt.title("Suhu Jakarta (Open-Meteo)")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, png))
    plt.close()

    return redirect("/dashboard")

# --- ABOUT PAGE ROUTE ---
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/outputs/<path:file>")
def outputs(file):
    return send_from_directory(OUT_DIR, file)

if __name__ == "__main__":
    app.run(debug=True)

