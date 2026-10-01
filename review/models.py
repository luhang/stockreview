from django.db import models


class Review(models.Model):
    ACTION_CHOICES = [
        ('buy', '买入'),
        ('sell', '卖出'),
        ('hold', '持有'),
    ]

    stock_code = models.CharField('股票代码', max_length=20)
    trade_date = models.DateField('交易日期')
    action = models.CharField('操作', max_length=10, choices=ACTION_CHOICES)
    price = models.DecimalField('价格', max_digits=10, decimal_places=3)
    note = models.TextField('备注', blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        ordering = ['-trade_date', '-created_at']
        verbose_name = '复盘记录'
        verbose_name_plural = '复盘记录'

    def __str__(self):
        return f'{self.stock_code} {self.trade_date} {self.get_action_display()}'


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('图片', upload_to='reviews/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '复盘图片'
        verbose_name_plural = '复盘图片'

    def __str__(self):
        return f'Image for {self.review.stock_code}'
