import django_tables2 as tables
from .models import Courses

class CourseTable(tables.Table): 
    class Meta:
        model = Courses
        fields = ("subject", "crse", "crstitle", "hoursperwkinclclass", "challenge")
        attrs = {'id': 'courseTable'}
        row_attrs = {
        	'draggable':True, 'ondragstart':'drag(event, this)'
        }

class RegisteredTable(tables.Table):
	class Meta:
			model = Courses			
			fields = ("subject", "crse", "crstitle", "hoursperwkinclclass", "challenge")


		