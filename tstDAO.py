from database.DAO import DAO
from model.model import Model

listObjects = DAO.getAllNodes()
mymodel=Model()
mymodel.getIdMap()

edges = DAO.getAllArchi(mymodel.getIdMap())
print(len(listObjects), len(edges))