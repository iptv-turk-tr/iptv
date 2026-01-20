# 🚀 GitHub Pages Manual Setup Guide

## GitHub Pages'i Enable Etme Adımları

### 1️⃣ Repository Settings'e Git
```
https://github.com/iptv-turk-tr/iptv/settings/pages
```

### 2️⃣ Pages Bölümüne Git
- Repository'nin sağ üst kısmında **Settings** tab'ı var
- Sol menüdeki **Pages** seçeneğini tıkla

### 3️⃣ Source Ayarla
**Build and deployment** bölümünde:
- **Source** dropdown'unda: `Deploy from a branch` seç
- **Branch** dropdown'unda: `main` seç
- **Folder** dropdown'unda: `/ (root)` seç

### 4️⃣ Save Düğmesine Bas
**Save** düğmesine tıkla

### 5️⃣ Birkaç Dakika Bekle
GitHub Actions otomatik olarak çalışacak ve site yayına alınacak

---

## ✅ Sonuç
Birkaç dakika sonra şu adresler çalışmaya başlayacak:
- 🌐 **Ana Sayfa:** https://iptv-turk-tr.github.io/
- 📺 **Dashboard:** https://iptv-turk-tr.github.io/dashboard.html
- 🔌 **Xtream Portal:** https://iptv-turk-tr.github.io/api/xtream-portal.html
- 📥 **M3U Playlist:** https://iptv-turk-tr.github.io/list.m3u

---

## 📸 Ekran Görüntüleri ile Talimatlar

```
1. Repository Settings → Pages sayfasında:
   ┌─────────────────────────────────────────┐
   │ Build and deployment                    │
   │                                         │
   │ Source: [Deploy from a branch] ▼       │
   │ Branch: [main] ▼                        │
   │ Folder: [/ (root)] ▼                    │
   │                                         │
   │ [Save] Düğmesine Tıkla                 │
   └─────────────────────────────────────────┘
```

---

## 🔍 Durum Kontrol Etme

Settings → Pages sayfasında şu mesajı göreceksin:
```
✅ Your site is published at https://iptv-turk-tr.github.io/
```

Veya Actions tab'ında çalışan workflow'u görebilirsin.

---

## ⚡ Hızlı Link
Bu linki tarayıcıya kopyala-yapıştır:
```
https://github.com/iptv-turk-tr/iptv/settings/pages
```

**NOT:** Manuel olarak bu ayarları yapılması lazım. Otomatize şekilde yapılamıyor.
