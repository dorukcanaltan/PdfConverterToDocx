from pdf2docx import Converter

# Kullanıcıdan PDF dosyasının yolunu al
pdf_path = input("Lütfen PDF dosyasının yolunu giriniz: ")
# DOCX dosya adını oluştur
docx_file = pdf_path.replace('.pdf', '') + ".docx"

# Dönüştürücüyü başlat
cv = Converter(pdf_path)
# PDF'i DOCX'e dönüştür
cv.convert(docx_file)
# Dönüştürücüyü kapat
cv.close()

print(f"'{pdf_path}' dosyası başarıyla '{docx_file}' olarak dönüştürüldü.")

cv.close()