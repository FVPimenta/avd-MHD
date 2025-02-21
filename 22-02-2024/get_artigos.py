
from jjcli import *
from bs4 import BeautifulSoup as bs 

ats=glob("1081-1087/Article.aspx*")
print(ats)

fo=open("saida.txt" , "w", encoding="utf-8") 

def proc_article (html):
    print (len(html)) #Conta os caracteres de cada artigo
    a=bs(html) #Cria uma árvore documental 
    cabecalho=""
    art= a.find("div", id="artigo") #procura

    # EXERCICIO 1- Procurar e extrair as datas, colocando-as no cabeçalho

    obter_data=art.find("span", id="ctl00_ContentPlaceHolder1_LabelInfo").text # obter o span de id ctl00_ContentPlaceHolder1_LabelInfo
    extrair_data=obter_data[:10] # obter os 10 primeiros caracteres que correspondem à data
    cabecalho += f"{extrair_data}\n" # colocar as datas no cabeçalho

    #EXERCICIO 4- Procurar e extrair as imagens, colocando-as no cabeçalho

    obter_slides = art.find("div", {'id':'slides'}) # ir ao div de id slides pois contém todas as imagens que queremos
    if obter_slides is not None: # caso exista div de id slides procurar pelas imagens
        for slide in obter_slides.find_all("div", {'class':'slide'}): # percorrer todos os div class slide pois contém todas as imagens que queremos
            imagem = slide.find('img') # obter a imagem
            cabecalho += f"{imagem['src']}\n" # adicionar imagem ao cabeçalho

    # EXERCICIO 2- Colocar depois do cabeçalho (---) 
    cabecalho += "---\n" # colocar os ---

    for meta in a.find_all("meta"):
        p =meta.get("property")
        if p is None:
            continue
        p.replace("og" , "")
        cabecalho+=f"{p}: {meta.get('content')}\n"
       # print(p, ":" , meta.get("content"))
        
    # EXERCICIO 3 - Função limpeza (remover o "voltar à pagina anterior")
    for div in art.find_all("div", {'class':'voltar'}): # percorrer todos os div class voltar pois contém voltar ao inicio
        div.decompose() # apaga os voltar ao inicio

    print("==========\n", cabecalho , art.get_text(), file =fo)

for file in ats:
    with open (file, encoding="utf-8") as f:
        html=f.read()
    proc_article(html)




