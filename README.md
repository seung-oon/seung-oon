<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=soft&height=140&color=0:161b22%2C100:1f6feb&text=Seungyoon%20Kim&fontSize=44&fontColor=f0f6fc&fontAlignY=40&desc=Backend%20Developer%20%C2%B7%20Medical%20AI%20Research&descSize=18&descAlignY=67&animation=none">
  <img alt="Seungyoon Kim · Backend Developer · Medical AI Research" width="100%" src="https://capsule-render.vercel.app/api?type=soft&height=140&color=0:ddf4ff%2C100:54aeff&text=Seungyoon%20Kim&fontSize=44&fontColor=1f2328&fontAlignY=40&desc=Backend%20Developer%20%C2%B7%20Medical%20AI%20Research&descSize=18&descAlignY=67&animation=none">
</picture>

<div align="center">

한성대학교 컴퓨터공학부 4학년 · **Backend Developer**<br>
Java / Spring Boot 백엔드를 중심으로 공간 DB, 클라우드 인프라, 의료 AI 연구까지 다루고 있습니다.

<a href="mailto:rlatmddbs02@gmail.com"><img alt="Email rlatmddbs02@gmail.com" src="https://img.shields.io/badge/Email-rlatmddbs02%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white"></a>
<a href="https://www.linkedin.com/in/%EC%8A%B9%EC%9C%A4-%EA%B9%80-87099041a/"><img alt="LinkedIn 김승윤" src="https://img.shields.io/badge/LinkedIn-%EA%B9%80%EC%8A%B9%EC%9C%A4-0A66C2?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTIwLjQ0NyAyMC40NTJoLTMuNTU0di01LjU2OWMwLTEuMzI4LS4wMjctMy4wMzctMS44NTItMy4wMzctMS44NTMgMC0yLjEzNiAxLjQ0NS0yLjEzNiAyLjkzOXY1LjY2N0g5LjM1MVY5aDMuNDE0djEuNTYxaC4wNDZjLjQ3Ny0uOSAxLjYzNy0xLjg1IDMuMzctMS44NSAzLjYwMSAwIDQuMjY3IDIuMzcgNC4yNjcgNS40NTV2Ni4yODZ6TTUuMzM3IDcuNDMzYy0xLjE0NCAwLTIuMDYzLS45MjYtMi4wNjMtMi4wNjUgMC0xLjEzOC45Mi0yLjA2MyAyLjA2My0yLjA2MyAxLjE0IDAgMi4wNjQuOTI1IDIuMDY0IDIuMDYzIDAgMS4xMzktLjkyNSAyLjA2NS0yLjA2NCAyLjA2NXptMS43ODIgMTMuMDE5SDMuNTU1VjloMy41NjR2MTEuNDUyek0yMi4yMjUgMEgxLjc3MUMuNzkyIDAgMCAuNzc0IDAgMS43Mjl2MjAuNTQyQzAgMjMuMjI3Ljc5MiAyNCAxLjc3MSAyNGgyMC40NTFDMjMuMiAyNCAyNCAyMy4yMjcgMjQgMjIuMjcxVjEuNzI5QzI0IC43NzQgMjMuMiAwIDIyLjIyMiAwaC4wMDN6Ii8%2BPC9zdmc%2B"></a>

<samp>
<a href="#tech-stack">stack</a> ·
<a href="#projects">projects</a> ·
<a href="#research">research</a> ·
<a href="#others">others</a> ·
<a href="https://github.com/seung-oon?tab=repositories">all repos</a>
</samp>

</div>

## Tech Stack

**Backend**<br>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=java%2Cspring%2Cmysql%2Cpostgres%2Credis&theme=dark"><img alt="Java, Spring Boot, MySQL, PostgreSQL, Redis" height="36" src="https://skillicons.dev/icons?i=java,spring,mysql,postgres,redis&theme=light"></picture> <sub>+ PostGIS</sub>

**Infra**<br>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=aws%2Cdocker%2Cgithubactions&theme=dark"><img alt="AWS, Docker, GitHub Actions" height="36" src="https://skillicons.dev/icons?i=aws,docker,githubactions&theme=light"></picture>

**AI / Research**<br>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=py%2Cpytorch&theme=dark"><img alt="Python, PyTorch" height="36" src="https://skillicons.dev/icons?i=py,pytorch&theme=light"></picture> <sub>+ LangChain / RAG</sub>

## Projects

### [Safe-walk](https://github.com/safe-waalk/BE)

지도 기반 안전 보행 서비스<br>
<sub>Team Lead · Backend — 경기도 공공데이터 공모전</sub>

- CCTV·보안등·안심벨·범죄주의구역·사용자 신고 데이터를 PostGIS에 적재, 좌표 반경 기반 **안전 인프라 집계·지도 레이어·안전점수 API** 제공
- ORM 없이 `NamedParameterJdbcTemplate`으로 공간 쿼리 직접 작성

<sub>Java 21 · Spring Boot 4 · PostgreSQL + PostGIS (Supabase) · Docker · JUnit 5</sub>

### [ShiftRhythm](https://github.com/2026-1-midtone/Backend)

교대근무자를 위한 생체리듬 코칭 앱<br>
<sub>Backend</sub>

- 근무표 사진을 **Google Document AI OCR**로 인식해 일정 자동 입력 (서비스 계정 impersonation, 키 파일 없음)
- Testcontainers 기반 MySQL·Redis 통합 테스트, Docker Compose 로컬 환경

<sub>Java 21 · Spring Boot 4 · MySQL · Redis · Docker · Google Document AI</sub>

### [OnRoot AI](https://github.com/On-root-AI/BE)

LLM 기반 자격증 학습 플래너<br>
<sub>Backend</sub>

- Q-Net 공공데이터 API로 시험 일정을 받아 **Gemini API**로 맞춤 학습 계획 생성

<sub>Java 21 · Spring Boot 3.5 · MySQL · Spring Data JPA · Gemini API</sub>

### [PocketCo](https://github.com/KozzilzzilE/Dataset)

AI 피드백 기반 모바일 알고리즘 학습 앱<br>
<sub>Dataset — 2026 한성대 모바일 캡스톤</sub>

- 알고리즘 학습 콘텐츠 **Firestore 데이터 스키마 설계** (topic → notion → code 계층), 샘플 데이터 구축, 스키마 통일 규칙 정리

## Research

### [Drug Recommendation Research](https://github.com/seung-oon/drug-recommendation-research)

MIMIC-III / IV 기반 의약품 추천 모델 재현성 연구 (7개 트랙)<br>
<sub>seung-oon/drug-recommendation-research · Python · PyTorch · MIMIC-III / IV</sub>

| 트랙 | 핵심 결과 |
|:--|:--|
| **02** · HI-DR (AAAI'25) 재현 → 후보 풀 확장으로 재설계 | Jaccard 0.4550 → **0.5231** <sub>동일 추천 크기 비교</sub> |
| **04** · SafeDrug 군집별 공정성 감사 | 보정 후 군집 간 Jaccard 격차 **0.061** <sub>p 0.003</sub> |
| **06** · SafeDrug DDI 제약 감사 | 페널티를 끄면 초과 DDI 격차가 **절반**으로 감소 <sub>4-seed</sub> |

<details>
<summary><b>7개 트랙 요약</b></summary>
<br>

- **01 · SOTA 논문 리뷰** — MR-DTR (WWW'25), CausalMed (CIKM'24), SubRec (NeurIPS'25) 정독, 세 논문의 데이터 자원·전처리 방식 비교
- **02 · HI-DR 재현 + 재설계** — "과다 추천을 걸러야 한다"는 전제를 데이터로 반증하고, 사후 필터 대신 **이력 기반 후보 풀 확장**으로 재설계 (5-seed). 실제 운영 임계값 기준 Jaccard는 약 0.503
- **03 · SafeDrug + 장기 기능 피처** — ICD-9/10 통합 MIMIC-IV 레코드 재구축, 신·간 기능 지표 주입. 파이프라인 완성, GPU 스모크 테스트 단계
- **04 · SafeDrug 군집별 공정성 감사** — 진단 텍스트로 방문을 군집화해 정확도 격차 검정. SafeDrug 재현 test Jaccard 0.508~0.515, precision 격차가 recall 격차의 2배. 격차 완화 개입 9종 시험, 격차 원인은 방문 표현(05)·DDI 제약(06)에서 추적
- **05 · 급성 attention 절제 실험** — 방문 표현을 입원 시점 텍스트 기반 attention으로 교체. Jaccard는 0.518까지 올랐지만 군집 격차는 줄지 않음
- **06 · DDI 제약 감사** — SafeDrug DDI 행렬의 출처를 추적해, TWOSIDES 비특이적 부작용 40종에 걸린 쌍이라 가이드라인 병용 조합까지 상호작용으로 표시됨을 확인. 페널티를 끄면 초과 DDI 격차가 절반으로 줄어듦 (4-seed)
- **07 · 급성/만성 사전검증** — 급성/만성 분리 가설을 구현 전에 검증해 반증하고 방향 재설정. MIMIC-IV에서는 kNN 검색 + 직전 처방 기준선(0.494)이 SafeDrug·GAMENet·MICRON(0.440~0.449)을 앞섬

</details>

> [!NOTE]
> 원본·행 단위 데이터는 포함하지 않고 코드·보고서·집계 결과만 공개합니다 (PhysioNet DUA 준수).

### [DCC 예선](https://github.com/KozzilzzilE/DCC_Problem)

119 신고 전화 음성·전사 데이터 AI 과제 (팀 5인)<br>
<sub>KozzilzzilE/DCC_Problem · Python · PyTorch · Hugging Face Transformers · scikit-learn · pytest</sub>

| 미션 | 결과 |
|:--|:--|
| **1 · 신고자 성별 분류**<br><sub>단독 담당</sub> | 정확도 **0.9835** <sub>Wav2Vec2 · Validation 3,640통화</sub> |
| **3 · 환자 증상 다중 라벨 분류**<br><sub>제출 경로·학습 개선 담당</sub> | Macro F1@0.5 0.5967 → 0.6496 → **0.6546** <sub>기준선 → pos_weight 거듭제곱 → 멀티시드 앙상블 + 블렌드</sub> |

<details>
<summary><b>Mission 1</b> — 조각 단위 학습 → 통화 단위 soft voting</summary>
<br>

- 통화 음성에서 신고자 발화만 잘라 **조각 단위 학습 → 통화 단위 soft voting** 구조 설계 (조각 정확도 0.88 → 통화 정확도 0.98)
- ResNet50(log-mel)·Wav2Vec2·전화 음성 사전학습 모델 3갈래 비교 하네스 구축, SpecAugment·지식 증류로 ResNet 개선
- 모델 간 오류 겹침 분석으로 앙상블 한계 확인
- 대회 규정(결정 임계값 0.5 고정)에 맞춰 제출 경로 정비, 오프라인 로딩·VRAM 페이징 등 1회 실행 채점 대비

</details>

<details>
<summary><b>Mission 3</b> — 제출 추론 경로 구현, 임계값 대신 손실로 보정</summary>
<br>

- 더미 상태였던 **제출 추론 경로 구현** — 학습 설정을 체크포인트에서 복원해 학습-추론 불일치 차단, 임계값 0.5 고정을 코드로 강제
- 임계값 대신 손실로 보정 — 기존 pos_weight는 과보정으로 Macro F1 0.6189에 그쳐, `pos_weight` 거듭제곱 옵션을 추가해 과보정을 줄임
- KLUE-RoBERTa 멀티시드 앙상블 + **TF-IDF·LogisticRegression 블렌드**로 제출 번들 구성
- 발화 경계 전처리 모드, 적대적 리뷰 반영(자기완결 번들, 인코딩·BOM·NaN 처리), 규정 준수 pytest 회귀 테스트 추가

</details>

## Others

- **[NextPerson](https://github.com/seung-oon/NextPerson)** — 은행 창구 업무 시뮬레이션 게임 (Unity 6 URP). *Papers, Please* 구조에 금융 규제 판단을 적용, 규정 근거를 검수한 고객 케이스 50개
- **[멋쟁이사자처럼 14기 Backend 1팀](https://github.com/HSU-Likelion-Backend-14th/Team-1)** — Spring 기반 백엔드 과제 수행

<br>

<details>
<summary>GitHub activity</summary>
<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=seung-oon&theme=github-dark-blue&hide_border=true&disable_animations=true">
  <img alt="seung-oon GitHub contribution streak" src="https://streak-stats.demolab.com?user=seung-oon&theme=github-light&hide_border=true&disable_animations=true">
</picture>

</details>
