import webapp2

form="""
<form action="/form">
	<input name="q" placeholder="Name">
	<input type="submit" >
</form>
"""

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/HTML'
      self.response.write(form)


class FormHandler(webapp2.RequestHandler):
  def get(self):
      #self.response.headers['Content-Type'] = 'text/HTML'
      q = self.request.get("q")
	  self.response.write(q)
	  
app = webapp2.WSGIApplication([('/', MainPage),
								('/form', FormHandler)],debug=True)