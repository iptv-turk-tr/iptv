#!/usr/bin/env python3
"""
IPTV TURK - Xtream Codes API Server
Gerçek çalışan Xtream Codes protokolü
"""

from flask import Flask, request, jsonify, Response
import json
from datetime import datetime
import base64

app = Flask(__name__)

# Xtream Codes Credentials
CREDENTIALS = {
    "iptv-turk": "iptv2026",
    "soylu": "soylu123"
}

# Channels Data
CHANNELS = [
    {"num": 1, "name": "TRT 1 4K+", "stream_type": "live", "stream_id": 2838, "category_id": 1, "logo": "https://via.placeholder.com/300x300?text=TRT+1", "epg_channel_id": "TRT1.tr"},
    {"num": 2, "name": "ATV 4K+", "stream_type": "live", "stream_id": 3054, "category_id": 1, "logo": "https://via.placeholder.com/300x300?text=ATV", "epg_channel_id": "ATV.tr"},
    {"num": 3, "name": "SHOW TV 4K+", "stream_type": "live", "stream_id": 2874, "category_id": 1, "logo": "https://via.placeholder.com/300x300?text=SHOW+TV", "epg_channel_id": "ShowTV.tr"},
    {"num": 4, "name": "BRTV Karadeniz", "stream_type": "live", "stream_id": 143912, "category_id": 2, "logo": "https://via.placeholder.com/300x300?text=BRTV", "epg_channel_id": ""},
]

CATEGORIES = [
    {"category_id": 1, "category_name": "Ulusal Kanallar"},
    {"category_id": 2, "category_name": "Yerel Kanallar"},
    {"category_id": 3, "category_name": "Spor"},
    {"category_id": 4, "category_name": "Belgesel"},
    {"category_id": 5, "category_name": "Çocuk"},
    {"category_id": 6, "category_name": "Film"},
    {"category_id": 7, "category_name": "Müzik"},
]

def check_auth():
    """Authentication kontrolü"""
    auth = request.args.get('auth') or request.form.get('auth')
    username = request.args.get('username') or request.form.get('username')
    password = request.args.get('password') or request.form.get('password')
    
    if not auth and username and password:
        if username not in CREDENTIALS or CREDENTIALS[username] != password:
            return None
        return {"username": username, "status": "Active"}
    
    return None

# ==================== API ENDPOINTS ====================

@app.route('/')
def index():
    return jsonify({"status": "online", "api": "IPTV TURK Xtream Codes API"})

# USER INFO
@app.route('/get_live_categories.php')
@app.route('/player_api.php')
def player_api():
    """Xtream Codes Player API - Categories"""
    action = request.args.get('action')
    
    if action == 'get_live_categories':
        return jsonify(CATEGORIES)
    
    if action == 'get_live_streams':
        cat_id = request.args.get('category_id')
        if cat_id:
            return jsonify([ch for ch in CHANNELS if ch['category_id'] == int(cat_id)])
        return jsonify(CHANNELS)
    
    if action == 'get_series_categories':
        return jsonify([])
    
    if action == 'get_movie_categories':
        return jsonify([])
    
    if action == 'get_iptv_live_categories':
        return jsonify(CATEGORIES)
    
    return jsonify({"error": "Invalid action"})

@app.route('/player_api.php', methods=['GET', 'POST'])
def get_live_categories():
    """Get Live Categories"""
    action = request.args.get('action') or request.form.get('action')
    
    if action == 'get_live_categories':
        return jsonify(CATEGORIES)
    elif action == 'get_live_streams':
        cat_id = request.args.get('category_id') or request.form.get('category_id')
        if cat_id:
            streams = [ch for ch in CHANNELS if ch['category_id'] == int(cat_id)]
        else:
            streams = CHANNELS
        return jsonify(streams)
    
    return jsonify({"error": "Unknown action"})

@app.route('/get_user_info.php')
def get_user_info():
    """Get User Information"""
    username = request.args.get('username')
    password = request.args.get('password')
    
    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401
    
    if username not in CREDENTIALS or CREDENTIALS[username] != password:
        return jsonify({"error": "Invalid credentials"}), 401
    
    return jsonify({
        "username": username,
        "password": password,
        "auth": 1,
        "status": "Active",
        "exp_date": 0,
        "is_trial": 0,
        "active_cons": "1",
        "created_at": 1609459200,
        "max_connections": 10,
        "allowed_output_formats": ["ts", "m3u8"]
    })

# STREAM URLs
@app.route('/get_live_stream.php')
def get_live_stream():
    """Get Live Stream URL"""
    username = request.args.get('username')
    password = request.args.get('password')
    stream_id = request.args.get('stream_id')
    
    if not username or not password or not stream_id:
        return jsonify({"error": "Missing parameters"}), 400
    
    if username not in CREDENTIALS or CREDENTIALS[username] != password:
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Stream URL'sini döndür
    stream_url = f"http://iptv.darktv.eu:80/Cigdem/c3WPPeRm/{stream_id}"
    
    return jsonify({
        "stream_id": stream_id,
        "username": username,
        "url": stream_url,
        "status": "online"
    })

# M3U PLAYLIST (Standart Format)
@app.route('/get_m3u_playlist.php')
def get_m3u_playlist():
    """Get M3U Playlist"""
    username = request.args.get('username')
    password = request.args.get('password')
    output = request.args.get('output', 'm3u8')
    
    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401
    
    if username not in CREDENTIALS or CREDENTIALS[username] != password:
        return jsonify({"error": "Invalid credentials"}), 401
    
    # M3U formatında döndür
    m3u_content = "#EXTM3U\n"
    
    for ch in CHANNELS:
        m3u_content += f"#EXTINF:-1 tvg-id=\"{ch.get('epg_channel_id', '')}\" tvg-name=\"{ch['name']}\" tvg-logo=\"{ch['logo']}\" group-title=\"Category\",{ch['name']}\n"
        m3u_content += f"http://iptv-turk-tr.github.io/api/stream.php?username={username}&password={password}&stream_id={ch['stream_id']}\n"
    
    return Response(m3u_content, mimetype='application/vnd.apple.mpegurl')

# STREAM PROXY
@app.route('/stream.php')
def stream():
    """Stream Proxy"""
    username = request.args.get('username')
    password = request.args.get('password')
    stream_id = request.args.get('stream_id')
    
    if not username or not password or not stream_id:
        return "Missing parameters", 400
    
    if username not in CREDENTIALS or CREDENTIALS[username] != password:
        return "Invalid credentials", 401
    
    # Redirect to actual stream
    return f"http://iptv.darktv.eu:80/Cigdem/c3WPPeRm/{stream_id}"

# Health Check
@app.route('/health')
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
