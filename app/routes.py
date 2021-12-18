from app.controllers import ArchiveController, RouteController
from app import app


archive_controller = ArchiveController()
route_controller = RouteController()

@app.route('/')
@app.route('/index')
@app.route('/main')
@app.route('/home')
@app.route('/current_exhibition')
def index():
    return route_controller.index()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return route_controller.login()

@app.errorhandler(404)
def resource_not_found(err):
    return route_controller.err404()


@app.route('/curators')
def curators():
    return route_controller.curators()