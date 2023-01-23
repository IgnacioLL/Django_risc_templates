from django.shortcuts import render
from django.http import JsonResponse
from .forms import PrescriptorForm
from django.views import View
# Create your views here.

#FBV
def prescriptorPage(request):
	form = PrescriptorForm()
	return render(request, "prescriptor.html", {"PrescriptorForm": form})

def postPrescriptor(request):
	if request.method == "POST":
		form = PrescriptorForm(request.POST)
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)

#CBV
class PrescriptorAjax(View):
	form_class = PrescriptorForm
	template_name = "prescriptor_cbv.html"

	def get(self, *args, **kwargs):
		form = self.form_class()
		return render(self.request, self.template_name, {"prescriptorForm": form})

	def post(self, *args, **kwargs):
		if self.request.method == "POST" and self.request.is_ajax():
			form = self.form_class(self.request.POST)
			form.save()
			return JsonResponse({"success":True}, status=200)
		return JsonResponse({"success":False}, status=400)