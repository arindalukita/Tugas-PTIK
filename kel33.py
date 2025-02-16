import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.title("AI dan Praktik Data Mining")
st.caption("By Kelompok 3")

# Membuat Slider
slider_value = st.slider("Sudah siap belajar? :satisfied:", 0, 100, 0)

# Menampilkan nilai slider
st.write(f"Rate: {slider_value}")

# Memunculkan confetti jika slider mencapai nilai maksimum
if slider_value == 100:
    st.success("Selamat Belajar! 🎉")
    streamlit_js_eval(js_code="confetti();")

st.subheader("Mari mempelajari konsep Big Data, Data Mining, Machine Learning, dan AI (Artificial Intelegent)! :sparkles:")

st.image("https://social-metrics.org/wp-content/uploads/2015/05/Big-Data.jpg")

if st.button("**Data & Big Data**"):
	st.write("Data adalah sekumpulan informasi yang terdiri dari beberapa fakta yang dapat berbentuk angka, kata-kata, atau simbol-simbol tertentu. Ia dapat dikumpulkan lewat proses pencarian ataupun pengamatan menggunakan pendekatan yang tepat berdasarkan sumber-sumber tertentu. Sedangkan, Big data adalah sekumpulan data yang memiliki volume atau ukuran yang sangat besar yang terdiri dari data yang terstruktur (structured), semi-terstruktur (semi structured), dan tidak terstruktur (unstructured) yang dapat berkembang seiring waktu berjalan.")

if st.button("**Artificial Intelligence (AI)**"):
	st.write("Cabang ilmu komputer yang berfokus pada pembuatan sistem yang dapat melakukan tugas-tugas yang biasanya membutuhkan kecerdasan manusia")


st.markdown("### Perbedaan Keuntungan Kecerdasan")
col1, col2 = st.columns (2)
with col1:
    with st.expander("Kecerdasan Buatan"):
        st.markdown(""" 
1. Sifatnya permanen & konsisten
2. Mengandalkan input-input simbolik
3. Pemikirannya terbatas
4. Lebih mudah dipublikasi, disebarkan, dan didokumentasi
5. Harganya murah
6. Pengerjaannya cepat dan lebih baik
""",True)
    with st.expander("Kecerdasan Alami"):
        st.markdown("""
1. Kreatif
2. Mengandalkan pengalaman
3. Pemikirannya luas
""",True)


st.markdown("### Karakteristik Big Data – 5")
st.markdown("""
1. Volume: Merujuk pada jumlah besar data yang dihasilkan atau dikumpulkan oleh suatu sistem atau aplikasi.
2. Velocity: Menunjukkan seberapa cepat data diproduksi, diproses, dan diperbarui.
3. Variety: Mengacu pada beragamnya jenis data yang dapat mencakup teks, gambar, suara, video, dan format data lainnya.
4. Veracity: Berkaitan dengan keandalan dan akurasi data. Data yang tidak akurat dapat mengarah pada kesalahan analisis dan pengambilan keputusan.
5. Value: Menunjukkan sejauh mana data dapat memberikan manfaat atau nilai tambah bagi organisasi.
""", True)

st.subheader("Data & Big Data")
st.video("https://youtu.be/bAyrObl7TYE?si=_PNKGj89MmZIsU0n")

show_text = st.button('Hubungan AI dan Data Mining')
if show_text:
	st.markdown("""
Data Mining sering digunakan sebagai bagian dari AI, terutama dalam machine learning. Teknik data mining digunakan untuk melatih model AI dengan data yang relevan. Sedangkan, AI memungkinkan otomatisasi dalam proses data mining, meningkatkan kecepatan dan akurasi dalam menemukan pola.
Machine Learning adalah jembatan antara AI dan data mining. Algoritma seperti decision trees, random forests, neural networks, dan support vector machines digunakan dalam kedua bidang.
""", True)



st.markdown("### Analisis pada Proses Pembuatan Keputusan")
st.markdown("""
1.	Analisis Deskriptif : Apa yang terjadi
2.	Analisis Diagnostik: Kenapa itu terjadi
3.	Analisis Prediktif: Apa yang akan terjadi
4.	Analisis Perspektif: Apa yang harus saya lakukan
5.	Kecerdasan Buatan: Peran manusia seperti apa yang ingin digantikan
""",True)

if st.button("**Kecerdasan**"):
	st.write("Belajar dari pengalaman dengan menemukan inti dari pemecahan persoalan untuk menghadapi situasi yang membingungkan.")

st.markdown("### Sudut Pandang Kecerdasan yaitu,")
st.markdown("""
1.	Sudut Pandang Kecerdasan: Mampu berbuat seperti apa yang dilakukan manusia
2.	Sudut Pandang Penelitian: Bagaimana computer dapat melakukan sesuatu sebaik yang dikerjakan manusia
3.	Sudut Pandang Bisnis: Kumpulan peralatan powerful dan metodologis dalam menyelesaikan masalah bisnis
4.	Sudut Pandang Pemrograman: Tentang pemrograman simbolik, penyelesaian masalah, dan pencarian
""",True)

st.markdown("## Data Knowledge")
col1, col2 = st.columns (2)
with col1:
    with st.expander("Lihat Gambar 1"):
        st.image("https://brianreynaldo.wordpress.com/wp-content/uploads/2009/12/data-informasi-knowledge.jpg", caption="Gambar 1", use_column_width=True)
with col2:
    with st.expander("Lihat Gambar 2"):
        st.image("https://ih1.redbubble.net/image.1558352901.6705/scarfflat,800x-pad,750x1000,f8f8f8.jpg",caption="Gambar 2", use_column_width=True)


st.markdown("## KONSEP AI")
st.markdown("""
1. Turing Test: Uji coba menentukan sejauh apa kemampuan mesin meniru manusia sehingga sulit ditemukan perbedaan dalam hasil pekerjaannya
2. Pemrosesan Simbolik: Manipulasi aturan logika dan symbol matematis untuk menghasilkan Solusi masalah
3. Heuristic: Teknik berbasis pengalama atau probabilitas untuk mempercepat proses pengambilan Keputusan
4. Inferensi (Penarikan Kesimpulan): Kemampuan membuat Kesimpulan berdasarkan informasi yang ada
5. Pencocokan Pola: Indentifikasi pola atau struktur dalam data
""",True)


show_text = st.button('Machine Learning')
if show_text:
	st.markdown("""
Sebuah metode menganalisa data yang secara otomatis membangun model data dengan system komputer dapat belajar dari data secara eksplisit, mengidentifikasi pola dan membuat keputusan dengan sedikit campur tangan manusia. 
Contoh:
Komputer secara otomatis dapat mengenali sebuah email yang masuk adalah spam atau bukan berdasarkan histori email yang masuk sebelumnya.
""", True)


st.image("https://cdn.elearningindustry.com/wp-content/uploads/2017/05/73348f2f23b70566eef2d9f10f9fe22c.png", caption="processing", width=400)


st.subheader("Machine Learning dan Mekanismenya")
st.video("https://youtu.be/ZvV0XTMlpJg?si=ZXKK-oQStm2pzwYT")

st.markdown("## Teknik Machine Learning")
col1, col2, col3 = st.columns (3)
with col1:
    with st.expander("Supervised"):
        st.markdown(""" 
Supervised Learning: pembelajaran dengan data diserta target
a.	Regresi: melakukan prediksi dengan nilai output berupa bilangan kontinu
b.	Klasifikasi: memprediksi nilai output dalam bentuk data kategori
""",True)
with col2:
    with st.expander("Unsipervised"):
        st.markdown("""
Unsipervised Learning: pembelajaran dengan data tidak disertai target. Clustering adalah mengelompokkan data berdasarkan kemiripan tanpa label sebelumnya.
""",True)
with col2:
    with st.expander("Reinforcement"):
        st.markdown("""
Reinforcement Learning: pembelajaran observasi interaksi dengan environment.
""",True)	


st.image("https://ai2people.com/wp-content/uploads/2023/03/how-does-machine-learining-work.jpg", caption="Cara AI 			Bekerja",width=400)

st.markdown("## Teknik Pemecahan Masalah")
st.markdown("""
1. Conventional/ Hard Computing : Metodologi konvensional yang bergantung pada prinsip-prinsip akurasi, kepastian, dan tidak fleksibel, contoh: Logika penalaran berbentuk symbol, pencarian & pemodelan masalah secara numeris
2. Soft Computing: Metodologi pendekatan modern yang didasarkan pada gagasan perkiraan, ketidakpastian, dan fleksibilitas, contoh: Penalaran melalui pendekatan, pendekatan fungsional, dan pencarian random
""",True)



import streamlit as st

# Judul Aplikasi
st.title("KUISS BIG DATA!!!!")

# Soal dan Jawaban
questions = [
    {
        'question': "Apa yang dimaksud dengan unsupervised learning?",
        'options': ['Volume, Velocity, Variety', 'Value, Volume, Vision', 'Velocity, Veracity, View', 'Volume, Validity, Velocity'],
        'answer': 'Volume, Velocity, Variety'
    },
    {
        'question': "Machine Learning merupakan cabang dari... ",
        'options': ['Ilmu Fisika', 'AI', 'Statistika Deskriptif', 'Pemrograman Web'],
        'answer': 'AI'
    },
    {
        'question': "Model Machine Learning yang digunakan untuk klasifikasi antara dua kategori disebut...",
        'options': ['Clustering', 'Regression', 'Binary Classification', 'Reinforcement Learning'],
        'answer': 'Binary Classification'
    },
    {
        'question': "Apa manfaat utama dari penerapan Big Data dalam bisnis?",
        'options': ['Mengurangi jumlah data yang disimpan', 'Meningkatkan efisiensi operasional dan pengambilan keputusan', 'Menggantikan seluruh pekerjaan manusia', 'Meminimalisir penggunaan teknologi informasi'],
        'answer': 'Meningkatkan efisiensi operasional dan pengambilan keputusan'
    },
    {
        'question': "Neural network merupakan bagian dari...",
        'options': ['Cloud Computing', 'Deep Learning', 'Data Warehousing', 'Big Data Storage'],
        'answer': 'Deep Learning'
    }, 
    {
        'question': "Apa yang dimaksud dengan unsupervised learning?",
        'options': ['Algoritma yang hanya digunakan dalam data kecil', 'Algoritma yang selalu menggunakan model regresi', 'Algoritma yang hanya bisa digunakan dalam AI', 'Algoritma yang menggunakan data tanpa label untuk menemukan pola'],
        'answer': 'Algoritma yang menggunakan data tanpa label untuk menemukan pola'
    }
]

score = 0

# Form untuk soal
with st.form("quiz_form"):
    for idx, q in enumerate(questions):
        user_answer = st.radio(q['question'], q['options'], key=f"question_{idx}")
        if user_answer == q['answer']:
            score += 1
    
    submitted = st.form_submit_button("Submit Jawaban")

if submitted:
    st.success(f"Skor kamu: {score} dari {len(questions)}")
    if score == len(questions):
        st.balloons()
    else:
        st.info("Coba lagi untuk mendapatkan skor sempurna!")



st.markdown("# SEKIAN DAN TERIMA KASIH DARI KELOMPOK 3")

