from flask import Blueprint

atendimentos_bp = Blueprint('atendimentos', __name__)

from atendimentos import routes