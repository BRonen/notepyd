import PySimpleGUI as sg

sg.theme('DarkAmber')

WIN_W = 100
WIN_H = 25
filename = None

menu_layout = [
               ['File', ['New     ', 'Open', 'Save', 'Save As', '---', 'Exit']],
               ['Tools', []],
               ['Help', ['About', 'Test']]
              ]

layout = [
          [sg.Menu(menu_layout)],
          [sg.Text('> New file <', size=(WIN_W, 1), key='_INFO_')],
          [sg.Multiline(size=(WIN_W, WIN_H), key='_BODY_')]
         ]

class App():
	def __init__(self):
		self.window = sg.Window('Notepad', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True)
		self.window.read(timeout=1)
		self.window['_BODY_'].expand(expand_x=True, expand_y=True)

	def new_file(self):
		self.window['_BODY_'].update(value='')
		self.window['_INFO_'].update(value='> New File <')
		filename = None
		return filename

	def open_file(self):
		try:
 			filename = sg.popup_get_file('Open File', no_window=True)
		except:
			return
		if filename not in (None, '') and not isinstance(filename, tuple):
			with open(filename, 'r') as f:
				self.window['_BODY_'].update(value=f.read())
				self.window['_INFO_'].update(value=filename)
			return filename

	def save_file(self, filename):
		if filename not in (None, ''):
			with open(filename,'w') as f:
				f.write(self.values.get('_BODY_'))
				self.window['_INFO_'].update(value=filename)
		else:
			self.save_file_as()

	def save_file_as(self):
		try:
			filename = sg.popup_get_file('Save File', save_as=True, no_window=True)
		except:
			return
		if filename not in (None, '') and not isinstance(filename, tuple):
			with open(filename,'w') as f:
				f.write(self.values.get('_BODY_'))
				self.window['_INFO_'].update(value=filename)
			return filename

	def about(self):
		sg.PopupQuick('"Just a notepad, use it!" - Me', auto_close=False)
    
	def test(self):
		sg.PopupQuick('"Hello world!" - A bored dev', auto_close=False)
		
	def Start(self):
		while True:
			event, self.values = self.window.read()
    
			print(event)

			if event in (None, 'Exit'):
				break
			if event in ('New     ',):
				filename = self.new_file()
			if event in ('Open',):
				filename = self.open_file()
			if event in ('Save',):
				self.save_file(filename)
			if event in ('Save As',):
				filename = self.save_file_as()
			if event in ('About',):
				self.about()
			if event in ('Test',):
				self.test()

App().Start()
