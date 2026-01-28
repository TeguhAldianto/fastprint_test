from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm

# 1. READ (Hanya status 'bisa dijual')
def product_list(request):
    # Filter khusus status 'bisa dijual' (sesuaikan string dengan data di DB)
    products = Produk.objects.filter(status__nama_status__icontains='bisa dijual')
    return render(request, 'produk_app/index.html', {'products': products})

# 2. CREATE
def product_add(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProdukForm()
    return render(request, 'produk_app/form.html', {'form': form, 'title': 'Tambah Produk'})

# 3. UPDATE
def product_edit(request, pk):
    product = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProdukForm(instance=product)
    return render(request, 'produk_app/form.html', {'form': form, 'title': 'Edit Produk'})

# 4. DELETE
def product_delete(request, pk):
    product = get_object_or_404(Produk, pk=pk)
    product.delete()
    return redirect('product_list')