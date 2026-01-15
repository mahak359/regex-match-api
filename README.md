# regex-match-api
Regex Matcher API (Regex101 Clone)
A lightweight Flask-based REST API that clones the core functionality of regex101.com. This backend service processes a regular expression against a provided test string and returns detailed information about every match found.

🚀 Features
Pattern Matching: Uses Python's re engine to find all occurrences of a pattern.

Positional Data: Returns exact start and end indices for every match (useful for frontend highlighting).

Capture Groups: Automatically identifies and extracts sub-groups defined within parentheses.

Error Handling: Gracefully catches and reports invalid regular expression syntax (e.g., unbalanced parentheses) without crashing the server.

🛠️ Technologies Used
Python 3.x

Flask (Web Framework)

Regex (Python built-in re module)

📥 Installation
Clone or Download this project folder.

Navigate to the project directory:

Bash

cd regex-matcher-backend
Install Dependencies:

Bash

pip install flask
🏃 How to Run
Start the Flask development server:

Bash

python app.py
The server will start running at http://127.0.0.1:5000.

📡 API Documentation
Match Regex
Performs a search on the test string using the provided regular expression.

URL: /api/match

Method: POST

Header: Content-Type: application/json

Request Body Example:

JSON

{
  "regex": "(\\d+)-([a-z]+)",
  "test_string": "Order 123-abc and Order 456-def"
}
Successful Response (200 OK):

JSON

{
  "match_count": 2,
  "matches": [
    {
      "match": "123-abc",
      "start": 6,
      "end": 13,
      "groups": ["123", "abc"]
    },
    {
      "match": "456-def",
      "start": 23,
      "end": 30,
      "groups": ["456", "def"]
    }
  ],
  "status": "success"
}
🧪 Testing with Postman
Set the request type to POST.

Enter the URL: http://127.0.0.1:5000/api/match.

Go to the Body tab, select raw, and choose JSON.

Paste your test JSON and click Send.
