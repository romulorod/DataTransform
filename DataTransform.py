# -*- coding: utf-8 -*-
import tabula
import pandas as pd
from tabula.io import build_options

pdf_file = './Padrão_TISS_Componente_Organizacional_202103.pdf'
tabela_1 = tabula.read_pdf(pdf_file, pages='79')
quadro_30 = tabela_1[0]
quadro_30.to_csv('new2.csv',encoding='utf-8-sig', index=False)
# tabula.convert_into(pdf_file, 'Quadro_30.csv', pages=79)
# print(quadro_30)
# build_options
# quadro_31 = tabula.read_pdf(pdf_file, multiple_tables = True, pages='79-84')
# print(quadro_31[1:7])