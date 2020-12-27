from flask import Blueprint


errors = Blueprint('erorrs', __name__)

from app.errors import handlers
