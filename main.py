from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.label = MDLabel(
            text="Bienvenue sur K-NODI\nMaillage Réseau Hors-Ligne",
            halign="center",
            font_style="H5"
        )
        layout.add_widget(self.label)
        
        self.code_input = MDTextField(
            hint_text="Entrez le code d'activation (ex: ACTIF123)",
            size_hint_x=0.9,
            pos_hint={'center_x': 0.5}
        )
        layout.add_widget(self.code_input)
        
        btn = MDRaisedButton(
            text="Activer le Nœud",
            pos_hint={'center_x': 0.5},
            on_release=self.check_activation
        )
        layout.add_widget(btn)
        
        self.status_label = MDLabel(text="", halign="center")
        layout.add_widget(self.status_label)
        
        self.add_widget(layout)
        
    def check_activation(self, instance):
        code = self.code_input.text.strip()
        if code == "ACTIF123":
            self.status_label.text = "Accès Hors-Ligne Activé - Nœud K-NODI Prêt !"
        else:
            self.status_label.text = "Code Invalide. Veuillez réessayer."

class KNodiApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return MainScreen()

if __name__ == '__main__':
    KNodiApp().run()
