from flask import Flask, render_template


app = Flask(__name__) 



noticias = [
    {
        "titulo": "Cadelinha assina projeto de lei",
        "texto": "CKASDK K KDSAKSDAKDS KASSDKSA KSADKSAK SAKSADKKSA KASDKSADKSAKKS K EPJFO POJFJDASPOMSFOSFOAO SF AJOPFQWJOFJASFM AL. OASO DOSAFOSAFOASNFSNFSAIAS."
    },
    {
        "titulo": "Musk perde 5 bilhões",
        "texto": "Bobo perdeu"
    },
    {

    }
    ]
#1 rota meusite.com.br/
#2 funcao 

@app.route("/home/")
def index():
    return render_template("index.html", notic=noticias)

#3 rodar nossa aplicacao

if __name__ == "__main__":
    app.run(debug=True)