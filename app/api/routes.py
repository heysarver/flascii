# app/api/routes.py
from flask import Blueprint, jsonify, request, render_template
import pyfiglet

api = Blueprint('api', __name__)

@api.route('/')
def index():
    fonts = pyfiglet.FigletFont.getFonts()
    return render_template('index.html', fonts=fonts)

@api.route('/api/generate', methods=['POST'])
def generate_ascii():
    data = request.get_json()
    text = data.get('text', '')
    font = data.get('font', 'standard')
    width = data.get('width', 80)
    justify = data.get('justify', 'left')
    
    try:
        figlet = pyfiglet.Figlet(font=font, width=width, justify=justify)
        ascii_art = figlet.renderText(text)
        
        return jsonify({
            'success': True,
            'ascii_art': ascii_art
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
