from model.model import Model

mymodel = Model()

mymodel.buildGraph()
print("N nodes:", mymodel.getNumNodes(),";N edges:", mymodel.getNumEdges())
mymodel.getInfoConnessa(1234)
