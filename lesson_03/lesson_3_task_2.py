from smartphone import Smartphone

catalog = [
  Smartphone("Apple", "iPhone 13", "+79123456789"),
  Smartphone("Samsung", "Galaxy S21", "+79234567890"),
  Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"),
  Smartphone("Huawei", "P40 Pro", "+79456789012"),
  Smartphone("Google", "Pixel 5", "+79567890123")
]

for smartphone in catalog:
    print(
        f"{smartphone.phone_brand} - {smartphone.phone_model}."
        f" {smartphone.phone_number}"
    )
