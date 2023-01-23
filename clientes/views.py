from django.shortcuts import render
from django.http import JsonResponse
from .forms import ClienteForm
from django.views import View
# Create your views here.

#FBV
def clientePage(request):
	form = ClienteForm()
	return render(request, "cliente.html", {"ClienteForm": form})

def postCliente(request):
	if request.method == "POST":
		form = ClienteForm(request.POST)
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)

#CBV
class ClienteAjax(View):
	form_class = ClienteForm
	template_name = "cliente_cbv.html"

	def get(self, *args, **kwargs):
		form = self.form_class()
		return render(self.request, self.template_name, {"ClienteForm": form})

	def post(self, *args, **kwargs):
		if self.request.method == "POST" and self.request.is_ajax():
			form = self.form_class(self.request.POST)
			form.save()
			return JsonResponse({"success":True}, status=200)
		return JsonResponse({"success":False}, status=400)