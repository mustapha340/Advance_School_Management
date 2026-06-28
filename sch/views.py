from django.shortcuts import render
from .models import Student

# View ya kuonyesha list ya wanafunzi wote
def student_list(request):
    # Kuchukua wanafunzi wote kutoka kwenye database
    students = Student.objects.all()
    
    # Kutuma data kwenye faili la HTML litakalotengenezwa baadae
    return render(request, 'sch/student_list.html', {'students': students})