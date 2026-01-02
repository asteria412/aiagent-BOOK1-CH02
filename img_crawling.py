import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import time

# 1. 긁어올 섹션 번호 목록 (100:정치 ~ 105:IT/과학)
section_list = range(100, 106)

# 사람인 척 하기 위한 헤더
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

print("크롤링을 시작합니다...")

# 2. 섹션별로 반복하기 (for문)
for section_id in section_list:
    base_url = f"https://news.naver.com/section/{section_id}"
    print(f"\n--- [섹션 {section_id}] 다운로드 시작: {base_url} ---")
    
    # 2-1. 저장할 폴더 만들기 (예: images/100, images/101...)
    save_folder = f"images/{section_id}"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        
    try:
        # 페이지 접속
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 2-2. 이미지 태그 찾기
        # 네이버 뉴스 '섹션' 페이지의 기사 썸네일은 보통 ".sa_thumb" 클래스 안에 있습니다.
        img_elements = soup.select(".sa_thumb img")
        
        print(f"발견된 이미지 개수: {len(img_elements)}개")
        
        # 2-3. 이미지 다운로드
        for i, img in enumerate(img_elements, 1):
            img_url = img.get("src") or img.get("data-src") # data-src에 숨어있는 경우도 대비
            
            if img_url:
                # 파일명: images/100/thumb_1.jpg
                filename = f"{save_folder}/thumb_{i}.jpg"
                
                # 이미지 주소가 http로 시작하지 않는 경우(상대경로) 처리
                if not img_url.startswith("http"):
                    continue 

                try:
                    urllib.request.urlretrieve(img_url, filename)
                    # 진행상황을 한 줄로 깔끔하게 출력 (선택사항)
                    # print(f"다운로드 중.. {filename}") 
                except Exception as e:
                    print(f"다운 실패({filename}): {e}")
            
            # 너무 빠르면 차단당할 수 있으니 이미지 1개 받고 0.1초 쉬기
            time.sleep(0.1)
            
    except Exception as e:
        print(f"섹션 {section_id} 처리 중 오류 발생: {e}")
        
    # 한 페이지(섹션) 작업이 끝나면 1초 쉬고 다음 페이지로 넘어감
    time.sleep(1)

print("\n모든 섹션의 다운로드가 완료되었습니다!")