
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.relativelayout import RelativeLayout

from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner


class HanoiGui(Widget):
    pass


class HanoiGuiApp(App):
    pass


class MainPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.step = 0

    def show_button_pressed(self, widget, shapes):
        self.step = 0
        try:
            shapes.clear_widgets(shapes.children)

        except:
            pass

        self.n = int(widget.text)
        self.A = list(range(self.n, 0, -1))

        self.B, self.C = [], []

        self.show_pole(self.A, self.B, self.C, shapes)
        self.hanoi(self.n, self.A, self.B, self.C, shapes)

    def show_pole(self, A, B, C, shapes):

        self.wiget = RelativeLayout(size_hint=(1, None), height=300*self.n/8)
        step_label = Label(text='Step {}'.format(str(self.step)))

        with self.wiget.canvas:
            w, h = self.width, self.wiget.height
            Color(1, 1, 1)
            line = Line(points=(w/6, 0, w/6, dp(self.n*9)), width=dp(4))
            line = Line(points=(w/2, 0, w/2, dp(self.n*9)), width=dp(4))
            line = Line(points=(w*5/6, 0, w*5/6, dp(self.n*9)), width=dp(4))
            Color(.2, .6, .7)
            Line(points=(0, self.wiget.height-dp(5),
                 self.width, self.wiget.height-dp(5)))
            k = 0
            Color(0, 1, 0)
            for i in A:
                Line(points=(w/6-i*10, k*dp(8), w /
                     6+i*10, k*dp(8)), width=dp(5))
                k += 1
            k = 0
            for i in B:
                Line(points=(w/2-i*10, k*dp(8), w /
                     2+i*10, k*dp(8)), width=dp(5))
                k += 1
            k = 0
            for i in C:
                Line(points=(w*5/6-i*10, k*dp(8), w *
                     5/6+i*10, k*dp(8)), width=dp(5))
                k += 1
        self.wiget.add_widget(step_label)
        shapes.add_widget(self.wiget)

    def hanoi(self, n, P1, P2, P3, shapes):
        """ Move n discs from pole P1 to pole P3. """

        if n == 0:
            return
        self.hanoi(n - 1, P1, P3, P2, shapes)
        if P1:
            P3.append(P1.pop())
            self.step += 1
            self.show_pole(self.A, self.B, self.C, shapes)

        self.hanoi(n - 1, P2, P1, P3, shapes)


if __name__ == '__main__':
    HanoiGuiApp().run()
