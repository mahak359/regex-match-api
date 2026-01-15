from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/api/match', methods=['POST'])
def match_regex():
    # 1. Get data from the request
    data = request.get_json()
    
    if not data or 'regex' not in data or 'test_string' not in data:
        return jsonify({"error": "Missing 'regex' or 'test_string' in request body"}), 400

    pattern = data['regex']
    text = data['test_string']
    
    results = []

    try:
        # 2. Perform the matching
        # finditer returns an iterator yielding match objects
        matches = re.finditer(pattern, text)
        
        for match in matches:
            results.append({
                "match": match.group(),      # The full matched string
                "start": match.start(),      # Start index
                "end": match.end(),          # End index
                "groups": match.groups()     # Any capture groups ()
            })

        # 3. Return JSON response
        return jsonify({
            "status": "success",
            "match_count": len(results),
            "matches": results
        })

    except re.error as e:
        # Handle invalid regex patterns
        return jsonify({
            "status": "error",
            "message": f"Invalid Regular Expression: {str(e)}"
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)