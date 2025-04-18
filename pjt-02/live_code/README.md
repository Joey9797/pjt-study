반응형 적용하기

1. flex - 정렬
  - 가장 기본적인 반응형 레이아웃 구현

2. Grid system (얘도 사실 내부적으로 flex 로 구현됨)
  - 즉, 반응형 레이아웃 구현 시
  - 가로 한 줄을 12칸으로 나눠 가지자 (row)
    - 각 요소들이 원하는 만큼 가져가자 (col-{N})
  - 정해진 픽셀 이상에서 원하는 크기를 재설정
    - breakpoint (xs, sm, md, lg, xl, xxl)
    - col-{breakpoint}-{N}

3. 추가적인 반응형 CSS
  - breakpoint 외의 작업은 ...? (300PX 일 때 조작하고 싶다)
  - 색깔을 바꾸고 싶다.
  - 미디어 쿼리 (@media)
