from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Atendimentos(Base):
    __tablename__ = "atendimentos"

    
    ID = Column(Integer, primary_key=True)
    Nome = Column(String)
    Nascimento = Column(String)
    CNS = Column(String)
    CPF = Column(String)
    UNIDADE = Column(String)
    data_atendimento = Column(Date)
    condicao_saude = Column(String)
    
    def to_dict(self):
        return {
            "id" : self.ID, 
            "nome" : self.Nome,
            "nascimento" : self.Nascimento,
            "unidade" : self.UNIDADE,
            "data_atendimento" : self.data_atendimento,
            "condicao_saude" : self.condicao_saude
        }

