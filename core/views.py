from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from app.models import Actividad, Publicacion
from .forms import ContactForm
from .models import SiteSettings

class HomePageView(TemplateView):
	template_name = "core/index.html"

class InstitucionalPageView(TemplateView):
	template_name = "core/institucional.html"

	def get_context_data(self, **kwargs):
		context['configuracion'] = SiteSettings.objects.all()[:1]
		return context

def InstitucionalPageView(request):
	template_name="core/institucional.html"
	configuracion = SiteSettings.objects.all()[:1]
	context = {'configuracion':configuracion}
	return render(request, template_name, context)

def HomePageView(request):
	template_name="core/index.html"
	actividades = Actividad.objects.all()[:4]
	publicaciones = Publicacion.objects.all()[:3]
	configuracion = SiteSettings.objects.all()[:1]
	context = {'actividades':actividades, 'publicaciones':publicaciones, 'configuracion':configuracion}
	return render(request, template_name, context)

def Contacto(request):
	contact_form = ContactForm
	if request.method == "POST":
		contact_form = ContactForm(data=request.POST)
		if contact_form.is_valid():
			name = request.POST.get('name', '')
			email = request.POST.get('email', '')
			content = request.POST.get('content', '')
			email_body = """\
			    <html>
					<head>
						<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-=1">
						<style type="text/css">
							body {font-family:Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)}
							p {margin-top:0; margin-bottom:0;}
							b {color:rgb(63,63,63); font-family:Arial; font-size:small}
							div{color:rgb(63,63,63); font-family:Arial; font-size:small}
							span{color:rgb(128,128,128); font-family:Verdana; font-size:8pt}
							hr{display:inline-block;}
							.justificar{text-align: justify;text-justify: inter-word;}
						</style>
					</head>
					<body dir="ltr">
						<div id="appendonsend"></div>
							<hr tabindex="-1">
						<div>
							<h2>De: %s</h2>
							<p>Mensaje: %s</p>
							<h5>Email de contacto: %s</h5>
						</div>
						<br>
						<div id="Signature">
							<div>
								<div id="divtagdefaultwrapper" >
									<div align="left"><b>Atentamente,</b></div>
									<div align="left"><hr></div>
									<div align="left"><b>Diego Osvaldo Cruz Torrez</b></div>
									<div align="left"><b>Consultor IT</b></div>
									<div align="left"><b><img class="EmojiInsert" alt="" src=""><br></b></div>
									<div align="left">
										<span><a href="https://twitter.com/diegocruztorrez" target="_blank">
											http://www.doctsystems.com.bo/</a><br>
										</span>
									</div>
									<div align="left">
										<span>Topater esq. German Busch #1074</span><br>
									</div>
									<div align="left">
										<span>Tel.: +591 4 6961620</span>
									</div>
									<span></span>
									<div align="left"><span>Cel.: +591 72900865 - +591 79260250</span></div>
									<span></span>
									<div align="left"><span>Bermejo - Bolivia</span></div>
									<div align="left"><br>
										<div align="left">
											<b><span class="justificar">La informacion contenida en este mensaje esta dirigida unicamente para el uso del(los) destinatarios(s) señalados arriba. Si el lector de este mensaje no es la persona a quien el mismo fue dirigido, se le notifica que cualquier envio,  distribucion o copia de esta comunicacion o cualquier parte de su contenido, estan estrictamente prohibidos. Si usted ha recibido esta comunicacion por error,  por favor devuelvala al remitente inmediatamente y elimine el mensaje original asi como cualquier copia del mismo en su sistema de computacion.  Si usted tiene alguna pregunta en relacion con este mensaje, por favor comuniquese con el remitente. Gracias por su ayuda.
											</span></b>
										</div>
									</div>
								</div>
							</div>
						</div>
					</body>
				</html>
			    """ % (name, content, email)
			email = EmailMessage('A new mail from AFISPOP', email_body, to=['doctsystems@gmail.com', 'd.cruz@outlook.com', 'carolinacosentinoalza@gmail.com'])
			email.content_subtype = "html" # this is the crucial part 
			# email.send()

			try:
				email.send()
				# Todo ok
				return redirect(reverse('core:contacto')+'?ok')
			except:
				# Algo fallo en el envio
				return redirect(reverse('core:contacto')+'?fail')

	return render(request, "core/contact.html", {'form': contact_form})
