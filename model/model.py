import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMap ={}
        for v in self._nodes:
            self._idMap[v.object_id] = v

    def buildGraph(self):
        #metodo che crea il grafo
        nodes = DAO.getAllNodes()
        self._graph.add_nodes_from(nodes)
        self.addAllEdges()

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def addEdgesV1(self):
        for u in self._nodes:
            for v in self._nodes:
                peso = DAO.getPeso(u,v)
                if(peso!=None):
                    self._graph.add_edge(u,v,weight=peso)

    def getIdMap(self):
        return self._idMap

    def addAllEdges(self):
        allEdges = DAO.getAllArchi(self._idMap)
        for e in allEdges:
            self._graph.add_edge(e.o1, e.o2, weight=e.peso)

    def hasNode(self,idInput):
        return idInput in self._idMap #vado a verificare che faccia parte del dizionario che ho creato (e quindi del grafo)

    def getObjectFromId(self, id):
        return self._idMap[id]

    def getInfoConnessa(self,idInput):
        """
        identifica la componente connessa che contiene idInput e ne restituisce la dimensione
        """
        source = self._idMap[idInput] #l'oggetto ArtObject che devo analizzare
        #devo trovare la componente connessa
        #modo1: conto i successori, esplorazione depthFirst
        succ = nx.dfs_successors(self._graph, source).values()
        res = []
        for s in succ:
            res.extend(s) #prendo i values del dizionario e faccio l'extend, quindi se la riga è una
            # lista mi conta tutti i valori della lista
        print("Modo 1 di size connessa: ", len(res))

        # modo2: conto i predecessori, esplorazione depthFirst
        pred = nx.dfs_predecessors(self._graph, source)
        print("Modo 2 di size connessa: ", len(pred.values()))

        #modo3: conto i nodi dell'albero di visita !!CONVIENE USARE QUESTO!!
        dfsTree= nx.dfs_tree(self._graph, source)
        print("Modo 3 di size connessa: ", len(dfsTree.nodes()))#qui viene già contato il source, mentre nei predecessori
                                                                #successori no

        #modo4: uso il metodo nodes connected components di networkx
        conn= nx.node_connected_component(self._graph, source)
        print("Modo 4 di size connessa: ", len(conn))
        return len(conn)
