from django.shortcuts import render
from django.http import JsonResponse
from .forms import elementosForm
from django.views import View
# Create your views here.

#FBV
def elementosPage(request):
	form = elementosForm()
	return render(request, "elementos.html", {"elementosForm": form})

def postelementos(request):
	if request.method == "POST":
		form = elementosForm(request.POST)
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)

#CBV
class elementosAjax(View):
	form_class = elementosForm
	template_name = "elementos_cbv.html"

	def get(self, *args, **kwargs):
		form = self.form_class()
		return render(self.request, self.template_name, {"elementosForm": form})

	def post(self, *args, **kwargs):
		if self.request.method == "POST" and self.request.is_ajax():
			form = self.form_class(self.request.POST)
			form.save()
			return JsonResponse({"success":True}, status=200)
		return JsonResponse({"success":False}, status=400)