from django.shortcuts import render
from django.http import JsonResponse
from .forms import EncargoForm
from django.views import View
# Create your views here.

#FBV
def encargoPage(request):
	form = EncargoForm()
	return render(request, "encargo.html", {"EncargoForm": form})

def postEncargo(request):
	if request.method == "POST":
		form = EncargoForm(request.POST)
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)

#CBV
class EncargoAjax(View):
	form_class = EncargoForm
	template_name = "encargo_cbv.html"

	def get(self, *args, **kwargs):
		form = self.form_class()
		return render(self.request, self.template_name, {"EncargoForm": form})

	def post(self, *args, **kwargs):
		if self.request.method == "POST" and self.request.is_ajax():
			form = self.form_class(self.request.POST)
			form.save()
			return JsonResponse({"success":True}, status=200)
		return JsonResponse({"success":False}, status=400)