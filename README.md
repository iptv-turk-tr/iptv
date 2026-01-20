# 📺 IPTV TURK - Türkiye IPTV Kanalları

> **Tamamen Ücretsiz • Açık Kaynak • Hiçbir Reklam • Herkese Açık**

## ⚙️ GITHUB PAGES KURULUMU

**⚠️ MANUEL SETUP GEREKLI - AŞAĞIĐAKI ADIMLAR GEREKLI:**

1. Şu URL'ye git: `https://github.com/iptv-turk-tr/iptv/settings/pages`
2. **Source** bölümünde:
   - Dropdown: `Deploy from a branch` seç
   - **Branch**: `main`
   - **Folder**: `/ (root)`
3. **Save** tuşuna bas

Birkaç dakika sonra site yayına alınacak:
- 🌐 **Web Site**: `https://iptv-turk-tr.github.io`
- 📺 **Dashboard**: `https://iptv-turk-tr.github.io/dashboard.html`

---

## 📥 RAW URLs (Şu Anda Çalışıyor!)

GitHub Pages kurulumundan önce bile, RAW URL'ler anında oynatılabilir:

### Ana M3U Listesi
```
https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/list.m3u
```

### Kategorilere Göre
- Ulusal Kanallar: `https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/ulusal.m3u`
- Yerel Kanallar: `https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/yerel.m3u`
- Spor: `https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/spor.m3u`
- Belgesel: `https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/belgesel.m3u`
- Çocuk: `https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/cocuk.m3u`
- Film: `https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/film.m3u`
- Müzik: `https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/playlists/muzik.m3u`

### Xtream Portal
```
https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/api/xtream-portal.html
```

**Hesaplar:**
- Kullanıcı: `iptv-turk` | Şifre: `iptv2026`
- Kullanıcı: `soylu` | Şifre: `soylu123`

---

[🌐 Web Sitesini Ziyaret Et](https://iptv-turk-tr.github.io)

---

## 🎯 Nedir?

IPTV TURK, Türkiye'nin en popüler TV kanallarının M3U formatında sunulduğu, **tamamen açık kaynak ve ücretsiz** bir IPTV platformudur.

- ✅ **5000+ Kanal** - Ulusal ve yerel tüm kanallar
- ✅ **M3U Format** - VLC, Kodi, Perfect Player ile uyumlu
- ✅ **Ücretsiz** - Hiçbir ücret, hiçbir reklam
- ✅ **Açık Kaynak** - GitHub'da tamamen açık
- ✅ **Eğitim Amaçlı** - Akademik araştırmalar için tasarlanmış

---

## ⚖️ YASAL UYARI

### 🎓 Eğitim Amaçlı Kullanım
Bu platform **yalnızca eğitim ve araştırma amaçlı** kullanılır. **Ticari kullanım kesinlikle YASAKLANMIŞTIR.**

### 📜 Telif Hakkı
- Tüm içerik kendi sahiplerinin telif hakkı altındadır
- Kullanıcılar tüm yasal sorumluluğu taşır
- Platform sahibi hiçbir sorumluluk kabul etmez

### 🔓 Açık Kaynak
- Kod tamamen açık ve incelenebilir
- Herkes geliştirebilir ve iyileştirebilir
- Apache 2.0 License altında yayınlanmıştır

### ⚠️ Sorumluluk Reddi
**Platformu kullanarak, tüm sorumluluğu kabul etmiş sayılırsınız.**

---

## 🚀 Hızlı Başlangıç

### M3U URL
```
https://raw.githubusercontent.com/iptv-turk-tr/iptv/main/list
```

### VLC Media Player
1. VLC'yi indirin: [videolan.org](https://www.videolan.org)
2. **Medya → Açık Ağ Akışı**
3. URL'yi yapıştırın ve **Oynat ▶️**

### Kodi
1. **Eklentiler → PVR İstemcileri**
2. **IPTV Basit İstemci** arayın ve kurun
3. Eklenti ayarlarında URL'yi yapıştırın
4. Kaydet ve yeniden başlat

### Perfect Player
1. **Çalma Listesi Ekle**
2. URL'yi yapıştırın
3. **Tamam ✅**

---

## 📊 İstatistikler

| Metrik | Değer |
|--------|-------|
| **Toplam Kanal** | 5000+ |
| **Ulusal Kanal** | 50+ |
| **Yerel Kanal** | 250+ |

---

## 📁 Dosya Yapısı

```
iptv/
├── README.md          # Dokümantasyon
├── index.html         # Web arayüzü (Türkçe/İngilizce)
├── list               # M3U oynatma listesi
└── .github/           # GitHub konfigürasyonu
```

---

## 📱 Uyumlu Oynatıcılar

- ✅ VLC Media Player
- ✅ Kodi
- ✅ Perfect Player
- ✅ IPTV Smarters
- ✅ Tivimate
- ✅ GSE Smart IPTV
- ✅ Tüm M3U destekli oynatıcılar

---

## 🛠️ Geliştiriciler İçin

### Kanal Ekleme
`list` dosyasını M3U formatında düzenleyebilirsiniz:

```
#EXTINF:-1 tvg-id="ID" tvg-name="KANAL ADI" group-title="KATEGORI","KANAL ADI"
http://stream-url.com/stream
```

### GitHub Pages
Web sitesi otomatik olarak yayınlanır:
- **URL**: `https://iptv-turk-tr.github.io`

---

## 📜 Lisans

**Apache License 2.0**

```
Copyright 2026 - IPTV TURK
Tüm hakları saklıdır | Ticari kullanım yasak
```

---

## 📞 İletişim

- 🐛 **Sorunlar**: [GitHub Issues](https://github.com/iptv-turk-tr/iptv/issues)
- 💬 **Tartışma**: [GitHub Discussions](https://github.com/iptv-turk-tr/iptv/discussions)

---

**Made with ❤️ | Open Source | Free Forever**