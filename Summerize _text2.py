import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Menambahkan stop words tambahan
additional_stop_words = ["python", "language", "programmers", "programming", "code", "development", "developer", "libraries", "applications", "software"]
stop_words = set(stopwords.words("english") + additional_stop_words)

def preprocess_text(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    return " ".join(words)

def generate_summary(text, num_sentences=5):
    sentences = sent_tokenize(text)
    preprocessed_text = preprocess_text(text)

    frequency = nltk.FreqDist(preprocessed_text.split())

    scores = {sentence: sum(frequency[word] for word in word_tokenize(sentence.lower()) if word in frequency)
              for sentence in sentences}

    summary = " ".join([sentence for sentence, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]])

    return summary

text = """
The Python programming language has evolved from a simple utility for automation and prototyping to a major player in modern software development. Python's key advantages include its ease of learning, broad adoption, versatility in application, and continuous improvement.

Python is known for being easy to learn and use, making it an ideal language for both beginners and experienced programmers. Its syntax is readable and straightforward, allowing developers to focus on problem-solving rather than syntactic complexities.

The language is widely adopted and supported, evident in its high rankings on the Tiobe Index and extensive use in GitHub projects. Python runs on various operating systems, and its compatibility with major libraries and API-powered services enhances its usability.

Python serves diverse purposes, from scripting and automation to building professional-quality software, web services, and data science applications. Its applications extend to command-line and GUI applications, data science, machine learning, web services, RESTful APIs, metaprogramming, code generation, and writing glue code.

Despite its strengths, Python has limitations. It is not suitable for system-level programming, creating cross-platform standalone binaries elegantly, or developing mobile-native applications with the simplicity of languages like Swift or Kotlin. Speed is not Python's forte, but ongoing efforts, such as removing the Global Interpreter Lock (GIL), aim to improve performance.

Python's success is attributed to its rich ecosystem of first- and third-party libraries. The standard library provides modules for various programming tasks, while third-party libraries from the Python Package Index (PyPI) showcase its popularity and versatility. Notable libraries include BeautifulSoup, Requests, Flask, Django, NumPy, Pandas, and Matplotlib.

The language's compromises, such as significant whitespace and dynamic typing, are balanced by its benefits. Python's dynamism facilitates high-level code writing, and optional compile-time type hinting addresses typing concerns.

While Python is acknowledged for its slower execution compared to languages like C/C++ or Java, its emphasis on developer time often outweighs machine time considerations. Python's speed of development and programmer comfort make it a preferred choice for many real-world applications, where the trade-off between development speed and execution speed is acceptable.

Ongoing efforts in Python performance optimization, alternative runtimes like PyPy, and projects to remove the GIL indicate the language's commitment to addressing performance concerns.

In conclusion, Python's journey from a gap-filler to a versatile powerhouse is marked by its simplicity, versatility, and continuous evolution, making it a valuable tool in various domains of software development.
"""

summary = generate_summary(text)
print("Original Text:\n", text)
print("\nSummary:\n", summary)
