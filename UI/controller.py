import flet as ft


class Controller:

    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno=None
        self._brand=None
        self._retailer=None

    def cambia_anno(self,e):
        if e.control.value=="Nessun Filtro":
            self._anno = "NULL"
        else:
            self._anno=e.control.value
    def cambia_brand(self,e):
        if e.control.value == "Nessun Filtro":
            self._brand = "NULL"
        else:
            self._brand=e.control.value
    def cambia_retailer(self,e):
        if e.control.value == "Nessun Filtro":
            self._retailers ="NULL"
        else:
            self._retailer=e.control.key
    def handle_top_vendite(self, e):
        self._view.txt_result.clean()
        vendite=self._model.handle_top_vendite(self._anno, self._brand,self._retailer)
        vendite_ordinate= sorted(vendite, key=lambda x: x.Ricavo, reverse=True)
        for i in range (5):
            self._view.txt_result.controls.append(ft.Text(vendite_ordinate[i]))
        self._view.update_page()
    def handle_analizza_vendite(selfself, e):
        pass
    def dd_fill_anni(self):
        return self._model.dd_fill_anni()
    def dd_fill_brands(self):
        return self._model.dd_fill_brands()
    def dd_fill_retailers(self):
        return self._model.dd_fill_retailers()
