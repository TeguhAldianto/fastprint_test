from rest_framework import serializers
from .models import Produk

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

    # Validasi harga harus angka (sudah dicover DecimalField, tapi kita pertegas)
    def validate_harga(self, value):
        if value < 0:
            raise serializers.ValidationError("Harga tidak boleh negatif.")
        return value
        
    # Validasi nama (required=True sudah default)