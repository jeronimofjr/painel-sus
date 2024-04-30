from flask import request, jsonify, json
from atendimentos import atendimentos_bp
from models.atendimentos import Atendimentos
from database.database import db


json.provider.DefaultJSONProvider.ensure_ascii = False

@atendimentos_bp.route("/atendimentos", methods=['GET'])
def get_atendimentos():
    try:
        filters = {"data_atendimento" : request.args.get('data_atendimento'),
                    "condicao_saude" : request.args.get('condicao_saude'),
                    "UNIDADE" : request.args.get('unidade')}
        
        filters = {key:value for key, value in filters.items() if value is not None}

        atendimentos = db.query(Atendimentos).filter_by(**filters).all()
        atendimentos_list = [atendimento.to_dict() for atendimento in atendimentos]
        if atendimentos_list is not None:
            return jsonify({"atendimentos" : atendimentos_list})
        return {"atendimentos" : []}
    except Exception as e:
        return {"message" : "Falha na busca dos dados"}