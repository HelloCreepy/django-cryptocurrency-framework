from rest_framework import routers

from cc_framework.rest import views


def register_views(router):
    router.register(r"transactions", views.TransactionViewSet)
    router.register(r"currencies", views.CurrencyViewSet)
    router.register(r"addresses", views.AddressViewSet)
    return router


urlpatterns = register_views(routers.SimpleRouter()).urls
