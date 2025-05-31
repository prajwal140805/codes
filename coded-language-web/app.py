from flask import Flask, render_template, request
from encode_logic import encode_sentence
from decode_logic import decode_sentence

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    input_text = ""
    action = ""
    
    if request.method == 'POST':
        action = request.form.get('action')
        input_text = request.form.get('sentence', '')
        
        if action == 'encode' and input_text:
            result = encode_sentence(input_text)
        elif action == 'decode' and input_text:
            result = decode_sentence(input_text)
    
    return render_template('index.html', 
                          result=result, 
                          input_text=input_text, 
                          action=action)

if __name__ == '__main__':
    app.run(debug=True)