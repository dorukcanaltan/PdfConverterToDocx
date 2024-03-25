from pdf2docx import Converter

pdf_path = input("Lütfen PDF dosyasının yolunu giriniz: ")

docx_file = pdf_path.replace('.pdf', '') + ".docx"

cv = Converter(pdf_path)

cv.convert(docx_file)

cv.close()

print(f"'{pdf_path}' dosyası başarıyla '{docx_file}' olarak dönüştürüldü.")

cv.close()