from rest_framework import serializers

from endpoint.models import Category, Product, Article


class ArticleSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'description', 'price', 'product']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        articles_serializer = ArticleSerializer(queryset, many=True)
        return articles_serializer.data

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'description', 'category', 'active']



class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description', 'active']


class CategoryDetailSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description', 'products']
    # Pour appliquer un filtre sur les produits retournés, en l'occurence ici que les produits actifs
    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        products_serializer = ProductSerializer(queryset, many=True)
        return products_serializer.data



