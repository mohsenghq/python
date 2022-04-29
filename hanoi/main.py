
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.uix.label import Label
from random import random


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
        self.colors = []
        for _ in range(10):
            self.colors.append(
                [round(random(), 2), round(random(), 2), round(random(), 2)])

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
        step_label = Label(
            text='[color=ff0]Step {}[/color]'.format(str(self.step)), markup=True)
        with self.wiget.canvas:
            w = self.width
            Color(1, 1, 1)
            Rectangle(pos=(w/6-5, -5), size=(dp(10), self.n*15))
            Rectangle(pos=(w/2-5, -5), size=(dp(10), self.n*15))
            Rectangle(pos=(w*5/6-5, -5), size=(dp(10), self.n*15))
            Color(.2, .6, .7)
            Line(points=(0, self.wiget.height-dp(5),
                 self.width, self.wiget.height-dp(5)))
            k = 0

            for i in A:
                Color(self.colors[i][0], self.colors[i][1], self.colors[i][2])
                Line(points=(w/6-i*10, k*dp(10), w /
                     6+i*10, k*dp(10)), width=dp(5))
                k += 1
            k = 0
            for i in B:
                Color(self.colors[i][0], self.colors[i][1], self.colors[i][2])
                Line(points=(w/2-i*10, k*dp(10), w /
                     2+i*10, k*dp(10)), width=dp(5))
                k += 1
            k = 0
            for i in C:
                Color(self.colors[i][0], self.colors[i][1], self.colors[i][2])
                Line(points=(w*5/6-i*10, k*dp(10), w *
                     5/6+i*10, k*dp(10)), width=dp(5))
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
