from django.urls import path


"Local"
from .views import (calc_formula, success_page, check_post, 
                    calculation_method,get_history,
                    HomePageView, CalculationResultView, AboutPageView)
urlpatterns = [
    path("", HomePageView.as_view(), name="home" ),
    path("about/", AboutPageView.as_view(), name="about" ),
    path("history/", get_history, name="history" ),
    path("calculate1/", calc_formula, name="calculate" ),
    path("success-page/", success_page, name="success-page" ),
    path("check/", check_post, name="check" ),
    path("calculation/", calculation_method, name="calculation" ),
    path("calculate2/", CalculationResultView.as_view(), name="calculation2" )
]