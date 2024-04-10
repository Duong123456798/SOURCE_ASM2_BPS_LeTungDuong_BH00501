import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('Asm2_data.csv')

# In ra 5 hàng đầu tiên của DataFrame ban đầu
print("DataFrame ban đầu:")
print(df.head())

# 1. Xóa các hàng có giá trị trống
df = df.dropna()

# In ra 5 hàng đầu tiên sau khi xóa các hàng có giá trị trống
print("\nDataFrame sau khi xóa các hàng có giá trị trống:")
print(df.head())

# 2. Loại bỏ các cột không cần thiết
columns_to_drop = ['Country']  # Đặt tên các cột bạn muốn loại bỏ
df = df.drop(columns_to_drop, axis=1)

# In ra 5 hàng đầu tiên sau khi loại bỏ các cột không cần thiết
print("\nDataFrame sau khi loại bỏ các cột không cần thiết:")
print(df.head())

# 3. Loại bỏ các hàng trùng lặp
df = df.drop_duplicates()

# In ra 5 hàng đầu tiên sau khi loại bỏ các hàng trùng lặp
print("\nDataFrame sau khi loại bỏ các hàng trùng lặp:")
print(df.head())

# 4. Chuyển đổi kiểu dữ liệu của cột 'email' sang chuỗi
df['email'] = df['email'].astype(str)

# In ra kiểu dữ liệu của cột 'email' sau khi chuyển đổi
print("\nKiểu dữ liệu của cột 'email' sau khi chuyển đổi:")
print(df['email'].dtypes)


# 5. Chuẩn hóa định dạng email trong cột 'email'
def normalize_email(email):
    normalized_email = email.lower()
    return normalized_email
df['email'] = df['email'].apply(normalize_email)

# In ra 5 hàng đầu tiên sau khi chuẩn hóa định dạng email
print("\nDataFrame sau khi chuẩn hóa định dạng email:")
print(df.head())


#6. Xóa các dòng chứa giá trị không hợp lệ trong cột 'gender'
df = df[df['gender'].isin(['Male', 'Female'])]

# In ra 5 hàng đầu tiên sau khi làm sạch
print(df.head())

# Lưu trữ dữ liệu đã xử lý vào file CSV mới
df.to_csv('Asm2_Cleaned_Data.csv', index=False)

print("Xử lý dữ liệu hoàn thành. Dữ liệu đã được lưu vào file Asm2_Cleaned_Data.csv.")
