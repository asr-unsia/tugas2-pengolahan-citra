import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import csv

# membaca gambar
image = iio.imread("./drive/MyDrive/gcolab_attachments/roland_berger_410_digital_ports_st.jpg")
# tampilkan gambar asli
plt.figure(figsize=(10,10))
plt.title("Original Image")
plt.axis("off")
plt.imshow(image)

# Konversi ke grayscale
gray_image = np.dot(image[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)
# tampilkan gambar grayscale
plt.figure(figsize=(10,10))
plt.title("Grayscale Image")
plt.axis("off")
plt.imshow(gray_image, cmap="gray")

# Hitung histogram
histogram, bins = np.histogram(gray_image, bins=256, range=(0, 256))

# Plot histogram
plt.figure(figsize=(10, 6))
plt.bar(range(256), histogram, color='gray', width=1.0)
plt.title('Histogram Intensitas Gambar Grayscale')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

dominant_intensity = 0
dominant_pixel_count = 0
for intensity, count in enumerate(histogram):
    if count > dominant_pixel_count:
        dominant_pixel_count = count
        dominant_intensity = intensity

# Menampilkan intensitas dominan beserta jumlah pikselnya
print(f"Intensitas dominan : {dominant_intensity}")
print(f"Jumlah piksel : {dominant_pixel_count} piksel")


# Ekspor data jumlah piksel per intensitas ke file CSV
with open('./drive/MyDrive/gcolab_attachments/histogram.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Intensitas", "-" "Jumlah Piksel"])  # Header
    for intensity, count in enumerate(histogram):
        writer.writerow([intensity, "-", count])
print("Data berhasil diekspor ke histogram.csv")
