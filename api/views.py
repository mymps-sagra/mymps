# Create your views here.
from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

from rest.models import Period, Rest
from rest.views import rest_get_queryset_sql
from .serializers import PeriodSerializer, RestSerializer


class PeriodList(generics.ListCreateAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class PeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class RestList(mixins.ListModelMixin, generics.GenericAPIView):
    period = None
    # для работы класса GenericAPIView - по нему определяется модель
    queryset = rest_get_queryset_sql(period)
    #print(queryset.model)
    serializer_class = RestSerializer

    def get(self, request, *args, **kwargs):
        if not "pk" in kwargs:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        pk = kwargs["pk"]
        if not pk == "0":
            try:
                self.period = Period.objects.get(pk=pk)
            except Period.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        self.queryset = rest_get_queryset_sql(self.period)
        return self.list(request, *args, **kwargs)


#EOF