# app.py
import streamlit as st
import json, os

# ——— 데이터 로드/저장 함수 ———
DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    # 기본값: 모두 0으로 초기화
    return {
        "incomes": {
            "급여": 0,
            "월세 수입": 0,
            "보증금 예금 월 이자": 0
        },
        "expenses": {
            "컴패션(25일)": {"예산": 0, "실제": 0},
            "생활비": {"예산": 0, "실제": 0},
            "관리비(23일)": {"예산": 0, "실제": 0},
            "가스비(25일)": {"예산": 0, "실제": 0},
            "통신비(21일)": {"예산": 0, "실제": 0},
            "인터넷비(22일)": {"예산": 0, "실제": 0},
            "한림보험(21일)": {"예산": 0, "실제": 0},
            "보증금대출이자(24일)": {"예산": 0, "실제": 0},
            "대출이자(22일)": {"예산": 0, "실제": 0},
            "월세": {"예산": 0, "실제": 0},
            "수정 보험금": {"예산": 0, "실제": 0},
            "수정 용돈": {"예산": 0, "실제": 0},
            "왁싱": {"예산": 0, "실제": 0},
            "예비비": {"예산": 0, "실제": 0},
            "카드값": {"예산": 0, "실제": 0},
        },
        "current_balance": 0
    }

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ——— 앱 시작 ———
st.set_page_config(page_title="간단 가계부", layout="wide")
data = load_data()

# 1) 요약(예산)
inc_sum = sum(data["incomes"].values())
exp_budget_sum = sum(v["예산"] for v in data["expenses"].values())
budget_balance = inc_sum - exp_budget_sum

st.markdown("## 요약(예산)")
c1, c2, c3 = st.columns(3)
c1.metric("수입", f"{inc_sum:,.0f}원")
c2.metric("지출예산", f"{exp_budget_sum:,.0f}원")
c3.metric("잔액", f"{budget_balance:,.0f}원")

# 2) 수입 내역
st.markdown("### 수입 내역")
for name in data["incomes"]:
    data["incomes"][name] = st.number_input(
        label=name,
        value=data["incomes"][name],
        format="%,.0f",
        step=10000,
        key=f"inc_{name}"
    )

# 3) 지출 내역
st.markdown("### 지출 내역")
for name, vals in data["expenses"].items():
    col_label, col_budget, col_actual = st.columns([2,1,1])
    col_label.write(name)
    vals["예산"] = col_budget.number_input(
        label="예산",
        value=vals["예산"],
        format="%,.0f",
        step=5000,
        key=f"exp_bud_{name}"
    )
    vals["실제"] = col_actual.number_input(
        label="실제 지출",
        value=vals["실제"],
        format="%,.0f",
        step=5000,
        key=f"exp_act_{name}"
    )

# 4) 수지 계산
actual_sum = sum(v["실제"] for v in data["expenses"].values())
expected_balance = data["current_balance"] - actual_sum

st.markdown("## 수지 계산")
data["current_balance"] = st.number_input(
    label="현재 잔액",
    value=data["current_balance"],
    format="%,.0f",
    step=10000,
    key="current_balance"
)

d1, d2 = st.columns(2)
d1.metric("남은 지출", f"{actual_sum:,.0f}원")
d2.metric("예상 잔액", f"{expected_balance:,.0f}원")

# 자동으로 저장
save_data(data)
