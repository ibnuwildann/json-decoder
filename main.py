from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/decode', methods=['POST'])
def decode_json():
    api_path = request.form.get('api_path')  # Ubah 'api_url' menjadi 'api_path'

    # Ganti URL statis dengan bagian dinamis yang diberikan oleh pengguna
    full_api_url = f'https://api.slingacademy.com/v1/sample-data/photos/{api_path}'

    try:
        response = requests.get(full_api_url)
        
        data = response.json()
        
        return jsonify(data)
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
    

if __name__ == '__main__':
    app.run(debug=True)
