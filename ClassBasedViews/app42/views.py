from django.shortcuts import render,redirect
from django.views.generic import TemplateView,RedirectView
from django.views.generic import View
from django.views.generic import CreateView,DeleteView
from .models import EmployeeModel
from django.views.generic import ListView,DetailView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class ShowIndex(TemplateView):
    template_name = "index.html"


class AddEmployee(SuccessMessageMixin,CreateView):

    template_name = 'employee.html'

    model = EmployeeModel

    fields = '__all__'

    success_url = '/add_employee/'

    success_message = "Employee Data is saved"


class ViewAllEmployee(ListView):

    template_name = 'viewallemployee.html'

    model = EmployeeModel


class ViewEmployee(ListView):

    template_name = 'viewemployee.html'

    model = EmployeeModel

    queryset = EmployeeModel.objects.values('idno','name','photo')


class CompleteView(DetailView):

    template_name = 'completeview.html'

    model = EmployeeModel


class UpdateValue(UpdateView):

    template_name = 'updateview.html'

    model = EmployeeModel

    fields = '__all__'

    success_url = '/view_employee/'


class DeleteValue(DeleteView):

    template_name = 'deletevalue.html'

    model = EmployeeModel

    success_url = '/view_employee/'


class SearchEmployee(View):
    def post(self,request):
        emp_idno = request.POST.get('s1')
        res = EmployeeModel.objects.filter(idno=emp_idno)
        if res:
            return redirect('/completeview/'+emp_idno)
        else:
            return render(request,"notfound.html",{'message':"IDNO Not Available"})