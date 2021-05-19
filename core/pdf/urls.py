from django.urls import path

from core.pdf.views import SaleInvoicePdfView, SecondView

app_name = 'pdf'

urlpatterns = [
    # user
    path('SalePdf/', SaleInvoicePdfView.as_view(), name='SalePdf'),
    path('second/', SecondView.as_view(), name='second'),

]
