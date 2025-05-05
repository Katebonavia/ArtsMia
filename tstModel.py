from model.model import Model

mymodel = Model()

mymodel.buildGraph()
print("N nodi:", mymodel.getNumNodes(), "; N Edges:", mymodel.getNumEdges())

mymodel.getInfoConnessa(1234)