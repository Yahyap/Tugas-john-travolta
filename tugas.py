nonlembur = 40
lembur = 12
pengeluaran = 600000

def gajinonlembur(nonlembur):
    hgajinonlembur = nonlembur * 15000
    return hgajinonlembur

def gajilembur(lembur):
    hgajilembur = lembur * 15000 * 1.5
    return hgajilembur

def totalgaji(gajinonlembur, gajilembur):
    htotalgaji = gajinonlembur + gajilembur
    return htotalgaji

def hasiltabungan(totalgaji, pengeluaran):
    hasiltabungan = totalgaji - pengeluaran
    return hasiltabungan

print("Gaji Non Lembur: Rp.", gajinonlembur(nonlembur))
print("Gaji Lembur: Rp.", gajilembur(lembur))
print("Total Gaji: Rp.", totalgaji(gajinonlembur(nonlembur), gajilembur(lembur)))

if (totalgaji(gajinonlembur(nonlembur), gajilembur(lembur)) > pengeluaran):
    print("Bisa menabung")
elif (totalgaji(gajinonlembur(nonlembur), gajilembur(lembur)) == pengeluaran):
    print("Tidak bisa menabung")
else:
    print("Cari tambahan")





