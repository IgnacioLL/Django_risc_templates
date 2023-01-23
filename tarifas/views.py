from django.shortcuts import render
from django.http import JsonResponse
from .forms import tarifasForm
from django.views import View
# Create your views here.

#FBV
def tarifasPage(request):
	form = tarifasForm()
	return render(request, "tarifas.html", {"tarifasForm": form})

def posttarifas(request):
	if request.method == "POST":
		form = tarifasForm(request.POST)
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)

#CBV
class tarifasAjax(View):
	form_class = tarifasForm
	template_name = "tarifas_cbv.html"

	def get(self, *args, **kwargs):
		form = self.form_class()
		return render(self.request, self.template_name, {"tarifasForm": form})

	def post(self, *args, **kwargs):
		if self.request.method == "POST" and self.request.is_ajax():
			form = self.form_class(self.request.POST)
			form.save()
			return JsonResponse({"success":True}, status=200)
		return JsonResponse({"success":False}, status=400)