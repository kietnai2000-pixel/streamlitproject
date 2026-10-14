# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 08:39:12 2026

@author: kietn
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
st.set_page_config(page_title="Quản lý điểm sinh viên", page_icon="🎓", layout="wide")
data={"Họ và tên": ["Nguyễn Văn An","Trần Thị Bình", "Nguyễn Đức Trí", "Phạm Hoài Giang", "Ngô Minh Đức", 
                    "Đỗ Đức Long", "Nguyễn Thị Yến","Bùi Ngọc Khánh", "Đỗ Duy Quang", "Vũ Ngọc Thương" ],
      "Chuyên cần": [9, 8, 6, 6, 7, 9, 8, 8, 9, 7],
      "Giữa kỳ": [8, 7, 8, 7, 8, 9, 10, 8, 10, 6],
      "Cuối kỳ": [9, 6, 9, 8, 9, 10, 10, 8, 9, 8],
      "Tên": ["An", "Bình","Trí", "Giang", "Đức", "Long", "Yến", "Khánh", "Quang", "Thương" ]}
df = pd.DataFrame(data)
df["Tổng kết"]=(0.2*df["Chuyên cần"]+0.3*df["Giữa kỳ"]+0.5*df["Cuối kỳ"])
df["Tổng kết"]=df["Tổng kết"].round(2)
def phan_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"
df["Xếp loại"] = df["Tổng kết"].apply(phan_loai)
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.subheader("Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)
st.subheader("Thống kê chung")
diem_trung_binh=round(df["Tổng kết"].mean(), 2)
so_sinh_vien_dat=(df["Tổng kết"]>=5.0).sum()
sinh_vien_cao_nhat=df.loc[df["Tổng kết"].idxmax()]
sinh_vien_thap_nhat=df.loc[df["Tổng kết"].idxmin()]
col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm trung bình của sinh viên", f"{diem_trung_binh}")
col2.metric("Điểm cao nhất", f"{sinh_vien_cao_nhat['Tổng kết']}", f"SV: {sinh_vien_cao_nhat['Họ và tên']}")
col3.metric("Điểm thấp nhất", f"{sinh_vien_thap_nhat['Tổng kết']}", f"SV: {sinh_vien_thap_nhat['Họ và tên']}")
col4.metric("Số SV đạt (>=5)", f"{so_sinh_vien_dat}/{len(df)}")
st.divider()
st.subheader("Tra cứu chi tiết từng sinh viên")
selected_sv = st.selectbox("Chọn tên sinh viên:", df["Họ và tên"].tolist())
row = df[df["Họ và tên"] == selected_sv].iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
c1.write(f"**Chuyên cần:** {row['Chuyên cần']}")
c2.write(f"**Giữa kỳ:** {row['Giữa kỳ']}")
c3.write(f"**Cuối kỳ:** {row['Cuối kỳ']}")
c4.write(f"**Tổng kết:** {row['Tổng kết']}")
c5.write(f"**Xếp loại:** {row['Xếp loại']}")
st.divider()
st.subheader("Biểu đồ điểm tổng kết của sinh viên")
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(df["Họ và tên"], df["Tổng kết"], color="cornflowerblue")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Tên")
ax.set_xlim(0, 10)
ax.invert_yaxis()
for bar in bars:
    w = bar.get_width()
    ax.text( w + 0.1, bar.get_y() + bar.get_height() / 2, f"{w}", va="center", ha="left")
st.pyplot(fig)
st.divider()
st.markdown("<p style='text-align: center; font-size: 12px; color: gray;'>"
    "Họ tên sinh viên: [Võ Tuấn Kiệt] | MSSV: [058208003139]"
    "</p>",
    unsafe_allow_html=True,)