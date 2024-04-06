from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = 12345

blacklist = {}
whitelist = {}

@app.route('/api/<API_KEY>/blacklist', methods=['GET'])
def getBlacklist(API_KEY):
    if API_KEY == API_KEY:
        return jsonify({'blacklist': blacklist}), 200
    else:
        print("Unauthorized request")
        return jsonify({'error': 'Unauthorized'}), 401
    
@app.route('/api/<API_KEY>/blacklist', methods=['POST'])
def postBlacklist(API_KEY):
    if API_KEY == API_KEY:
        data = request.get_json()
        if 'hwid' in data:
            hwid = data['hwid']            
            if 'Hardware Identifiers' not in blacklist:
                blacklist['Hardware Identifiers'] = [hwid]
            else:
                blacklist['Hardware Identifiers'].append(hwid)
            print("Updated blacklist:", blacklist)
            return jsonify({'message': f'Added {hwid} to the blacklist', 'blacklist': blacklist}), 200
        else:
            print("No HWID provided in the request")
            return jsonify({'error': 'No HWID provided', 'blacklist': blacklist}), 400
    else:
        print("Unauthorized request")
        return jsonify({'error': 'Unauthorized', 'blacklist': blacklist}), 401

@app.route('/api/<API_KEY>/whitelist', methods=['GET'])
def getWhitelist(API_KEY):
    if API_KEY == API_KEY:
        return jsonify({'whitelist': whitelist}), 200
    else:
            print("Unauthorized request")
            return jsonify({'error': 'Unauthorized'}), 401
    
@app.route('/api/<API_KEY>/whitelist', methods=['POST'])
def postWhitelist(API_KEY):
    if API_KEY == API_KEY:
        data = request.get_json()
        if 'hwid' in data:
            hwid = data['hwid']            
            if 'Hardware Identifiers' not in whitelist:
                whitelist['Hardware Identifiers'] = [hwid]
            else:
                whitelist['Hardware Identifiers'].append(hwid)
            print("Updated whitelist:", whitelist)
            return jsonify({'message': f'Added {hwid} to the whitelist', 'whitelist': whitelist}), 200
        else:
            print("No HWID provided in the request")
            return jsonify({'error': 'No HWID provided', 'whitelist': whitelist}), 400
    else:
        print("Unauthorized request")
        return jsonify({'error': 'Unauthorized', 'whitelist': whitelist}), 401


if __name__ == '__main__':
    app.run(debug=True)
