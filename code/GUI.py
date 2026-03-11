# 고용위기 지역
corejob_dict = {
    '울산광역시 동구': ['금속·재료 설치·정비·생산직(판금·단조·주조·용접·도장 등)', '전기·전자 설치·정비·생산직', '기계 설치·정비·생산직', '운전·운송직', '제조 연구개발직 및 공학기술직'], # 심각
    '전라남도 여수시': ['농림어업직', '기계 설치·정비·생산직', '제조 연구개발직 및 공학기술직', '건설·채굴직(연구개발직 포함)', '운전·운송직'], # 심각
    '경상남도 하동군': ['경영·회계·행정·사무직', '돌봄 서비스직(간병·육아)', '사회복지·종교직', '식품 가공·생산직', '전기·전자 설치·정비·생산직'], # 심각
    '경기도 의정부시': ['돌봄 서비스직(간병·육아)'], # 심각
    '서울특별시 광진구': ['돌봄 서비스직(간병·육아)', '건설·채굴직(연구개발직 포함)', '기계 설치·정비·생산직'], # 주의
    '경기도 동두천시': ['식품 가공·생산직', '기계 설치·정비·생산직', '건설·채굴직(연구개발직 포함)', '화학·환경 설치·정비·생산직', '제조 연구개발직 및 공학기술직'], # 주의
    '전라남도 구례군': ['건설·채굴직(연구개발직 포함)', '사회복지·종교직', '농림어업직', '경호·경비·청소·기타 개인서비스직', '금속·재료 설치·정비·생산직(판금·단조·주조·용접·도장 등)'], # 주의
    '부산광역시 수영구': ['돌봄 서비스직(간병·육아)', '건설·채굴직(연구개발직 포함)', '기계 설치·정비·생산직', '농림어업직', '화학·환경 설치·정비·생산직'] # 주의
}

# 고용위기 지역 취업 시 혜택
benefit_list = {
    '울산광역시 동구': '청년 대상 취업 지원 프로그램 진행 및 이수 시 최대 300만원 지원, 조선 및 유관 산업 인력 육성 지원',
    '전라남도 여수시': '대학생 현장실습 활성화 지원(지역일자리 목표 공시제)',
    '경상남도 하동군': '2024년 청년성장 프로젝트 진행, 하동드림스테이션 건립 추진, 농업인재인력은행 사업 진행',
    '경기도 의정부시': '일자리 수요데이 4U 행사 진행(보건복지업 중심)',
    '서울특별시 광진구': '일자리 6197개 창출, 취업 프로그램 이수 시 최대 300만원 지원, 청년 대상 어학/자격증 응시료 지원, 중장년 대상 인턴십 프로그램 진행',
    '경기도 동두천시': '섬유제조기업 디지털 생태계 전환 패키지 지원',
    '전라남도 구례군': '지역 중소기업 취업청년 학자금대출 상환지원(월 10만원)',
    '부산광역시 수영구': '청년 사업자 임차료 지원, (경비원 고용 유지 지원금 지급 특화 사업)',
}

import pandas as pd

df = pd.read_csv(r'C:\Users\jiwon\Desktop\구인 - 구직.csv')

### GUI 부분 ###
from tkinter import *
from tkinter import font, messagebox

window = Tk()
window.title('Job Secure')
f = Frame(window)
window.resizable(False, False)

label_font = font.Font(family='맑은 고딕', size=25, weight='bold')
button_font = font.Font(family='맑은 고딕', size=10)

label = Label(window, text = 'Job Secure', font=label_font).pack(pady=1)
label = Label(window, text = '-직종을 선택해주세요-\n많은 혜택을 받을 수 있는 고용위기 지역 일자리를 추천해드립니다!', font=button_font).pack(pady=1)

def create_button(parent, text, row, column, bg_color, font, job, width=25, height=3):
    button = Button(parent, text=text, bg=bg_color, fg='black', font=font, width=width, height=height, command=lambda: recommend(job))
    button.grid(row=row, column=column, padx=2, pady=2)
    return button

def recommend(job):
    recommend_region = [key for key, value in corejob_dict.items() if (isinstance(value, list) and job in value) or (isinstance(value, str) and job == value)]
    job_columns = [col for col in df.columns if job in col]
    job_data = df[job_columns].iloc[0]
    seek_seeker = job_data.to_dict()
    sorted_ss = sorted(seek_seeker.items(), key=lambda item: item[1])
    min_regions = sorted_ss[:5]
    max_regions = sorted_ss[-5:]

    max_regions_list = [region[0].replace(f'_{job}', '') for region in min_regions]
    min_regions_list = [region[0].replace(f'_{job}', '') for region in max_regions]

    if recommend_region:
        result1 = f"'{job}' 직종의 직업을 구할 수 있는 지역을 추천해드립니다\n \n"
        result2 = f"이런 지역의 일자리도 많아요 👉 {', '.join(max_regions_list)}"
        for region in recommend_region:
            benefit = benefit_list.get(region)
            result1 += f"지역: {region} | 혜택: {benefit}\n"
        result = f'{result1}\n{result2}'
        messagebox.showinfo("추천 결과", result)
            
    else:
        # 결과 문자열의 시작 부분
        result = f'{job} 직종에 해당하는 고용위기 지역이 없지만, 전국 지역에 대한 정보를 드릴게요\n\n'

        # 일자리가 많은 지역 목록
        max_result = "이 지역에 일자리가 많아요!\n"
        max_result += f"👉 {', '.join(max_regions_list)}\n"
        max_result += "========================================\n"

        # 피해야 할 지역 목록
        min_result = "이 지역은 피하세요!\n"
        min_result += f"👉 {', '.join(min_regions_list)}"

        # 결과 문자열에 각각의 목록 추가
        result += max_result + min_result

        # 메시지 박스로 결과 표시
        messagebox.showinfo("추천 결과", result)

def emp_crisis():
    messagebox.showinfo("고용위기 지역",
                        '''
고용위기 🚨심각🚨 지역 | 고용위기 ⚠️주의⚠️ 지역
       울산광역시 동구   |   서울특별시 광진구
       전라남도 여수시   |   경기도 동두천시
       경상남도 하동군   |   전라남도 구례군
       경기도 의정부시   |   부산광역시 수영구

관심이 필요한 지역 👉
매우 심각: 서울특별시 성동구, 경기도 안산시, 경기도 용인시, 전라남도 나주시
심각: 전라남도 화순군, 강원특별자치도 고성군
주의: 서울특별시 마포구, 서울특별시 구로구, 충청북도 청주시 흥덕구, 충청남도 태안군, 경상남도 함양군 
                        ''')

create_button(f, '건설・채굴직\n(연구개발직 포함)', 0, 0, 'LightSkyBlue1', button_font, '건설·채굴직(연구개발직 포함)')
create_button(f, '경영・회계・행정・사무직', 0, 1, 'LightSkyBlue1', button_font, '경영·회계·행정·사무직')
create_button(f, '경호・경비・청소\n・기타 개인서비스직', 0, 2, 'LightSkyBlue1', button_font, '경호·경비·청소·기타 개인서비스직')
create_button(f, '관리직', 0, 3, 'LightSkyBlue1', button_font, '관리직')

create_button(f, '교육 및 자연과학, 사회과학\n연구관련직', 2, 0, 'LightSkyBlue3', button_font, '교육 및 자연과학 사회과학연구관련직')
create_button(f, '군인', 2, 1, 'LightSkyBlue3', button_font, '군인')
create_button(f, '금속·재료 설치·정비·생산직\n(판금·단조·주조·용접·도장 등)', 2, 2, 'LightSkyBlue3', button_font, '금속·재료 설치·정비·생산직(판금·단조·주조·용접·도장 등)')
create_button(f, '금융·보험직', 2, 3, 'LightSkyBlue3', button_font, '금융·보험직')

create_button(f, '기계 설치·정비·생산직', 4, 0, 'LightSkyBlue1', button_font, '기계 설치·정비·생산직')
create_button(f, '농림어업직', 4, 1, 'LightSkyBlue1', button_font, '농림어업직')
create_button(f, '돌봄 서비스직(간병·육아)', 4, 2, 'LightSkyBlue1', button_font, '돌봄 서비스직(간병·육아)')
create_button(f, '미용·숙박·여행\n·오락·스포츠직', 4, 3, 'LightSkyBlue1', button_font, '미용·숙박·여행·오락·스포츠직')

create_button(f, '법률·경찰·소방·교도직', 6, 0, 'LightSkyBlue3', button_font, '법률·경찰·소방·교도직')
create_button(f, '보건·의료직', 6, 1, 'LightSkyBlue3', button_font, '보건·의료직')
create_button(f, '사회복지·종교직', 6, 2, 'LightSkyBlue3', button_font, '사회복지·종교직')
create_button(f, '섬유·의복 생산직', 6, 3, 'LightSkyBlue3', button_font, '섬유·의복 생산직')

create_button(f, '식품 가공·생산직', 8, 0, 'LightSkyBlue1', button_font, '식품 가공·생산직')
create_button(f, '영업·판매직', 8, 1, 'LightSkyBlue1', button_font, '영업·판매직')
create_button(f, '예술·디자인·방송직', 8, 2, 'LightSkyBlue1', button_font, '예술·디자인·방송직')
create_button(f, '운전·운송직', 8, 3, 'LightSkyBlue1', button_font, '운전·운송직')

create_button(f, '음식 서비스직', 10, 0, 'LightSkyBlue3', button_font, '음식 서비스직')
create_button(f, '인쇄·목재·공예 및\n기타 설치·정비·생산직', 10, 1, 'LightSkyBlue3', button_font, '인쇄·목재·공예 및 기타 설치·정비·생산직')
create_button(f, '전기·전자 설치·정비·생산직', 10, 2, 'LightSkyBlue3', button_font, '전기·전자 설치·정비·생산직')
create_button(f, '정보통신 설치·정비직\n(연구개발직 포함)', 10, 3, 'LightSkyBlue3', button_font, '정보통신 설치·정비직(연구개발직 포함)')

create_button(f, '제조 연구개발직 및\n공학기술직', 12, 0, 'LightSkyBlue1', button_font, '제조 연구개발직 및 공학기술직')
create_button(f, '화학·환경 설치·정비·생산직', 12, 3, 'LightSkyBlue1', button_font, '화학·환경 설치·정비·생산직')


Button(f, text='종료하기😭', bg='Pink', font=button_font, width=25, height=3, command=window.destroy).grid(row=12, column=2, padx=2, pady=2)
Button(f, text='고용위기 지역 확인하기', bg='Pink', font=button_font, width=25, height=3, command=emp_crisis).grid(row=12, column=1, padx=2, pady=2)

f.pack(pady=20)

window.mainloop()
