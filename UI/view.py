import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._dd_anno=None
        self._dd_brand=None
        self._dd_retailer=None
        self._btn_top_vendite=None
        self._btn_analizza_vendite=None
        self._txt_result=None

    def read_retailer(self, e):
        self._retailer = e.control.data
    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)
        #ROW1
        self._dd_anno = ft.Dropdown(
            label="anno",
            width=self._page.window_width*1/4,
            hint_text="selziona un filtro per l'anno",
            on_change=self._controller.cambia_anno,
            options=[ft.dropdown.Option("Nessun Filtro")]
        )
        self._dd_brand = ft.Dropdown(
            label="brand",
            width=self._page.window_width*1/4,
            hint_text="selziona un filtro per il brand",
            on_change=self._controller.cambia_brand,
            options=[ft.dropdown.Option("Nessun Filtro")]
        )
        self._dd_retailer = ft.Dropdown(
            label="retailer",
            width=self._page.window_width*1/2,
            hint_text="selziona un filtro per il retailer",
            on_change=self._controller.cambia_retailer,
            options=[ft.dropdown.Option("Nessun Filtro")]
        )
        anni=self._controller.dd_fill_anni()
        for anno in anni:
            self._dd_anno.options.append(ft.dropdown.Option(anno))
        brands = self._controller.dd_fill_brands()
        for brand in brands:
            self._dd_brand.options.append(ft.dropdown.Option(brand))
        retailers = self._controller.dd_fill_retailers()
        for retailer in retailers:
            self._dd_retailer.options.append(ft.dropdown.Option(key= retailer.Retailer_code, text=retailer.Retailer_name, data=retailer, on_click=self.read_retailer))
        row1=ft.Row([self._dd_anno, self._dd_brand, self._dd_retailer],ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.update()
        #ROW 2
        self._btn_top_vendite=ft.ElevatedButton(text="Top Vendite", on_click=self._controller.handle_top_vendite)
        self._btn_analizza_vendite = ft.ElevatedButton(text="Analizza Vendite", on_click=self._controller.handle_analizza_vendite)
        row2=ft.Row([self._btn_top_vendite, self._btn_analizza_vendite],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self._page.update()
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
