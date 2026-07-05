from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class RememberApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MDLabel(
            text="Remember v0.1\n\nIt works! 🎉",
            halign="center"
        )

RememberApp().run()
