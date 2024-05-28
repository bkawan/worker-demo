from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.v1.worker.models import Unit
from apps.v1.worker.serializers import UnitListModelSerializer, VistCreateSerializer
from apps.v1.worker.services import create_visit


class UnitListByWorkerListAPI(ListAPIView):
    serializer_class = UnitListModelSerializer
    queryset = Unit.objects.all()

    """
       Return all units associated with a worker based on their phone number.

       To retrieve units associated with a specific worker, include the 'phone_number' query parameter in the request.
    """

    # todo    need to paginate
    def get_queryset(self):
        """
        Filter units based on the phone number of the associated worker.

        Raises:
            ValidationError: If 'phone_number' is missing from the query parameters.
        """
        qs = super().get_queryset()
        phone_number = self.request.query_params.get('phone_number', '')
        if not phone_number:
            raise ValidationError({'phone_number': 'A phone_number is required as query params'})
        qs = qs.filter(worker__phone_number=phone_number)
        return qs


class VisitCreateAPI(APIView):
    serializer_class = VistCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        phone_number = validated_data.pop('phone_number')
        # check if unit and worker phone number match
        if Unit.objects.filter(pk=validated_data['unit_id'], worker__phone_number=phone_number).exists():
            visit = create_visit(**validated_data)
            return Response(data={
                'pk': visit.id,
                'datetime': visit.datetime
            })
        raise ValidationError({'error': 'Sorry,Unit does not exit with given detail'})
