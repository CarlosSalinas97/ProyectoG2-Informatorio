from django.core.exceptions import PermissionDenied

class PermisosMixin:
	rol = None
	def dispatch(self,request,*args,**kwargs):
		if check(request,self.rol):
			return super().dispatch(request,*args,**kwargs)
		else:
			raise PermissionDenied


def check(request,rol):
	u = request.user
	if u.es_duenio and rol == 'duenio':
		return True
	elif not (u.es_duenio) and rol == 'cliente':
		return True
	else:
		return False