from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, get_expenses_by_date, category_summary

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('expenses-by-date/', get_expenses_by_date),
    path('category-summary/', category_summary),
]
