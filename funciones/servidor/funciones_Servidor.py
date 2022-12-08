from flask import render_template
def Error_404(error):
    titulo="404 PAGINA NO ENCONTRADA"
    return render_template('SERVIDOR/404.html',titulo=titulo)
    