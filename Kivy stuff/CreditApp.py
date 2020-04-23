#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:30:25 2019

@author: austinmccarson
"""

import kivy
from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.recycleview import RecycleView
#from kivy.base import runTouchApp
from kivy.lang import Builder
#from functools import partial
#from kivy.uix.textinput import TextInput

kvWidget = """
MyWidget: 
    orientation: 'vertical'
    canvas:
        Color:
            rgb: (255,0,0)
        Rectangle:
            size: self.size
            pos: self.pos
"""

class MyWidget(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class CanvasApp(App):
    def build(self):
        return Builder.load_string(kvWidget)

CanvasApp().run()


# =============================================================================
# class KivyApp(App):
# 
#     def build(self):
#         self.box = BoxLayout(orientation = 'horizontal', spacing = 20, pos=(0,550))
#         self.txt = TextInput(hint_text = "Write here", size_hint = (.5,.1))
#         
#         self.btn = Button(text='Clear all', on_press=self.clearText, size_hint=(.1,.1))
#         
#         self.box.add_widget(self.txt)
#         self.box.add_widget(self.btn)
#         
#         return self.box
#     
#     def clearText(self, instance):
#         self.txt.text = ''
# 
# KivyApp().run()
# =============================================================================

# =============================================================================
# Builder.load_string('''
# <ExampleRV>:
#     viewclass: 'Button'
#     RecycleBoxLayout:
#         size_hint_y: None
#         height: self.minimum_height
#         orientation: 'vertical'
#                     ''')
# =============================================================================
    
# =============================================================================
# root = Builder.load_string(r'''
# ScrollView:
#     Label:
#         text: 'Scrollview Example' *100
#         font_size: 30
#         size_hint_x: 1.0
#         size_hint_y: None
#         text_size: self.width, None
#         height: self.texture_size[1]
#                     ''')
#     
# runTouchApp(root)
# =============================================================================
# =============================================================================
#     
# class ExampleRV(RecycleView):
#     
#     def __init__(self, **kwargs):
#         super(ExampleRV, self).__init__(**kwargs)
#         self.data = [{'text': str(x)} for x in range(20)]
# 
# 
# class KivyApp(App):
#     
# # =============================================================================
# #     def disable(self, instance, *args):
# #         instance.disabled = True
# #         
# #     def update(self, instance, *args):
# #         instance.text = "I am disabled"
# # =============================================================================
#     
#     def build(self):
# # =============================================================================
# #         
# #         mybtn = Button(text = "Click me to disable", pos = (300, 350), size_hint = (.25, .18))
# #         
# #         mybtn.bind(on_press = partial(self.disable, mybtn))
# #         
# #         mybtn.bind(on_press = partial(self.update, mybtn))
# #         
# # =============================================================================
#         return ExampleRV()
#     
#     
# KivyApp().run()
#     
#     
# =============================================================================
