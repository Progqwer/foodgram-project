from django.contrib import admin

from .models import (FavoriteRecipe, Ingredient, Recipe, RecipeIngredient,
                     ShoppingCart, Tag)


class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'name', 'author', 'text', 'cooking_time',
        'added_in_favorites', 'pub_date']
    search_fields = ['name', 'author', 'cooking_time', 'text']
    readonly_fields = ['added_in_favorites']
    list_filter = ['name', 'pub_date', 'author', 'tags']
    empty_value_display = '-empty-'
    inlines = [RecipeIngredientsInline]

    def added_in_favorites(self, obj):
        return obj.favorites.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'color', 'slug']
    search_fields = ['name', 'color', 'slug']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'measurement_unit']
    search_fields = ['name', 'measurement_unit']
    list_filter = ['name', 'measurement_unit']
    inlines = [RecipeIngredientsInline]


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ['pk', 'recipe', 'ingredient', 'amount']
    search_fields = ['recipe', 'ingredient']
    list_filter = ['recipe', 'ingredient']


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'recipe']
    search_fields = ['user', 'recipe']
    list_filter = ['user', 'recipe']


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'recipe']
    search_fields = ['user', 'recipe']
    list_filter = ['user', 'recipe']
