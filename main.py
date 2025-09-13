# app.py
import streamlit as st
import pandas as pd

# 데이터프레임 생성
data = {
    '지역': ['서울', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '경기'],
    '장소': ['국립서울현충원', '전쟁기념관', '유엔기념공원', '국립신암선열공원', '인천상륙작전기념관', '국립5.18민주묘지', '국립대전현충원', '국립4.19민주묘지(울산)', '국립이천호국원', 'DMZ(비무장지대)'],
    '설명': [
        '대한민국 순국선열과 호국영령이 잠들어 있는 곳입니다.',
        '전쟁의 역사와 교훈을 배우고 평화의 소중함을 되새기는 공간입니다.',
        '6.25 전쟁에 참전하여 전사한 유엔군 장병들의 유해가 안장된 세계 유일의 유엔군 묘지입니다.',
        '일제강점기 순국선열들의 넋을 기리는 영남권 최대의 독립운동가 묘역입니다.',
        '6.25 전쟁의 흐름을 바꾼 인천상륙작전의 역사와 의의를 기념하는 곳입니다.',
        '5.18 민주화운동의 희생자들을 추모하고 민주주의의 가치를 기리는 공간입니다.',
        '국가와 민족을 위해 헌신한 분들의 숭고한 정신을 기리는 곳입니다.',
        '4.19 혁명 당시 울산에서 희생된 학생들의 넋을 기리는 묘역입니다.',
        '국가를 위해 희생, 공헌하신 국가유공자와 참전용사들을 모신 곳입니다.',
        '남북 분단의 현실을 생생하게 느낄 수 있는 역사적 장소입니다.'
    ],
    '이미지_URL': [
        'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202206/06/617e1e40-ed81-424a-ae9c-6a1618a5996c.jpg',
        'https://korean.visitseoul.net/comm/getImage?srvcId=MEDIA&imgTy=MEDIA&imgNo=161575',
        'https://www.unmck.or.kr/wp-content/uploads/2021/08/main_image_unmck.jpg',
        'https://www.daegufacilities.or.kr/damun/images/sub/02_02_02_img01.jpg',
        'https://www.incheon.go.kr/img/main/slogan_img.jpg',
        'https://518.org/cms/files/518story_220215161048_1.jpg',
        'https://www.ncsl.go.kr/img_2016/img_main.jpg',
        'https://www.ulsan.go.kr/rep_file/view.html?filename=20230217094054.jpg',
        'https://www.icn.go.kr/icn/images/main/main_visual01.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/f/fa/DMZ_%ED%8C%90%EB%AC%B8%EC%A0%90.jpg'
    ]
}

df = pd.DataFrame(data)

# Streamlit 앱 구성
st.set_page_config(page_title="보훈 관련 방문지 안내 🇰🇷", page_icon="✨")

# 메인 페이지 - 보훈 관련 이미지
st.image("https://www.mvis.go.kr/img/content/main_visual.jpg", use_column_width=True)

st.title("지역별 보훈 관련 방문지 안내 🇰🇷")
st.markdown("나라를 위해 헌신하신 분들을 기억하고, 그 의미를 되새길 수 있는 장소를 소개해 드려요. 🙏")

st.info("🗺️ **지역을 선택하고, 소중한 분들의 발자취를 따라가 보세요!**")

# 지역 선택 드롭다운 메뉴
regions = ['전체'] + sorted(df['지역'].unique().tolist())
selected_region = st.selectbox("원하는 지역을 선택해 주세요:", regions)

# 선택된 지역에 따라 데이터 필터링
if selected_region == '전체':
    filtered_df = df
else:
    filtered_df = df[df['지역'] == selected_region]

st.markdown("---")

# 필터링된 데이터 출력
if not filtered_df.empty:
    for index, row in filtered_df.iterrows():
        with st.expander(f"📍 {row['장소']} ({row['지역']})"):
            # 각 장소에 대한 대표 이미지
            st.image(row['이미지_URL'], caption=row['장소'], use_column_width=True)
            st.write(f"**{row['설명']}**")
            st.markdown(f"**➡️ {row['장소']}**에 대해 더 자세히 알아보기:", unsafe_allow_html=True)
            
            # 구글 검색 링크 제공
            st.markdown(f"[구글에서 '{row['장소']}' 검색하기](https://www.google.com/search?q={row['장소']})", unsafe_allow_html=True)

else:
    st.warning("선택하신 지역에는 등록된 보훈 관련 방문지가 없습니다. 다른 지역을 선택해 주세요. 🧐")

st.markdown("---")
st.markdown("© 2025 대한민국 보훈처 | Made with Streamlit")

# 추가적인 재미 요소
st.sidebar.markdown("## ✨ 함께 기억해요!")
st.sidebar.markdown("이 앱을 통해 나라를 위해 헌신하신 모든 분께 감사하는 마음을 가져보는 건 어떨까요? 🙏")
st.sidebar.button("마음속으로 감사 인사 보내기! 💌")
