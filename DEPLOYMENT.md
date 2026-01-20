#!/usr/bin/env bash
# 🚀 IPTV TURK - GitHub Pages Deployment Kılavuzu

echo "╔════════════════════════════════════════════════════════════╗"
echo "║         🚀 GITHUB PAGES DEPLOYMENT KIZLAVUZU              ║"
echo "║         IPTV TURK - 181 Çalışan Türkiye Kanalları        ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

echo "📋 ADIM 1: Depo Ayarlarına Git"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔗 URL: https://github.com/iptv-turk-tr/iptv/settings/pages"
echo ""
echo "VEYA"
echo ""
echo "1. GitHub'da depoya git:"
echo "   → https://github.com/iptv-turk-tr/iptv"
echo ""
echo "2. Üst menüden 'Settings' tuşuna tıkla"
echo ""
echo "3. Sol menüden 'Pages' seç"
echo ""

echo "📋 ADIM 2: GitHub Pages Yapılandırması"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔧 Source (Kaynak) Bölümünde:"
echo ""
echo "  Deploy Method:"
echo "  ├─ Dropdown: 'Deploy from a branch' ← SEÇ BU"
echo "  │"
echo "  Branch:"
echo "  ├─ Repository: main ✅"
echo "  ├─ Folder: / (root) ✅"
echo "  │"
echo "  └─ 'Save' tuşuna bas"
echo ""

echo "⏳ ADIM 3: Bekle"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "⏱️  Deployment başladı!"
echo "   Sayfayı yenile: F5 veya Ctrl+R"
echo "   "
echo "   ✓ Sarı nokta = Building..."
echo "   ✓ Yeşil nokta = Deployed ✅"
echo "   ✓ Kırmızı X = Error ❌"
echo ""
echo "   Genellikle 1-2 dakika içinde tamamlanır."
echo ""

echo "🌐 ADIM 4: Web Sitesine Erişim"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Deployment tamamlandıktan sonra:"
echo ""
echo "📺 Ana Sayfa:"
echo "   🔗 https://iptv-turk-tr.github.io"
echo ""
echo "📊 Dashboard:"
echo "   🔗 https://iptv-turk-tr.github.io/dashboard.html"
echo ""
echo "🔌 Xtream Portal:"
echo "   🔗 https://iptv-turk-tr.github.io/api/xtream-portal.html"
echo ""

echo "📥 ADIM 5: M3U URL'leri (GitHub Pages Kurmadan Önce De Çalışıyor)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📺 Ana M3U Listesi:"
echo "   🔗 https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/list.m3u"
echo ""
echo "📂 Kategoriler:"
echo "   🔗 https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/ulusal.m3u"
echo "   🔗 https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/spor.m3u"
echo "   🔗 https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/belgesel.m3u"
echo ""

echo "❓ Sorun mu Yaşıyorsun?"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "❌ 'You don't have permission' hatası:"
echo "   → Admin değilsen bu hatayı alamazsın"
echo "   → Repository sahibiyle iletişime geç"
echo ""
echo "❌ Pages bölümü görünmüyor:"
echo "   → Depo Private ise Settings'te yetki kontrol et"
echo "   → Public yapman gerek"
echo ""
echo "❌ Site yüklenmiyor (404):"
echo "   → Sayfayı 5 dakika sonra yenile"
echo "   → Settings > Pages'te status kontrol et"
echo ""

echo "✅ DOSYA KONTROL"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Dosya kontrolü
if [ -f /workspaces/iptv/index.html ]; then
    echo "  ✅ index.html (ana sayfa)"
else
    echo "  ❌ index.html (EKSIK!)"
fi

if [ -f /workspaces/iptv/dashboard.html ]; then
    echo "  ✅ dashboard.html (M3U göstericisi)"
else
    echo "  ❌ dashboard.html (EKSIK!)"
fi

if [ -f /workspaces/iptv/.nojekyll ]; then
    echo "  ✅ .nojekyll (Jekyll devre dışı)"
else
    echo "  ❌ .nojekyll (EKSIK!)"
fi

if [ -f /workspaces/iptv/list.m3u ]; then
    count=$(grep -c "^http" /workspaces/iptv/list.m3u 2>/dev/null || echo "0")
    echo "  ✅ list.m3u ($count kanal)"
else
    echo "  ❌ list.m3u (EKSIK!)"
fi

if [ -d /workspaces/iptv/api ]; then
    echo "  ✅ api/ klasörü (Xtream portal)"
else
    echo "  ❌ api/ klasörü (EKSIK!)"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🚀 GİT! HER ŞEY HAZIR - ADIM 1'İ TAKİP ET!              ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
