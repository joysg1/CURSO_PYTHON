import fitz 


def dividir_pdf(archivo_pdf, nombre_pagina1, nombre_pagina2):
    documento_pdf = fitz.open(archivo_pdf)
    if len(documento_pdf)<2:
        print("El archivo PDF no tiene suficientes páginas.")
        return 
    pdf_pagina1 = fitz.open()
    pdf_pagina1.insert_pdf(documento_pdf, from_page=0, to_page=0)
    pdf_pagina1.save(nombre_pagina1)
    pdf_pagina2 = fitz.open()
    pdf_pagina2.insert_pdf(documento_pdf, from_page=2, to_page=2)
    pdf_pagina2.save(nombre_pagina1)
    documento_pdf.close()
    
    
archivo_pdf = "PDF_DIVISION.PDF"
nombre_pagina1 = "01" +archivo_pdf
nombre_pagina2 = "02" +archivo_pdf

dividir_pdf(archivo_pdf, nombre_pagina1, nombre_pagina2)


