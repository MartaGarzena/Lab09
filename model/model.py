import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        from database.DAO import DAO
        self._listFlights = DAO.getAllFlights()
        self._listAirports = DAO.getAllAirport()
        self._idMapAreoporti = {}
        for a in self._listAirports:
            self._idMapAreoporti[a.ID] = a
        self._grafo = nx.Graph()

    @property
    def listFlights(self):
        return self._listFlights

    @property
    def listAirports(self):
        return self._listAirports

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def buildGraph(self):
        self._grafo.add_nodes_from(self._idMapAreoporti.keys())
        self.addEdges()

    def addEdges(self):
        allEdges = self._listFlights
        for volo in allEdges:
            u = volo.ORIGIN_AIRPORT_ID
            v = volo.DESTINATION_AIRPORT_ID
            self._grafo.add_edge(u, v)

    def buildGraphPesato(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._listAirports)
        self.addEdgesPesatiV2()

    def addEdgesPesatiV2(self):
        self._grafo.clear_edges()
        allEdgesPesati = DAO.getAllEdgesPesati()

        for e in allEdgesPesati:
            self._grafo.add_edge(
                self._idMapAreoporti[e[0]],
                self._idMapAreoporti[e[1]],
                weight=e[2]
            )

    def getArchiPesoMaggiore(self, distMin):
        edges = self._grafo.edges(data=True)
        res = []
        for e in edges:
            if e[2]["weight"] >= distMin:
                res.append(e)

        # Ordina la lista in ordine decrescente rispetto al peso
        res.sort(key=lambda x: x[2]["weight"], reverse=False)

        return res
