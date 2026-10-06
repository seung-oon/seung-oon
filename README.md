<a id="top"></a>

<!-- 이 파일은 단독으로 사용할 수 있도록 이미지 경로를 모두 절대 URL로 지정했습니다. -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0%3A0F172A%2C50%3A2563EB%2C100%3A22D3EE&amp;height=230&amp;section=header&amp;text=Seungyoon+Kim&amp;fontSize=56&amp;fontColor=FFFFFF&amp;animation=fadeIn&amp;fontAlignY=35&amp;desc=Backend+Developer+%7C+Medical+AI+Research&amp;descSize=19&amp;descAlignY=58" width="100%" alt="Seungyoon Kim · Backend Developer · Medical AI Research">
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;size=21&amp;duration=3200&amp;pause=1000&amp;color=38BDF8&amp;center=true&amp;vCenter=true&amp;width=740&amp;height=48&amp;lines=Backend+Developer%3BMedical+AI+Research%3BSpatial+Data+%26+Graph+Search">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;size=21&amp;duration=3200&amp;pause=1000&amp;color=0369A1&amp;center=true&amp;vCenter=true&amp;width=740&amp;height=48&amp;lines=Backend+Developer%3BMedical+AI+Research%3BSpatial+Data+%26+Graph+Search" width="740" alt="Backend Developer · Medical AI Research · Spatial Data &amp; Graph Search">
  </picture>
</p>

<p align="center">
  <b>한성대학교 컴퓨터공학부 4학년</b><br>
  추천 모델의 <b>재현성과 평가</b>를 연구하고,<br>
  <b>공간 DB와 그래프 탐색 기반의 백엔드</b>를 개발합니다.
</p>

<p align="center">
  <a href="mailto:rlatmddbs02@gmail.com"><img src="https://img.shields.io/badge/Email-334155?style=for-the-badge&amp;logo=gmail&amp;logoColor=white" alt="Email"></a>
  <a href="https://www.linkedin.com/in/%EC%8A%B9%EC%9C%A4-%EA%B9%80-87099041a/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white" alt="LinkedIn"></a>
  <a href="https://github.com/seung-oon?tab=repositories"><img src="https://img.shields.io/badge/Repositories-181717?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="All repositories"></a>
</p>

<p align="center">
  <a href="#research">🔬 Research</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#projects">🚀 Projects</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#tech-stack">🛠 Tech Stack</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#others">🌱 Others</a>
</p>

<p align="center">
  <a href="#research"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/stat-hidr-dark.svg"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/stat-hidr-light.svg" width="260" alt="HI-DR · Jaccard 0.4550 → 0.5231 · 현재 방문 기준, 추천 약 20개, 재점수화 헤드 5-seed"></picture></a>
  <a href="#dcc-예선"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/stat-dcc-dark.svg"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/stat-dcc-light.svg" width="260" alt="DCC 예선 · Wav2Vec2 성별 분류 정확도 0.9835 · Validation 3,640통화"></picture></a>
  <a href="#project-runify"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/stat-runify-dark.svg"><img src="https://raw.githubusercontent.com/seung-oon/seung-oon/main/assets/stat-runify-light.svg" width="260" alt="Runify · Kafka·pgRouting 기반 러닝 코스 생성 서버 전담 구현"></picture></a>
</p>

## Research

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

### DCC 예선

**119 신고 전화 음성·전사 데이터 AI 과제 · 5인 팀 · 2026.09**  
[GitHub ↗](https://github.com/KozzilzzilE/DCC_Problem)

`Python` `PyTorch` `Hugging Face Transformers` `scikit-learn` `pytest`

| 과제 | 담당 | Validation 결과 |
| --- | --- | --- |
| **Mission 1 · 신고자 성별 분류** | 구현·제출 단독 담당 | Wav2Vec2 정확도 **0.9835** · 3,640통화 |
| **Mission 3 · 환자 증상 다중 라벨 분류** | 제출 추론 경로·학습 개선 | F1@0.5 **0.5967 → 0.6496 → 0.6599** |

Mission 3의 제출 설정은 **Training 내부 dev로 결정**하고, Validation은 **마지막 1회 확인**에 사용했습니다.

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

## Projects

<table>
<tr>
<td width="50%" valign="top">
<h3>🏃 <a href="https://github.com/KozzilzzilE/Running-Sketch-Server">Runify</a></h3>
<p><b>그린 도형을 실제 러닝 코스로</b></p>
<p>Backend · 코스 생성 서버 전담<br>2026.08</p>
<p>계산기하·그래프 탐색 파이프라인과 이벤트 처리 구현</p>
<p><code>PostGIS · pgRouting · Kafka</code></p>
<p><a href="https://github.com/KozzilzzilE/Running-Sketch-Server">Repository ↗</a> · <a href="#project-runify">구현 내용 ↓</a></p>
</td>
<td width="50%" valign="top">
<h3>🛡️ <a href="https://github.com/safe-waalk/BE">Safe-walk</a></h3>
<p><b>지도 기반 안전 보행 서비스</b></p>
<p>Team Lead · Backend<br>2026.07</p>
<p>공간 데이터 설계와 안전 인프라·점수 API 구현</p>
<p><code>PostGIS · PostgreSQL · Spring Boot</code></p>
<p><a href="https://github.com/safe-waalk/BE">Repository ↗</a> · <a href="#project-safe-walk">구현 내용 ↓</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3>🌙 <a href="https://github.com/2026-1-midtone/Backend">ShiftRhythm</a></h3>
<p><b>교대근무자를 위한 생체리듬 코칭</b></p>
<p>Backend<br>2026.08</p>
<p>근무표 사진 OCR을 통한 일정 초안 자동 입력</p>
<p><code>Document AI · MySQL · Redis</code></p>
<p><a href="https://github.com/2026-1-midtone/Backend">Repository ↗</a> · <a href="#project-shiftrhythm">구현 내용 ↓</a></p>
</td>
<td width="50%" valign="top">
<h3>🧭 <a href="https://github.com/On-root-AI/BE">OnRoot AI</a></h3>
<p><b>자격증 학습을 위한 AI 플래너</b></p>
<p>Backend<br>2026.05</p>
<p>Q-Net 시험 일정 기반 맞춤 학습 계획 생성</p>
<p><code>Gemini API · Spring Data JPA</code></p>
<p><a href="https://github.com/On-root-AI/BE">Repository ↗</a> · <a href="#project-onroot-ai">구현 내용 ↓</a></p>
</td>
</tr>
</table>

<a id="project-runify"></a>

<details>
<summary><b>Runify · 구현 내용과 측정 결과</b></summary>

**그린 도형을 실제 도보 도로망 위의 러닝 코스로 바꾸는 서비스**  
Backend · 코스 생성 서버 전담 · 팀 프로젝트 · 2026.08  
[GitHub ↗](https://github.com/KozzilzzilE/Running-Sketch-Server) · 저장소 내 이름: ArtRun Route Worker

`Java 21` `Spring Boot 4` `Kafka` `PostgreSQL` `PostGIS` `pgRouting` `Flyway` `Testcontainers` `Docker`

- **코스 생성:** 도형 정규화 → 배치 탐색 → 도로 스냅 → `pgr_dijkstra` 스티칭 → 닮음도 채점·보정으로 이어지는 계산기하·그래프 탐색 파이프라인을 구현했습니다. 강남·서초 약 **8×8km OSM 도보망**을 사용합니다.
- **품질 검증:** 계단 모양 코스가 곧은 코스보다 높게 채점되는 결함을 실측으로 확인했습니다. 꺾임·방문 항을 추가해 해당 코스를 발행 관문에서 걸러내도록 보정했습니다.
- **이벤트 처리:** Kafka 요청 소비부터 결과 이벤트 발행까지 구현했습니다. 수동 커밋, 재시도 후 DLT, `generationId` 멱등 처리, 정체된 RUNNING 작업 자동 복귀와 Testcontainers 통합 테스트를 적용했습니다.

#### 측정 결과와 남은 한계

- **채점 결함:** 4,000m V자 입력에서 코너 26개의 계단 코스가 0.9015로, 곧은 코스의 0.784보다 높게 채점됐습니다. 보정 후 재측정 **3/3건**에서 계단 코스가 발행 관문에서 걸러졌습니다.
- **되돌린 시도:** 경유점 간격을 600m로 바꿨을 때 측정 35건 중 발행 가능한 코스가 **24 → 15건**으로 줄어, 측정 근거와 함께 되돌렸습니다.
- **남은 한계:** 여러 획으로 그린 도형 미지원은 저장소의 이슈 #1에, 코너가 많은 도형의 한계는 측정 문서에 기록했습니다. 왕관 도형은 **0/5건**이었습니다.


</details>

<a id="project-safe-walk"></a>

<details>
<summary><b>Safe-walk · 구현 내용</b></summary>

**지도 기반 안전 보행 서비스**  
Team Lead · Backend · 경기도 공공데이터 공모전 · 2026.07  
[GitHub ↗](https://github.com/safe-waalk/BE)

`Java 21` `Spring Boot 4` `PostgreSQL` `PostGIS` `Supabase` `Docker` `JUnit 5`

- CCTV·보안등·안심벨·범죄주의구역·사용자 신고 테이블을 PostGIS로 설계했습니다.
- 좌표 반경 기반 **안전 인프라 집계·지도 레이어·안전점수 API**를 구현했습니다.
- ORM 없이 `NamedParameterJdbcTemplate`으로 공간 쿼리를 직접 작성했습니다.

</details>

<a id="project-shiftrhythm"></a>

<details>
<summary><b>ShiftRhythm · 구현 내용</b></summary>

**교대근무자를 위한 생체리듬 코칭 앱**  
Backend · 2026.08  
[GitHub ↗](https://github.com/2026-1-midtone/Backend)

`Java 21` `Spring Boot 4` `MySQL` `Redis` `Docker` `Google Document AI`

- 근무표 사진을 **Google Document AI OCR**로 인식해 일정 초안을 자동 입력하도록 구현했습니다. 키 파일 없이 서비스 계정 impersonation을 사용했습니다.
- Testcontainers 기반 MySQL·Redis 통합 테스트와 Docker Compose 로컬 환경을 구성했습니다.

</details>

<a id="project-onroot-ai"></a>

<details>
<summary><b>OnRoot AI · 구현 내용</b></summary>

**LLM 기반 자격증 학습 플래너**  
Backend · 2026.05  
[GitHub ↗](https://github.com/On-root-AI/BE)

`Java 21` `Spring Boot 3.5` `MySQL` `Spring Data JPA` `Gemini API`

- Q-Net 공공데이터 API에서 시험 일정을 받아 **Gemini API로 맞춤 학습 계획을 생성**하도록 구현했습니다.

</details>

## Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=java,spring,python,pytorch,postgres,mysql,redis,kafka,docker,aws,gcp,githubactions&amp;perline=6" width="360" alt="Java, Spring, Python, PyTorch, PostgreSQL, MySQL, Redis, Kafka, Docker, AWS, GCP, GitHub Actions">
</p>

| 분야 | 기술 |
| --- | --- |
| **Backend** | Java · Spring Boot · MySQL · PostgreSQL · PostGIS · pgRouting · Redis · Kafka |
| **Infra** | AWS · GCP · Docker · GitHub Actions |
| **AI · ML** | Python · PyTorch · LangChain / RAG |

## Others

- **[NextPerson](https://github.com/seung-oon/NextPerson)** · Unity 6 기반 은행 창구 업무 시뮬레이션 게임. *Papers, Please* 구조에 금융 규제 판단을 적용했습니다.
- **[멋쟁이사자처럼 14기 Backend 1팀](https://github.com/HSU-Likelion-Backend-14th/Team-1)** · Spring 기반 백엔드 과제 수행 · 2026.03–05

<p align="center"><a href="#top">↑ Back to top</a></p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0%3A0F172A%2C50%3A2563EB%2C100%3A22D3EE&amp;height=100&amp;section=footer" width="100%" alt="">
</p>
