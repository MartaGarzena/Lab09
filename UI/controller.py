import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI

        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        #self._idMap = None
        #self.fillIDMap()

    def handle_analizza(self, e):
        self._view.txt_result.controls.clear()
        dist = self._view.txt_distanza.value
        if dist is None or dist == "":
            self._view.create_alert("Inserire la distanza")
            return

        self._model.buildGraphPesato()
        self._view.txt_result.controls.append(ft.Text(f"Numero di areoporti, {self._model.getNumNodi()}", color="orange"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di tratte , {self._model.getNumArchi()}",color="orange"))

        archiMaggiori = self._model.getArchiPesoMaggiore(float(dist))
        self._view.txt_result.controls.append(ft.Text(f"Tratte con distanza media percorsa di almeno {dist} miglia sono {len(archiMaggiori)}", color="pink"))
        for a in archiMaggiori:
            self._view.txt_result.controls.append(ft.Text(f"Dall'areoporto {a[0].ID} ({a[0].CITY}) a quello di {a[1].AIRPORT} la distanza media percorsa è {a[2]["weight"]}"))
        #fai cose

        self._view.update_page()

    #def fillIDMap(self):
    #    values = self._model.listAirports
    #    for v in values:
    #        self._idMap[v.getId()] = v
