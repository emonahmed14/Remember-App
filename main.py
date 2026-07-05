from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout


class RememberApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        screen = MDScreen()
        layout = FloatLayout()

        toolbar = MDTopAppBar(
            title="Remember",
            pos_hint={"top": 1},
            elevation=0,
        )

        center = AnchorLayout(
            anchor_x="center",
            anchor_y="center"
        )

        label = MDLabel(
            text="No notes yet.",
            halign="center",
            theme_text_color="Hint",
            font_style="H5",
        )

        center.add_widget(label)

        fab = MDFloatingActionButton(
            icon="plus",
            md_bg_color=self.theme_cls.primary_color,
            pos_hint={"right": 0.95, "y": 0.04},
            elevation=0,
        )

        layout.add_widget(toolbar)
        layout.add_widget(center)
        layout.add_widget(fab)

        screen.add_widget(layout)
        return screen


RememberApp().run()
