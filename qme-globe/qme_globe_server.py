
"""
Created on Mon Nov 27 15:21:38 2017

@author: User
"""

import web
import json

urls = (
    '/', 'qme_globe_ui'
)

render = web.template.render('ui/')

class qme_globe_ui:
  def GET(self):
    return render.qme_globe_ui()
    

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
    