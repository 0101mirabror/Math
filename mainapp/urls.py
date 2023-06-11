from django.urls import path


"Local"
from .views import (calc_formula, success_page, check_post, 
                    calculation_method,get_history, homepage_view,
                    HomePageView, CalculationResultView, AboutPageView,
                    coor_3, coor_4, differ3_4, AnswersDeleteView,
                    calc_inaccuracy
                    )
urlpatterns = [
    path("", homepage_view, name="home"),
    path("about/", AboutPageView.as_view(), name="about" ),
    path("calculate2/", CalculationResultView.as_view(), name="profil" ),
    path("history/", get_history, name="history" ),
    path('history/<int:pk>', AnswersDeleteView.as_view(), name="delete"),
    path('3/', coor_3, name="coor3"),
    path('4/', coor_4, name="coor4"),
    path('inaccuracy', calc_inaccuracy, name="inaccuracy"),
    path('differ/', differ3_4, name="differ"),
    path("calculate/", calc_formula, name="calculate" ),
    path("success-page/", success_page, name="success-page" ),
    path("check/", check_post, name="check" ),
    path("calculation/", calculation_method, name="calculation" ),
    path("calculate2/", CalculationResultView.as_view(), name="calculation2" ),
]