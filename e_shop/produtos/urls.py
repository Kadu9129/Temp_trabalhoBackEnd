
# from django.urls import path
# from .views import (
#     ProdutoListView, ProdutoCreateView,
#     ProdutoUpdateView, ProdutoDeleteView
# )

# urlpatterns = [
#     path('', ProdutoListView.as_view(), name='listar_produtos'),
#     path('adicionar/', ProdutoCreateView.as_view(), name='adicionar_produto'),
#     path('editar/<int:pk>/', ProdutoUpdateView.as_view(), name='editar_produto'),
#     path('remover/<int:pk>/', ProdutoDeleteView.as_view(), name='remover_produto'),
# ]


from django.urls import path
from .views import (
    menu,
    ProdutoListView, ProdutoCreateView,
    ProdutoUpdateView, ProdutoDeleteView,
    LoginViewSimple
)

urlpatterns = [
    path('', menu, name='menu'), 
    path('login/', LoginViewSimple.as_view(), name='login'),
    path('produtos/', ProdutoListView.as_view(), name='listar_produtos'),
    path('adicionar/', ProdutoCreateView.as_view(), name='adicionar_produto'),
    path('editar/<int:pk>/', ProdutoUpdateView.as_view(), name='editar_produto'),
    path('remover/<int:pk>/', ProdutoDeleteView.as_view(), name='remover_produto'),
]