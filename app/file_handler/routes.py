from app.file_handler import bp


@bp.route("/")
def index():
    return "Heloo"
