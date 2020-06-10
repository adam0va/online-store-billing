from rest_framework import status
from rest_framework.views import Response, Request, APIView
from billing_app.models import Billing
from billing_app.serializers import BillingSerializer
from rest_framework.generics import ListCreateAPIView


class BillingList(ListCreateAPIView):
    serializer_class = BillingSerializer

    def get_queryset(self):
        return Billing.objects.all()


class BillingDetail(APIView):
    def get(self, request, uuid):
        try:
            reader = Billing.objects.get(pk=uuid)
        except Billing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BillingSerializer(reader)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, uuid):
        try:
            reader = Billing.objects.get(pk=uuid)
        except Billing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BillingSerializer(instance=reader, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        try:
            reader = Billing.objects.get(uuid=uuid)
        except Billing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        reader.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)