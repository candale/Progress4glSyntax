import sublime_plugin

class StatusBarFunctionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		region = view.sel()[0]
		functionRegs = view.find_by_selector('entity.name.function.Progress4gl')
		for r in reversed(functionRegs):
			if r.a < region.a:
				txt = view.substr(r)
				name = txt.split(" ")[1]
				if ":" in name:
					name = name.replace(":", "")
					
				final_txt = "Procedure %s" % name
				view.set_status('procedure', final_txt)
				return
		view.erase_status('procedure')