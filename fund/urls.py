from django.urls import path

from fund.views import (
    GetFundViewset,
    RetrieveFundViewset,
    CreateFundView,
    UpdateFundView,
    DeleteFundView
)

app_name = "fund"

urlpatterns = [
    path("fund_l/", GetFundViewset.as_view({'get': 'list'}), name="fund_l"),
    path("fund_r/<int:id>", RetrieveFundViewset.as_view({'get': 'retrieve'}), name="fund_r"),
    path("fund_c/", view=CreateFundView.as_view(), name="fund_c"),
    path("fund_u/<int:id>", view=UpdateFundView.as_view(), name="fund_u"),
    path("fund_d/<int:id>", view=DeleteFundView.as_view(), name="fund_d"),
]
