from django.core.exceptions import ValidationError

from fund.serializers import FundSerializer, FundListSerializer
from fund.models import Fund

from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response


class GetFundViewset(viewsets.ModelViewSet):
    serializer_class = FundListSerializer
    queryset = Fund.objects.all()

class RetrieveFundViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = FundSerializer

    def get_object(self):
        try:
            fund = Fund.objects.get(id=self.kwargs.get("id"))
        except Exception:
            raise ValidationError("Fund Does Not Exist")
        return fund

class CreateFundView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = FundSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        return obj
        
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        fund_obj = self.perform_create(serializer)

        data = request.data.copy()
        data['id'] = fund_obj.id
        response = {
            "data": data,
            "message": "New Fund Created",
        }
        return Response(response, status=status.HTTP_201_CREATED)
    
class UpdateFundView(generics.UpdateAPIView):
    serializer_class = FundSerializer

    def get_object(self):
        try:
            fund = Fund.objects.get(id=self.kwargs.get("id"))
        except Exception:
            raise ValidationError("Fund Does Not Exist")
        return fund


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.serializer_class(
            instance, data=request.data, partial=partial, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        fund_id= kwargs.get("id")
        response = {
                "data": request.data,
                "message":  f"Fund with ID {fund_id} has been successfully updated"
            }
        return Response(response, status=status.HTTP_200_OK)
    
class DeleteFundView(generics.DestroyAPIView):
    serializer_class = FundSerializer

    def get_object(self):
        try:
            fund = Fund.objects.get(id=self.kwargs.get("id"))
        except Exception:
            raise ValidationError("Fund Does Not Exist")
        return fund
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        fund_id = kwargs.get("id")
        response = {
            "message":  f"Fund with ID {fund_id} has been successfully deleted"
        }
        return Response(response, status=status.HTTP_200_OK)
