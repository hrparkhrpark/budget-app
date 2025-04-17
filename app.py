import streamlit as st

st.set_page_config(page_title="간단한 가계부", layout="centered")

st.title("💸 간단한 가계부")

st.header("수입 입력")
income_items = ["급여", "월세 수입", "보증금 예금 이자"]
incomes = {}
for item in income_items:
    val = st.number_input(item, min_value=0, value=0, step=1000)
    incomes[item] = val

st.header("지출 입력")
expense_items = [
    "컴패션", "생활비", "관리비", "가스비", "통신비", "인터넷비", 
    "HR보험", "보증금대출이자", "대출이자", "월세", "SJ 보험금"
]
expenses = {}
for item in expense_items:
    val = st.number_input(item, min_value=0, value=0, step=1000)
    expenses[item] = val

# 계산
total_income = sum(incomes.values())
total_expense = sum(expenses.values())
balance = total_income - total_expense

# 표시
st.markdown("---")
st.subheader("📊 결과 요약")
st.write(f"**총 수입:** {total_income:,} 원")
st.write(f"**총 지출:** {total_expense:,} 원")
st.success(f"💰 **예상 잔액:** {balance:,} 원")
