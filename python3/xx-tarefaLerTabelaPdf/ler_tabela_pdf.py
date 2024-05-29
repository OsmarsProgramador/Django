import tabula
import pandas as pd

col_areas=[(202.455,3.63,432.135,77.88),(200.475,79.86,430.155,92.73),(201.465,94.71,430.155,256.08),(200.475,258.06,430.155,303.6),(201.465,302.61,432.135,348.15),(199.485,349.14,432.135,365.97),(200.475,366.96,430.155,385.77),(200.475,384.78,431.145,502.59),(199.485,503.58,432.135,522.39),(201.465,521.4,430.155,576.84),(200.475,576.84,432.135,594.66),(200.475,594.66,432.135,618.42),(198.495,617.43,432.135,646.14),(200.475,646.14,430.155,695.64)]

def ler_pdf_padrao(path):
    tabela=pd.DataFrame()
    for col in col_areas:
        col1=tabula.read_pdf(path,pages=1,area=col,stream=True)
        col1=col1[0]
        col1=pd.DataFrame(col1)
        tabela= pd.concat([tabela, col1], ignore_index=False,axis=1)
        
    return tabela


print(ler_pdf_padrao('teste.pdf'))