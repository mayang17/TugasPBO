# Implementasi kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):# Konstruktor init dengan parameter nama, nim, dan jurusan untuk inisialisasi objek Mahasiswa
        self.nama = nama  # Menyimpan nama mahasiswa ke atribut nama
        self.nim = nim  # Menyimpan NIM mahasiswa ke atribut nim
        self.jurusan = jurusan  # Menyimpan objek jurusan ke atribut jurusan

    def tampilkan_info(self):# Menampilkan informasi tentang mahasiswa
        print("Nama:", self.nama)  # Menampilkan nama mahasiswa
        print("NIM:", self.nim)  # Menampilkan NIM mahasiswa
        if self.jurusan is not None:# Memeriksa apakah atribut jurusan tidak None (tidak kosong)
            print("Jurusan:", self.jurusan.NamaJurusan)  # Menampilkan nama jurusan
        else:
            print("Jurusan: -")  # Menampilkan "-" jika jurusan tidak terdefinisi

# Implementasi kelas Jurusan
class Jurusan:
    def __init__(self, nama_jurusan):# Konstruktor init dengan parameter nama_jurusan.
        self.NamaJurusan = nama_jurusan  # Menyimpan nama jurusan ke atribut NamaJurusan
        self.DaftarMahasiswa = []  # Inisialisasi daftar mahasiswa dengan list kosong

    def tambah_mahasiswa(self, mahasiswa):#metode untuk menambahkan objek mahasiswa ke daftar mahasiswa jurusan.
        self.DaftarMahasiswa.append(mahasiswa)  # Menambahkan objek mahasiswa ke daftar mahasiswa jurusan ini
        mahasiswa.jurusan = self  # Mengatur objek jurusan pada atribut jurusan mahasiswa
        print("------------------")  # Menampilkan pemisah antara setiap mahasiswa yang ditambahkan

    def tampilkan_daftar_mahasiswa(self):# Metode untuk menampilkan daftar mahasiswa dalam jurusan
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)#untuk mencetak judul daftar mahasiswa berdasarkan nama jurusan.
        for mahasiswa in self.DaftarMahasiswa:#kode iterasi melalui daftar mahasiswa dalam objek jurusan saat ini.
            mahasiswa.tampilkan_info()  # Memanggil metode tampilkan_info untuk setiap mahasiswa di daftar
            print("------------------")  # Menampilkan pemisah antara setiap mahasiswa

# Implementasi kelas Universitas
class Universitas:
    def __init__(self, nama_universitas):# Konstruktor init dengan parameter nama_universitas.
        self.NamaUniversitas = nama_universitas  # Menyimpan nama universitas ke atribut NamaUniversitas
        self.DaftarJurusan = []  # Inisialisasi daftar jurusan dengan list kosong

    def tambah_jurusan(self, jurusan):#metode untuk menambahkan jurusan ke dalam daftar jurusan dalam objek universitas.
        self.DaftarJurusan.append(jurusan)  # Menambahkan objek jurusan ke daftar jurusan universitas ini

    def tampilkan_daftar_jurusan(self):#metode untuk menampilkan daftar jurusan dalam objek Universitas.
        print("Daftar Jurusan di", self.NamaUniversitas)# Menampilkan judul daftar jurusan di universitas
        for jurusan in self.DaftarJurusan:# Melakukan iterasi untuk setiap jurusan dalam daftar jurusan
            print("Jurusan:", jurusan.NamaJurusan)  # Menampilkan nama jurusan

# Membuat objek Universitas dengan nama "University XYZ"
universitas = Universitas("University XYZ")

# Membuat objek Jurusan dengan nama-nama jurusan yang diinginkan dan menambahkannya ke dalam objek Universitas
jurusan1 = Jurusan("Teknik Informatika")
jurusan2 = Jurusan("Teknik Sipil")
jurusan3 = Jurusan("Teknik Mesin")
jurusan4 = Jurusan("Teknik Elektro")
jurusan5 = Jurusan("Arsitektur")
jurusan6 = Jurusan("Sistem Informasi")

universitas.tambah_jurusan(jurusan1)
universitas.tambah_jurusan(jurusan2)
universitas.tambah_jurusan(jurusan3)
universitas.tambah_jurusan(jurusan4)
universitas.tambah_jurusan(jurusan5)
universitas.tambah_jurusan(jurusan6)

# Membuat objek Mahasiswa dengan nama sendiri,
# lalu memasukkannya ke dalam Jurusan "Teknik Informatika" di objek Universitas "XYZ University"
mahasiswa = Mahasiswa("Julia Mayang Sari", "G1A022010", jurusan1)
jurusan1.tambah_mahasiswa(mahasiswa)

# Menampilkan daftar jurusan yang ada di Universitas "University XYZ"
universitas.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar di Jurusan "Teknik Informatika" di Universitas "University XYZ"
jurusan1.tampilkan_daftar_mahasiswa()
