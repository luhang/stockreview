from django.contrib import admin
from .models import Review, ReviewImage


class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 0


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['stock_code', 'trade_date', 'action', 'price', 'created_at']
    list_filter = ['action', 'trade_date']
    search_fields = ['stock_code', 'note']
    inlines = [ReviewImageInline]


@admin.register(ReviewImage)
class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ['review', 'created_at']
