import pandas as pd
import altair as alt
import streamlit as st
import io

# 데이터 로드 함수
@st.cache_data
def load_data(uploaded_file=None):
    """
    1. 'countriesMBTI_16types.csv' 파일을 로컬에서 먼저 시도합니다.
    2. 파일이 없으면 사용자가 업로드한 파일을 사용합니다.
    """
    file_path = 'countriesMBTI_16types.csv'
    try:
        # 로컬 파일 시도
        df = pd.read_csv(file_path)
        st.success("로컬 파일에서 데이터를 성공적으로 읽었습니다.")
        return df
    except FileNotFoundError:
        st.info("로컬 파일을 찾을 수 없습니다. 업로드된 파일을 사용합니다.")
        if uploaded_file is not None:
            # 업로드된 파일 사용
            df = pd.read_csv(uploaded_file)
            st.success("업로드된 파일에서 데이터를 성공적으로 읽었습니다.")
            return df
        else:
            st.error("데이터 파일을 찾을 수 없습니다. 'countriesMBTI_16types.csv' 파일을 업로드해주세요.")
            return None

# 데이터 처리 및 시각화 함수
def create_chart(df, selected_mbti):
    """
    선택된 MBTI 유형에 대한 상위 10개 국가 막대 그래프를 생성합니다.
    """
    # 선택된 MBTI 유형에 대해 상위 10개 국가 데이터프레임 생성
    top_10_df = df.sort_values(by=selected_mbti, ascending=False).head(10)

    # 데이터프레임 이름 변경
    source = top_10_df[['Country', selected_mbti]].copy()
    source.rename(columns={selected_mbti: 'Proportion'}, inplace=True)

    # Altair 차트 생성
    chart = alt.Chart(source).mark_bar().encode(
        x=alt.X('Country:N', sort='-y', title='국가'),
        y=alt.Y('Proportion:Q', title='비율'),
        tooltip=['Country', alt.Tooltip('Proportion', format='.2%')]
    ).properties(
        title=f'{selected_mbti} 유형 비율이 가장 높은 국가 Top 10'
    ).interactive()

    return chart

def main():
    """
    스트림릿 앱의 메인 함수입니다.
    """
    st.set_page_config(
        page_title='MBTI 유형별 국가 비율 분석',
        layout='wide'
    )

    st.title('MBTI 유형별 국가 비율 분석')
    st.write('파일이 로컬에 없을 경우 업로드하신 파일을 사용합니다.')

    # 파일 업로드 위젯
    uploaded_file = st.file_uploader("CSV 파일을 업로드해주세요", type=["csv"])

    # 데이터 로드
    if uploaded_file is not None:
        df = load_data(uploaded_file)
    else:
        df = load_data()

    if df is not None:
        # 드롭다운 메뉴를 위한 MBTI 유형 목록 생성
        mbti_types = df.columns.drop('Country').tolist()
        
        # 사이드바에 셀렉트 박스 추가
        selected_mbti = st.sidebar.selectbox(
            'MBTI 유형을 선택해 주세요:',
            mbti_types
        )
        
        if selected_mbti:
            # 차트 생성 및 표시
            chart = create_chart(df, selected_mbti)
            st.altair_chart(chart, use_container_width=True)

if __name__ == '__main__':
    main()
