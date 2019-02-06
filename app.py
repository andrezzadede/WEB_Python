'''

Dessa forma é comm orientação objetos 

from bottle import Bottle, route, run

app = Bottle()

@app.route('/') # Deve interpretar um determinado caminho, endereço que vai no navegador
def index():
    return '<h1>Hellooo WORLD</h1>'


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
'''


'''
@route('/') # Deve interpretar um determinado caminho, endereço que vai no navegador
@route('/user/<nome>')
def index(nome='Annie'):
    return '<center><h1>Bonjour ' + nome + '</h1></center>'

@route('/python')
def python():
    return '<h1>Curso de Python</h1>'

# imagine que vc tem um site com varios artigos

@route('/artigo/<id>')
def artigo(id):
    return '<h1>Você está lendo o artigo ' + id + '</h1>'

#No caso de uma pagina ter um id e um nome de arquivo

@route('/pagina/<id>/<nome>')
def pagina(id, nome):
    return '<h1> Você está vendo a pagina ' + id + ' com o nome ' + nome
'''

from bottle import route, run
from bottle import request, template
from bottle import static_file, get
from bottle import error

# Static routes
#usadas para serem colocados arquivos com versoes, em css, js, img, fonts
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

''' LOGIN '''

@route('/login') # @get('/login')
def login():
    return template('login')
    
def check_login(username, password):
    d = {'marcos':'python', 'joao':'java', 'pedro':'go'}
    if username in d.keys() and d[username] == password:
        return True
    return False

@route('/login', method='POST') # @post('/login')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('verificacao_login', sucesso=check_login(username, password), nome=username)
    
@error(404)
def error404(error):
    return template('pagina404')


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)

#Quando coloca em produção o debug precisa ficar false, para que os erros da aplicação não fiquem expostos aos usuarios