#!/bin/bash
# ✅ IPTV Kanal Doğrulama Scripti
# Tüm M3U dosyalarındaki URL'leri test eder ve çalışmayanları kaldırır

echo "🔍 IPTV Kanalları Doğrulanıyor..."
echo "=================================="

TIMEOUT=3
MAX_WORKERS=10
WORKING_DIR="/tmp/iptv_validate"
mkdir -p "$WORKING_DIR"

test_url() {
    local url=$1
    timeout $TIMEOUT curl -s -I -m $TIMEOUT "$url" 2>/dev/null | head -1 | grep -qE "200|206|301|302"
    return $?
}

export -f test_url
export TIMEOUT

process_m3u_file() {
    local file=$1
    local category=$(basename "$file" .m3u)
    
    echo "📝 $category test ediliyor..."
    
    local working_file="/tmp/iptv_validate/${category}_working.m3u"
    local total=0
    local passed=0
    
    echo "#EXTM3U" > "$working_file"
    
    while IFS= read -r line; do
        if [[ $line == #EXTINF:* ]]; then
            extinf=$line
            read -r url
            total=$((total + 1))
            
            if test_url "$url"; then
                echo "$extinf" >> "$working_file"
                echo "$url" >> "$working_file"
                passed=$((passed + 1))
                # echo "  ✅ ${extinf##*,}"
            else
                # echo "  ❌ ${extinf##*,}"
                :
            fi
        fi
    done < "$file"
    
    cp "$working_file" "$file"
    echo "  ✅ $passed/$total kanal çalışıyor"
    echo ""
}

export -f process_m3u_file

# Tüm M3U dosyalarını işle
for m3u_file in /workspaces/iptv/playlists/*.m3u; do
    process_m3u_file "$m3u_file"
done

# Ana liste oluştur
echo "#EXTM3U" > /workspaces/iptv/list.m3u
cat /workspaces/iptv/playlists/*.m3u | grep -v "^#EXTM3U$" >> /workspaces/iptv/list.m3u

total_channels=$(grep -c "^http" /workspaces/iptv/list.m3u)
echo "=================================================="
echo "✅ Ana Liste: $total_channels çalışan kanal"
echo "=================================================="
