from django.shortcuts import get_object_or_404, render
#if importing from the same file you can use commas between imports
from .models import Cohort, Student

# Create your views here.
def index(request):
    # print("request", request)
    cohort_list = Cohort.objects.all()
    # print("from db", cohort_list)
    #cohort_list inside dictionary is what we'll be iterating over, 'cohort_list'
    context = { 'cohort_list': cohort_list }
    # print("context", context)
    return render(request, 'cohorts/index.html', context)

#this cohort id is passed through url/id
def detail(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk = cohort_id)
    #sql version
    #select * from cohort c
    #where c.id = cohort_id
    #where cohort_id from student is equal to cohort_id from cohort
    student_list = Student.objects.filter(cohort_id = cohort_id)
    #sql version
    #select * from cohort c
    #join student s on c.id = s.cohort_id
    context = { 'cohort': cohort, 'student_list': student_list }
    return render(request, 'cohorts/detail.html', context)