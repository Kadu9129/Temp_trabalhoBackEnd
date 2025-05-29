
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
    ProdutoUpdateView, ProdutoDeleteView
)

urlpatterns = [
    path('', menu, name='menu'), 
    path('produtos/', ProdutoListView.as_view(), name='listar_produtos'),
    path('adicionar/', ProdutoCreateView.as_view(), name='adicionar_produto'),
    path('editar/<int:pk>/', ProdutoUpdateView.as_view(), name='editar_produto'),
    path('remover/<int:pk>/', ProdutoDeleteView.as_view(), name='remover_produto'),
]