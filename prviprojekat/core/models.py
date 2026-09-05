from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile

from PIL import Image
from io import BytesIO

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3)]
        )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )
    image = models.ImageField(
        upload_to="product/", 
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])],
        null=True
        )
    amount = models.PositiveIntegerField(default=0)
    promo_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
 
    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.title

    def clean(self):
        if self.promo_price and self.price:
            if self.promo_price > self.price:
                raise ValidationError({"promo_price": "Promo price must be lower then actual price."})

# nije mi bas najjasnije treba da mi se objasni kako prikazuje ovo def str i related name malo blize da se objasni,
# i kako dodaje vise image kad nemamo listu ili nesto slicno
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(
        upload_to="product/", 
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])]
        )

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            max_size = (1920, 1080)
            if img.width > max_size[0] or img.height > max_size[1]:
                img.thumbnail(max_size, Image.LANCZOS)

            buffer = BytesIO()
            img.save(buffer, format="WEBP", quality=80)
            buffer.seek(0)

            self.image.save(f"{self.image.name.split(".")[0]}.webp", ContentFile(buffer.read()), save=False)

        super().save(*args, **kwargs)


    def __str__(self):
        return f"Image for{self.product.title}"

