from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import cgi

form="""
<form method="post">
	<label> Day
		<input name="d" type="text" value="%(D)s"> 
	</label>
	<label> Month
		<input name="m" type="text" value="%(M)s"> 
	</label>
	<label> Year
		<input name="y" type="text" value="%(Y)s"> 
	</label> 
	<br>
	<div style="color:red">
	%(error)s		
	</div>
	<input type="submit" value="Go!!">
</form>
"""
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
month_abbvs = dict((m[:3].lower(),m) for m in months)	
          
def valid_month(month):
	if month:
		short_month = month[:3].lower()
		return month_abbvs.get(short_month)

def valid_day(day):
	if day and day.isdigit():
		day=int(day)
		if day>0 and day<=31:
			return day

def valid_year(year):
	if year and year.isdigit():
		year=int(year)
		if year<2022 and year>1900:
			return year

def escape_html(s):
	return cgi.escape(s, quote= True)

# Main starts here...

class MainPage(webapp.RequestHandler):
	def write_form(self, error = "", day="", month="", year=""):
		self.response.out.write(form %{"error":error,
						"D":escape_html(day),
						"M":escape_html(month),
						"Y":escape_html(year)})

	def get(self):
        	#self.response.headers['Content-Type'] = 'text/plain'
        	self.write_form()
		#self.response.out.write(self.request)


	def post(self):
		user_day = self.request.get('d')
		user_month = self.request.get('m')
		user_year = self.request.get('y')

		day = valid_day(user_day)
		month = valid_month(user_month)
		year = valid_year(user_year)
		
		if not(day and month and year):
			self.write_form("That is wrong Bitch !!!", user_day, user_month, user_year)
		else:
			self.redirect("/thanks")
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.out.write("awesome!!")

class ThanksHandler(webapp.RequestHandler):
    def get(self):
        #q=self.request.get("q")
        self.response.out.write("Awesome !!!")
	

application = webapp.WSGIApplication(
                                     	[('/', MainPage),('/thanks',ThanksHandler) ],
					debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
