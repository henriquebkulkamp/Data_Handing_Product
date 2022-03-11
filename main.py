import columns, functions

productPattern = 'Smart TV Samsung Crystal UHD TU8000 4K 82, Borda Infinita, Visual Livre de Cabos e Wi-Fi - UN82TU8000GXZD"'
productNamePattern = 'Smart TV Samsung'

def ExtractData():
    product, allPrice = functions.Scraping(productPattern)
    functions.creatingExcel(product, allPrice, productNamePattern)

ExtractData()