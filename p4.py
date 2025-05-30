import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load English model
nlp = spacy.load("en_core_web_sm")

# ✅ Add the spacytextblob component correctly (MUST be before calling `nlp(text)`)
if "spacytextblob" not in nlp.pipe_names:
    nlp.add_pipe("spacytextblob")

def analyze_sentiment_spacy(text):
    doc = nlp(text)
    polarity = doc._.polarity  # This will now work
    if polarity > 0:
        return f"Positive ☺ (score: {polarity:.2f})"
    elif polarity < 0:
        return f"Negative 😞 (score: {polarity:.2f})"
    else:
        return f"Neutral 😐 (score: {polarity:.2f})"

def analyze_input():
    while True:
        text = input("\nEnter a sentence (or type 'exit' to quit):\n> ")
        if text.lower() == "exit":
            break
        print(f"\nspaCy Sentiment: {analyze_sentiment_spacy(text)}")

if __name__ == "__main__":
    analyze_input()
