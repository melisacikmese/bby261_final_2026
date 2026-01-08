import requests
from bs4 import BeautifulSoup
from rommenu import MenuSistemi

def etkinlikleri_listele():
    print("\nHacettepe Üniversitesi Etkinlikleri:\n")
    url = "https://etkinlikler.hacettepe.edu.tr/tr/aylik"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Etkinlik kartlarını bul
        etkinlikler = soup.find_all("div", class_="haber_card")
        if not etkinlikler:
            print("Etkinlik bulunamadı.")
            return

        for idx, etkinlik in enumerate(etkinlikler, 1):
            baslik = etkinlik.find("div", class_="haber_card_baslik").get_text(strip=True) if etkinlik.find("div", class_="haber_card_baslik") else "Başlık yok"
            ozet = etkinlik.find("div", class_="haber_ozet").get_text(strip=True) if etkinlik.find("div", class_="haber_ozet") else "Özet yok"
            link_tag = etkinlik.find("div", class_="haber_ayrinti_but").a if etkinlik.find("div", class_="haber_ayrinti_but") else None
            link = f"https://etkinlikler.hacettepe.edu.tr{link_tag['href']}" if link_tag else "Link yok"
            tarih_kategori = etkinlik.find("div", class_="haber_alt").get_text(strip=True) if etkinlik.find("div", class_="haber_alt") else "Tarih/Kategori yok"
            
            print(f"{idx}. {baslik}\n   Özet: {ozet}\n   Link: {link}\n   {tarih_kategori}\n")

    except Exception as e:
        print("Etkinlikler çekilirken hata oluştu:", e)

def haberleri_listele():
    print("\nHacettepe Üniversitesi Haberleri:\n")
    url = "https://gazete.hacettepe.edu.tr/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        haberler = soup.find_all("div", class_="slide_txt")
        if not haberler:
            print("Haber bulunamadı.")
            return

        for idx, haber in enumerate(haberler, 1):
            baslik = haber.find("div", class_="slide_baslik").get_text(strip=True) if haber.find("div", class_="slide_baslik") else "Başlık yok"
            ozet = haber.find("div", class_="slide_ozet").get_text(strip=True) if haber.find("div", class_="slide_ozet") else "Özet yok"
            link = haber.find("div", class_="slide_devam").a['href'] if haber.find("div", class_="slide_devam") and haber.find("div", class_="slide_devam").a else "Link yok"
            print(f"{idx}. {baslik}\n   Özet: {ozet}\n   Link: {link}\n")

    except Exception as e:
        print("Haberler çekilirken hata oluştu:", e)

# ----------------- Program Başlat -----------------
def main():
    program_adi = "Hacettepe Bilgi Uygulaması"
    MenuSistemi.karsilama(program_adi)

    menu_map = {
        "Etkinlikleri listele": etkinlikleri_listele,
        "Haberleri listele": haberleri_listele
    }

    MenuSistemi.menuyuCalistir(menu_map)

if __name__ == "__main__":
    main()
