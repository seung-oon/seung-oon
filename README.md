# Hi, I'm Seungyoon 👋

한성대학교 컴퓨터공학부 4학년 · **Backend Developer**
Java / Spring Boot 백엔드를 중심으로 공간 DB, 클라우드 인프라, 의료 AI 연구까지 다루고 있습니다.

<br>

## 🛠 Tech Stack

**Backend** &nbsp;
![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL%20%2F%20PostGIS-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

**Infra** &nbsp;
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

**AI / Research** &nbsp;
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain%20%2F%20RAG-1C3C3C?style=flat-square&logo=langchain&logoColor=white)

<br>

## 🖥 Backend Projects

### 🚶 Safe-walk · [safe-waalk/BE](https://github.com/safe-waalk/BE)
경기도 공공데이터 공모전 — 지도 기반 안전 보행 서비스
- **Role**: Team Lead · Backend
- CCTV·보안등·안심벨·범죄주의구역·사용자 신고 데이터를 PostGIS에 적재하고, 좌표 반경 기반 **안전 인프라 집계·지도 레이어·안전점수 API** 제공
- ORM 없이 `NamedParameterJdbcTemplate`으로 공간 쿼리 직접 작성
- **Stack**: Java 21, Spring Boot 4, PostgreSQL + PostGIS (Supabase), Docker, JUnit 5

### 🌙 ShiftRhythm · [2026-1-midtone/Backend](https://github.com/2026-1-midtone/Backend)
교대근무자를 위한 생체리듬 코칭 앱
- **Role**: Backend
- 근무표 사진을 **Google Document AI OCR**로 인식해 일정 자동 입력 (서비스 계정 impersonation, 키 파일 없음)
- Testcontainers 기반 MySQL·Redis 통합 테스트, Docker Compose 로컬 환경
- **Stack**: Java 21, Spring Boot 4, MySQL, Redis, Docker, Google Document AI

### 📚 OnRoot AI · [On-root-AI/BE](https://github.com/On-root-AI/BE)
LLM 기반 자격증 학습 플래너
- **Role**: Backend
- Q-Net 공공데이터 API로 시험 일정을 받아 **Gemini API**로 맞춤 학습 계획 생성
- **Stack**: Java 21, Spring Boot 3.5, MySQL, Spring Data JPA, Gemini API

### 📱 PocketCo · [KozzilzzilE/Dataset](https://github.com/KozzilzzilE/Dataset)
2026 한성대 모바일 캡스톤 — AI 피드백 기반 모바일 알고리즘 학습 앱
- **Role**: Dataset
- 알고리즘 학습 콘텐츠 **Firestore 데이터 스키마 설계** (topic → notion → code 계층) 및 샘플 데이터 구축, 스키마 통일 규칙 정리

<br>

## 🔬 Research

### 💊 Drug Recommendation Research · [drug-recommendation-research](https://github.com/hs-2171395-seungyoonkim/drug-recommendation-research)
MIMIC-III / IV 기반 의약품 추천 모델 재현성 연구 (7개 트랙)
- **HI-DR (AAAI'25) 재현 + 재설계**: "과다 추천을 걸러야 한다"는 전제를 데이터로 반증 → 사후 필터 대신 **이력 기반 후보 풀 확장**으로 재설계 (5-seed)
- **SafeDrug 군집별 공정성 감사**: 진단 텍스트로 방문을 군집화해 정확도 격차 검정, 격차 원인을 방문 표현·DDI 제약에서 추적
- **SafeDrug + 장기 기능 피처**: ICD-9/10 통합 MIMIC-IV 레코드 재구축, 신·간 기능 지표 주입
- 원본·행 단위 데이터는 포함하지 않고 코드·보고서·집계 결과만 공개 (PhysioNet DUA 준수)
- **Stack**: Python, PyTorch, MIMIC-III/IV

### 🎧 DCC 예선 · [KozzilzzilE/DCC_Problem](https://github.com/KozzilzzilE/DCC_Problem)
119 신고 전화 음성·전사 데이터 AI 과제 (팀 5인)

**Mission 1 — 신고자 성별 분류** (단독 담당)
- 통화 음성에서 신고자 발화만 잘라 **조각 단위 학습 → 통화 단위 soft voting** 구조 설계 (조각 정확도 0.88 → 통화 정확도 0.98)
- ResNet50(log-mel)·Wav2Vec2·전화 음성 사전학습 모델 3갈래 비교 하네스 구축, SpecAugment·지식 증류로 ResNet 개선
- Validation 3,640통화 기준 **정확도 0.9835** (Wav2Vec2), 모델 간 오류 겹침 분석으로 앙상블 한계 확인
- 대회 규정(결정 임계값 0.5 고정)에 맞춰 제출 경로 정비, 오프라인 로딩·VRAM 페이징 등 1회 실행 채점 대비

**Mission 3 — 환자 증상 다중 라벨 분류** (제출 경로·학습 개선 담당)
- 더미 상태였던 **제출 추론 경로 구현**: 학습 설정을 체크포인트에서 복원해 학습-추론 불일치 차단, 임계값 0.5 고정을 코드로 강제
- 임계값 대신 손실로 보정: `pos_weight` 거듭제곱 옵션으로 기존 pos_weight(0.6189) 과보정을 줄여 **Macro F1@0.5 0.6496** (기준선 0.5967)
- KLUE-RoBERTa 멀티시드 앙상블 + **TF-IDF·LogisticRegression 블렌드** 제출 번들 → **0.6546**
- 발화 경계 전처리 모드, 적대적 리뷰 반영(자기완결 번들, 인코딩·BOM·NaN 처리), 규정 준수 pytest 회귀 테스트 추가

- **Stack**: Python, PyTorch, Hugging Face Transformers, scikit-learn, pytest

<br>

## 🎮 Others

- **[NextPerson](https://github.com/hs-2171395-seungyoonkim/NextPerson)** — 은행 창구 업무 시뮬레이션 게임 (Unity 6). *Papers, Please* 구조에 금융 규제 판단을 적용, 규정 근거를 검수한 고객 케이스 50개
- **[멋쟁이사자처럼 14기 Backend 1팀](https://github.com/HSU-Likelion-Backend-14th/Team-1)** — Spring 기반 백엔드 과제 수행

<br>

## 📊 GitHub Stats

<img src="https://github-readme-stats.vercel.app/api?username=hs-2171395-seungyoonkim&show_icons=true&include_all_commits=true&count_private=true&theme=github_dark&hide_border=true" height="160"/>
