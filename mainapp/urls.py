from django.urls import path


"Local"
from .views import (calc_formula, success_page, check_post, 
                    calculation_method,
                    HomePageView, CalculationResultView)
urlpatterns = [
    path("calculate1/", calc_formula, name="calculate" ),
    path("success-page/", success_page, name="success-page" ),
    path("check/", check_post, name="check" ),
    path("home/", HomePageView.as_view(), name="home" ),
    path("calculation/", calculation_method, name="home" ),
    path("calculate2/", CalculationResultView.as_view(), name="calculate" )
]