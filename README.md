<a id="top"></a>

<!-- 이 파일은 단독으로 사용할 수 있도록 이미지 경로를 모두 절대 URL로 지정했습니다. 그림은 tools/make_assets.py로 만들며, 포트폴리오 사이트와 같은 디자인(회색 바탕, 검정 글자, 녹색 하나, Pretendard)을 씁니다. -->
<a href="https://seungyoon-portfolio.vercel.app"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/hero-light.svg#gh-light-mode-only" width="100%" alt="Seungyoon Kim · 김승윤 · 백엔드 개발자 · 한성대학교 컴퓨터공학부 4학년 · seungyoon-portfolio.vercel.app"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/hero-dark.svg#gh-dark-mode-only" width="100%" alt="Seungyoon Kim · 김승윤 · 백엔드 개발자 · 한성대학교 컴퓨터공학부 4학년 · seungyoon-portfolio.vercel.app"></a>

지도 위에서 경로를 계산하는 서버를 만들고, 의료 추천 모델을 재현하는 연구를 합니다. 주로 Spring Boot, PostGIS, PyTorch를 씁니다.

**[포트폴리오](https://seungyoon-portfolio.vercel.app)** · **[메일](mailto:rlatmddbs02@gmail.com)** · **[LinkedIn](https://www.linkedin.com/in/%EC%8A%B9%EC%9C%A4-%EA%B9%80-87099041a/)** · **[전체 저장소](https://github.com/seung-oon?tab=repositories)**

### 실험 기록

<p><a href="https://github.com/seung-oon/drug-recommendation-research"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/check-hidr-light.svg#gh-light-mode-only" width="270" alt="HI-DR 과다 추천 가설: 가설과 다른 결과. 방문당 후보 20.07개, 정답 20.16개. 후보 풀을 재설계해 현재 방문 기준 Jaccard 0.4550 → 0.5231"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/check-hidr-dark.svg#gh-dark-mode-only" width="270" alt="HI-DR 과다 추천 가설: 가설과 다른 결과. 방문당 후보 20.07개, 정답 20.16개. 후보 풀을 재설계해 현재 방문 기준 Jaccard 0.4550 → 0.5231"></a> <a href="https://github.com/KozzilzzilE/DCC_Problem"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/check-dcc-light.svg#gh-light-mode-only" width="270" alt="DCC 증상 분류 F1 개선: 드문 증상의 확률 보정 문제를 확인하고 손실 가중 power 0.5 등으로 Macro F1@0.5 0.5967 → 제출 0.6599"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/check-dcc-dark.svg#gh-dark-mode-only" width="270" alt="DCC 증상 분류 F1 개선: 드문 증상의 확률 보정 문제를 확인하고 손실 가중 power 0.5 등으로 Macro F1@0.5 0.5967 → 제출 0.6599"></a> <a href="https://github.com/seung-oon/drug-recommendation-research"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/check-ddi-light.svg#gh-light-mode-only" width="270" alt="SafeDrug DDI 페널티의 군집별 영향: 군집마다 다르게 작동. 페널티를 끄면 군집 간 초과 DDI 격차 0.030 → 0.016, k = 10, 4-seed 모두"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/check-ddi-dark.svg#gh-dark-mode-only" width="270" alt="SafeDrug DDI 페널티의 군집별 영향: 군집마다 다르게 작동. 페널티를 끄면 군집 간 초과 DDI 격차 0.030 → 0.016, k = 10, 4-seed 모두"></a></p>

### 작업

| 작업 | 역할 · 시기 | 한 줄 요약 |
| --- | --- | --- |
| **[의약품 추천 연구](https://github.com/seung-oon/drug-recommendation-research)** | 재현성 독립연구 · 7개 트랙 | HI-DR 재현·확장, Jaccard **0.4550 → 0.5231** |
| **[DCC 예선](https://github.com/KozzilzzilE/DCC_Problem)** | 5인 팀 · 2026.09 | 신고자 성별 분류 **0.9835**, 증상 다중 라벨 F1@0.5 **0.5967 → 0.6599** |
| **[Runify](https://github.com/KozzilzzilE/Running-Sketch-Server)** | 코스 생성 서버 전담 · 2026.08 | 그린 도형을 실제 러닝 코스로, PostGIS · pgRouting · Kafka |
| **[Safe-walk](https://github.com/safe-waalk/BE)** | Team Lead · Backend · 2026.07 | 지도 기반 안전 보행 서비스, 안전 인프라·점수 API |
| **[ShiftMate](https://github.com/2026-1-midtone/Backend)** | Backend · 2026.08 | 근무표 사진 OCR로 일정 초안 자동 입력 |
| **[OnRoot AI](https://github.com/On-root-AI/BE)** | Backend · 2026.05 | Q-Net 시험 일정 기반 맞춤 학습 계획 생성 |
| **[NextPerson](https://github.com/seung-oon/NextPerson)** | Unity 6 게임 | *Papers, Please* 구조에 금융 규제 판단을 적용한 은행 창구 시뮬레이션 |
| **[멋쟁이사자처럼 14기](https://github.com/HSU-Likelion-Backend-14th/Team-1)** | Backend 1팀 · 2026.03–05 | Spring 기반 백엔드 과제 수행 |

<a id="research"></a>

<details>
<summary><b>Research</b> · 의약품 추천 연구와 DCC 예선 상세</summary>

### Drug Recommendation Research

**MIMIC-III / IV 기반 의약품 추천 모델 재현성 연구 · 7개 트랙**  
[GitHub ↗](https://github.com/seung-oon/drug-recommendation-research)

`Python` `PyTorch` `MIMIC-III / IV`

모델을 재현하고, 후보 풀 설계·군집별 성능 격차·DDI(약물 간 상호작용) 제약을 검증합니다. 실험으로 반증된 가설과 남은 검증 과제도 함께 기록합니다.

| 연구 | 주요 결과 | 비교 조건 |
| --- | --- | --- |
| **HI-DR 재현·확장** | Jaccard **0.4550 → 0.5231** | HI-DR 빔 출력 대비, 현재 방문 기준, 방문당 추천 약 20개로 맞춤, 재점수화 헤드 5-seed |
| **SafeDrug 공정성 감사** | 보정 후 Jaccard 격차 **0.061** | 4-seed 풀링, k 선택 보정 후 p = 0.016 |
| **SafeDrug DDI 제약 감사** | 페널티를 끄면 군집 간 초과 DDI 격차 **0.030 → 0.016** | k = 10, 4-seed 모두 감소 |

<img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/projects/safedrug-clusters.webp" width="100%" alt="SafeDrug 진단 군집 10개의 보정 Jaccard(4-seed 풀링, long_k10). 호흡부전·폐렴·패혈증 0.488부터 안면외상·뇌동맥류 0.554까지.">

원본 데이터와 행 단위 데이터는 공개하지 않고, **코드·보고서·집계 결과만 공개**합니다.

<details>
<summary><b>전체 연구 트랙과 검증 과제</b></summary>

#### 01 · SOTA 논문 리뷰

MR-DTR (WWW'25), CausalMed (CIKM'24), SubRec (NeurIPS'25)를 정독하고 데이터 자원과 전처리 방식을 비교했습니다.

#### 02 · HI-DR (AAAI'25) 재현과 확장 시도

- **가설 검증:** “모델이 과다 추천하므로 사후 필터가 필요하다”는 가설을 검증했습니다. HI-DR의 방문당 후보는 20.07개, 정답은 20.16개로 가설과 달랐습니다.
- **설계 변경:** 사후 필터 대신 이력 기반 후보 풀 확장으로 재설계했습니다.
- **평가 조건:** 위 표의 결과는 현재 방문 기준입니다. 운영 임계값 기준 Jaccard는 약 **0.503**입니다.

#### 03 · SafeDrug와 장기 기능

ICD-9/10을 통합한 MIMIC-IV 레코드를 재구축하고 신장·간 기능 지표를 주입했습니다. 현재 **GPU 스모크 테스트 단계**입니다.

#### 04 · 군집별 공정성 감사

- 진단 텍스트로 방문을 군집화해 정확도 격차를 검정했습니다.
- 재현 test Jaccard는 **0.508~0.515**이며, precision 격차가 recall 격차의 약 **2배**였습니다.
- 6개 계열의 개입 **9종**을 시험했습니다.

#### 05 · 급성 attention

- 방문 표현을 입원 시점 텍스트 attention으로 교체했습니다.
- Jaccard는 시드 0에서 **0.508 → 0.518**, 4-seed 평균에서 **0.511 → 0.515**로 변했습니다.
- **군집 간 격차는 줄지 않았습니다.**

#### 06 · DDI 제약 감사

- SafeDrug DDI 행렬이 TWOSIDES에서 가장 드문 부작용 40종에 해당하는 약물 쌍으로 구성되어 있음을 확인했습니다.
- 스타틴–질산염과 같은 가이드라인상 병용도 상호작용으로 표시되는 사례를 확인했습니다.
- 배포된 **337쌍을 정확히 재현**했습니다.

#### 07 · 급성·만성 사전 검증

- 구현 전에 가설을 검증해 반증하고 연구 방향을 다시 설정했습니다.
- MIMIC-IV test 전이에서 kNN 검색과 직전 처방을 결합한 기준선의 Jaccard는 **0.494**로, SafeDrug·GAMENet·MICRON의 **0.440~0.449**보다 높았습니다.
- **남은 과제:** ICD 9→10 전환 구간을 제외한 재계산, 동등한 튜닝 조건에서의 비교.

</details>

<a id="dcc-예선"></a>

### DCC 예선

**119 신고 전화 음성·전사 데이터 AI 과제 · 5인 팀 · 2026.09**  
[GitHub ↗](https://github.com/KozzilzzilE/DCC_Problem)

`Python` `PyTorch` `Hugging Face Transformers` `scikit-learn` `pytest`

| 과제 | 담당 | Validation 결과 |
| --- | --- | --- |
| **Mission 1 · 신고자 성별 분류** | 구현·제출 단독 담당 | Wav2Vec2 정확도 **0.9835** · 3,640통화 |
| **Mission 3 · 환자 증상 다중 라벨 분류** | 제출 추론 경로·학습 개선 | F1@0.5 **0.5967 → 0.6496 → 0.6599** |

Mission 3의 제출 설정은 **Training 내부 dev로 결정**하고, Validation은 **마지막 1회 확인**에 사용했습니다.

<img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/projects/dcc-steps.webp" width="100%" alt="DCC Mission 3 Macro F1@0.5 단계별 변화. Plain BCE 0.5967, pos_weight power 1.0 0.6189, power 0.5 0.6496, TF-IDF 0.6536, 4-seed 0.6546, TAPT+LLRD 0.6593, 제출 0.6599.">

<details>
<summary><b>Mission 1 · 음성 조각 학습과 통화 단위 예측</b></summary>

- 신고자 발화만 잘라 **조각 단위 학습 → 통화 단위 soft voting** 구조를 설계했습니다. 조각 정확도는 0.88~0.90, 통화 정확도는 약 0.98이었습니다.
- ResNet50(log-mel), Wav2Vec2, 전화 음성 사전학습 모델을 비교하는 3갈래 실험 하네스를 구축했습니다.
- SpecAugment와 지식 증류로 ResNet 개선을 시도했지만, 통화 정확도 **0.9791 → 0.9824**의 차이는 노이즈 범위였습니다.
- 모델 간 오류 겹침을 분석해 앙상블의 한계를 확인했습니다.
- 결정 임계값 0.5 고정 규정에 맞춰 제출 경로를 정비하고, 오프라인 로딩·VRAM 페이징 등 1회 실행 채점에 대비했습니다.

</details>

<details>
<summary><b>Mission 3 · 제출 추론 경로와 학습 손실 개선</b></summary>

- **추론 경로 구현:** 더미 상태의 제출 경로를 구현했습니다. 체크포인트에서 학습 설정을 복원해 학습·추론 불일치를 방지하고, 임계값 0.5 고정을 코드로 강제했습니다.
- **손실 보정:** 기존 `pos_weight`의 과보정으로 Macro F1이 0.6189에 그쳐, 거듭제곱 옵션을 추가했습니다. 기준선 **0.5967 → 거듭제곱 적용 0.6496 → 최종 제출 번들 0.6599**로 개선했습니다.
- **평가 절차 정비:** 주최 측의 09-30 답변에 따라 p·학습 레시피·저장 epoch·앙상블 구성을 Training 내부 dev로 다시 결정했습니다. 선택 규칙은 결과 확인 전에 커밋해 사전 등록했습니다.
- **최종 구성:** KLUE-RoBERTa TAPT·LLRD **4-seed 앙상블**을 사용했습니다. TF-IDF 블렌드는 dev에서 이득이 없어 제외했습니다.
- **제출 안정성:** 적대적 리뷰를 반영해 자기완결 번들, 인코딩·BOM·NaN 처리를 정비하고 규정 준수 여부를 확인하는 pytest 회귀 테스트를 추가했습니다.

</details>

</details>

<a id="projects"></a>

<details>
<summary><b>Projects</b> · 백엔드 프로젝트 구현 상세</summary>

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/KozzilzzilE/Running-Sketch-Server"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/projects/runify-course.webp" width="100%" alt="Runify 측정 문서의 4km 코스 비교: 회색 목표 도형 위에 이전 기준과 현재 기준으로 생성한 코스"></a>
<h3><a href="https://github.com/KozzilzzilE/Running-Sketch-Server">Runify</a></h3>
<p><b>그린 도형을 실제 러닝 코스로</b></p>
<p>Backend · 코스 생성 서버 전담<br>2026.08</p>
<p><code>PostGIS · pgRouting · Kafka</code></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/safe-waalk/BE"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/projects/safewalk-radius.webp" width="100%" alt="Safe-walk가 적재한 서울 OSM 보행 도로망 위에 안전점수 집계 반경(CCTV·범죄주의구역 150m, 보안등·안심벨 100m)을 그린 지도"></a>
<h3><a href="https://github.com/safe-waalk/BE">Safe-walk</a></h3>
<p><b>지도 기반 안전 보행 서비스</b></p>
<p>Team Lead · Backend<br>2026.07</p>
<p><code>PostGIS · PostgreSQL · Spring Boot</code></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/2026-1-midtone/Backend"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/projects/shiftmate-mascot.webp" width="100%" alt="ShiftMate 캐릭터: 확성기를 든 보라색 고양이"></a>
<h3><a href="https://github.com/2026-1-midtone/Backend">ShiftMate</a></h3>
<p><b>교대근무자를 위한 생체리듬 코칭</b></p>
<p>Backend<br>2026.08</p>
<p><code>Document AI · MySQL · Redis</code></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/On-root-AI/BE"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/projects/onroot-mascot.webp" width="100%" alt="OnRoot AI 캐릭터: 초록 바탕 위의 새싹"></a>
<h3><a href="https://github.com/On-root-AI/BE">OnRoot AI</a></h3>
<p><b>자격증 학습을 위한 AI 플래너</b></p>
<p>Backend<br>2026.05</p>
<p><code>Gemini API · Spring Data JPA</code></p>
</td>
</tr>
</table>

<a id="project-runify"></a>

#### Runify · 구현 내용과 측정 결과

**그린 도형을 실제 도보 도로망 위의 러닝 코스로 바꾸는 서비스**  
Backend · 코스 생성 서버 전담 · 팀 프로젝트 · 2026.08  
[GitHub ↗](https://github.com/KozzilzzilE/Running-Sketch-Server) · 저장소 내 이름: ArtRun Route Worker

`Java 21` `Spring Boot 4` `Kafka` `PostgreSQL` `PostGIS` `pgRouting` `Flyway` `Testcontainers` `Docker`

- **코스 생성:** 도형 정규화 → 배치 탐색 → 도로 스냅 → `pgr_dijkstra` 스티칭 → 닮음도 채점·보정으로 이어지는 계산기하·그래프 탐색 파이프라인을 구현했습니다. 강남·서초 약 **8×8km OSM 도보망**을 사용합니다.
- **품질 검증:** 계단 모양 코스가 곧은 코스보다 높게 채점되는 결함을 실측으로 확인했습니다. 꺾임·방문 항을 추가해 해당 코스를 발행 관문에서 걸러내도록 보정했습니다.
- **이벤트 처리:** Kafka 요청 소비부터 결과 이벤트 발행까지 구현했습니다. 수동 커밋, 재시도 후 DLT, `generationId` 멱등 처리, 정체된 RUNNING 작업 자동 복귀와 Testcontainers 통합 테스트를 적용했습니다.
- **채점 결함:** 4,000m V자 입력에서 코너 26개의 계단 코스가 0.9015로, 곧은 코스의 0.784보다 높게 채점됐습니다. 보정 후 재측정 **3/3건**에서 계단 코스가 발행 관문에서 걸러졌습니다.
- **되돌린 시도:** 경유점 간격을 600m로 바꿨을 때 측정 35건 중 발행 가능한 코스가 **24 → 15건**으로 줄어, 측정 근거와 함께 되돌렸습니다.
- **남은 한계:** 여러 획으로 그린 도형 미지원은 저장소의 이슈 #1에, 코너가 많은 도형의 한계는 측정 문서에 기록했습니다. 왕관 도형은 **0/5건**이었습니다.

<a id="project-safe-walk"></a>

#### Safe-walk · 구현 내용

**지도 기반 안전 보행 서비스**  
Team Lead · Backend · 경기도 공공데이터 공모전 · 2026.07  
[GitHub ↗](https://github.com/safe-waalk/BE)

`Java 21` `Spring Boot 4` `PostgreSQL` `PostGIS` `Supabase` `Docker` `JUnit 5`

- CCTV·보안등·안심벨·범죄주의구역·사용자 신고 테이블을 PostGIS로 설계했습니다.
- 좌표 반경 기반 **안전 인프라 집계·지도 레이어·안전점수 API**를 구현했습니다.
- ORM 없이 `NamedParameterJdbcTemplate`으로 공간 쿼리를 직접 작성했습니다.

<a id="project-shiftrhythm"></a>

#### ShiftMate · 구현 내용

**교대근무자를 위한 생체리듬 코칭 앱**  
Backend · 2026.08  
[GitHub ↗](https://github.com/2026-1-midtone/Backend)

`Java 21` `Spring Boot 4` `MySQL` `Redis` `Docker` `Google Document AI`

- 근무표 사진을 **Google Document AI OCR**로 인식해 일정 초안을 자동 입력하도록 구현했습니다. 키 파일 없이 서비스 계정 impersonation을 사용했습니다.
- Testcontainers 기반 MySQL·Redis 통합 테스트와 Docker Compose 로컬 환경을 구성했습니다.

<a id="project-onroot-ai"></a>

#### OnRoot AI · 구현 내용

**LLM 기반 자격증 학습 플래너**  
Backend · 2026.05  
[GitHub ↗](https://github.com/On-root-AI/BE)

`Java 21` `Spring Boot 3.5` `MySQL` `Spring Data JPA` `Gemini API`

- Q-Net 공공데이터 API에서 시험 일정을 받아 **Gemini API로 맞춤 학습 계획을 생성**하도록 구현했습니다.

</details>

<a id="tech-stack"></a>

<details>
<summary><b>Tech Stack</b></summary>

<br>


| 분야 | 기술 |
| --- | --- |
| **Backend** | Java · Spring Boot · MySQL · PostgreSQL · PostGIS · pgRouting · Redis · Kafka |
| **Infra** | AWS · GCP · Docker · GitHub Actions |
| **AI · ML** | Python · PyTorch · LangChain / RAG |

</details>

<a id="others"></a>

<details>
<summary><b>Others</b> · NextPerson, 멋쟁이사자처럼</summary>

<br>

<a href="https://github.com/seung-oon/NextPerson"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/projects/nextperson-case.webp" width="480" alt="NextPerson 규칙 일러스트(게임 화면 아님): DSR 67.3%가 규제 한도 40%를 넘어 거절이 정답인 사례, 손님당 25초, 사원부터 지점장까지 직급, 불만 5건이면 권고사직"></a>

- **[NextPerson](https://github.com/seung-oon/NextPerson)** · Unity 6 기반 은행 창구 업무 시뮬레이션 게임. *Papers, Please* 구조에 금융 규제 판단을 적용했습니다.
- **[멋쟁이사자처럼 14기 Backend 1팀](https://github.com/HSU-Likelion-Backend-14th/Team-1)** · Spring 기반 백엔드 과제 수행 · 2026.03–05

</details>

<a href="https://seungyoon-portfolio.vercel.app"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/footer-light.svg#gh-light-mode-only" width="100%" alt="seungyoon · seungyoon-portfolio.vercel.app"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/footer-dark.svg#gh-dark-mode-only" width="100%" alt="seungyoon · seungyoon-portfolio.vercel.app"></a>
