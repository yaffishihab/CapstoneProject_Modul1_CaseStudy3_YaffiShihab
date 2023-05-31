
stocksObat = [
    {
        'code':'Ci23',
        'nama_obat':'Citirizine',
        'stocks':'30',
        'satuan':'Strip',
        'ED':'Dec 2023',
        'pemakaian':'Obat Dalam'
    },
    {
        'code':'Ra23', 
        'nama_obat':'Ranitidine',
        'stocks':'25',
        'satuan':'Box',
        'ED':'August 2023',
        'pemakaian':'Obat Dalam'
    },
    {
        'code':'Ti23',
        'nama_obat':'Timol',
        'stocks':'20',
        'satuan':'Supp',
        'ED':'Sep 2023',
        'pemakaian':'Obat Luar'
    }
]

def menampilkanDaftarObat() :
    print('\nDaftar Obat\n')
    print('Index\t| Code Barang \t| Nama Obat \t| Stocks\t| Satuan\t| Expired Date\t| Pemakaian')
    for i in range(len(stocksObat)) :
        print('{}\t| {}\t\t| {}  \t| {}\t\t| {}\t\t| {}\t| {}'.format(i,
                                                                stocksObat[i]['code'],
                                                                stocksObat[i]['nama_obat'],
                                                                stocksObat[i]['stocks'],
                                                                stocksObat[i]['satuan'],
                                                                stocksObat[i]['ED'],
                                                                stocksObat[i]['pemakaian']))


def menambahObat() :
    codeBarang = input ('Masukkan Code Barang : ')
    namaObat = input('Masukkan Nama Obat : ')
    stockObat = int(input('Masukkan Stock Obat : '))
    satuan = input('Masukkan Nama Satuan : ')
    expDate = input('Masukkan Expired Date : ')
    pemakaian = input('Masukkan Jenis Pemakaian : ')
    stocksObat.append({
            'code': codeBarang,
            'nama_obat': namaObat,
            'stocks': stockObat,
            'satuan': satuan,
            'ED': expDate,
            'pemakaian': pemakaian 
    })
    menampilkanDaftarObat()

def menghapusObat() :
    menampilkanDaftarObat()
    indexObat = int(input('Masukkan index obat yang ingin dihapus : '))
    del stocksObat[indexObat]
    menampilkanDaftarObat()

def revisiDaftarStocks() :
    
    def updateCodeObat() :
        menampilkanDaftarObat()
        code = input('Masukkan Code Barang: ')
        newCode = input('Revisi Code Obat: ')

        for Obat in stocksObat:
            print(Obat)
            if (Obat['code']==code):
                Obat['code']=newCode
            break
        menampilkanDaftarObat()


    def updateNamaObat() :
        menampilkanDaftarObat()
        code = input('Masukkan Code Barang: ')
        newName = input('Revisi Nama Obat: ')

        for Obat in stocksObat:
            print(Obat)
            if (Obat['code']==code):
                Obat['nama_obat']=newName
            break
        menampilkanDaftarObat()
   

    def updateJumlahStock() :
        menampilkanDaftarObat()
        code = input('Masukkan Code Barang: ')
        newStocks = input('Revisi Jumlah Obat: ')

        for Obat in stocksObat:
            print(Obat)
            if (Obat['code']==code):
                Obat['stocks']=newStocks
            break
        menampilkanDaftarObat()
   

    def updateJenisSatuan() :
        menampilkanDaftarObat()
        code = input('Masukkan Code Barang: ')
        newSatuan = input('Revisi Satuan Obat: ')

        for Obat in stocksObat:
            print(Obat)
            if (Obat['code']==code):
                Obat['satuan']=newSatuan
            break
        menampilkanDaftarObat()


    def updateED() :
        menampilkanDaftarObat()
        code = input('Masukkan Code Barang: ')
        newDate = input('Revisi ED Obat (Month/Year): ')

        for Obat in stocksObat:
            print(Obat)
            if (Obat['code']==code):
                Obat['ED']=newDate
            break
        menampilkanDaftarObat()
 

    def updateJenisPemakaian() :
        menampilkanDaftarObat()
        code = input('Masukkan Code Barang: ')
        newJenis = input('Revisi Jenis Pemakaian Obat: ')

        for Obat in stocksObat:
            print(Obat)
            if (Obat['code']==code):
                Obat['pemakaian']=newJenis
            break
        menampilkanDaftarObat()

    while True :
        updateStock = input('''
            Revisi Daftar Stock

            Daftar Pilihan:
            1. Update Code Obat
            2. Update Nama Obat
            3. Update Jumlah Stock
            4. Update Jenis Satuan
            5. Update Tgl Expired
            6. Update Jenis Pemakaian
            7. Done

            Masukkan angka pada daftar pilihan : ''')
        
        if(updateStock == '1') :
            updateCodeObat()
        elif(updateStock == '2') :
            updateNamaObat()
        elif(updateStock == '3') :
            updateJumlahStock()
        elif(updateStock == '4') :
            updateJenisSatuan()
        elif(updateStock == '5') :
            updateED()
        elif(updateStock == '6') :
            updateJenisPemakaian()
        elif(updateStock == '7') :
            break
        
    

while True :
    pilihanMenu = input('''
        Selamat Datang di Pasar Buah

        List Menu :
        1. Menampilkan Daftar Obat
        2. Menambah Stock Obat
        3. Menghapus Stock Obat
        4. Revisi Daftar Stocks
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDaftarObat()
    elif(pilihanMenu == '2') :
        menambahObat()
    elif(pilihanMenu == '3') :
        menghapusObat()
    elif(pilihanMenu == '4') :
        revisiDaftarStocks()
    elif(pilihanMenu == '5') :
        break
    
