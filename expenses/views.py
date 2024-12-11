from django.db import models
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer
from datetime import datetime


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    Base expense viewset.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET'])
def get_expenses_by_date(request):
    """
    Get expenses by a date range.
    """
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    if start_date and end_date:
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            expenses = Expense.objects.filter(user=request.user, date__range=[start_date, end_date])
            serializer = ExpenseSerializer(expenses, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response({"detail": "Invalid date format, please use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail": "Start date and end date are required."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def category_summary(request):
    """
    Get the total expenses per category for a month.
    """
    month = request.query_params.get('month')
    if not month:
        return Response({"detail": "Month is required (YYYY-MM format)"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        expenses = Expense.objects.filter(user=request.user, date__month=int(month.split('-')[1]), date__year=int(month.split('-')[0]))
        category_summary = expenses.values('category').annotate(total_amount=models.Sum('amount'))
        return Response(category_summary)
    except ValueError:
        return Response({"detail": "Invalid month format, please use YYYY-MM"}, status=status.HTTP_400_BAD_REQUEST)
