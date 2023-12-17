# alculator_main.py-

pyQt5 based calculator - used for practice

## goal

- git hub 저장소 생성 및 관리 실습
- pyQt5 기반 계산기 기능 및 사용방법 개선

## getting started

- pyqt5 모듈 설치 (python -m pip install pyqt5)
- 파이썬 파일 실행 (pytion calculator_main.py)

# 수정된 사항

UI 출력 로직 변경 - QLineEdit을 이용해 사용자 입력 받음 - UI 테이블을 이용해 관리하기 편하게 button 테이블 추가함

"=" 버튼 입력시 수식 계산 로직변경 - eval() 사용에서, 기본적인 사칙연산 및 math 모듈 이용함 - 복잡한 수식에 대해 다루지 못해, 연산자 우선순위는 고려하지 않음

새로운 버튼 추가 - C,CE,1/x, x^2, 제곱근 등 math 모듈을 이용해 구현한 새로운 버튼을 추가함.
