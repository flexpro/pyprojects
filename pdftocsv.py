import tabula

df = tabula.read_pdf("file path.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("file path.pdf", "csvFileName.csv", output_format="csv", pages='all')
print(df)
