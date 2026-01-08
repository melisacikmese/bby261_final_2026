import requests
from bs4 import BeautifulSoup
from rommenu import MenuSistemi

def etkinlikleri_listele():
    print("\nEtkinlikler")
    print("https://etkinlikler.hacettepe.edu.tr/\n")

def haberleri_listele():
    print("\nHacettepe Üniversitesi Haberleri:\n")
    url = "https://gazete.hacettepe.edu.tr/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Slider içindeki haber başlıkları
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
